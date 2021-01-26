import numpy as np
import matplotlib.pyplot as plt
import sys
import re

# 100 run
#files = [ "continuous_20_0.9_10000_100.npy",  "continuous_rerun1_5_0.9_10000_100.npy", "continuous_rerun2_5_0.9_10000_100.npy", "continuous_rerun3_5_0.9_10000_100.npy", "continuous_rerun4_5_0.9_10000_100.npy"]

#inital runs
#files = [ "continuous_5_0.9_10000_100.npy", "continuous_5_0.9_10000_150.npy", "continuous_5_0.9_10000_200.npy", "continuous_5_0.9_10000_250.npy", "continuous_5_0.9_10000_300.npy"]

#long
files = [ "continuous_5_0.9_48000_200.npy" ]
arr = []

if len(sys.argv) == 1:
    arr = files;

elif sys.argv[1].isdigit():
    arr = sys.argv[2:]
else:
    arr = sys.argv[1:]

for x in arr:
    n = [float(s) for s in re.findall(r'-?\d+\.?\d*', x)]
    res = np.load(x)
    res = res / n[-2]
    plt.plot(res,label=x)
#plt.axis([ 0, 10000,-10,0])
plt.legend(bbox_to_anchor=(1,1), loc="lower center")
plt.ylabel('Moving average ep reward divided by iteration length')
plt.xlabel('Step')
plt.tight_layout() 
plt.show()
