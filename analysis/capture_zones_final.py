"""Final capture zones (judgment overlay on capture_zones.py output), with the stats for each band.
Zones as of the 3 Nov 2026 close, re-mapped on the 30 Oct weekly closes (first map: 14 Oct; previous: 27 Oct). Edit ZONES each Wednesday when a zone breaks or the map steps up."""
import json, math, os, csv
import numpy as np
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
mech = json.load(open(os.path.join(ROOT, "analysis", "capture_zones_output.json")))
fund = {r["ticker"]: r for r in csv.DictReader(open(os.path.join(ROOT, "data", "fundamentals_2026-10-13.csv")))}
HIGH_OVERRIDE = {"NBIS": 299.86, "IREN": 76.87, "SOFI": 32.73, "V": 414.60}  # official 52-week (intraday) high from the drawdown plan; older than the 50-session window
VOL_OVERRIDE = {"SOFI": 0.53}  # only 10 weekly closes in the file; 50-session daily-return volatility instead
# ticker: (testing_now, zone1, zone2, ceiling1, ceiling2)
ZONES = {
 "VST":  ((136, 141), (124, 131), (115, 122), (146, 150), (154, 155)),   # 4 Nov: 146–150 broke (weekly close 138.37) -> ceiling; price inside the old Zone 1 at the 52-week closing low (136.21, 7 sources) -> "testing"; nothing structural below -> Zone 1 is a volatility band
 "NEE":  ((81.9, 82.1), (79.2, 80.6), (75.4, 76.7), (84.0, 84.4), (87.6, 87.6)),   # 28 Oct: rallied off the old Zone 1 after results; new shelf 81.9–82.1 (22–26 Oct closes); old Zone 1 becomes Zone 2
 "NVDA": ((204, 210), (192, 199), (173, 179), (212, 218), (219.6, 221.1)),  # 4 Nov: 212–218 broke (weekly close 204.64) -> ceiling; price inside the old Zone 1 with the 40-week average (204.15) -> "testing"; Zone 1/2 = weekly swing-close clusters (195.5, 176.1)
 "TSM":  ((406, 417), (393, 404), (373, 387), (422, 428), (440, 446)),   # 4 Nov: 422–428 broke (weekly close 406.13) -> ceiling; price at the foot of the old Zone 1 -> "testing"; Zone 1 = old Zone 2 with the 40-week average (401.1) and the 399.75 swing; Zone 2 a volatility band
 "GOOGL":((271, 280), (255, 265), (227, 237), (301, 310), (319, 328)),   # 4 Nov: 319–328 and 301–310 both broke (weekly close 279.84) -> ceilings; price inside the old Zone 2 -> "testing"; Zone 1 = the 52-week closing low (259.92); Zone 2 a volatility band
 "UNP":  ((285, 286), (272, 278), (262, 270), (289, 293), (306, 314)),
 "NU":   ((None, None), (10.9, 11.7), (9.5, 10.3), (14.2, 14.4), (15.6, 16.2)),  # 28 Oct: both zones broke on the 26 Oct election gap (12.59, 12.40); no structure below -> volatility bands; watch only (V replaced NU, 27 Oct)
 "MCD":  ((234, 235), (229, 233), (218, 222), (242, 250), (286, 287)),
 "NBIS": ((148, 160), (105, 118), (80, 90), (168, 175), (175, 183)),       # 4 Nov: 168–175 broke (weekly close 154.14) -> ceiling; price inside the old Zone 1 -> "testing" (2 Nov close 141.39 below it, not a weekly close); Zone 1 = old Zone 2 (weekly swing close 100.8 below); Zone 2 = the 85.2 cluster (5 sources)
 "AMD":  ((None, None), (451, 488), (383, 408), (606, 620), (648, 658.5)),
 "CEG":  ((250, 256), (242, 250), (206, 222), (264, 271), (286, 301)),      # 21 Oct: 264–271 broke (closes 263.19, 258.84) -> ceiling; now at the 52-week closing low 250.55
 "MU":   ((800, 845), (734, 784), (564, 615), (888, 903), (978, 1003)),   # 4 Nov: 888–903 broke (weekly close 884.74) -> ceiling; the 836 swing sits in the old Zone 1 -> "testing"; Zone 1 = the 40-week average (758.9); Zone 2 a volatility band
 "TLN":  ((334, 344), (302, 321), (283, 297), (349, 356), (374, 391)),   # 4 Nov: 349–356 broke (weekly close 343.12) -> ceiling (3 Nov close 357.28 back above it; a Friday close above restores it); testing = the 341.4 cluster (6 sources)
 "AVGO": ((None, None), (314, 325), (295, 306), (336, 343), (357, 368)),    # 21 Oct: 336–343 broke (weekly close 328.75) -> ceiling
 "QQQ":  ((680, 690), (648, 665), (606, 621), (700, 709), (714, 718)),   # 4 Nov: 714–718 and 700–709 broke (weekly close 690.49) -> ceilings; testing = the 40-week average (680.4) and the −10% line (686.57); Zone 1 starts at the −15% drawdown line (648.43); Zone 2 = weekly swing closes (~613)
 "IREN": ((23.7, 24.5), (20.0, 22.5), (12.0, 15.0), (25.6, 27.0), (28.8, 30.5)),  # 4 Nov: 25.6–27 broke (weekly close 23.95, the 52-week closing low) -> ceiling; testing = the 52-week lows (23.72 intraday, 23.95 close); 2 Nov close 22.02 inside Zone 1
 "APLD": ((17.6, 18.4), (15.5, 17.2), (11.5, 13.3), (20.1, 20.4), (26.9, 27.0)),  # added 21 Oct; 28 Oct: 17.6–18.4 held (17.50 low, 26 Oct)
 "SOFI": ((15.67, 16.02), (15.25, 15.84), (13.86, 14.6), (16.55, 17.14), (18.3, 18.4)),  # added 28 Oct: results gap 26->27 Oct (14.46 -> 16.40, 160M shares); Zone 1 = early-Oct shelf / top of the gap; Zone 2 = gap filled, the 52-week low (13.86, 15 Oct)
 "V":    ((397, 402), (375.3, 382.7), (356.1, 363.5), (407, 410), (414.6, 414.6)),  # added 28 Oct: Zone 1 = Sept swing lows + volume shelf; Zone 2 = 40-week-average cluster; ceiling = the 22 Oct record
}
rng = np.random.default_rng(20261015)
def ptouch(last, lvl, vol, days=63, n=20000):
    if lvl >= last: return 1.0
    sd = vol / math.sqrt(252)
    z = rng.standard_normal((n, days)) * sd - 0.5 * sd * sd
    return float((last * np.exp(np.cumsum(z, axis=1))).min(axis=1).__le__(lvl).mean())
