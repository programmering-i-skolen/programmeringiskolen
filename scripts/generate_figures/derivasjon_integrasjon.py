import matplotlib.pyplot as plt 
import matplotlib as mpl 
import numpy as np

from generate_figure_common import figure_begin, figure_end, figure_save

###
### Der plott
### 


figure_begin()
def f(x):
    return x**3 - 2*x**2 + 2*x - 5

# Metode for numerisk derivasjon
def numerisk_derivert(f, x, delta_x):
    fder = (f(x + delta_x) - f(x))/delta_x
    return fder

# Plotting
x = np.linspace(-2,5,1000)
y = f(x)
yder = numerisk_derivert(f,x,1E-8)

plt.plot(x,y,color='green',label='f(x)')
plt.plot(x,yder,color='red',label='f\'(x)')
plt.xlabel('x')
plt.legend()
plt.grid()
figure_end()
figure_save("der_plott")

###
### Heistur
###

figure_begin()
# Leser av fila
data = np.loadtxt('datasett/heistur.csv', delimiter = ',', skiprows = 1)
t = data[:,0]
h = data[:,2]

# Derivasjonsvariabler
n = len(t)
v = np.zeros(n)
a = np.zeros(n)

# Derivasjonsløkke
for i in range(0, n-1):
    v[i] = (h[i+1] - h[i])/(t[i+1] - t[i])
    
plt.plot(t, v, color = 'mediumseagreen')
plt.title('Heistur')
plt.xlabel('Tid (s)')
plt.ylabel('Hastighet (m/s)')
plt.grid()
figure_end()
figure_save("heistur_plott")


###
### Trapesmetoden
###

def f(x):
    return 1/(5+x**3)

linecolor_boxes = (0.7, 0.5, 1)
linecolor_graph = (0.25, 0.25, 1)
fillcolor = (0.9, 0.83, 1)

x = np.linspace(0, 5, 200)
y = f(x)
x2 = np.linspace(0, 5, 6)
y2 = f(x2)

figure_begin(size=(4.5, 3))
plt.plot(x2, y2, color= linecolor_boxes, linewidth=1)
plt.fill_between(x2, 0, y2, color=fillcolor)

for i in range(6):
    plt.plot([i,i], [0, f(i)], color=  linecolor_boxes, linewidth=1)
plt.plot([0,5], [0,0], color=  linecolor_boxes, linewidth=1)
plt.plot(x, y, color = linecolor_graph)
plt.title(r"Trapesmetoden, $N=5$")
plt.xlabel("x")
plt.ylabel("y")

figure_end()
figure_save("Trapesmetoden")


###
### Rektangelmetoden
###

x = np.linspace(0, 5, 200)
y = f(x)
x2 = np.linspace(0, 5, 6)
x3 = np.zeros(11)
x3[1::2] = x2[1:]
x3[0::2] = x2[:]
x4 = np.zeros(11)
x4[0::2] = x2[:]
x4[1::2] = x2[:-1]
print(x3)
print(x4)
y3 = f(x4)

figure_begin(size=(4.5, 3))
plt.plot(x3, y3, color= linecolor_boxes, linewidth=1)
plt.fill_between(x3, 0, y3, color=fillcolor)

for i in range(6):
    plt.plot([i,i], [0, f(i)], color=  linecolor_boxes, linewidth=1)
plt.plot([0,5], [0,0], color=  linecolor_boxes, linewidth=1)
plt.plot(x, y, color = linecolor_graph)
plt.title(r"Rektangelmetoden, $N=5$")
plt.xlabel("x")
plt.ylabel("y")

figure_end()
figure_save("Rektangelmetoden")


###
### Illustrasjon trapesmetoden
###

x0 = 1.5
x = np.linspace(-x0, x0, 200)
y = x**3-x
x2 = np.linspace(-x0,x0, 2)
y2 = x2**3-x2
figure_begin()
plt.plot(x, y, "-")
plt.plot(x2, y2,"-o")
figure_end()
figure_save("trapesregel2")


###
### Diskret integrasjon 
###

v_int = np.zeros(len(v))
v_sum = np.zeros(len(v))

for i in range(len(v)-1):
    bredde = t[i+1] - t[i]
    v_int[i] = (v[i]+v[i+1])*(bredde/2)
    for j in range(len(v_int)):
        v_sum[i] += v_int[j]

figure_begin()
plt.plot(t,h,color='mediumseagreen',label='Originaldata')
plt.title('Heistur')
plt.xlabel('Tid (s)')
plt.ylabel('Høyde (m)')
plt.grid()
plt.plot(t[:-1],v_sum[:-1],color='navy',label='Derivert, så integrert, data')
plt.legend()
figure_end()
figure_save("heistur_integrasjon")
