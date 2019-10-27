import turtle
from math import pi, sin, cos

# Déclaration des variables : 
p_x = 0
p_y = 0
p_z = 0
point = (p_x, p_y, p_z)

longueur = 0

col1 = 'red'
col2 = 'black'
col3 = 'blue'
col = (col1, col2, col3)

c_x = 0
c_y = 0
c_z = 0
centre = (c_x, c_y, c_z)

rayon = 0




# code déformation

def deformation(point, centre, rayon):
    """renvoie le point sans le modifier"""
    return point



# code pavé

def pave(abscisse_centre, ordonnee_centre, longueur_arete, color1, color2, color3):

    turtle.up()
    turtle.goto(abscisse_centre, ordonnee_centre)
    turtle.down()

    turtle.color(color1)
    turtle.begin_fill()
    turtle.goto(abscisse_centre + longueur_arete * cos(0), ordonnee_centre + longueur_arete * sin(0))
    turtle.goto(abscisse_centre + longueur_arete * cos(pi / 3), ordonnee_centre + longueur_arete * sin(pi / 3))
    turtle.goto(abscisse_centre + longueur_arete * cos(pi * 2 / 3), ordonnee_centre + longueur_arete * sin(pi * 2 / 3))
    turtle.goto(abscisse_centre, ordonnee_centre)
    turtle.end_fill()
    turtle.up()
    turtle.goto(abscisse_centre + longueur_arete * cos(pi * 2 / 3), ordonnee_centre + longueur_arete * sin(pi * 2 / 3))
    turtle.down()
    turtle.color(color2)
    turtle.begin_fill()
    turtle.goto(abscisse_centre - longueur_arete, ordonnee_centre)
    turtle.goto(abscisse_centre + longueur_arete * cos(4 / 3 * pi), ordonnee_centre + longueur_arete * sin(4 / 3 * pi))
    turtle.goto(abscisse_centre, ordonnee_centre)
    turtle.end_fill()
    turtle.up()
    turtle.goto(abscisse_centre + longueur_arete * cos(4 / 3 * pi), ordonnee_centre + longueur_arete * sin(4 / 3 * pi))
    turtle.down()
    turtle.color(color3)
    turtle.begin_fill()
    turtle.goto(abscisse_centre + longueur_arete * cos(5 / 3 * pi), ordonnee_centre + longueur_arete * sin(5 / 3 * pi))
    turtle.goto(abscisse_centre + longueur_arete * cos(0), ordonnee_centre + longueur_arete * sin(0))
    turtle.goto(abscisse_centre, ordonnee_centre)
    turtle.end_fill()
    turtle.hideturtle()
    turtle.done()

pave(4, 6, 70, 'black', 'red', 'grey')