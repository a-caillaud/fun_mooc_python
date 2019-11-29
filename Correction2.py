"""
    Projet Vasarely
    Auteur : Luka Delić
    Date : 25 octobre 2019
    Ce programme crée un programme à la Vasarely.
"""
import turtle
from math import sin, cos, pi
from deformation import deformation

def losanges(sommets, col):
    """
    Dessine/Trace les 3 losanges d'un hexagone
    :param sommets:
    :param col:
    :return:
    """
    for i in range(3):
        turtle.color(col[i])  # fonction qui trace le premier losange
        turtle.begin_fill()   # fonction qui fait que dès que le dessin est tracé il est coloré
        for sommet in sommets[i]:
            turtle.goto(sommet[0], sommet[1])    # on bouge le turtle vers le commet (0,1)
        turtle.end_fill()       # on arrête de tracer

def hexagone(point, longueur, col, centre, rayon):
    """
    fonction hexagone permettant  à partir de 3 losanges d'afficher
    un hexagone déformé peint de 3 couleurs centré en un point appelée "point" et
    de longueur longueur, cela est fait grâce à la méthode goto de turtle et
    à la fonction déformation qui renvoie un point déformé.
    Calcul des coordonnées des sommets des losanges réalisés
    grâce au théorème de Pythagore et l'aide du cosinus.
    :param point:
    :param longueur:
    :param col:
    :param centre:
    :param rayon:
    """
    point_x, point_y = point
    point_z = 0
    centre_hexagone = (deformation((point_x, point_y, point_z), centre, rayon)[0:2])
    sommet_a = (deformation((point_x+longueur, point_y, point_z), centre, rayon)[0:2])
    sommet_b = (deformation((point_x+(longueur/2), point_y + cos(pi / 6) * longueur, point_z), centre, rayon)[0:2])
    sommet_c = (deformation((point_x-(longueur/2), point_y + cos(pi / 6) * longueur, point_z), centre, rayon)[0:2])
    sommet_d = (deformation((point_x-longueur, point_y, 0), centre, rayon)[0:2])
    sommet_e = (deformation((point_x-(longueur/2), point_y+(-1*cos(pi/6)*longueur), point_z), centre, rayon)[0:2])
    sommet_f = (deformation((point_x+(longueur/2), point_y+(-1*cos(pi/6)*longueur), point_z), centre, rayon)[0:2])
    turtle.up()  # ceci lève et permet à turtle de se déplacer sans tracer jusqu'au centre d'un hexagone
    turtle.goto(centre_hexagone[0], centre_hexagone[1])
    turtle.down()  # rabaisse turtle pour tracer
    sommets = [(sommet_a, sommet_b, sommet_c, centre_hexagone),
               (sommet_e, sommet_f, sommet_a, centre_hexagone),
               (sommet_c, sommet_d, sommet_e, centre_hexagone)]
    losanges(sommets, col)

def pavage(inf_gauche, sup_droit, longueur, col, centre, rayon):
    """
    fonction permettant l'affichage d'un pavage hexagonale
    dont les coins inférieur gauche et supérieur droit représentent
    la limite de la fenêtre dont tous les hexagones ont leurs centres
    non déformé sont dans cette fenêtre.
    :param inf_gauche:
    :param sup_droit:
    :param longueur:
    :param col:
    :param centre:
    :param rayon:
    """
    point = (inf_gauche, inf_gauche)  # centre de départ du pavage.
    saut_ligne = True  # permet de passer à ligne supérieur pour afficher les hexagones
    while point[1] < sup_droit:
        while point[0] < sup_droit:
            hexagone(point, longueur, col, centre, rayon)
            # permet d'afficher la première ligne du pavage
            point = (point[0]+3*longueur, point[1])
        if saut_ligne:  # permet de décaler chaque second ligne à partir de la 1ére ligne du bas
            point = (inf_gauche + 3*longueur/2, point[1]+sin(pi/3)*longueur)
            saut_ligne = False
        elif not saut_ligne :  # sinon recommence une ligne comme la première ligne
            point = (inf_gauche, point[1] + sin(pi/3)*longueur)
            saut_ligne = True

def main():
    """
    Fonction principal demandant les inputs
    """
    # inf_gauche = int(input("Entrée l'abscisse du coin inférieur gauche : "))
    # sup_droit = int(input("Entrée l'abscisse du coin supérieur droit : "))
    # longueur = int(input("Entrée la Longueur d'un côté de l'hexagone : "))
    # col1 = input("Entrée la couleur 1 du premier losange (Nord-Est) : ")
    # col2 = input("Entrée la couleur 2 du deuxième losange (Ouest) : ")
    # col3 = input("Entrée la couleur 3 du troisième losange (Sud-Est): ")
    # col = (col1, col2, col3)
    # c_x = int(input("Entrée l'abscisse du centre de déformation : "))
    # c_y = int(input("Entrée l'ordonnée du centre de déformation : "))
    # c_z= int(input("Entrée la cote du centre de déformation : "))
    # centre = (c_x, c_y, c_z)
    # rayon = int(input("Entrée le rayon de la déformation : "))
    # pavage(inf_gauche, sup_droit, longueur, col, centre, rayon)
    centre = (-50, -50, -50)
    rayon = 200
    pavage(inf_gauche= -305, sup_droit=305, longueur=20, col=('red', 'purple', 'black'), centre=centre, rayon=rayon)

if __name__ == '__main__':
    turtle.speed('normal')
    main()
    turtle.getcanvas().postscript(file="pavage.eps")
    turtle.done()