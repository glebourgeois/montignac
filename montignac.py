import requests
import pyquery
import json

items = []

doc = pyquery.PyQuery(requests.get("http://www.montignac.com/fr/rechercher-l-index-glycemique-d-un-aliment/").content)
for item in doc(".item-row").items():
    nom = item(".item-title").text()
    ig = item(".item-ig-alpha").text()

    noms = nom.split(",")
    if len(noms) == 2:
        if noms[1].endswith(" de") or noms[1].endswith(" au"):
            noms = [noms[1].strip() + " " + noms[0]]
    nom = ','.join(noms)
    items.append({"nom": nom, "ig": ig})

json.dump(items, open("items.json", "w"), indent=2)
