"""Parse executed trades from a Trading 212 Stocks ISA activity statement.

Usage: python analysis/parse_t212_statement.py private/t212.txt private/t212/trades.csv
"""
import re, sys, pandas as pd
txt=open(sys.argv[1]).read()
sec=txt[txt.index('Stocks ISA account - executed trades'):]
row=re.compile(r'^\s*(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\s+(\S+)\s+([A-Z]{2}[A-Z0-9]{9}\d)\s+(\d+)\s+(Buy|Sell)\s+([\d.]+)\s+(\S+)\s+(\S+)\s+(Market|Limit|Stop|Stop limit)\s+.*?([\d.]+)\s+£([\d.,]+)\s+(?:-|£[\d.,]+)\s+(-|-?£[\d.,]+)\s+£([\d.,]+)\s*$')
rows=[];miss=[]
for l in sec.splitlines():
    if re.match(r'^\s*\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\s+\S+\s+[A-Z]{2}[A-Z0-9]{9}\d',l):
        m=row.match(l)
        if not m: miss.append(l); continue
        g=m.groups(); f=lambda s: float(s.replace('£','').replace(',',''))
        rows.append(dict(date=g[0],sym=g[1],side=g[4],qty=float(g[5]),price=g[6],fx_fee=f(g[10]),ret=None if g[11]=='-' else f(g[11]),value=f(g[12])))
df=pd.DataFrame(rows); df.to_csv(sys.argv[2],index=False)
print(len(df),'trades; unparsed',len(miss)); [print(m[:200]) for m in miss[:5]]
print(df.groupby('sym').size().to_dict())
