"""Group orders into round trips (zero -> position -> zero) and score them.

Usage:
  python analysis/roundtrips.py private/trades.csv private/cycles.csv

Return after fees = cash from sells / cash spent on buys - 1 (commissions included).
"""
import pandas as pd, sys
t=pd.read_csv(sys.argv[1]); t['date']=pd.to_datetime(t['date'],format='%d %b %Y %H:%M:%S')
t=t.sort_values('date',kind='stable')
t['sq']=t.qty.where(t.side=='Buy',-t.qty)
pos=t.groupby('sym').sq.sum().round(6); print('open positions:',pos[pos.abs()>1e-4].to_dict())
cyc=[]
for sym,g in t.groupby('sym'):
    q=0;cur=None
    for _,r in g.iterrows():
        if cur is None: cur=dict(sym=sym,open=r.date,buys=0,sells=0,gross_buy=0,gross_sell=0,fees=0,n=0)
        cur['n']+=1; cur['fees']+=r.com+r.fee
        if r.side=='Buy': cur['buys']+=r.value; cur['gross_buy']+=r.qty*r.price; q+=r.qty
        else: cur['sells']+=r.value; cur['gross_sell']+=r.qty*r.price; q-=r.qty
        if q<=1e-6*max(1,r.qty) or abs(q)<1e-5:
            cur['close']=r.date; cyc.append(cur); cur=None; q=0
    if cur: cur['close']=pd.NaT; cur['open_qty']=q; cyc.append(cur)
c=pd.DataFrame(cyc)
c['ret']=c.sells/c.buys-1; c['gross_ret']=c.gross_sell/c.gross_buy-1
c['days']=(c.close-c.open).dt.days; c['pnl']=c.sells-c.buys
c.to_csv(sys.argv[2],index=False)
closed=c[c.close.notna()]
print(f"closed round trips: {len(closed)}  open: {c.close.isna().sum()}")
print(f"win rate: {(closed.pnl>0).mean():.0%}  wins {int((closed.pnl>0).sum())} losses {int((closed.pnl<=0).sum())}")
print(f"avg return/trade: {closed.ret.mean():+.1%}  median {closed.ret.median():+.1%}  avg gross(pre-fee) {closed.gross_ret.mean():+.1%}")
print(f"total cost {closed.buys.sum():.0f} proceeds {closed.sells.sum():.0f} -> money-weighted {closed.sells.sum()/closed.buys.sum()-1:+.1%}  net P&L ${closed.pnl.sum():.0f}")
print(f"total fees+commission ${t.com.sum()+t.fee.sum():.0f} on ${t.value.sum():.0f} traded; median hold {closed.days.median():.0f} days")
pd.set_option('display.width',200)
print(closed.sort_values('open')[['sym','open','close','days','n','buys','sells','pnl','ret','gross_ret']].assign(open=lambda d:d.open.dt.date,close=lambda d:d.close.dt.date).round(3).to_string(index=False))
print(c[c.close.isna()][['sym','open','buys','sells','open_qty']])
