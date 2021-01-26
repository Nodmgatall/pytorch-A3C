GLOBAL_UPDATE = [ 4,8,10,15 ]
G = [ x  / 10.0 for x in range(7,9)]
MaxEpisodes = [ 10000 ]
MaxEpStep = [150,250, 350, 450]
WorkerCount = [10,8,6,4]

import os
os.system('cmd /k "Your Command Prompt Command"')

for gup in GLOBAL_UPDATE:
    for g in G:
        for me in MaxEpisodes:
            for mes in MaxEpStep:
                for wc in WorkerCount:
                    s = "python continuous_A3C.py {} {:f} {} {} {}".format(gup,g,me,mes,wc)
                    print(s)

