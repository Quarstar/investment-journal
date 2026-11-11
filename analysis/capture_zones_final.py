"""Final capture zones (judgment overlay on capture_zones.py output), with the stats for each band.
Zones as of the 10 Nov 2026 close, re-mapped on the 6 Nov weekly closes (first map: 14 Oct; previous: 3 Nov). Edit ZONES each Wednesday when a zone breaks or the map steps up."""
import json, math, os, csv
import numpy as np
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
mech = json.load(open(os.path.join(ROOT, "analysis", "capture_zones_output.json")))
fund = {r["ticker"]: r for r in csv.DictReader(open(os.path.join(ROOT, "data", "fundamentals_2026-10-13.csv")))}
HIGH_OVERRIDE = {"NBIS": 299.86, "IREN": 76.87, "SOFI": 32.73, "V": 414.60}  # official 52-week (intraday) high from the drawdown plan; older than the 50-session window
VOL_OVERRIDE = {"SOFI": 0.53}  # only 10 weekly closes in the file; 50-session daily-return volatility instead
# ticker: (testing_now, zone1, zone2, ceiling1, ceiling2)
ZONES = {
 "VST":  ((124, 131), (115, 122), (106, 112), (136, 141), (146, 150)),   # 11 Nov: 136–141 broke (weekly close 124.80) -> ceiling; testing = the old Zone 1 with the new 52-week closing low (124.80); Zone 1 = old Zone 2 (11.6×); Zone 2 = the 110.89 daily swing low (10.8×)
 "NEE":  ((81.9, 82.1), (79.2, 80.6), (75.4, 76.7), (84.0, 84.4), (87.6, 87.6)),   # 28 Oct: rallied off the old Zone 1 after results; new shelf 81.9–82.1 (22–26 Oct closes); old Zone 1 becomes Zone 2
 "NVDA": ((165, 173), (152, 162), (137, 146), (173, 179), (192, 199)),  # 11 Nov: 204–210 and 192–199 broke (weekly close 186.64); 10 Nov close 168.89 under the old Zone 2 -> 173–179 is now the first ceiling; testing = the 52-week lows (164.27 intraday, 167.52 close); Zones 1/2 are volatility bands (12.9×, 11.6×): no structure below
 "TSM":  ((393, 404), (373, 387), (342, 360), (406, 417), (422, 428)),   # 11 Nov: 406–417 broke (weekly close 375.44, inside the old Zone 2, which held) -> ceiling; testing = old Zone 1 with the 40-week average (402.2); Zone 1 = old Zone 2; Zone 2 = the 351.19 swing (15.5×)
 "GOOGL":((271, 280), (255, 265), (227, 237), (301, 310), (319, 328)),   # 4 Nov: 319–328 and 301–310 both broke (weekly close 279.84) -> ceilings; price inside the old Zone 2 -> "testing"; Zone 1 = the 52-week closing low (259.92); Zone 2 a volatility band
 "UNP":  ((285, 286), (272, 278), (262, 270), (289, 293), (306, 314)),
 "NU":   ((None, None), (10.9, 11.7), (9.5, 10.3), (14.2, 14.4), (15.6, 16.2)),  # 28 Oct: both zones broke on the 26 Oct election gap (12.59, 12.40); no structure below -> volatility bands; watch only (V replaced NU, 27 Oct)
 "MCD":  ((234, 235), (229, 233), (218, 222), (242, 250), (286, 287)),
 "NBIS": ((125, 135), (105, 115), (80, 90), (148, 160), (168, 175)),       # 11 Nov: 148–160 broke (weekly close 129.49) -> ceiling; testing = the 6 Nov weekly close area; Zone 1 = the 107.06 cluster (2 sources) within the old Zone 1; Zone 2 = the 85.2 cluster (5 sources) unchanged
 "AMD":  ((None, None), (451, 488), (383, 408), (606, 620), (648, 658.5)),
 "CEG":  ((250, 256), (242, 250), (206, 222), (264, 271), (286, 301)),      # 21 Oct: 264–271 broke (closes 263.19, 258.84) -> ceiling; now at the 52-week closing low 250.55
 "MU":   ((800, 845), (734, 784), (564, 615), (888, 903), (978, 1003)),   # 4 Nov: 888–903 broke (weekly close 884.74) -> ceiling; the 836 swing sits in the old Zone 1 -> "testing"; Zone 1 = the 40-week average (758.9); Zone 2 a volatility band
 "TLN":  ((334, 344), (302, 321), (283, 297), (349, 356), (374, 391)),   # 4 Nov: 349–356 broke (weekly close 343.12) -> ceiling (3 Nov close 357.28 back above it; a Friday close above restores it); testing = the 341.4 cluster (6 sources)
 "AVGO": ((None, None), (314, 325), (295, 306), (336, 343), (357, 368)),    # 21 Oct: 336–343 broke (weekly close 328.75) -> ceiling
 "QQQ":  ((645, 665), (604, 622), (562, 596), (680, 690), (700, 709)),   # 11 Nov: 680–690 broke (weekly close 656.10) -> ceiling; testing holds the 5 Nov close (647.05) and the −15% line on the highest close ($645.71); Zone 1 = weekly swing closes (613.4, ~−19%); Zone 2 = 562.6–596 (52-week low, contains the −25% line $569.75)
 "IREN": ((20.0, 22.5), (15.0, 17.5), (9.7, 12.6), (23.7, 24.5), (25.6, 27.0)),  # 11 Nov: 23.7–24.5 broke (weekly close 21.64) -> ceiling; testing = old Zone 1 (10 Nov close 19.73 just under it, the 52-week closing low); Zone 1 = the 17.16 swing / volatility band; Zone 2 a volatility band
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
