import numpy as np
import matplotlib.pyplot as plt
import sys
import re

arr = []
shortForms = ["gu", "g","me","mes","wc"]
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
    _l = [str(x[0]) + "="+str(x[1]) for x in zip( shortForms,n)]
    del _l[2]
    plt.plot(res,label=" ".join(_l))
#plt.axis([ 0, 10000,-10,0])
plt.legend(bbox_to_anchor=(1,1), loc="lower center")
plt.ylabel('Moving average ep reward')
plt.xlabel('Step')
plt.tight_layout() 
plt.savefig("outSingle.png")
