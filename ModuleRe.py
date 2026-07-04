import re

#Exercie 1 > Extrait les chiffres

retour = re.findall(r"\d+", "J'ai 3 chats, 12 poissons et 150 fourmis")

print(f'Exercice 1: {retour}')

#Valider un code postal français

pattern = r"\d{5}"
retour = bool(re.match(pattern,"7500000"))

print(f'Exercice 2: {retour}')