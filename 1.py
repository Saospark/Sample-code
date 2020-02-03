import numpy as np
import math
from scipy.stats import spearmanr

def Edist(a,b):
    dist=0
    for i in range(len(a)):
        dist+=(a[i]-b[i])**2
    return math.sqrt(dist)

def parsestrings(infile):
    file=infile.read()
    list=file.split('\n')
    for i in list:
        if i =='':
            list.remove(i)
    return list[0:]
k=100
scrna=np.loadtxt('scrnaintegratedafter38.txt')
merfish=np.loadtxt('merfishintegratedafter38.txt')
matchdist=[]
print(len(scrna),len(scrna[0]))
for i in range(1000):
    print(i)
    index=0
    distlist=[]
    corr, p_value = spearmanr(merfish[i],scrna[0])
    distdict={}
    distdict[corr]=0
    for j in range(1,len(scrna)):
        corr, p_value = spearmanr(merfish[i],scrna[j])
        distdict[corr]=j
        if len(distlist)<k:
            distlist.append(corr)
        else:
            distlist.sort()
            if corr>distlist[0]:
                distlist[0]=corr
    distlist.sort()
    matchlist=np.zeros((k,len(merfish[0])))
    for i in range(len(distlist)):
        matchlist[i]=(scrna[distdict[distlist[i]]])
    med=np.median(matchlist,axis=0)
    corr, p_value = spearmanr(merfish[i],med)
    matchdist.append(corr)
file=open('1000after38mediandist.txt','w')
for i in matchdist:
    file.write(str(i)+'\n')
file.close()
