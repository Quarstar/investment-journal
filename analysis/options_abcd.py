"""Compare core options A/B/C/D for the 14 Oct 2026 review.
Data: data/weekly_closes_2025-10-10_to_2026-10-09.csv (Friday closes; US10Y = 10-year Treasury yield, %).
Run: python analysis/options_abcd.py
"""
import csv, itertools, numpy as np
rows=list(csv.DictReader(open('data/weekly_closes_2025-10-10_to_2026-10-09.csv')))
cols=[c for c in rows[0] if c not in ('week_ending','US10Y')]
S={c:np.array([float(r[c]) for r in rows]) for c in cols}
Y=np.array([float(r['US10Y']) for r in rows])
R={k:np.diff(np.log(v)) for k,v in S.items()}
q=R['QQQ']; dy=np.diff(Y); w10=np.argsort(q)[:10]
names=['NVDA','TSM','VST','CEG','GOOGL','NBIS']
def stats(r):
    p=np.exp(np.concatenate([[0],np.cumsum(r)]))
    X=np.column_stack([np.ones_like(q),q,dy]); b=np.linalg.lstsq(X,r,rcond=None)[0]
    e=r-X@b; s2=e@e/(len(r)-3); t=b/np.sqrt(np.diag(s2*np.linalg.inv(X.T@X)))
    return dict(vol=r.std(ddof=1)*52**.5*100, beta=np.cov(r,q,ddof=1)[0,1]/q.var(ddof=1),
        corrQ=np.corrcoef(r,q)[0,1], corrN=np.corrcoef(r,R['NVDA'])[0,1],
        worst10=(np.exp(r[w10])-1).mean()*100, maxdd=(p/np.maximum.accumulate(p)-1).min()*100,
        ret1y=(p[-1]/p[0]-1)*100, b_rate100=b[2]*100, t_rate=t[2],
        betaN=np.cov(r,R['NVDA'],ddof=1)[0,1]/R['NVDA'].var(ddof=1))
print(f"{'name':6}{'vol':>5}{'beta':>6}{'corrQ':>7}{'corrN':>7}{'worst10':>9}{'maxdd':>7}{'ret1y':>7}{'rate%/pt':>9}{'t':>6}")
for k in names:
    s=stats(R[k]); print(f"{k:6}{s['vol']:5.0f}{s['beta']:6.2f}{s['corrQ']:7.2f}{s['corrN']:7.2f}{s['worst10']:9.1f}{s['maxdd']:7.1f}{s['ret1y']:7.1f}{s['b_rate100']:9.1f}{s['t_rate']:6.2f}")
opts={'A':{'NVDA':10.5,'TSM':10.5,'VST':10,'CEG':10,'NBIS':6},
      'B':{'NVDA':10.5,'TSM':10.5,'CEG':10,'GOOGL':10,'NBIS':6},
      'C':{'NVDA':10.5,'TSM':10.5,'VST':10,'GOOGL':10,'NBIS':6},
      'D':{'VST':12,'CEG':9,'NVDA':9,'TSM':9,'GOOGL':8}}
bx=lambda k:np.cov(R[k],q,ddof=1)[0,1]/q.var(ddof=1)
restb=0.12*bx('XLVP')+0.06*bx('VUKG')+0.05*0.69+0.04*0.57+0.01*1.5   # Jan weights; UBER/NU betas from the anchor test
bN=lambda k:np.cov(R[k],R['NVDA'],ddof=1)[0,1]/R['NVDA'].var(ddof=1)
restN=(0.12*bN('XLVP')+0.06*bN('VUKG')+0.09*0.1)
print("\noption vol beta corrN worst10 maxdd avgpair rate%/pt ret1y | book: QQQ-15 QQQ-25 QQQ-35 AIbust +50bp&-5 QQQ+20")
for o,w in opts.items():
    ws={k:v/sum(w.values()) for k,v in w.items()}
    r=np.log(1+sum(ws[k]*(np.exp(R[k])-1) for k in ws)); s=stats(r)
    pr=[(ws[a]*ws[b],np.corrcoef(R[a],R[b])[0,1]) for a,b in itertools.combinations(ws,2)]
    avg=sum(x*c for x,c in pr)/sum(x for x,_ in pr)
    book=lambda sh:0.47*s['beta']*sh+restb*sh
    ai=sum(w[k]/100*bN(k)*-40 for k in w)+restN*-40
    rate=0.47*(s['beta']*-5+s['b_rate100']*0.5)+restb*-5
    print(f"{o}   {s['vol']:4.0f} {s['beta']:5.2f} {s['corrN']:5.2f} {s['worst10']:7.1f} {s['maxdd']:6.1f} {avg:7.2f} {s['b_rate100']:8.1f} {s['ret1y']:6.1f} | {book(-15):6.1f} {book(-25):6.1f} {book(-35):6.1f} {ai:6.1f} {rate:8.1f} {book(20):6.1f}")