out = {}
for t, (tn, z1, z2, c1, c2) in ZONES.items():
    m = mech[t]; last = m["last_close"]; vol = VOL_OVERRIDE.get(t, m["vol_annual"]); hi = HIGH_OVERRIDE.get(t, m["high_52w"])
    try: eps = float(fund[t]["price_usd"]) / float(fund[t]["fwd_pe"])
    except Exception: eps = None
    def z(b):
        mid = (b[0] + b[1]) / 2
        return {"band": b, "from_last_pct": round(100 * (b[1] / last - 1), 1), "from_high_pct": round(100 * (mid / hi - 1), 1),
                "fwd_pe": round(mid / eps, 1) if eps else None, "p_touch_13w": round(ptouch(last, b[1], vol), 2)}
    out[t] = {"last": last, "high_52w": hi, "vol": vol, "fwd_pe_now": round(last / eps, 1) if eps else None,
              "testing_now": tn, "zone1": z(z1), "zone2": z(z2), "ceiling1": c1, "ceiling2": c2,
              "ceiling1_pct": round(100 * (c1[0] / last - 1), 1)}
json.dump(out, open(os.path.join(ROOT, "analysis", "capture_zones_final.json"), "w"), indent=1)
for t, r in out.items():
    print(t, r["last"], r["high_52w"], f"{r['vol']:.0%}", r["fwd_pe_now"], "|Z1", r["zone1"], "|Z2", r["zone2"], "|C1", r["ceiling1"], r["ceiling1_pct"])
