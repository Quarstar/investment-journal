"""Final capture zones (judgment overlay on capture_zones.py output), with the stats for each band.
Zones as of the 17 Nov 2026 close, re-mapped on the 13 Nov weekly closes (first map: 14 Oct; previous: 10 Nov). Edit ZONES each Wednesday when a zone breaks or the map steps up."""
import json, math, os, csv
import numpy as np
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
mech = json.load(open(os.path.join(ROOT, "analysis", "capture_zones_output.json")))
fund = {r["ticker"]: r for r in csv.DictReader(open(os.path.join(ROOT, "data", "fundamentals_2026-10-13.csv")))}
HIGH_OVERRIDE = {"NBIS": 299.86, "IREN": 76.87, "SOFI": 32.73}  # official 52-week (intraday) high from the drawdown plan; older than the 50-session window
VOL_OVERRIDE = {"SOFI": 0.53}  # only 10 weekly closes in the file; 50-session daily-return volatility instead
# ticker: (testing_now, zone1, zone2, ceiling1, ceiling2)
ZONES = {
 "VST":  ((124, 131), (115, 122), (106, 112), (136, 141), (146, 150)),   # 11 Nov: 136–141 broke (weekly close 124.80) -> ceiling; testing = the old Zone 1 with the new 52-week closing low (124.80); Zone 1 = old Zone 2 (11.6×); Zone 2 = the 110.89 daily swing low (10.8×)
 "NEE":  ((81.9, 82.1), (79.2, 80.6), (75.4, 76.7), (84.0, 84.4), (87.6, 87.6)),   # 28 Oct: rallied off the old Zone 1 after results; new shelf 81.9–82.1 (22–26 Oct closes); old Zone 1 becomes Zone 2
 "NVDA": ((149, 162), (137, 146), (123, 134), (165, 173), (173, 179)),  # 18 Nov: 165–173 broke (weekly close 162.85) -> ceiling; testing = old Zone 1 with the 12 Nov swing low (148.80) and the 17 Nov 52-week closing low (155.46); Zone 1 = old Zone 2 (11.6×); Zone 2 a volatility band (10.6×): no structure below
 "TSM":  ((393, 404), (373, 387), (342, 360), (406, 417), (422, 428)),   # 11 Nov: 406–417 broke (weekly close 375.44, inside the old Zone 2, which held) -> ceiling; testing = old Zone 1 with the 40-week average (402.2); Zone 1 = old Zone 2; Zone 2 = the 351.19 swing (15.5×)
 "GOOGL":((271, 280), (255, 265), (227, 237), (301, 310), (319, 328)),   # 4 Nov: 319–328 and 301–310 both broke (weekly close 279.84) -> ceilings; price inside the old Zone 2 -> "testing"; Zone 1 = the 52-week closing low (259.92); Zone 2 a volatility band
 "UNP":  ((285, 286), (272, 278), (262, 270), (289, 293), (306, 314)),
 "NU":   ((None, None), (10.9, 11.7), (9.5, 10.3), (14.2, 14.4), (15.6, 16.2)),  # 28 Oct: both zones broke on the 26 Oct election gap (12.59, 12.40); no structure below -> volatility bands; watch only (V replaced NU, 27 Oct)
 "MCD":  ((271, 276), (263.5, 271), (242, 250), (283.5, 287), (341, 341)),  # 18 Nov: stepped up after a second Friday above 250 (276.52, 271.97): testing = the 8 May weekly swing close (275.75) and the 13 Nov close; Zone 1 = Jun/Jul swing closes (267.3); Zone 2 = old ceiling with the volume shelf (248.1); ceilings = the 10 Nov swing high (283.5) with the old 286–287 band, then the 52-week high
 "NBIS": ((102, 115), (80, 90), (55, 67), (125, 135), (148, 160)),       # 18 Nov: 125–135 broke (weekly close 115.88) -> ceiling; testing = old Zone 1 with the 12–17 Nov low (102.25); Zone 1 = old Zone 2 (the 52-week closing low 83.26 / 86.4 cluster, 6 sources); Zone 2 a volatility band
 "AMD":  ((None, None), (451, 488), (383, 408), (606, 620), (648, 658.5)),
 "CEG":  ((250, 256), (242, 250), (206, 222), (264, 271), (286, 301)),      # 21 Oct: 264–271 broke (closes 263.19, 258.84) -> ceiling; now at the 52-week closing low 250.55
 "MU":   ((650, 690), (567, 634), (417, 484), (734, 784), (800, 845)),   # 18 Nov: 800–845 broke (weekly closes 690.00 on 6 Nov, 778.31 on 13 Nov) -> ceiling; testing = the 5 Nov swing low (650) and the 6 Nov weekly close; 734–784 (the 40-week average 775) is the first ceiling; Zones 1/2 volatility bands
 "TLN":  ((334, 344), (302, 321), (283, 297), (349, 356), (374, 391)),   # 4 Nov: 349–356 broke (weekly close 343.12) -> ceiling (3 Nov close 357.28 back above it; a Friday close above restores it); testing = the 341.4 cluster (6 sources)
 "AVGO": ((None, None), (314, 325), (295, 306), (336, 343), (357, 368)),    # 21 Oct: 336–343 broke (weekly close 328.75) -> ceiling
 "QQQ":  ((645, 665), (604, 622), (562, 596), (680, 690), (700, 709)),   # 11 Nov: 680–690 broke (weekly close 656.10) -> ceiling; testing holds the 5 Nov close (647.05) and the −15% line on the highest close ($645.71); Zone 1 = weekly swing closes (613.4, ~−19%); Zone 2 = 562.6–596 (52-week low, contains the −25% line $569.75)
 "IREN": ((15.0, 17.5), (11.5, 14.25), (7.6, 10.3), (20.0, 22.5), (23.7, 24.5)),  # 18 Nov: 20–22.5 broke (weekly close 18.17) -> ceiling; testing = old Zone 1 (17 Nov 52-week closing low 15.81); Zones 1/2 volatility bands
 "APLD": ((13.1, 14.3), (11.5, 13.1), (8.7, 10.5), (15.5, 17.2), (17.6, 18.4)),  # 18 Nov: 17.6–18.4 broke (weekly closes 15.55, 15.97) -> ceiling; testing = the 5 Nov swing low (13.11) and the 17 Nov 52-week closing low (14.22); Zone 1 = old Zone 2; Zone 2 a volatility band
 "SOFI": ((13.86, 14.6), (12.7, 13.5), (11.1, 11.9), (15.25, 16.02), (16.55, 17.14)),  # 18 Nov: 15.67–16.02 broke (weekly close 15.42) and the 17 Nov close (14.28, a 52-week closing low) sits in the old Zone 2 -> testing; old testing + Zone 1 merge into the first ceiling; Zones 1/2 volatility bands
 "V":    ((407, 414.6), (394, 402), (375.3, 382.7), (436, 442.2), (442.2, 442.2)),  # 18 Nov: stepped up after a second Friday above 410 (422.65, 425.76): old ceilings -> testing (with the 6 Nov swing low 412.75); old testing + the 28 Oct swing low (394) -> Zone 1; old Zone 1 -> Zone 2; ceiling = the 5 Nov record 442.23
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
