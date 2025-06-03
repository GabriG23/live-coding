import pandas as pd
import numpy as np
import yfinance as yp

# Crea bot di trading online
# usa y finance per prendere dati

data = yp.Ticker("AMZN")
print(data.analyst_price_targets)
print(data.history(period='1wk'))

# estrazione info / attivita
# messaggio "il prezzo di amazon è"

# check type of variable
price_tag = data.analyst_price_targets
print(type(price_tag))

# Printa solo Pricetag "Current"

print("Il Valore corrente di Amazon è:" , price_tag["current"])

# Usa Pandas e Numpy per fare la media dei prezzi correnti in un mese

# prendi dati history 1 settimana
settimana = data.history(period = '1wk')
# print(settimana)

# estrai "open" da settimana
print(type(settimana))
print(settimana['Open'])


# _____ FERMI QUI ____ 03/06/25 (da Marco) #


# media di "Open"





