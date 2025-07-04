import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Esercizio: Simuliamo dei dati numerici due materie
# Crea array numpy materie Matematica e Informatica

VotiMatematica = np.array([25, 29, 20, 21, 26, 18])
VotiInformatica = np.array([25, 26, 30, 29, 18, 22])

# crea un dataframe pandas

df = pd.DataFrame(({'Matematica' : VotiMatematica, 'Informatica' : VotiInformatica})
 )
print(df)

# calcola statistiche di base sulle colonne dei database media artimetica

MediaMat = df["Matematica"].mean()
print(MediaMat)
MediaInf = df["Informatica"].mean()
print(MediaInf)

# print (df.describe() )    # metodo di ange

# visualizziamo relazione tra le due materie usando Scatterplot

# plt.scatter(df['Informatica'], df['Matematica'], color="green" )
# plt.xlabel("Voti Informatica")
# plt.ylabel("Voti Matematica")
# plt.title("Grafico Scatterplot")
# plt.show()

# Introduciamo un anomalia

df.iloc[ 3 , 1] = np.nan
print(df)

# gestisci valore mancante

df.fillna(MediaInf, inplace=True)
print(df)

# rappresenta ogni riga con una classe Python
# def una classe chiamata studente

class Studente:
    def __init__(self, VotoMatematica, VotoInformatica):
        self.VotoMatematica = VotoMatematica
        self.VotoInformatica = VotoInformatica
        pass

    def __str__(self):
        return f"{self.VotoMatematica} {self.VotoInformatica}"
    
    
# Create lista di oggetti studenti per i primi 3 studenti del DF 


listud = []
for i in range(3) :
    riga = df.iloc[i]
    stud = Studente(riga["Matematica"], riga["Informatica"])
    listud.append(stud)

for studente in listud:
    print(studente)  