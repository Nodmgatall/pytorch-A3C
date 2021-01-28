import numpy as np
import matplotlib.pyplot as plt
import sys
import re
import glob
import argparse
from multi_key_dict import multi_key_dict
import matplotlib

GLOBAL_UPDATE = [ 4,5,8,10,15 ]
G = [ x  / 10.0 for x in range(7,9) ]+[ 0.85, 0.875,0.9,0.95]
MaxEpisodes = [ 10000 ]
MaxEpStep = [150,250, 350, 450]
WorkerCount = [30,20,10,8,6,5,4]
shortForms = ["gu", "g","me","mes","wc"]

colors = matplotlib.cm.tab20(range(20))
markers = matplotlib.lines.Line2D.markers.keys()
def createDefs():
    l = []
    for x in colors:
        for y in markers:
            l.append([x,y])
    return l

usedDef = 0

def genP():
    p = []
    for gu in GLOBAL_UPDATE:
        for g in G:
            for me in MaxEpisodes:
                for mes in MaxEpStep:
                    for wc in WorkerCount:
                        p.append(tuple([float(gu),float(g),float(me),float(mes),float(wc)]))
    return p

p = genP()
defs = createDefs()

cnt= 0
colorSchemes= {key : None for key in p}
for x in colorSchemes:
    colorSchemes[x] = defs[cnt * 42 % len(defs)]
    cnt +=1

parser = argparse.ArgumentParser(description='Plot various run comparisons.')
parser.add_argument('--folder', type=str,
                    help='folder to search for *.npy files')

args = parser.parse_args()
folderName = args.folder +  "/" if args.folder else ""

numberPlots = 0
def get(a,b,c,d,e):
    return a,b,c,d,e
def combi( gu = "*", g  = "*", me = "*", mes = "*", wc = "*"):
    global numberPlots
    numberPlots +=1
    s_gu = "GlobalUpdateIter_" + gu
    s_g  = "Gamma" + g
    s_me = "MaxEp_" + me
    s_mes = "MaxEpStep_" + mes
    s_wc = "WorkerCount_" + wc
    a = ["-",s_gu,"-", s_g,"-", s_me,"-", s_mes,"-", s_wc]
    gl = folderName  + "continuous" + "".join(a) + ".npy"
    files = glob.glob(gl)
    ret = []
    for x in files:
        f = np.load(x)
        n = [float(s) for s in re.findall(r'-?\d+\.?\d*', x)]
        ret.append([f/int(n[-2]), n])

    return ret

def complexCombi( gu = ["*"], g  = ["*"], me = ["*"], mes = ["*"], wc = ["*"]):
    combis = []
    for a in gu:
        for b in g:
            for c in me:
                for d in mes:
                    for e in wc:
                        combis.append([a,b,c,d,e])

    res = combi(*combis[0])
    for x in combis[1:]:
        res += combi(*x)

    return res



files = [
 combi(gu="4",wc="*", mes="*"),
 combi(gu="8",wc="*", mes="*"),
 combi(gu="10",wc="*", mes="*"),
 combi(gu="15",wc="*", mes="*")]

files = [
 combi(gu="*",wc="4", mes="*"),
 combi(gu="*",wc="6", mes="*"),
 combi(gu="*",wc="8", mes="*"),
 combi(gu="*",wc="10", mes="*")]

files = [
 complexCombi(gu=["15","10"],g=["0.95"],wc=["10","8"], mes=["350","150"]),
 complexCombi(gu=["15","10"],g=["0.7"],wc=["10","8"], mes=["150"]),
 complexCombi(gu=["15","10"],g=["0.7"],wc=["10","8"], mes=["250"]),
 complexCombi(gu=["15","10"],g=["0.7"],wc=["10","8"], mes=["350"]),
 complexCombi(gu=["15","10"],g=["0.7"],wc=["10","8"], mes=["450"]),
 complexCombi(gu=["15","10"],g=["0.9"],wc=["10","8"], mes=["350","150"]),
 complexCombi(gu=["15","10"],g=["0.8"],wc=["10","8"], mes=["150"]),
 complexCombi(gu=["15","10"],g=["0.8"],wc=["10","8"], mes=["250"]),
 complexCombi(gu=["15","10"],g=["0.8"],wc=["10","8"], mes=["350"]),
 complexCombi(gu=["15","10"],g=["0.8"],wc=["10","8"], mes=["450"])]

#files = [
# complexCombi(gu=["10"],g=["0.95"],wc=["10","8"], mes=["350","150"]),
# complexCombi(gu=["10"],g=["0.7"],wc=["10","8"], mes=["350","150"]),
# complexCombi(gu=["10"],g=["0.9"],wc=["10","8"], mes=["350","150"]),
# complexCombi(gu=["10"],g=["0.8"],wc=["10","8"], mes=["350","150"])]

#USED IN PAPER
#files = [
# complexCombi(gu=["15","10"],g=["0.8"],wc=["10","4"], mes=["150"]),
# complexCombi(gu=["15","10"],g=["0.8"],wc=["10","4"], mes=["250"]),
# complexCombi(gu=["15","10"],g=["0.8"],wc=["10","4"], mes=["350"]),
# complexCombi(gu=["15","10"],g=["0.8"],wc=["10","4"], mes=["450"])]
##

