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
    for e in data:
        if e['r'] == 'PutDone':
            continue
        r[e['r']] += 1

h = ROOT.TH3I()


c = ROOT.TCanvas()
c.SetGrid()
h['Get'].SetFillColor(ROOT.kBlue)
h['PrepareToGet'].SetFillColor(ROOT.kRed)
h['Put'].SetFillColor(ROOT.kGreen)
hstack.Draw("nostack")
c.Draw()
print "Done"