#%%
class Livre():
    def __init__(self, titre, auteur, annee):
        self.titre = titre
        self.auteur = auteur
        self.annee = annee
        self.emprunteur = None

    def emprunter(self,emprunteur):
        if self.emprunteur == None:
            self.emprunteur = emprunteur
            return True
        else:
            return False

    def rendre(self):
        if self.emprunteur != None:
            self.emprunteur = None
            return True
        else:
            return False
        
# %%
class Utilisateur():
    def __init__(self, nom, emprunts=[]):
        self.nom = nom
        self.emprunts = emprunts

    def emprunter_livre(self, livre):
        if livre.emprunter(self.nom):
            self.emprunts.append(livre)
            return True
        else:
            return False

    def rendre_livre(self, livre):
        if livre.emprunteur == self.nom:
            self.emprunts.remove(livre)
            livre.rendre()
            return True
        else:
            return False

    def afficher_emprunts(self):
        print(f"Livres empruntés par {self.nom}")
        for livre in self.emprunts:
            print(f"    {livre.titre} ({livre.annee}) par {livre.auteur}")
# %%

class Bibliotheque:
    def __init__(self):
        self.livres = {}
        self.utilisateurs = {}

    def ajouter_livre(self, livre):
        if (not livre.titre in self.livres):
            self.livres[livre.titre] = livre
            return True
        else:
            return False
            
    def ajouter_utilisateur(self, utilisateur):
        if (not utilisateur.nom in self.utilisateurs):
            self.utilisateurs[utilisateur.nom] = utilisateur
            return True
        else:
            return False

    def emprunter(self, nom, titre):
        # Vérification nom
        if not nom in self.utilisateurs:
            return "echec:uInconnu"

        # Vérification titre
        elif not titre in self.livres:
            return "echec:lInconnu"

        # Vérification livre non emprunté
        elif not self.livres[titre].emprunteur == None:
            return "echec:dejaEmprunte"

        # Emprunt si nom et titre existant
        else:
            self.utilisateurs[nom].emprunter_livre(self.livres[titre])
            return "reussite"

# %%
