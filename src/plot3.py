import json
import ROOT

try:
    loaded
except NameError:
    loaded = False
    data = {}
    experiments = []

if not loaded:
    with open("../allreqs2018-12-parsed.json") as f:
        data = json.load(f)
    loaded = True
    experiments = list(set([i["cls"] for i in data]))

histograms = {}
hstack = ROOT.THStack("hs", "Distribution of CASTOR requests across experiments")
for i in ["Get", "Put", "PrepareToGet", "PutDone"]:
    histograms[i] = ROOT.TH1I("myHisto"+i, "Requests distribution;t;count", 14, 0, 0)
    hstack.Add(histograms[i])

classes = []
for i in data:
    histograms[i["r"]].Fill(i["cls"], 1)
    classes.append(i["cls"])


c = ROOT.TCanvas()
c.SetGrid()
histograms["Get"].SetFillColor(ROOT.kBlue)
histograms["PrepareToGet"].SetFillColor(ROOT.kRed)
histograms["Put"].SetFillColor(ROOT.kGreen)
histograms["PutDone"].SetFillColor(ROOT.kYellow)
hstack.Draw("nostackb")
c.Draw()

print "Done"
