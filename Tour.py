from jeu import *

def tours(x,y):
    if tour_jeux == 0:
        tours = 0
        if tours == 0:
            avance = x + y
            p1.pos += avance
            tours += 1
            tour_jeux = 1
        elif tours == 1:
            avance = x + y
            p2.pos += avance
    else:
        if tours == 0:
            avance = x + y
            p1.pos += avance
            tours = 1
        elif tours == 1:
            avance = x + y
            p2.pos += avance
            tours = 0
        