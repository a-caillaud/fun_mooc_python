"""
Projet Vasarely (version 1)
Auteur : Alexis
Date : 27/10/2019
Ce programme Python dessine des tableaux d’art optique de tendance 'Vasarely'
Ces tableaux représentent des pavages hexagonaux, vus d’en haut, 
formés avec des losanges de couleurs différentes, déformés par une boule.
Entrée : paramètres globaux proposé dans le sujet Vasarely (code principal)
Sortie : fenêtre de visualisation du tableau de Vasarely

"""

# importation des modules

import turtle # module le dessin des pavéd
from math import pi, sin, cos # permet de calculer les coordonnées des sommets dans les hexagones
from deformation import deformation # calcule la déformation des coordonnées des hexagones


# Définition des constantes globales
# pas de constante globale dans ce code

# Définition des fonctions

def face1(point, longueur, col, centre, rayon):
    """
    La fonction 'face1' dessine la première face de l'hexagone, en utilisant la fontion déformation, à partir des paramètres suivants : 
    - un point sous forme d’un triple (tuple de trois composantes) donnant la valeur des trois coordonnées, correspondant au point avant déformation où l’hexagone doit être peint,
    - la distance (avant déformation) longueur entre le centre et n’importe quel coin de l’hexagone,
    - tuple col contenant les trois couleurs (col1, col2, col3) qui vont être utilisées pour dessiner les hexagones,
    - Le centre sous forme de triple (c_x, c_y, c_z) qui donne le centre de la sphère de déformation,
    - le rayon de la sphère de déformation.
    """
    p_x, p_y, p_z = point # attribution des coordonnées de départ de l'hexagone
    col1, col2, col3 = col # attribution des couleurs des faces de l'hexagone
    p = p_x, p_y, 0 # on attibue les coordonnées d'origine à la variable p, qui est utilisée dans la fonction déformation
    xprim, yprim, zprim = deformation(p, centre, rayon) # on récupere les coordonnées après déformation par la fonction déformation
    turtle.goto(xprim, yprim) # on se rend aux coordonnées calculées par la fonction déformation
    turtle.down() # on descend la tortue pour commencer à dessiner
    turtle.color(col[0]) # on dessine avec la couleur correspondante dans le tupple
    turtle.begin_fill() # on remplie la forme que l'on dessine avec la couleur choisie à la ligne précédente
    p = p_x + longueur * cos(0), p_y + longueur * sin(0), 0
    xprim, yprim, zprim = deformation(p, centre, rayon)
    turtle.goto(xprim, yprim)
    p = p_x + longueur * cos(pi / 3), p_y + longueur * sin(pi / 3), 0
    xprim, yprim, zprim = deformation(p, centre, rayon)
    turtle.goto(xprim, yprim)
    p = p_x + longueur * cos(pi * 2 / 3), p_y + longueur * sin(pi * 2 / 3), 0
    xprim, yprim, zprim = deformation(p, centre, rayon)
    turtle.goto(xprim, yprim)
    p = p_x, p_y, 0
    xprim, yprim, zprim = deformation(p, centre, rayon)
    turtle.goto(xprim, yprim)
    turtle.end_fill() # on arrete de remplir la forme avec la couleur
    turtle.up() # on relève la tortue pour ne pas dessiner    

def face2(point, longueur, col, centre, rayon):
    """
    La fonction 'face2' dessine la seconde face de l'hexagone, en utilisant la fontion déformation, à partir des paramètres suivants : 
    - un point sous forme d’un triple (tuple de trois composantes) donnant la valeur des trois coordonnées, correspondant au point avant déformation où l’hexagone doit être peint,
    - la distance (avant déformation) longueur entre le centre et n’importe quel coin de l’hexagone,
    - tuple col contenant les trois couleurs (col1, col2, col3) qui vont être utilisées pour dessiner les hexagones,
    - Le centre sous forme de triple (c_x, c_y, c_z) qui donne le centre de la sphère de déformation,
    - le rayon de la sphère de déformation.
    """
    p_x, p_y, p_z = point # attribution des coordonnées de départ de l'hexagone
    col1, col2, col3 = col # attribution des couleurs des faces de l'hexagone
    p = p_x + longueur * cos(pi * 2 / 3), p_y + longueur * sin(pi * 2 / 3), 0
    xprim, yprim, zprim = deformation(p, centre, rayon)
    turtle.goto(xprim, yprim)
    turtle.down()
    turtle.color(col[1])
    turtle.begin_fill()
    p = p_x - longueur, p_y, 0
    xprim, yprim, zprim = deformation(p, centre, rayon)
    turtle.goto(xprim, yprim)
    p = p_x + longueur * cos(4 / 3 * pi), p_y + longueur * sin(4 / 3 * pi), 0
    xprim, yprim, zprim = deformation(p, centre, rayon)
    turtle.goto(xprim, yprim)
    p = p_x, p_y, 0
    xprim, yprim, zprim = deformation(p, centre, rayon)
    turtle.goto(xprim, yprim)
    turtle.end_fill()
    turtle.up()

