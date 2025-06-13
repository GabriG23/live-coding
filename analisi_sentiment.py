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
 
def analisi_testo(df, reviews): # analisi del sentiment del testo
    # PASSO 0 PREPROCESSING DATASET
    testo_train, testo_test, sentiment_train, sentiment_test = train_test_split(reviews, df['sentiment'], test_size=0.3, random_state=42)
    # dividiamo il dataset delle recenzioni in train e test
    # TRASFORMARE parole in numeri per il modello
    # TRAINING: 80% dei dati, ci servono per addestrare il modello di predizione
    # TEST# 20% dei dati, ci servono per testare il modello
 
    # PASSO 1 conta parole
    vectorizer = CountVectorizer() # modello che conta le parole
    vectorizer.fit(reviews)
    train_vectorized = vectorizer.transform(testo_train) # fit and trasnform i dati di train
    # passiamo del testo al vectorizer, lui lo trasforma
    # ritorna: n_samples (matrice che ci dice le corrispondenze delle parole nel testo), n_features (parole contate)
     # ci restituisce una matrice + parole contate
    #print(f"train vectorized\n\b: {train_vectorized}")
    test_vectorized = vectorizer.transform(testo_test)
 
    # PASSO 2 TRAINING DEL MODELLO
    classifier = LogisticRegression()
    classifier.fit(train_vectorized, sentiment_train)

    # PASSO 3 ANALISI METRICHE
    accuracy = classifier.score(test_vectorized, sentiment_test)
    precision = precision_score(sentiment_test, classifier.predict(test_vectorized))  # o 1, a seconda di come è codificato
    recall = recall_score(sentiment_test, classifier.predict(test_vectorized))

    print('accuracy:', accuracy)    # quante volte il modello ha indovinato
    print('precision:', precision)  # quanti dei positivi predetti sono corretti
    print('recall:', recall)        # quanti dei veri positivi sono stati trovati	
    # esempio: positivi 6, negativi 10
    # accuracy: previsioni corrette / previsioni totali
    # precision: 8 predetti, quanti sono corretti
    # recall: dei 6 positivi quanti sono stati trovati. GLi ha trovati tutti

if __name__ == "__main__":
    df = dataset()      # print(df.columns) # testo, sentiment, Lunghezza, testo_pulito
    print("Analisi del sentiment con testo non pulito (tutte le parole separate)")
    analisi_testo(df, df['testo'])  # testo normale, "esempio: Ottimo prodotto, spedione rapida!"
    print("Analisi del sentiment con testo pulito (un'unica stringa)")
    analisi_testo(df, df['testo_pulito']) # testo pulito, esempio: "ottimoprodottospedionerapida"