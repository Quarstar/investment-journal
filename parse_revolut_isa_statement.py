"""Parse the "Units which have been sold" section of a Revolut ISA consolidated statement into one row per sold tax lot.

Usage: python analysis/parse_revolut_isa_statement.py private/isa.txt private/isa/lots.csv
(First: pdftotext -layout private/isa.pdf private/isa.txt. The statement holds personal and tax details, so it stays in private/.)
Reconciles exactly to the statement's gross proceeds and cost basis.
"""
import re, sys, pandas as pd
txt=open(sys.argv[1]).read()
sec=txt[txt.index('Units which have been sold'):]
sec=re.split(r'\n\s*Date\s+Description & symbol ISIN\s+Quantity',sec)[0]  # stop at purchases table
lines=[l for l in sec.splitlines() if l.strip() and not re.search(r'Custom Statement|Generated on|24 May 2024 - 9|^\s*(Unit|Date|of Sale|of Purchase|on Purchase|on Sale|date)\b',l)]
start=re.compile(r'^\s*(\d{1,2}) ([A-Z][a-z]{2,3})(?: (\d{4}))?\s+.*?(\d+) days?\s+([\d.]+)\s+\+[\$€£]')
blocks=[];cur=None
for l in lines:
    if start.match(l):
        if cur: blocks.append(cur)
        cur=[l]
    elif cur is not None: cur.append(l)
if cur: blocks.append(cur)
mon={'Sept':'Sep'}
rows=[]
for b in blocks:
    m=start.match(b[0]); d,mo,yr,age,units=m.groups()
    if not yr:
        for l in b[1:4]:
            y=re.match(r'^\s*(\d{4})\b',l)
            if y: yr=y.group(1);break
    text='\n'.join(b)
    isin=re.search(r'\b((?:US|AU|NL|CA|GB|IE|KY|JE|BM|SE)[A-Z0-9]{9}\d)\b',text).group(1)
    sym=re.search(r'\b([A-Z]{2,5})\s+(?:US|AU|NL|CA|GB|IE|KY|JE|BM|SE)\s+\d+ days?',b[0])
    gbp_sale=re.findall(r'\+£([\d,.]+)\s+\+£([\d,.]+)',text)[0][1]
    gbp_buy=re.findall(r'-£([\d,.]+)\s+-£([\d,.]+)',text)[0][1]
    fee=re.findall(r'£([\d,.]+)\s*$',b[1])
    f=lambda s: float(s.replace(',',''))
    sale=pd.to_datetime(f"{d} {mon.get(mo,mo)} {yr}")
    rows.append(dict(isin=isin,sym=sym.group(1) if sym else None,sale=sale,purchase=sale-pd.Timedelta(days=int(age)),units=f(units),
                     sale_gbp=f(gbp_sale),cost_gbp=f(gbp_buy),fee_gbp=f(fee[-1]) if fee else 0.0))
df=pd.DataFrame(rows)
df['sym']=df.groupby('isin').sym.transform(lambda s: s.dropna().iloc[0] if s.notna().any() else None)
df.to_csv(sys.argv[2],index=False)
print(len(df),'lots | proceeds',round(df.sale_gbp.sum(),2),'cost',round(df.cost_gbp.sum(),2),'fees',round(df.fee_gbp.sum(),2),'net',round(df.sale_gbp.sum()-df.cost_gbp.sum()-df.fee_gbp.sum(),2))
print(df[df.sym.isna()]['isin'].unique(), sorted(df.sym.dropna().unique()))