##USED IN PAPER
#files = [
# complexCombi(gu=["15","4"],g=["0.7"],wc=["10","4"], mes=["150"]),
# complexCombi(gu=["15","4"],g=["0.7"],wc=["10","4"], mes=["250"]),
# complexCombi(gu=["15","4"],g=["0.7"],wc=["10","4"], mes=["350"]),
# complexCombi(gu=["15","4"],g=["0.7"],wc=["10","4"], mes=["450"])]


##USED IN PAPER
files = [
 complexCombi(gu=["15","10"],g=["0.9"],wc=["10","8"], mes=["150"]),
 complexCombi(gu=["15","10"],g=["0.9"],wc=["10","8"], mes=["350"]),
 complexCombi(gu=["15","10"],g=["0.95"],wc=["10","8"], mes=["150"]),
 complexCombi(gu=["15","10"],g=["0.95"],wc=["10","8"], mes=["350"])]

files = [
 complexCombi(gu=["15","10"],g=["0.9"],wc=["10","8"], mes=["150"]),
 complexCombi(gu=["15","10"],g=["0.9"],wc=["10","8"], mes=["350"]),
 complexCombi(gu=["15","10"],g=["0.95"],wc=["10","8"], mes=["150"]),
 complexCombi(gu=["15","10"],g=["0.95"],wc=["10","8"], mes=["350"])]

#files = [
# complexCombi(g=["0.8"] , wc=["10"], mes=["350","450"] )  ,
# complexCombi(g=["0.8"] , wc=["8"] , mes=["350","450"] )  ,
# complexCombi(g=["0.8"] , wc=["4"] , mes=["350","450"] )  ,
# complexCombi(g=["0.8"] , wc=["10"], mes=["350","450"] )  ,
# complexCombi(g=["0.8"] , wc=["8"] , mes=["350","450"] )  ,
# complexCombi(g=["0.8"] , wc=["4"] , mes=["350","450"] )  ,
# complexCombi(g=["0.8"] , wc=["10"], mes=["350","450"] )  ,
# complexCombi(g=["0.8"] , wc=["8"] , mes=["350","450"] )  ,
# complexCombi(g=["0.8"] , wc=["4"] , mes=["350","450"] )]
#
files = [
 complexCombi(g=["0.8","0.9","0.95"] , wc=["10"], mes=["150"] )  ,
 complexCombi(g=["0.8","0.9","0.95"] , wc=["8"] , mes=["150"] )  ,
 complexCombi(g=["0.8","0.9","0.95"] , wc=["4"] , mes=["150"] )  ,
 complexCombi(g=["0.8","0.9","0.95"] , wc=["10"], mes=["350"] )  ,
 complexCombi(g=["0.8","0.9","0.95"] , wc=["8"] , mes=["350"] )  ,
 complexCombi(g=["0.8","0.9","0.95"] , wc=["4"] , mes=["350"] )  ,
 complexCombi(g=["0.8","0.9","0.95"] , wc=["10"], mes=["450"] )  ,
 complexCombi(g=["0.8","0.9","0.95"] , wc=["8"] , mes=["450"] )  ,
 complexCombi(g=["0.8","0.9","0.95"] , wc=["4"] , mes=["450"] )]

files = [
 complexCombi(gu=["10","5","15"],g=["0.85"] , wc=["10"], mes=["350"] )  ,
 complexCombi(gu=["10","5","15"],g=["0.85"] , wc=["20"] , mes=["350"] ),
 complexCombi(gu=["10","5","15"],g=["0.85"] , wc=["30"] , mes=["350"] ),
 complexCombi(gu=["10","5","15"],g=["0.9"] , wc=["10"], mes=["350"] )  ,
 complexCombi(gu=["10","5","15"],g=["0.9"] , wc=["20"] , mes=["350"] ),
 complexCombi(gu=["10","5","15"],g=["0.9"] , wc=["30"] , mes=["350"] )]



numPlots = len(files)
fig, ax = plt.subplots(2,int(3), sharey=True, sharex=True)
matplotlib.rcParams['lines.linewidth'] = 0.75
numRow = 3
labels = []
for x in range(0, len(ax)):
    for y in range(0,numRow):
        for z in files[(x * numRow)+y ]:
            file = z
            print(file[1])
            print(file[0])
            colorScheme = colorSchemes[tuple(file[1])]
            labels.append(file[1])
            _l = [str(x[0]) + "="+str(x[1]) for x in zip( shortForms,file[1])]
            del _l[2]
            l = " ".join(_l)
            ax[x,y].set_ylim([-8,-0.05])
            ax[x,y].plot(file[0],color=colorScheme[0],label=l, marker=colorScheme[1],markevery=700,ms=4)
            ax[x,y].axes.xaxis.set_visible(False)
            ax[x,y].legend(bbox_to_anchor=(1,0), loc="upper right",fontsize=4)
plt.tight_layout()
plt.savefig("out.png", dpi=200)

