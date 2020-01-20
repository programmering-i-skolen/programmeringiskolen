import matplotlib.pyplot as plt 
import matplotlib as mpl 
import numpy as np

from generate_figure_common import figure_begin, figure_end, figure_save


### 
### Motstand eksperiment 
###


figure_begin()
data = np.loadtxt("datasett/motstand_eksperiment.txt")

spenning = data[:,0]
strøm = data[:,1]

plt.plot(spenning, strøm, "o")
plt.xlabel("Spenning (V)")
plt.ylabel("Strøm (A)")
figure_end()
figure_save("motstand_eksperiment")


### 
### SAS-fly
### 

figure_begin()
data = np.loadtxt("datasett/sas_fly.txt", skiprows=1, usecols=(1, 2, 3, 4, 5, 6))
navn = np.loadtxt("datasett/sas_fly.txt", skiprows=1, usecols=(0), dtype=str)

plt.barh(navn, data[:,5])
plt.xlabel("Drivstofforbruk $(\mathrm{liter} \cdot \mathrm{sete}^{-1} \cdot \mathrm{km}^{-1})$")
plt.ylabel("Flymodell")
figure_end()
figure_save("sas_fly")


###
### Lineær regresjon 
### 

figure_begin()
T = [0, 20, 40, 60, 80, 100] # temperatur i C
L = [35.7, 35.9, 36.4, 37.1, 38.0, 39.2] # løselighet i g/100 ml

p = np.polyfit(T, L, 1)
a = p[0]
b = p[1]
T_fit = np.linspace(0, 100, 100)
L_fit = a*T_fit + b

plt.plot(T, L, "o", label="data")
plt.plot(T_fit, L_fit, label="lineær modell")
plt.xlabel("Temperatur (°C)")
plt.ylabel("Løselighet (g/100 mL)")
plt.legend()
figure_end()
figure_save("nacl_linear_fit")


###
### Solflekker 1
### 

figure_begin()
data = np.loadtxt("datasett/solflekkdata.txt", skiprows=2)
years = data[:,0]
months = data[:,1]  
days = data[:,2] 
pa = data[:,3]
ca = data[:,4] 
plt.plot(pa, color="crimson")
figure_end()
figure_save("sunspots_1")

### 
### Solflekker 2 
###

figure_begin()
utvalg = (pa >= 0)
years = years[utvalg]
months = months[utvalg]
days = days[utvalg]
pa = pa[utvalg]
ca = ca[utvalg]

float_years = years + months/12 + days/365

plt.plot(float_years, pa, color="crimson")
plt.xlabel("År")
plt.ylabel("Aktivitet")
figure_end()
figure_save("sunspots_2")


###
### Virrevandring
###

np.random.seed(3429)

M = 5
N = 1000

def virrevandring(N):
    steg = np.zeros((N,2))
    for i in range(N-1): 
        angle = np.random.random()*2*np.pi
        steg[i+1,:] = steg[i,:] + np.asarray([np.cos(angle), np.sin(angle)])
    return steg

figure_begin(size=(3,3))
for walk in range(M):
    steg = virrevandring(N)
    plt.plot(steg[:,0], steg[:,1], linewidth=0.75)
plt.xlabel("x")
plt.ylabel("y")
figure_end()
plt.axis("equal")
figure_save("random_walk")

###
### Virrevandrer-histogram
###

def virrevandring(N):
    enkeltsteg = np.zeros((N,2))
    angles = np.random.random(N)*2*np.pi
    enkeltsteg[:,0] = np.cos(angles)
    enkeltsteg[:,1] = np.sin(angles)
    steg = np.cumsum(enkeltsteg, axis=0)
    return steg


M = 100000
N = 1000

endepunkter = np.zeros((M, 2))

for walk in range(M):
    steg = virrevandring(N)
    endepunkter[walk,:] = steg[-1,:]
figure_begin(size=(4,3))
plt.hist2d(endepunkter[:,0], endepunkter[:,1], bins=30)
plt.xlabel("x")
plt.ylabel("y")
plt.colorbar()
figure_end()
figure_save("random_walk_hist2d")