import pandas as pd
import numpy as np
import re
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import precision_score, recall_score

def dataset():
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
                {"testo": "questo prodotto è spettacolare, lo consiglio ai miei amici.", "sentiment": 1},
                {"testo": "Servizio impeccabile, consegna puntuale e prodotto perfetto.", "sentiment": 1},
                {"testo": "Non ho mai ricevuto il mio ordine, esperienza pessima.", "sentiment": 0},
                {"testo": "Tutto ok, prodotto conforme e ben imballato.", "sentiment": 1},
                {"testo": "Prodotto arrivato graffiato, assistenza inesistente.", "sentiment": 0},
                {"testo": "Davvero soddisfatto, super consigliato!", "sentiment": 1},
                {"testo": "Consegna in ritardo di una settimana, mai più!", "sentiment": 0},
                {"testo": "Ottimo rapporto qualità/prezzo, ne comprerò altri.", "sentiment": 1},
                {"testo": "Non corrisponde alla descrizione, molto deluso.", "sentiment": 0},
                {"testo": "Tutto perfetto, lo ricomprerei sicuramente.", "sentiment": 1},
                {"testo": "Esperienza negativa, il prodotto non funziona.", "sentiment": 0},
                {"testo": "Spedizione veloce e servizio clienti gentilissimo.", "sentiment": 1}
                ]

    df = pd.DataFrame(recensioni)
    lunghezza = [len(x.replace(' ','')) for x in df['testo']]
    df['Lunghezza'] = lunghezza
    box = []
 
    for linea in df["testo"]:
        linea = linea.replace(' ','').lower() # rimuove maiuscole e spazi
        risultato = re.sub(r"[^\w\s]", "", linea ) # rimuovi punteggiatura
        box.append(risultato)
        #print(risultato)
 
    df["testo_pulito"] = box   # modifica df con nuova colonna testo pulito
 
    # trasforma testo in numeris
    # prendi le recensioni, trasforma ogni parola in una tabella di numeri(?)
    # testo = df['testo']
    # sentiment = df['sentiment']
 
    return df