"""Turn Revolut ISA sold lots and Trading 212 trades into round trips and print stats.

Run from the private/ working folder containing isa/lots.csv and t212/trades.csv.
"""
import pandas as pd, numpy as np
# --- Revolut ISA: sold lots -> round trips (overlapping holding periods per ticker) ---
L=pd.read_csv('isa/lots.csv',parse_dates=['sale','purchase'])
fix={'US0079031078':'AMD','US1725731079':'CRCL','SE0017486889':'ATCO-B'}
L['sym']=L.apply(lambda r: fix.get(r.isin,r.sym),axis=1)
out=[]
for sym,g in L.sort_values('purchase').groupby('sym'):
    cur=None
    for _,r in g.sort_values(['purchase','sale']).iterrows():
        if cur and r.purchase<=cur['close']:
            cur['close']=max(cur['close'],r.sale); cur['cost']+=r.cost_gbp; cur['proc']+=r.sale_gbp-r.fee_gbp; cur['lots']+=1; cur['last_sale']=max(cur['last_sale'],r.sale)
        else:
            if cur: out.append(cur)
            cur=dict(acct='Revolut ISA',sym=sym,open=r.purchase,close=r.sale,last_sale=r.sale,cost=r.cost_gbp,proc=r.sale_gbp-r.fee_gbp,lots=1)
    out.append(cur)
A=pd.DataFrame(out); A['close']=A.last_sale; A=A.drop(columns='last_sale')
# --- Trading 212 ISA: running quantity per ticker ---
T=pd.read_csv('t212/trades.csv',parse_dates=['date']).sort_values('date')
rows=[];orphans=[]
for sym,g in T.groupby('sym'):
    q=0;cur=None
    for _,r in g.iterrows():
        if r.side=='Sell' and q<=1e-9:
            orphans.append((sym,r.date.date(),r.ret)); continue
        if cur is None: cur=dict(acct='Trading 212 ISA',sym=sym,open=r.date,cost=0,proc=0,lots=0)
        cur['lots']+=1
        if r.side=='Buy': cur['cost']+=r.value; q+=r.qty
        else: cur['proc']+=r.value; q-=r.qty
        if q<=1e-6: cur['close']=r.date; rows.append(cur); cur=None; q=0
    if cur: cur['close']=pd.NaT; cur['open_qty']=q; rows.append(cur)
B=pd.DataFrame(rows)
print('T212 sells with no buy in statement period (bought before June):',orphans)
for name,D in [('Revolut ISA',A),('Trading 212 ISA',B)]:
    c=D[D.close.notna()].copy(); c['ret']=c.proc/c.cost-1; c['pnl']=c.proc-c.cost; c['days']=(c.close-c.open).dt.days
    w=c[c.pnl>0];l=c[c.pnl<=0]
    print(f"\n== {name}: {len(c)} closed, open {D.close.isna().sum() if 'close' in D else 0} | win {len(w)/len(c):.0%} | avg {c.ret.mean():+.1%} med {c.ret.median():+.1%} | avg win {w.ret.mean():+.1%} avg loss {l.ret.mean():+.1%} | PF {w.pnl.sum()/-l.pnl.sum():.2f} | net £{c.pnl.sum():.0f} | med hold {c.days.median():.0f}d")
    print(c.sort_values('open')[['sym','open','close','days','lots','ret']].assign(open=lambda d:d.open.dt.date,close=lambda d:d.close.dt.date,ret=lambda d:(d.ret*100).round(1)).to_string(index=False))
    c.to_csv(f'{name.split()[0].lower()}_{"isa"}_cycles.csv' if name=='Revolut ISA' else 't212_cycles.csv',index=False)
print(B[B.close.isna()][['sym','open','open_qty']].to_string(index=False))
