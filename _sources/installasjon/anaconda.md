# Installasjon av *Anaconda*

Vi har erfart at den enkleste måten å komme i gang på dersom du ønsker å ha Python installert på datamaskinen din, er å bruke *Anaconda*. 

Du kan laste ned anaconda fra [https://www.anaconda.com/products/individual](https://www.anaconda.com/products/individual) ved å velge riktig versjon (linux, mac, windows) nederst på siden. Det finnes to alternativer per operativsystem. Dersom du ikke vet hva du skal velge, kan du prøve å første installere det øversete alternativet. Dersom det ikke fungerer prøver du det nederste alternativet. 

Når du har lastet ned installasjonsfilen fra anaconda.com, åpner du den og følger vanlige installasjonssteg: Litt kryptisk informasjon, godta brukervilkår og velge hvor anaconda skal installeres. Når installsjonen holder på ser det slik ut på mac:

```{figure} anaconda_installer.png
---
width: 500px
---
Screenshot fra installasjon av *Anaconda*. 
```

Når installasjonen er ferdig, kan det hende du får et tilbud om å prøve noe programvare som skal gjøre livet enklere, men som koster penger etterhvert. Dette kan du trygt gå forbi uten å installere.

For å starte å programmere åpner du nå *Anaconda Navigator*. Du får da opp et vindu slik som dette: 

```{figure} anaconda_navigator.png
---
width: 600px
---
Startmenyen til *Anaconda Navigator*. 
```

Fra denne menyen trykker du på *Launch*-knappen under *Spyder*. Da åpnes *Spyder*, som er et såkalt *integrert utviklingsmiljø* (IDE). Da skal du få opp et vindu som ser noe slikt ut: 

```{figure} spyder.png
---
width: 800px
---
Spyder. 
```

På venstre side kan du skrive kode. Du kan for eksempel skrive inn følgende kodesnutt: 

```python 
print("Hei, verden")
```

Når du har skrevet inn denne kodelinja kan du så lagre filen, enten med `file -> save` eller med tastatursnarvei. Etter at du har lagret filen kan du trykke på den grønne pila (trekanten) på menylinja. Da kjører koden. Du får output fra koden på høyre side av vinduet, under `Console`. 

Det kan være lurt å passe litt på hvor du lagrer programmene dine. For de fleste vil det i begynnelsen passe fint å lage en mappe som heter `Pythonprogrammer` under `Dokumenter`, og lagre programmene der. Dersom du lagrer programmene der *Spyder* først foreslår, kan det hande de blir vanskelige å finne igjen senere. 

Til slutt, for å unngå problemer senere, anbefaler vi å sjekke én spesifikk instilling: Åpne `Preferences` vha. skiftenøkkel-symbolet på menylinjen og velg `run` fra menyen på venstre side. Pass på at innstillingen "Remove all variables before execution" er aktivert, slik som i figuren under: 

```{figure} remove_variables.png
---
width: 600px
---
Spyder. 
```

Dette sørger for at ikke variabler og innstillinger fra et program du nettopp har kjørt, blander seg inn i kjøringen av andre programmer. 