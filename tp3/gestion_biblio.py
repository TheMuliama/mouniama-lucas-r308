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
