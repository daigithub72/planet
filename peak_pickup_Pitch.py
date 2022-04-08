import pandas as pd
from scipy.signal import argrelmax
from scipy.signal import argrelmin
import numpy as np
import matplotlib.pyplot as plt


df=pd.read_excel("pickup.xlsx")

t=df["Time(s)"]
Pitch=df["Pitch.1"]
Pitch=np.array(Pitch)

maxid=argrelmax(Pitch,order=1)
minid=argrelmin(Pitch,order=200)

print(maxid)
print(maxid[0])
print(maxid[0].shape[0])
print(Pitch[maxid[0][0]])

n=maxid[0].shape[0]
m=minid[0].shape[0]

for i in range(n):
    print(Pitch[maxid[0][i]])

print(minid[0])
print(minid[0].shape[0])

for i in range(m):
    print(Pitch[minid[0][i]])

plt.rcParams["font.family"]="Times New Roman"
plt.rcParams["mathtext.fontset"]="stix"
plt.rcParams["font.size"]=20
plt.rcParams["xtick.direction"]="in"
plt.rcParams["ytick.direction"]="in"
plt.rcParams["legend.edgecolor"]="black"
plt.rcParams["legend.framealpha"]=1
plt.rcParams["legend.fontsize"]=12
plt.rcParams["figure.autolayout"]=True
plt.rcParams["axes.grid"]=True

plt.plot(t,Pitch)
plt.scatter(t[maxid[0]]-t[0],Pitch[maxid])
#plt.scatter(t[np.where(Pitch[maxid]>2)[0]],Pitch[np.where(Pitch[maxid]>2)[0]])
plt.scatter(t[minid[0]],Pitch[minid])
plt.xlabel("Time [s]")
#plt.ylabel("Time [s]")
plt.show()
print(t[maxid[0]])
print(Pitch[maxid])
print(np.where(Pitch[maxid]>3)[0])
print("=======")
print(t[np.where(Pitch[maxid]>3)[0]])

#with pd.ExcelWriter('pickupresult.xlsx') as writer:
    #t[maxid[0]].to_excel(writer,sheet_name='result')
    #t[np.where(Pitch[maxid]>3)].to_excel(writer,sheet_name='result')
