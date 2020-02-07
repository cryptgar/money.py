"""
Generates currencies based on https://en.wikipedia.org/wiki/ISO_4217

Data gathered from https://github.com/datasets/currency-codes/blob/master/data/codes-all.csv
"""

import os
import urllib.request
import csv

data_url = 'https://raw.githubusercontent.com/datasets/currency-codes/master/data/codes-all.csv'

response = urllib.request.urlopen(data_url)

data = response.read()

text = data.decode('utf-8')

reader = csv.reader(text.splitlines())

with open(os.path.join("moneypy", "currencies.py"), "w") as f:
    f.write("""\"\"\"
List of currencies from ISO 4217
\"\"\"

from .currency import Currency

""")

    added = []

    for row in reader:
        entity, currency, alphacode, numcode, minorunit, withdrawaldate = row

        if alphacode == 'AlphabeticCode':
            continue

        if alphacode != '':
            if numcode == '':
                numcode = 'None'

            if minorunit == '' or minorunit == '-':
                minorunit = 0

            if alphacode not in added:            
                f.write(f"{alphacode}_CURRENCY = Currency('{currency}', '{alphacode}', '{numcode}', {minorunit})\n")
                added.append(alphacode)