""""
Projet : Vasarely
Auteur : Achraf Zihmid
Date : 28 octobre 2019
But : Réaliser un pavage hexagonal vus d’en haut, formés avec des losanges de couleurs différentes, déformés par une boule.
Entrées : Les dimensions du pavage, Un côté de l'hexagon, Les  trois couleurs des losanges, le centre et le rayon de la sphere de deformation
Résultat : affiche un pavage hexagonal vus d'en haut, formés avec des losanges de couleurs différentes, déformés par une boule.
"""

### Import ###
import turtle as t
from math import cos, sin, pi, sqrt
from deformation import deformation


### Function ###
def losange_sup_gauche(point, col, longueur, centre, rayon):
    """
       Réalise le dessin du losange supérieur gauche
    """
    t.penup()
    x, y = point
    p = (x, y, 0)
    p = deformation(p, centre, rayon)
    t.goto(p[0], p[1])
    t.fillcolor(col[0])
    t.begin_fill()
    p = (longueur * cos(0) + x, longueur * sin(0) + y, 0)
    p = deformation(p, centre, rayon)
    t.goto(p[0], p[1])
    p = (longueur * cos(pi / 3) + x, longueur * sin(pi / 3) + y, 0)
    p = deformation(p, centre, rayon)
    t.goto(p[0], p[1])
    p = (longueur * cos(2 * pi / 3) + x, longueur * sin(2 * pi / 3) + y, 0)
    p = deformation(p, centre, rayon)
    t.goto(p[0], p[1])
    p = (x, y, 0)
    p = deformation(p, centre, rayon)
    t.goto(p[0], p[1])
    t.end_fill()

def losange_sup_droit(point, col, longueur, centre, rayon):
    """
        Réalise le dessin du losange supérieur droit
    """
    x, y = point
    t.fillcolor(col[2])
    t.begin_fill()
    p = (longueur * cos(0) + x, longueur * sin(0) + y, 0)
    p = (deformation(p, centre, rayon))
    t.goto(p[0], p[1])
    p = (longueur * cos(-pi / 3) + x, longueur * sin(-pi / 3) + y, 0)
    p = (deformation(p, centre, rayon))
    t.goto(p[0], p[1])
    p = (longueur * cos(-2 * pi / 3) + x, longueur * sin(-2 * pi / 3) + y, 0)
    p = (deformation(p, centre, rayon))
    t.goto(p[0], p[1])
    p = (x, y, 0)
    p = (deformation(p, centre, rayon))
    t.goto(p[0], p[1])
    t.end_fill()

def  losange_inf_gauche(point, col, longueur, centre, rayon):
    """
        Réalise  le dessin du losange inferieur gauche
    """
    x, y = point
    t.fillcolor(col[1])
    t.begin_fill()
    p = (longueur * cos(2 * pi / 3) + x, longueur * sin(2 * pi / 3) + y, 0)
    p = (deformation(p, centre, rayon))
    t.goto(p[0], p[1])
    p = (longueur * cos(pi) + x, longueur * sin(pi) + y, 0)
    p = (deformation(p, centre, rayon))
    t.goto(p[0], p[1])
    p = (longueur * cos(-2 * pi / 3) + x, longueur * sin(-2 * pi / 3) + y, 0)
    p = (deformation(p, centre, rayon))
    t.goto(p[0], p[1])
    t.end_fill()

def hexagon(point, col, longueur, centre, rayon):
    """
    Réalise un hexagon
    Entrées :
            point : centre de l'hexagone
            longueur : la distance entre le centre et n’importe quel coin de l’hexagone
            col : les trois couleurs (col1, col2, col3) qui vont être utilisées pour dessiner les hexagones,
            centre : le centre de la sphère de déformation
            rayon : le rayon de la sphère de déformation.
    Sorties : Un hexagon
    """
    t.penup()
    losange_sup_gauche(point, col, longueur, centre, rayon)  # Appelle de la fonction losange_sup_gauche
    losange_sup_droit(point, col, longueur, centre, rayon)   # Appelle de la fonction losange_sup_droit
    losange_inf_gauche(point, col, longueur, centre, rayon)  # Appelle de la fonction losange_inf_gauche
    t.hideturtle()

def pavage(inf_gauche, sup_droit ,longueur ,col ,centre, rayon):
    """
        Réalise le pavage d'hexagones
    Entrées :
            inf_gauche : valeur entière donnant les coordonnées du bord inférieur gauche de la fenêtre de visualisation
            sup_droit : valeur entière donnant les coordonnées  du bord supérieur droit de la fenêtre de visualisation ;
            longueur : valeur entière longueur d’un segment de pavé
            col : triple de chaîne de caractères donnant les trois couleurs des pavés
            centre : trois entiers donnant les coordonnées du centre de la sphère déformante
            rayon : entier donnant le rayon de la sphère déformante.
    Sorties : Pavage d'hexagones
    """
    pasy = int(sqrt((longueur**2)-(longueur/2)**2))
    count = 0
    for y in range(inf_gauche,sup_droit,pasy): #Boucle qui trace le pavage d'hexagones
        x = inf_gauche
        if (count % 2) == 0:
            x += 1.5*longueur

        for j in range(inf_gauche,sup_droit,3*longueur):
            point = (x,y)
            hexagon(point,col,longueur,centre,rayon)   # Appelle de la fonction hexagon
            x += 3*longueur
        count += 1

### Code Global ###
inf_gauche = int(input("Bord inférieur gauche de la fenêtre de visualisation : "))
sup_droit = int(input("Bord supérieur droit de la fenêtre de visualisation : "))
longueur = int(input("Veulliez entrez votre longueur : "))
col1 = str(input("Couleur 1 : "))
col2 = str(input("Couleur 2 : "))
col3 = str(input("Couleur 3 : "))
x_c = int(input("Cordonnée en x : "))
y_c = int(input("Cordonnée en y : "))
z_c = int(input("Cordonnée en z : "))
rayon = int(input("Rayon de la sphère : "))
col = (col1, col2, col3)
centre = (x_c, y_c, z_c)
t.speed("fastest")      # Augmente la vitesse de dessin
t.delay(0)              # définit le délai d'affichage en millisecondes
t.tracer(10000)         # définit le nombre de deplacement affiché



pavage(inf_gauche, sup_droit ,longueur ,col ,centre, rayon)

t.done()