import json
import ROOT

try:
    loaded
except NameError:
    loaded = False
    data = {}
    r = {}
    r['PrepareToGet'] = r['Get'] = r['Put'] = 0


if not loaded:
    with open('allreqs2018-12-parsed.json') as f:
        data = json.load(f)
    loaded = True
    for l in data:
        if l['r'] == 'PutDone':
            continue
        r[l['r']] += 1




t0 = data[0]['t']
tN = data[-1]['t']
h = {}
hstack = ROOT.THStack("stacked", "Requests distribution")
for r in ['Get', 'Put', 'PrepareToGet']:
    h[r] = ROOT.TH1I("myHisto","Requests distribution;t;count",
                     720, t0, tN)
    hstack.Add(h[r])

for l in data:
    if l['r'] == 'PutDone':
        continue
    h[l['r']].Fill(l['t'])


c = ROOT.TCanvas()
c.SetGrid()
h['Get'].SetFillColor(ROOT.kBlue)
h['PrepareToGet'].SetFillColor(ROOT.kRed)
h['Put'].SetFillColor(ROOT.kGreen)
hstack.Draw("nostack")
c.Draw()
print "Done"