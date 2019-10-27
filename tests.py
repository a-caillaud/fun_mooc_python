import turtle
from math import pi, sin, cos, sqrt, acos, asin, atan2


# p_x = 0
# p_y = 0
# p_z = 0
# point = p_x, p_y, p_z

# longueur = 0

# col1 = 'red'
# col2 = 'black'
# col3 = 'blue'
# col = col1, col2, col3

# c_x = 0 
# c_y = 0
# c_z = 0
# centre = c_x, c_y, c_z

# rayon = 0



# def deformation(point, centre, rayon):
#     x, y, z = point
#     xprim, yprim, zprim = x, y, z
#     xprim = x * 3
#     yprim = y * 2
#     zprim = z
#     print(xprim, yprim, zprim)
#     return xprim, yprim, zprim



def deformation(p, centre, rayon):
    """ Calcul des coordonnées d'un point suite à la déformation engendrée par la sphère émergeante
        Entrées : 
          p : coordonnées (x, y, z) du point du dalage à tracer (z = 0) AVANT déformation
          centre : coordonnées (X0, Y0, Z0) du centre de la sphère
          rayon : rayon de la sphère
        Sorties : coordonnées (xprim, yprim, zprim) du point du dallage à tracer APRÈS déformation
    """
    x, y, z = p
    xprim, yprim, zprim = x, y, z
    xc, yc, zc = centre
    if rayon**2 > zc**2:
        zc = zc if zc <= 0 else -zc
        r = sqrt(
            (x - xc) ** 2 + (y - yc) ** 2)                  # distance horizontale depuis le point à dessiner jusqu'à l'axe de la sphère
        rayon_emerge = sqrt(rayon ** 2 - zc ** 2)           # rayon de la partie émergée de la sphère
        rprim = rayon * sin(acos(-zc / rayon) * r / rayon_emerge)
        if 0 < r <= rayon_emerge:                 # calcul de la déformation dans les autres cas
            xprim = xc + (x - xc) * rprim / r               # les nouvelles coordonnées sont proportionnelles aux anciennes
            yprim = yc + (y - yc) * rprim / r
        if r <= rayon_emerge:             
            beta = asin(rprim / rayon) 
            zprim = zc + rayon * cos(beta) 
            if centre[2] > 0:
                zprim = -zprim
    return (xprim, yprim, zprim)

if __name__ == "__main__": # code de test
    for i in range(-150,150,50):
        for j in range(-150,150,50):
            print(deformation((i,j,0), (0,0,100), 100))
        print()









def hexagone(point, longueur, col, centre, rayon):
    
    p_x, p_y, p_z = point
    col1, col2, col3 = col
    c_x, c_y, c_z = centre
    p = point
    
    turtle.up()
    turtle.goto(p_x, p_y)
    turtle.down()

    turtle.color(col[0])
    turtle.begin_fill()
    turtle.goto(p_x + longueur * cos(0), p_y + longueur * sin(0))
    turtle.goto(p_x + longueur * cos(pi / 3), p_y + longueur * sin(pi / 3))
    turtle.goto(p_x + longueur * cos(pi * 2 / 3), p_y + longueur * sin(pi * 2 / 3))
    turtle.goto(p_x, p_y)
    turtle.end_fill()
    turtle.up()
    turtle.goto(p_x + longueur * cos(pi * 2 / 3), p_y + longueur * sin(pi * 2 / 3))
    turtle.down()
    turtle.color(col[1])
    turtle.begin_fill()
    turtle.goto(p_x - longueur, p_y)
    turtle.goto(p_x + longueur * cos(4 / 3 * pi), p_y + longueur * sin(4 / 3 * pi))
    turtle.goto(p_x, p_y)
    turtle.end_fill()
    turtle.up()
    turtle.goto(p_x + longueur * cos(4 / 3 * pi), p_y + longueur * sin(4 / 3 * pi))
    turtle.down()
    turtle.color(col[2])
    turtle.begin_fill()
    turtle.goto(p_x + longueur * cos(5 / 3 * pi), p_y + longueur * sin(5 / 3 * pi))
    turtle.goto(p_x + longueur * cos(0), p_y + longueur * sin(0))
    turtle.goto(p_x, p_y)
    turtle.end_fill()
    turtle.hideturtle()
    turtle.done()
    print(point)
    


# hexagone((2, 2, 0), 50, ('red', 'blue', 'grey'), (0, 0, 0), 0)
xprim, yprim, zprim = deformation((10, 5, 2), (5, 5, 5), 50)
# print(xprim, yprim, zprim)
hexagone((xprim, yprim, zprim), 50, ('red', 'blue', 'grey'), (0, 0, 0), 0)