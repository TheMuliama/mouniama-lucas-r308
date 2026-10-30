#%% 
class grille:
    def __init__(self):
        self.matrice = [[" "," "," "],
                        [" "," "," "],
                        [" "," "," "]]


    def afficher(self):
        affichage = ""
        for ligne in self.matrice:
            affichage = affichage + "| "
            for element in ligne:
                affichage = affichage + element + " | "
            affichage = affichage + "\n"
        print(affichage)
                

    def jouer(self, x, y, joueur):
        self.matrice[y][x] = joueur

    def est_gagnant(self,joueur):
        gagnant = False
        # vérification des lignes
        for ligne in self.matrice:
            if ligne == [joueur,joueur,joueur]:
                gagnant = True
            
        # vérification des collones
        for i in range(0,len(self.matrice)):
            collone = []
            for j in range(0,len(self.matrice)):
                collone.append(self.matrice[j][i])
            if collone == [joueur,joueur,joueur]:
                gagnant = True

        # vérification des diagonales
        diag = []
        for i in range(0,len(self.matrice)):
            diag.append(self.matrice[i][i])
        
        if diag == [joueur,joueur,joueur]:
            gagnant = True

        diag = []

        for i in range(0,len(self.matrice)):
            diag.append(self.matrice[i][len(self.matrice)-1+i])
        
        if diag == [joueur,joueur,joueur]:
            gagnant = True


    def est_plein(self):
        plein = True

        for ligne in self.matrice:
            for element in ligne:
                if element == ' ':
                    plein = False

        return plein

# %%
