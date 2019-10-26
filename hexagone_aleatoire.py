
import turtle
from math import pi, sin, cos
import random
import time

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
    # turtle.hideturtle()
    # turtle.done()

turtle.hideturtle()
turtle.speed(0)
turtle.reset()
time.sleep(5)


while True:
     pave(random.randint(-300,300),  random.randint(-300,300),
         random.randint(10,50), 'black', 'red', 'blue')
     pave(random.randint(-300,300),  random.randint(-300,300),
         random.randint(10,50), 'white', 'grey', 'black')
