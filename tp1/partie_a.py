# %%
# Définition des fonctions

def moyenne_classe(d):
    somme = sum(d.values())
    return(somme/len(d))

def meilleur_etudiant(d):
    return max(d)

def ajouter_etudiant(d, nom:str, note:float):
    d[nom] = note

def enregistrer_dict(d:dict, fichier="tp1/fichier.txt"):
    contenu = ""

    for nom in d.keys():
        contenu += f"{nom}:{d.get(nom)}\n"

    # Retirer le dernier saut de ligne
    contenu = contenu[:-1]

    

    
    with open(fichier, "w", encoding="utf-8") as f:
        f.write(contenu)

#%%
def charger_dict(fichier="tp1/fichier.txt"):
    d = {} 

    try:
        with open(fichier, "r", encoding="utf-8") as f:
            contenu = f.read()
    except:
        return None
    
    lignes = contenu.split()

    for ligne in lignes:
        if len(ligne.split(":")) != 2:
            continue

        nom, note = ligne.split(":")

        try:
            note = float(note)
        except:
            continue

        d[nom] = note

    return d



# %%
if __name__ == "__main__":
    d = {
        "alice":float(12), 
        "bob":float(15),
        "Claire":float(9.5)
    }

print(d)

print(f"moyenne_classe(d)    ->     {moyenne_classe(d)}")
print(f"meilleur_etudiant(d)(d)    ->     {meilleur_etudiant(d)}")


# %%
