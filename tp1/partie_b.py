#%%
import random

class devine_nombre():
    def __init__(self, borne_min=0,borne_max=100):
        self.borne_max = borne_max
        self.borne_min = borne_min
        self.nombre = random.randint(borne_min, borne_max)
        self.reponse = None
        self.reussite = False
        self.erreur = False

    def entree(self,entree):
        if entree == "R":
            self.nombre = random.randint(borne_min, borne_max)
            self.reussite = False
        else:
            try:
                entree = int(entree)
            except:
                self.erreur = True


    def texte(self):
        if self.reussite == True:
            return "Tu as déjà gagné ! Mais tu peux rejouter en écrivant 'R'."

        if self.erreur == True:
            self.erreur = False
            return "Erreur : Veuillez entrer un nombre valide ou 'R' pour recommencer."

        if self.reponse == None:
            return f"Devine le nombre entre {self.borne_min} et {self.borne_max}."
        elif self.reponse == self.nombre:
            return f"GAGNÉ LE NOMBRE ÉTAIT BIEN f{self.nombre} !!!!"
        elif self.reponse < self.nombre:
            return "Trop petit"
        elif self.reponse > self.nombre:
            return "Trop grand"
            
            