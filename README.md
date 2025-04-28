# Live Coding
Live coding di gruppo

# Poetry
- Cos'è `Poetry`?
- E' uno strumento di gestione progetti in Python, e serve principalmente a gestire le dipendenze (quindi le librerie del progetto), creare ambienti virtuali e
- Sostituisce il classico ambiente virtuale .venv con pip, requirements.txt etc... per avere un sistema più dinamico per lavorare in gruppo.
### Caratteristiche
- file `pyproject.toml`: è il file principale dove vengono inserire tutte le dipendenze. Toml è un formato come il JSON, ma più leggibile. Questo file viene modificato automaticamente quando vengono aggiunti pacchetti.
- file `poetry.lock`: è il file che blocca esattamente quali versioni delle librerie sono installate. Viene creato automaticamente da poetry e non va modificato manualmente! (fa tutto in automatico)
- Quindi con `pyproject.toml` dichiaro cosa mi serve e nel `poetry.lock` blocco esattamente cosa uso
### Istallare poetry su windows via terminale
- Python deve essere istallato dal sito (Python)[https://www.python.org/] e non da windows Store. Quindi se lo avete istallato da windows store, disinstallatelo.

- Istallare poetry dal sito lanciando da terminale:
``` (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python - ```

- Ora dovrebbe averlo messo nel PATH, provate ad eseguire ```poetry --version```. Se non ve lo da allora dovete sistemare il PATH di poetry, come avete fatto con python

Ecco un po' di comandi base:
- `poetry new project`: per creare un nuovo progetto (voi non dovete farlo, in quanto sarà già creato)
- `poetry init`: per inizializzare una cartella, fa la stessa cosa di poetry new project ma senza creare la cartella
- `poetry install`: istalla tutte le dipendenze nel file toml
- `poetry add nome_libreria`: aggiunge un nuovo pacchetto, per esempio poetry add numpy per aggiungere numpy oppyre poetry add --dev black per aggiungere una serie di librerie per programmare

- una volta clonata la cartella sul proprio pc quello da fare è istallare poetry ed istallare le dipendenze creando un ambiente virtuale uguale per tutti