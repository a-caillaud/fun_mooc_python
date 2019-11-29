import json
chemin = "/Users/caillaud/Documents/OneDrive/informatique/projets/projets_python/fichier.json"

with open(chemin, "r") as f:
    # json.dump([1, 2, 3, 4, 5], f, indent=4)
    liste = json.load(f)
    print(liste)