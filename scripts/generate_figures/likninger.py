import matplotlib.pyplot as plt 
import matplotlib as mpl 
import numpy as np

from generate_figure_common import figure_begin, figure_end, figure_save

###
### Andregrads 1
###

x = np.linspace(-1, 3, 200)
y = x**2 - 2*x

figure_begin()
plt.axhline(y=0, color = 'black') # Horisontal linje ved y = 0
plt.axvline(x=0, color = 'black') # Vertikal linje ved x = 0
plt.plot(x, y, color=(1,0.3,0.3))
plt.xlabel("x")
plt.ylabel("f(x)")

plt.grid()
figure_end()
figure_save("andregrads1")



###
### Graf 1
###

x = np.linspace(-1, 2, 200)
y = x**3 + x -1

figure_begin()
plt.axhline(y=0, color = 'black') # Horisontal linje ved y = 0
plt.axvline(x=0, color = 'black') # Vertikal linje ved x = 0
plt.plot(x, y, color=(0.4,0.4,1))
plt.xlabel("x")
plt.ylabel("f(x)")

plt.grid()
figure_end()
figure_save("graf1")


###
### Newtons metode 
###

def f(x):
    return x**2 - x -2 

def dfdx(x): 
    return 2*x - 1 

x = np.linspace(-1, 6, 200)
y = f(x)

figure_begin()
plt.axhline(y=0, color = 'black') # Horisontal linje ved y = 0
plt.axvline(x=0, color = 'black') # Vertikal linje ved x = 0
plt.plot(x, y, color=(0.3,0.3,0.8), linewidth=2.5, label="f(x)")
plt.plot(x, f(5)+dfdx(5)*(x-5), "-", color=(1,0.3,0.8), linewidth=1.7, label="Tangent 1")
plt.plot(x, f(3)+dfdx(3)*(x-3), "-", linewidth=1.7, color=(0.8,0.2,1), label="Tangent 2")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.ylim([-5, 25])
plt.xlim([-0.5, 6])

plt.grid()
plt.legend()
figure_end()
figure_save("Newtons_metode")
