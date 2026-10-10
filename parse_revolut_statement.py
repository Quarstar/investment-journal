"""Parse a Revolut Trading account statement into one row per order.

Usage:
  pdftotext -layout private/statement.pdf private/statement.txt
  python analysis/parse_revolut_statement.py private/statement.txt private/trades.csv

The raw statement contains personal details, so it lives in private/ (git-ignored).
"""
import re, sys, csv
txt=open(sys.argv[1]).read().split('GBP Account summary')[0]
pat=re.compile(r'^\s*(\d{2} \w{3} \d{4} \d{2}:\d{2}:\d{2}) GMT\s+(\S+)?\s+(Trade - \w+|Cash top-up|Cash withdrawal|Dividend tax|Dividend|[A-Z][\w ]+?)\s{2,}(.*)$')
rows=[];other=[]
for line in txt.splitlines():
    m=pat.match(line)
    if not m: continue
    d,sym,typ,rest=m.groups()
    nums=re.findall(r'-?\$?[\d,]+\.?\d*|Buy|Sell',rest)
    if typ.startswith('Trade'):
        q,p,side,val,fee,com=nums[:6]
        f=lambda s: float(s.replace('$','').replace(',',''))
        rows.append(dict(date=d,sym=sym,type=typ,qty=f(q),price=f(p),side=side,value=f(val),fee=f(fee),com=f(com)))
    else:
        other.append((d,sym,typ,rest.strip()))
w=csv.DictWriter(open(sys.argv[2],'w'),fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
print(len(rows),'trades')
for o in other:
    if o[2] not in('Cash top-up','Cash withdrawal'): print(o)
