# What's this?
This is a piece of code that uses Python and CERN's PyROOT library to plot data on a graph. It was written during my
IT stage at CERN. The produced graphs are like these:

 plot1.py                      | plot2.py
:-----------------------------:|:-----------------------------:
 ![plot1](plot1.png "Plot 1")  |  ![plot2](plot2.png "Plot 2")

### In particular:
- `plot1.py` plots the number of requests received each day
- `plot2.py` plots the type of requests received by timestamp
- `plot3.py` plots the type of requests received by experiment

---

# How to use:

### First method (best):
1. Install [Python 2.7](https://www.python.org/downloads/release/python-272/) on your machine
1. Install ROOT library from [CERN's official website](https://root.cern.ch/downloading-root)
1. Clone this repo and cd into the src folder
    ```
    git clone https://github.com/P2-718na/CERN-plots.git
    cd CERN-plots/src
    ```
1. Get some data. I couldn't upload the whole dataset i used to make the graphs (400MB), but you
can use `sample.json` and `sample-parsed.json` in the `samples` folder to get an idea.
1. Open a Python console and run the program
    ```
    python
    execfile("plot[1|2|3].py")
    ```
1. If you want to make changes to the graph, re-run
    `execfile("plot[1|2|3].py")`  
    without closing the Python console (it will be faster, since you won't have to re-read the whole dataset)

### Second method (fastest):
- If you are a CERN employee, you can download the `plot1.ipynb` notebook, upload it to CERNbox and run it using SWAN
- If you are *not* a CERN employee, you can still view the notebook using
[Jupyter notebook viewer](https://nbviewer.jupyter.org/github/P2-718na/CERN-plots/blob/master/plot1.ipynb)

---
 
