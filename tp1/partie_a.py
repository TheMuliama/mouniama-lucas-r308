#%%
import json

# %%
# Définition des fonctions

def moyenne_classe(d):
    somme = sum(d.values())
    return(somme/len(d))

def meilleur_etudiant(d):
    return max(d)

def ajouter_etudiant(d, nom:str, note:float):
    d[nom] = note

def enregistrer_dict(d, fichier):
    
    try:
        with open(fichier, "w") as f:
            json.dump(d, f, indent=4)
    except:
        print("Erreur: dictionnaire vide ou ligne mal formée")

def charger_dict(d, fichier):
     
    with open(fichier, "r") as f:
        d = json.load(f)


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
