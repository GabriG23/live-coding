import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import re
from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.feature_extraction import CountVectorizer, TfidfVectorizer
# from sklearn.linear_model import LogisticRegression

# sentiment positivo 1, negativo e 0
recensioni = [{"testo": "Ottimo prodotto, spedione rapida!", "sentiment": 1},
               {"testo": "Pacco arrivato rotto, ho dovuto fare il reso.", "sentiment": 0},
               {"testo": "Prodtto come da descrizione, ottimo!", "sentiment": 1},
               {"testo": "Bel prodotto, peccato per il ritardo.", "sentiment": 1},
               {"testo": "Pacco smarrito dal corriere, recensione pessima.", "sentiment": 0},
               {"testo": "Troppo caro per il prodotto che è.", "sentiment": 0},
               {"testo": "ho ricevuto il prodotto, ma la taglia era sbagliata.", "sentiment": 0},
               {"testo": "Prodotto fantastico, ha soddisfatto le mie aspettative.", "sentiment": 1},
               {"testo": "Ho ordinato una maglia meravigliosa, peccato sia arrivata rotta.", "sentiment": 0},
               {"testo": "ho ricevuto la scatola senza prodotto, ho effettuato il rimborso", "sentiment": 0},
               {"testo": "questo prodotto è spettacolare, lo consiglio ai miei amici.", "sentiment": 1}
               ]

'''for reecensione in recensioni:
    for k,v in reecensione.items():
        print(k,v)'''

df = pd.DataFrame(recensioni)
#print(df)

#print(df.groupby('sentiment').count())


lunghezza = [len(x.replace(' ','')) for x in df['testo']]
#print(lunghezza)

df['Lunghezza'] = lunghezza
#print(df)

# Marco Pirrotta - 10/6/25

# Pre-Processing sostituisci maiuscole in minuscole e rimuovi punteggiatura e spazi

testo_non_pulito = df["testo"]
box = []

for linea in testo_non_pulito:
    linea = linea.replace(' ','').lower() # rimuove maiuscole e spazi
    risultato = re.sub(r"[^\w\s]", "", linea ) # rimuovi punteggiatura
    box.append(risultato)
    #print(risultato)


df["testo_pulito"] = box   # modifica df con nuova colonna testo pulito
#print(df)


# trasforma testo in numeri
# prendi le recensioni, trasforma ogni parola in una tabella di numeri(?)

vectorizer = CountVectorizer()
testo_non_vectorized = df["testo_pulito"]

vectorizedtest = vectorizer.fit_transform(testo_non_vectorized) # da fare inisieme out-of-session

print(vectorizedtest)

#df["testo_vectorized"]

# Marco Pirrotta - 10/06/2025
