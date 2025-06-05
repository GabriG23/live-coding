import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import CountVectorizer, TfidfVectorizer
from sklearn.linear_model import LogisticRegression

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
print(df)

print(df.groupby('sentiment').count())


lunghezza = [len(x.replace(' ','')) for x in df['testo']]
print(lunghezza)

df['Lunghezza'] = lunghezza
print(df)

#