def face3(point, longueur, col, centre, rayon):
    """
    La fonction 'face3' dessine la troisième face de l'hexagone, en utilisant la fontion déformation, à partir des paramètres suivants : 
    - un point sous forme d’un triple (tuple de trois composantes) donnant la valeur des trois coordonnées, correspondant au point avant déformation où l’hexagone doit être peint,
    - la distance (avant déformation) longueur entre le centre et n’importe quel coin de l’hexagone,
    - tuple col contenant les trois couleurs (col1, col2, col3) qui vont être utilisées pour dessiner les hexagones,
    - Le centre sous forme de triple (c_x, c_y, c_z) qui donne le centre de la sphère de déformation,
    - le rayon de la sphère de déformation.
    """
    p_x, p_y, p_z = point # attribution des coordonnées de départ de l'hexagone
    col1, col2, col3 = col # attribution des couleurs des faces de l'hexagone
    p = p_x + longueur * cos(4 / 3 * pi), p_y + longueur * sin(4 / 3 * pi), 0
    xprim, yprim, zprim = deformation(p, centre, rayon)
    turtle.goto(xprim, yprim)
    turtle.down()
    turtle.color(col[2])
    turtle.begin_fill()
    p = p_x + longueur * cos(5 / 3 * pi), p_y + longueur * sin(5 / 3 * pi), 0
    xprim, yprim, zprim = deformation(p, centre, rayon)
    turtle.goto(xprim, yprim)
    p = p_x + longueur * cos(0), p_y + longueur * sin(0), 0
    xprim, yprim, zprim = deformation(p, centre, rayon)
    turtle.goto(xprim, yprim)
    p = p_x, p_y, 0
    xprim, yprim, zprim = deformation(p, centre, rayon)
    turtle.goto(xprim, yprim)
    turtle.end_fill()

def hexagone(point, longueur, col, centre, rayon): # dessine un hexagone en tenant compte de la déformation
    """
    La fonction 'hexagone' dessine un pavé en 3D en utilisant les fonctions face1, face2 et face3, à partir des paramètres suivants : 
    - un point sous forme d’un triple (tuple de trois composantes) donnant la valeur des trois coordonnées, correspondant au point avant déformation où l’hexagone doit être peint,
    - la distance (avant déformation) longueur entre le centre et n’importe quel coin de l’hexagone,
    - tuple col contenant les trois couleurs (col1, col2, col3) qui vont être utilisées pour dessiner les hexagones,
    - Le centre sous forme de triple (c_x, c_y, c_z) qui donne le centre de la sphère de déformation,
    - le rayon de la sphère de déformation.
    """
    turtle.speed(10) # on accèlere la vitesse de dessin de l'hexagone
    turtle.up() # on relève la tortue pour ne pas dessiner

    face1(point, longueur, col, centre, rayon)
    face2(point, longueur, col, centre, rayon)
    face3(point, longueur, col, centre, rayon)

def pavage(inf_gauche, sup_droit, longueur,col,centre,r):
    """
    La fonction 'pavage' génère le pavage hexaognal et la déformation à partir de la fonction 'hexagone' et et des paramètes suivants : 
    inf_gauche : (valeur entière) donnant les coordonnées (inf_gauche, inf_gauche) du bord inférieur gauche de la fenêtre de visualisation
    sup_droit : (valeur entière) donnant les coordonnées (sup_droit, sup_droit) du bord supérieur droit de la fenêtre de visualisation
    longueur : (valeur entière) longueur d’un segment de pavé (avant déformation)
    col : (triple de chaîne de caractères) donnant les trois couleurs des pavés
    centre : (trois entiers) donnant les coordonnées du centre de la sphère déformante
    r : (entier) donnant le rayon de la sphère déformante
    """
    n = 1 #compteur de ligne
    angle = pi / 3  # angle utilisé pour calculer les positions de départ et finale d'une ligne de pavage
    sup_droit1 = sup_droit # coordonnée y de départ d'une ligne de pavé, commun à tous les hexagone d'une ligne
    pas = 3 * longueur # espacement entre deux polygones
    new_inf_gauche = int(inf_gauche - longueur * (1 + cos(angle))) # position de depart  du polygone pour les lignes paires
    new_sup_droit = int(sup_droit + longueur * (1 + cos(angle)))# position finale du polygone pour les lignes paires

    while sup_droit1 > inf_gauche: #tant le polygone n'est pas arrivé a la derniere ligne de la fenetre
        # on fait un test pour savoir si l'on dessine une ligne paire ou impaire
        if n % 2 != 0: #cas d'une ligne impaire
            for x in range(inf_gauche, sup_droit, pas): # pour x dans l'intervalle entre les coordonnées de inf_gauche et sup_droit
                point = x, sup_droit1, 0 # on attribue les coordonnées de départ de l'hegagone
                hexagone(point,longueur,col,centre, r) # on dessine le pavé
            n+=1
        else: #cas d'une ligne paire
            for x in range(new_inf_gauche, new_sup_droit, pas):
                point = x, sup_droit1, 0
                hexagone(point,longueur,col,centre, r)
            n+=1
        sup_droit1 = sup_droit1-longueur *  sin(angle) # on calucule la nouvelle coordonnées sup_droit1 après le test paire vs impaire

# Code principal

pavage(-305, 305, 20, ("Blue", "Red", "Black"), (-50, -50, -50), 200) # avec les paramètres dans le sujet
turtle.hideturtle() # on cache la tortue
turtle.getcanvas().postscript(file="fun_mooc_python/pavage.eps") # on sauverage le tableau
turtle.done() # on arrete le module turtle