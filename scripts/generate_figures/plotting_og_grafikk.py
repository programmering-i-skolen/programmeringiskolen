import matplotlib.pyplot as plt 
import matplotlib as mpl 
import numpy as np

from generate_figure_common import figure_begin, figure_end, figure_save

tid = [0, 15, 30, 45, 60, 90] # Tid i minutter
kontroll = [4.9, 5.1, 4.8, 4.3, 4.5, 4.7]
sukkerbrus = [4.5, 8.2, 9.5, 7.5, 5.4, 4.9]
eple = [4.6, 7.5, 9.2, 8.4, 6.4, 5.8]

###
### Blodsukker 1
###
figure_begin()
plt.plot(tid, kontroll) # Plotter kontrollverdiene mot tida
figure_end()
figure_save("blodsukker1")

###
### Blodsukker 2
###
figure_begin()
plt.plot(tid, kontroll) 
plt.title('Blodsukkermåling')       # Tittel på plottet
plt.xlabel('Tid (s)')               # Aksetittel på x-aksen
plt.ylabel('Blodsukkerkonsentrasjon (mmol/L)') # Aksetittel på y-aksen
plt.xlim(-10,100) # Definisjonsmengde
plt.ylim(-1,12)  # Verdimengde
plt.axhline(y=0, color = 'black') # Horisontal linje ved y = 0
plt.axvline(x=0, color = 'black') # Vertikal linje ved x = 0
plt.grid()
figure_end()
figure_save("blodsukker2")

###
### Blodsukker 3
###
figure_begin()
plt.plot(tid, kontroll) 
plt.plot(tid, sukkerbrus)
plt.plot(tid, eple)
plt.title('Blodsukkermåling')       # Tittel på plottet
plt.xlabel('Tid (s)')               # Aksetittel på x-aksen
plt.ylabel('Blodsukkerkonsentrasjon (mmol/L)') # Aksetittel på y-aksen
plt.xlim(-10,100) # Definisjonsmengde
plt.ylim(-1,12)  # Verdimengde
plt.axhline(y=0, color = 'black') # Horisontal linje ved y = 0
plt.axvline(x=0, color = 'black') # Vertikal linje ved x = 0
plt.grid()  
figure_end()
figure_save("blodsukker3")

###
### Blodsukker 4
###
figure_begin()
plt.plot(tid, kontroll, color = 'red', linestyle = 'dashed', marker = 'o', label = 'Kontroll')
plt.plot(tid, sukkerbrus, color = 'magenta', linestyle = 'dotted', marker = '^', label = 'Brus')
plt.plot(tid, eple, color = 'lawngreen', linestyle = 'solid', marker = 's', label = 'Eple')
plt.legend()
plt.title('Blodsukkermåling')       # Tittel på plottet
plt.xlabel('Tid (s)')               # Aksetittel på x-aksen
plt.ylabel('Blodsukkerkonsentrasjon (mmol/L)') # Aksetittel på y-aksen
plt.xlim(-10,100) # Definisjonsmengde
plt.ylim(-1,12)  # Verdimengde
plt.axhline(y=0, color = 'black') # Horisontal linje ved y = 0
plt.axvline(x=0, color = 'black') # Vertikal linje ved x = 0
plt.grid()
figure_end()
figure_save("blodsukker4")

###
### Arter
###
figure_begin(size=(4.5,3.5))
t = [0,1,2,3,4,5,6] # Tid i dager
ringhalelemurer = [3, 5, 5, 0, 1, 2, 8]
edderkopper = [234, 198, 345, 333, 308, 215, 250]
frosker = [75, 70, 78, 89, 104, 90, 92]

plt.subplot(3,1,1) #3 rader, 1 kolonne, figur nr. 1
plt.plot(t, ringhalelemurer, color = 'brown')
plt.xlabel('Tid (dager)')
plt.ylabel('Lemurer')

plt.subplot(3,1,2) #3 rader, 1 kolonne, figur nr. 2
plt.plot(t, edderkopper, color = 'purple')
plt.xlabel('Tid (dager)')
plt.ylabel('Edderkopper')

plt.subplot(3,1,3) #3 rader, 1 kolonne, figur nr. 3
plt.plot(t, frosker, color = 'blue')
plt.xlabel('Tid (dager)')
plt.ylabel('Frosker')

figure_end()
figure_save("arter")

### 
### Iris 
###

# Leser av fila
data = np.loadtxt('datasett/iris.csv', delimiter = ',', skiprows = 1, usecols=(0,1,2,3))
lengde_begerblad = data[:,0]
bredde_begerblad = data[:,1]
lengde_kronblad = data[:,2]
bredde_kronblad = data[:,3]


# Plott
figure_begin()
plt.scatter(lengde_kronblad, bredde_kronblad, color = 'darkorchid', s=10)
plt.title('Iris-blomster')
plt.xlabel('Lengde kronblad (cm)')
plt.ylabel('Bredde kronblad (cm)')
figure_end()
figure_save("iris")

### 
### Iris histogram
### 
figure_begin()
plt.hist(lengde_kronblad, edgecolor = 'black')
plt.title('Fordeling av kronbladlengde')
plt.xlabel('Lengde på kronblad (cm)')
plt.ylabel('Antall')
figure_end()
figure_save("iris_histogram")


###
### Kake 
###
figure_begin(size=(3,2))
fag = ['Kjemi 1', 'Fysikk 1', 'Biologi 1', 'Tekforsk', 'Promod', 'R1', 'S1']
antall = [78, 84, 34, 12, 46, 108, 52]
plt.pie(antall, labels = fag)
figure_end()
plt.axis("equal")
figure_save("kake")

### 
### Søyle 
###
figure_begin()
plt.bar(fag, antall)
figure_end()
figure_save("fagvalg")


###
### Hakkegraf
###
figure_begin()
def f(x):
    return x**2 - 2

x = np.linspace(-3,3,5)
y = f(x)

plt.plot(x,y)
plt.grid()
figure_end()
figure_save("hakkegraf")

###
### Gltgraf
###
figure_begin()
def f(x):
    return x**2 - 2

x = np.linspace(-3,3,1000)
y = f(x)

plt.plot(x,y)
plt.grid()
figure_end()
figure_save("glattgraf")


### 
### 3D-plott
###

from mpl_toolkits.mplot3d import Axes3D
figure_begin(size=(4,2))
# Lager et objekt som vi tegner i
ax = plt.axes(projection='3d')

def f(x, y):
    return np.sin(np.sqrt(x**2 + y**2))

# Genererer x- og y-verdier
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)

# Lager et nett av x- og y-verdiene
X, Y = np.meshgrid(x, y)

# Genererer funksjonsverdier gitt nettet av x og y
Z = f(X, Y)

# Plotter  overflaten i objektet vårt (ax)
ax.plot_surface(X, Y, Z, cmap='inferno')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
#figure_end()
figure_save("3D-plott")