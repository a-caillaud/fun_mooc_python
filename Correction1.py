"""
    Projet dans le cadre du MOOC "Apprendre a coder avec Python
    Auteur : Mohammed BERRIAH
    Date : 27 octobre 2019
"""

import math
import turtle
from deformation import deformation

def pave(abscisse_centre, ordonnee_centre, longueur_arete, color1, color2, color3):
    """
        Construction de plusieurs paves.
        Fonction a creer : pave(abscisse_centre, ordonnee_centre, longueur_arete, color1, color2, color3)
        abscisse_centre ordonnee_centre : coordonnees du point central
        longueur_arete : longueur de cote
        color1, color2, color3 : couleurs de remplissage
    """
    turtle.speed(100)
    #Dessim de la face rouge du pave
    turtle.color(color1)
    turtle.begin_fill()
    turtle.forward(longueur_arete)
    turtle.right(120)
    turtle.forward(longueur_arete)
    turtle.right(60)
    turtle.forward(longueur_arete)
    turtle.right(120)
    turtle.forward(longueur_arete)
    turtle.right(60)
    turtle.end_fill()

    #Dessin de la face bleue du pave
    turtle.color(color2)
    turtle.begin_fill()
    turtle.forward(longueur_arete)
    turtle.left(120)
    turtle.forward(longueur_arete)
    turtle.left(60)
    turtle.forward(longueur_arete)
    turtle.left(120)
    turtle.forward(longueur_arete)
    turtle.right(60)
    turtle.end_fill()

    #Dessin de la face noire du pave
    turtle.color(color3)
    turtle.begin_fill()
    turtle.forward(longueur_arete)
    turtle.right(120)
    turtle.forward(longueur_arete)
    turtle.right(60)
    turtle.forward(longueur_arete)
    turtle.right(120)
    turtle.forward(longueur_arete)
    turtle.left(60)
    turtle.end_fill()

x_centre = -300
y_centre = -300
COTE = 20
n_pave = 0
n_ligne = 0

#Pavage
while n_ligne < 35:
    #Dessin des paves sur la nieme ligne
    while n_pave < 11:
        turtle.up()
        turtle.goto(x_centre, y_centre)
        turtle.down()

        pave(x_centre, y_centre, COTE, "red", "blue", "black")

        x_centre = x_centre + (COTE*3)
        n_pave += 1

    n_pave = 0

    #Recentrage si nunero de ligne paire
    if n_ligne % 2 == 0:
        x_centre = -300 + (COTE * 1.5)
        y_centre = y_centre + (math.sin(1/3*math.pi) * COTE)

    #Recetrange si numero de ligne impaire
    else:
        x_centre = -300
        y_centre = y_centre + (math.sin(1/3*math.pi) * COTE)
        print(y_centre)
    n_ligne += 1

turtle.done()