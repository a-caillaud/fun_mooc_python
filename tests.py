import turtle
from math import pi, sin, cos, sqrt, acos, asin, atan2
from deformation import deformation


def hexagone(point, longueur, col, centre, rayon): # dessine un hexagone en tenant compte de la déformation
    p_x, p_y = point # attribution des tupples point et couleurs
    col1, col2, col3 = col

    turtle.speed(10) # on lance le dessin de l'hexagone
    turtle.up()

    # Face 1
    p = p_x, p_y, 0
    xprim, yprim, zprim = deformation(p, centre, rayon)
    turtle.goto(xprim, yprim)

    turtle.down()

    turtle.color(col[0])
    turtle.begin_fill()

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

    turtle.end_fill()
    turtle.up()


    # Face 2
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

    # Face 3
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
    

def pavage (inf_gauche, sup_droit, longueur,col,centre,r):
    n = 1 #compteur de ligne
    angle = pi / 3 
    sup_droit1 = sup_droit # position du polygone apres chaque ligne
    pas = 3 * longueur # espacement entre deux polygones
    new_inf_gauche = int(inf_gauche - longueur * (1 + cos(angle))) # position de depart  du polygone pour les lignes paires
    new_sup_droit = int(sup_droit + longueur * (1 + cos(angle)))# position finale du polygone pour les lignes paires

    while sup_droit1 > inf_gauche: #tant le polygone n'est pas arrivé a la derniere ligne de la fenetre
        if n % 2 != 0: #cas d'une ligne impaire
            for x in range(inf_gauche, sup_droit, pas):
                point = (x, sup_droit1)
                hexagone(point,longueur,col,centre, r)
            n+=1
        else: #cas d'une ligne paire
            for x in range(new_inf_gauche, new_sup_droit, pas):
                point = (x, sup_droit1)
                hexagone(point,longueur,col,centre, r)
            n+=1
        sup_droit1 = sup_droit1-longueur *  sin(angle)
    turtle.hideturtle()
    turtle.getcanvas().postscript(file="pavage.eps")
    turtle.done()


pavage(-305, 305, 60, ('blue', 'black', 'red'), (-50, -50, -50), 240)
