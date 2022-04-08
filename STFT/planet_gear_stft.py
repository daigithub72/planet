import soundfile as sf
import numpy as np
from scipy.fftpack import fft, ifft
from scipy import signal
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os
import pandas as pd

os.chdir("I:/1月12日")
path="Gcp1_Nr1000_Br0.3_キャリア慣性down_00010001.xlsx"

df=pd.read_excel(path)

print(df)

t=df["Unnamed: 0"]
T=df["Unnamed: 2"]

print(t)
print(T)

plt.plot(t,T)
plt.show()

samplerate=1/t.diff().mean()
print(samplerate)

def stft(data):
    f, t, Zxx=signal.stft(data,fs=samplerate,nperseg=500,
                          window="hann")
    Zxx=np.abs(Zxx)
    #Pxx=10*np.log10((Zxx/(20e-6))**2)
    Pxx=10*np.log10((Zxx/(np.max(Zxx)))**2)

    return f, t, Pxx

f, t, Pxx=stft(T)
df=np.mean(np.diff(f))
dt=np.mean(np.diff(t))
print("df=",df)
print("dt=",dt)
print(df*dt)

"""Zxx=np.power(Zxx,2)
Zoo=(20e-6)**2
Pxx=np.where(Zxx>0,10*np.log10(Zxx/Zoo),0)"""

"""Zoo=Zxx[:,:100]
Zfi=np.mean(Zoo,axis=1)
for i in range(Zxx.shape[1]):
    Zxx[:,i]-=Zfi"""

#Zxx=Zxx-Zfi

#Pxx=20*np.log10(Zxx/np.max(Zxx))#最大値で正規化
#Pxx=10*np.log10(Zxx/(20e-6)**2)#基準音圧で正規化

"""
Poo=Pxx[:,:100]
Pfi=np.mean(Poo,axis=1)
for i in range(Pxx.shape[1]):
    Pxx[:,i]-=Pfi
"""

plt.rcParams["font.family"]="Times New Roman"
plt.rcParams["mathtext.fontset"]="stix"
plt.rcParams["font.size"]=20
plt.rcParams["xtick.direction"]="in"
plt.rcParams["ytick.direction"]="in"
plt.rcParams["legend.edgecolor"]="black"
plt.rcParams["legend.framealpha"]=1
plt.rcParams["legend.fontsize"]=12

plt.figure(figsize=(8,4))
plt.xlabel("Time [s]")
plt.ylabel("Frequency [Hz]")
plt.pcolormesh(t, f, Pxx,cmap="magma",vmin=np.round(np.min(Pxx)/2,decimals=-1),vmax=np.round(np.max(Pxx),decimals=-1))
plt.colorbar(format='%+2.0f dB')
plt.ylim(0,500)
plt.tight_layout()
plt.show()

"""

dt=(t[-1]-t[0])/(len(t)-1)

def plot(ts,alpha=1,linestyle="solid"):
        plt.plot(f,Pxx[:,np.where((ts-dt/2<t)&(t<ts+dt/2))[0][0]],
                label=str(t[np.where((ts-dt/2<t)&(t<ts+dt/2))[0][0]])+" [s]",alpha=alpha,linestyle=linestyle)

def plot2(ts,alpha=1,linestyle="solid"):
        plt.plot(f,Pxx[:,np.where((ts-dt/2<t)&(t<ts+dt/2))[0][0]],
                label=str(ts)+" s",alpha=alpha,linestyle=linestyle)

#plt.axvline(x=820,color="red")
#plot(4)
#plot(12)
#plot(20)
#plot(28)
#plot2(43)
#plot(13)
#plot(21)
#plot2(44)

plt.xlabel("Frequency [Hz]")
plt.ylabel("Power spectral density [dB]")
plt.grid()
plt.legend()
plt.tight_layout()
plt.xlim(0,2000)
plt.show()

df=(f[-1]-f[0])/(len(f)-1)

def plot_freq(fs,label,alpha=1,linestyle="solid"):
        plt.plot(t,Pxx[np.where((fs-df/2<f)&(f<fs+df/2))[0][0],:],
                label=str(fs)+" s",alpha=alpha,linestyle=linestyle)

plot_freq(1212,label=None)
plt.grid()
plt.xlabel("Time [s]")
plt.ylabel("Power spectral density [dB]")
plt.tight_layout()
plt.show()

"""

plt.rcParams["font.size"]=12
T,F=np.meshgrid(t,f)
fig=plt.figure()
ax=fig.gca(projection='3d')
ax.plot_surface(T,F,Pxx,cmap='plasma')
#plt.ylim(0,5000)
plt.xlabel("Time [s]",fontsize=12)
plt.ylabel("Frequency [Hz]",fontsize=12)
ax.set_zlabel("Sound Pressure Level [dB]",fontsize=12)
plt.show()

def plot_freq(fs,label,alpha=1,linestyle="solid"):
        plt.plot(t,Pxx[np.where((fs-df/2<f)&(f<fs+df/2))[0][0],:],
                label=str(fs)+" s",alpha=alpha,linestyle=linestyle)

plot_freq(1212,label=None)
plt.grid()
plt.xlabel("Time [s]")
plt.ylabel("Power spectral density [dB]")
plt.tight_layout()
plt.show()
