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
