import matplotlib.pyplot as plt 
import matplotlib as mpl 
import numpy as np

from generate_figure_common import figure_begin, figure_end, figure_save



###
### Skrått kast
###

figure_begin()

for dt in [0.1, 0.3, 1]:
    T = 6

    N = int(np.ceil(T/dt))+1

    t = np.zeros(N)
    s = np.zeros(N)
    v = np.zeros(N)

    s[0] = 10 
    v[0] = 2 # Kaster ballen litt oppover i starten 

    m = 0.15 
    b = 0.3 # Ns/m 
    g = 9.81
    
    for i in range(N-1):
        a = -m*g - b*v[i]
        v[i+1] = v[i] + a*dt 
        s[i+1] = s[i] + v[i]*dt + 0.5*a*dt**2 
        t[i+1] = t[i] + dt 
    
    plt.plot(t, s, "-o", label=r"$\Delta t = %.2f$" % dt)
plt.xlabel("Tid (s)")
plt.ylabel("Posisjon (m)")
plt.legend()

figure_end()
figure_save("rettlinjet_bevegelse")


###
### Ball med luftmotstand
###

def akselerasjon_skrått_kast(r, v, t):
    m = 0.15 
    b = 0.2 
    g = np.array([0, 9.81])
    return -m*g - b*np.sqrt(np.dot(v, v)) * v
    
dt = 0.01 
T = 4
N = int(T/dt)

t = np.zeros(N)
r = np.zeros((N, 2))
v = np.zeros((N, 2))

r[0,0] = 0
r[0,1] = 2
v[0,0] = 13
v[0,1] = 4

for i in range(N-1):
    a = akselerasjon_skrått_kast(r[i,:], v[i,:], t[i])
    v[i+1, :] = v[i, :] + a[:]*dt 
    r[i+1, :] = r[i, :] + v[i, :]*dt + 0.5*a[:]*dt**2 
    t[i+1] = t[i] + dt 

figure_begin()
plt.plot(r[:,0], r[:,1])
plt.ylim([0, 4])
plt.xlabel("x (m)")
plt.ylabel("y (m)")
figure_end()
figure_save("ball_luftmotstand")

###
### Harepopulasjon
###

import matplotlib.pyplot as plt
import numpy as np

#Initialbetingelser
t0 = 0          # Starttid i måneder
P0 = 100       # Antall harer ved t = 0
k = 0.2         # Reproduksjonsraten

#Tidssteg
N = 12*20     # antall intervaller
tid = 20      # antall måneder
dt = tid/N

#Arrayer
t = np.zeros(N)
P = np.zeros(N)
Pder = np.zeros(N)

# Initierer arrayene
t[0] = t0
P[0] = P0

# Eulers metode
for i in range(N-1):
    Pder[i] = k*P[i]
    P[i+1] = P[i] + Pder[i]*dt
    t[i+1] = t[i] + dt

figure_begin()
plt.plot(t,P)
plt.title('Vekst i harepopulasjon')
plt.xlabel('Tid (måneder)')
plt.ylabel('Antall harer')
figure_end()
figure_save("harepopulasjon")


###
### Harepopulasjon med bæreevne
###

N = 12*60     # antall intervaller
tid = 60      # antall måneder
dt = tid/N

b = 10000 


#Arrayer
t = np.zeros(N)
P = np.zeros(N)
Pder = np.zeros(N)

# Initierer arrayene
t[0] = t0
P[0] = P0


for i in range(N-1):
    Pder[i] = k*P[i]*(1 - P[i]/b) 
    P[i+1] = P[i] + Pder[i]*dt
    t[i+1] = t[i] + dt

figure_begin()
plt.plot(t,P)
plt.title('Vekst i harepopulasjon')
plt.xlabel('Tid (måneder)')
plt.ylabel('Antall harer')
figure_end()
figure_save("harepopulasjon2")


###
### Hare og gaupe
###

#Initialbetingelser
H0 = 2000       # Antall harer ved t = 0
G0 = 10        # Antall gauper ved t = 0
a = 0.1         # Reproduksjonsrate, harer
b = 10000       # Bæreevnen
c = 0.005         # Hare-gaupe møterate
d = 0.00005       # Reproduksjon og mat, gauper
e = 0.06         # Nedgangsrate for gauper


#Tidssteg
N = 100000     # antall intervaller
tid = 400      # antall måneder
dt = tid/N      

#Arrayer
t = np.zeros(N)
H = np.zeros(N)
G = np.zeros(N)
Hder = np.zeros(N)
Gder = np.zeros(N)

# Initierer arrayene
H[0] = H0
G[0] = G0

# Eulers metode
for i in range(N-1):
    Hder[i] = a*H[i]*(1 - H[i]/b)  - c*H[i]*G[i]
    Gder[i] = d*H[i]*G[i] - e*G[i]
    H[i+1] = H[i] + Hder[i]*dt
    G[i+1] = G[i] + Gder[i]*dt
    t[i+1] = t[i] + dt

# Plotting
fig = figure_begin()
ax = fig.add_subplot(111)
data1 = ax.plot(t, H, '-b', label = 'Harer')
ax2 = ax.twinx()
data2 = ax2.plot(t, G, '-r', label = 'Gauper')

data = data1 + data2
datatittel = [l.get_label() for l in data]
ax.legend(data, datatittel, loc=0)

ax.grid()
ax.set_xlabel("Tid (måneder)")
ax.set_ylabel("Antall harer")
ax2.set_ylabel("Antall gauper")
ax2.set_ylim(0, 200)
ax.set_ylim(0,2500)
figure_end()
figure_save("haregaupe")