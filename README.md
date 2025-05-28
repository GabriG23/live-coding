# Docker
- installare Docker da: {link}[https://www.docker.com/products/docker-desktop/], selezionare windows AMD64
- verificare l'installazione con `docker --version`
- creare una cartella `docker`
- creare un `Dockerfile` senza estenzione, scrivere dentro (questo è un esempio con Python 3.11):
```
# Usa l'immagine base ufficiale di Python 3.11
FROM python:3.11-slim

# Imposta la directory di lavoro dentro al container
WORKDIR /app

# Copia i file locali nella directory di lavoro del container
COPY . .

# Installa le dipendenze (se hai un requirements.txt)
RUN pip install --upgrade pip \
 && pip install -r requirements.txt

# Comando di default (modificabile)
CMD ["python"]
```

- aggiungere un requirements.txt con le librerie:
```
pandas
numpy
matplotlib
seaborn
```

- costruisci il container: in questo caso `docker build -t python-app:3.11 .`
- per avviare una sessione interattiva `docker run -it --rm python-app:3.11`
- per aprire il bash: `docker run -it --rm -v ${PWD}:/app python:3.11 bash`
- cambiare cartella `cd app`
- eseguire il file python con `python main.py`