"""Final capture zones (judgment overlay on capture_zones.py output), with the stats for each band.
Zones as of the 14 Oct 2026 close. Edit ZONES each Wednesday when a zone breaks or the map steps up."""
import json, math, os, csv
import numpy as np
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
mech = json.load(open(os.path.join(ROOT, "analysis", "capture_zones_output.json")))
fund = {r["ticker"]: r for r in csv.DictReader(open(os.path.join(ROOT, "data", "fundamentals_2026-10-13.csv")))}
HIGH_OVERRIDE = {"NBIS": 299.86}  # official 52-week (intraday) high from the drawdown plan; older than the 50-session window
# ticker: (testing_now, zone1, zone2, ceiling1, ceiling2)
ZONES = {
 "VST":  ((146, 150), (132, 141), (115, 122), (154, 155), (164, 169)),
 "NEE":  ((77.3, 77.7), (75.4, 76.7), (71.5, 72.8), (84.0, 84.4), (87.6, 87.6)),
 "NVDA": ((219.6, 221.1), (212, 218), (198, 204), (230, 234), (243, 243.4)),
 "TSM":  ((422, 428), (406, 417), (393, 404), (440, 446), (486, 487.5)),
 "GOOGL":((None, None), (334, 342), (298, 307), (352, 359), (400, 401)),
 "UNP":  ((285, 286), (272, 278), (262, 270), (289, 293), (306, 314)),
 "NU":   ((14.2, 14.4), (13.3, 13.9), (11.7, 12.4), (15.6, 16.2), (18.0, 18.0)),
 "MCD":  ((234, 235), (229, 233), (218, 222), (242, 250), (286, 287)),
 "NBIS": ((175, 183), (148, 160), (105, 118), (209, 221), (228, 237)),
 "AMD":  ((None, None), (451, 488), (383, 408), (606, 620), (648, 658.5)),
 "CEG":  ((264, 271), (242, 256), (206, 222), (286, 301), (310, 310)),
 "MU":   ((888, 903), (800, 845), (698, 743), (978, 1003), (1088, 1108)),
 "TLN":  ((349, 356), (324, 344), (283, 302), (374, 391), (436, 436)),
 "AVGO": ((336, 343), (314, 325), (295, 306), (357, 368), (446, 447)),
 "QQQ":  ((722, 723), (700, 709), (684, 688), (744, 752), (759.7, 762.9)),
}
rng = np.random.default_rng(20261015)
def ptouch(last, lvl, vol, days=63, n=20000):
    if lvl >= last: return 1.0
    sd = vol / math.sqrt(252)
    z = rng.standard_normal((n, days)) * sd - 0.5 * sd * sd
    return float((last * np.exp(np.cumsum(z, axis=1))).min(axis=1).__le__(lvl).mean())
out = {}
for t, (tn, z1, z2, c1, c2) in ZONES.items():
    m = mech[t]; last = m["last_close_14oct"]; vol = m["vol_annual"]; hi = HIGH_OVERRIDE.get(t, m["high_52w"])
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
