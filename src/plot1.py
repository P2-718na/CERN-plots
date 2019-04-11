import ROOT
import json

try:
    loaded
except NameError:
    loaded = False
    days = []

if not loaded:
    with open('../allreqs2018-12.json') as f:
        data = json.load(f)
    loaded = True
    days = [int(i["t"][8:10]) for i in data]

h = ROOT.TH1I("Logged events","Logged events per day (Dec 2018);Time (days);Events", 31, 1, 32)
h.SetFillColor(212)
h.SetLineWidth(2)
h.SetLineColor(210)
c = ROOT.TCanvas()
for e, i in enumerate(days):
    h.Fill(i)

h.Draw()
c.Draw()

print "Done"