from jeu import *

#definition des positions que peux prendre le joueur

def case1(x):
    if x == 1:
        p1.pos_x = 400
        p1.pos_y = 600
    if x == 2:
        p1.pos_x = 500
        p1.pos_y = 600
    if x == 3:
        p1.pos_x = 600
        p1.pos_y = 600
    if x == 4:
        p1.pos_x = 700
        p1.pos_y = 600
    if x == 5:
        p1.pos_x = 800
        p1.pos_y = 600
    if x == 6:
        p1.pos_x = 1200
        p1.pos_y = 300
    if x == 7:
        p1.pos_x = 1000
        p1.pos_y = 600
    if x == 8:
        p1.pos_x = 1100
        p1.pos_y = 600
    if x == 9:
        p1.pos_x = 1200
        p1.pos_y = 600
    if x == 10:
        p1.pos_x = 1200
        p1.pos_y = 500
    if x == 11:
        p1.pos_x = 1200
        p1.pos_y = 400
    if x == 12:
        p1.pos_x = 1200
        p1.pos_y = 300
    if x == 13:
        p1.pos_x = 1200
        p1.pos_y = 200
    if x == 14:
        p1.pos_x = 1200
        p1.pos_y = 100
    if x == 15:
        p1.pos_x = 1200
        p1.pos_y = 0
    if x == 16:
        p1.pos_x = 1100
        p1.pos_y = 0
    if x == 17:
        p1.pos_x = 1000
        p1.pos_y = 0
    if x == 18:
        p1.pos_x = 900
        p1.pos_y = 0
    if x == 19:
        p1.pos_x = 800
        p1.pos_y = 0
    if x == 20:
        p1.pos_x = 700
        p1.pos_y = 0
    if x == 21:
        p1.pos_x = 600
        p1.pos_y = 0
    if x == 22:
        p1.pos_x = 500
        p1.pos_y = 0
    if x == 23:
        p1.pos_x = 400
        p1.pos_y = 0
    if x == 24:
        p1.pos_x = 400
        p1.pos_y = 100
    if x == 25:
        p1.pos_x = 400
        p1.pos_y = 200
    if x == 26:
        p1.pos_x = 400
        p1.pos_y = 300
    if x == 27:
        p1.pos_x = 400
        p1.pos_y = 400
    if x == 28:
        p1.pos_x = 400
        p1.pos_y = 500
    if x == 29:
        p1.pos_x = 500
        p1.pos_y = 500
    if x == 30:
        p1.pos_x = 600
        p1.pos_y = 500
    if x == 31:
        p1.pos_x = 700
        p1.pos_y = 500
    if x == 32:
        p1.pos_x = 800
        p1.pos_y = 500
    if x == 33:
        p1.pos_x = 900
        p1.pos_y = 500
    if x == 34:
        p1.pos_x = 1000
        p1.pos_y = 500
    if x == 35:
        p1.pos_x = 1100
        p1.pos_y = 500
    if x == 36:
        p1.pos_x = 1100
        p1.pos_y = 400
    if x == 37:
        p1.pos_x = 1100
        p1.pos_y = 300
    if x == 38:
        p1.pos_x = 1100
        p1.pos_y = 200
    if x == 39:
        p1.pos_x = 1100
        p1.pos_y = 100
    if x == 40:
        p1.pos_x = 1000
        p1.pos_y = 100
    if x == 41:
        p1.pos_x = 900
        p1.pos_y = 100
    if x == 42:
        p1.pos_x = 600
        p1.pos_y = 500
    if x == 43:
        p1.pos_x = 700
        p1.pos_y = 100
    if x == 44:
        p1.pos_x = 600
        p1.pos_y = 100
    if x == 45:
        p1.pos_x = 500
        p1.pos_y = 100
    if x == 46:
        p1.pos_x = 500
        p1.pos_y = 200
    if x == 47:
        p1.pos_x = 500
        p1.pos_y = 300
    if x == 48:
        p1.pos_x = 500
        p1.pos_y = 400
    if x == 49:
        p1.pos_x = 600
        p1.pos_y = 400
    if x == 50:
        p1.pos_x = 700
        p1.pos_y = 400
    if x == 51:
        p1.pos_x = 800
        p1.pos_y = 400
    if x == 52:
        p1.pos_x = 900
        p1.pos_y = 400
    if x == 53:
        p1.pos_x = 1000
        p1.pos_y = 400
    if x == 54:
        p1.pos_x = 1000
        p1.pos_y = 300
    if x == 55:
        p1.pos_x = 1000
        p1.pos_y = 200
    if x == 56:
        p1.pos_x = 900
        p1.pos_y = 200
    if x == 57:
        p1.pos_x = 800
        p1.pos_y = 200
    if x == 58:
        p1.pos_x = 400
        p1.pos_y = 600
    if x == 59:
        p1.pos_x = 600
        p1.pos_y = 200
    if x == 60:
        p1.pos_x = 600
        p1.pos_y = 300
    if x == 61:
        p1.pos_x = 700
        p1.pos_y = 300
    if x == 62:
        p1.pos_x = 800
        p1.pos_y = 300
    if x == 63:
        p1.pos_x = 900
        p1.pos_y = 300
    if x > 63:
        p1.pos_x = 900
        p1.pos_y = 300

def case2(x):
    if x == 1:
        p2.pos_x = 400
        p2.pos_y = 600
    if x == 2:
        p2.pos_x = 500
        p2.pos_y = 600
    if x == 3:
        p2.pos_x = 600
        p2.pos_y = 600
    if x == 4:
        p2.pos_x = 700
        p2.pos_y = 600
    if x == 5:
        p2.pos_x = 800
        p2.pos_y = 600
    if x == 6:
        p2.pos_x = 900
        p2.pos_y = 600
    if x == 7:
        p2.pos_x = 1000
        p2.pos_y = 600
    if x == 8:
        p2.pos_x = 1100
        p2.pos_y = 600
    if x == 9:
        p2.pos_x = 1200
        p2.pos_y = 600
    if x == 10:
        p2.pos_x = 1200
        p2.pos_y = 500
    if x == 11:
        p2.pos_x = 1200
        p2.pos_y = 400
    if x == 12:
        p2.pos_x = 1200
        p2.pos_y = 300
    if x == 13:
        p2.pos_x = 1200
        p2.pos_y = 200
    if x == 14:
        p2.pos_x = 1200
        p2.pos_y = 100
    if x == 15:
        p2.pos_x = 1200
        p2.pos_y = 0
    if x == 16:
        p2.pos_x = 1100
        p2.pos_y = 0
    if x == 17:
        p2.pos_x = 1000
        p2.pos_y = 0
    if x == 18:
        p2.pos_x = 900
        p2.pos_y = 0
    if x == 19:
        p2.pos_x = 800
        p2.pos_y = 0
    if x == 20:
        p2.pos_x = 700
        p2.pos_y = 0
    if x == 21:
        p2.pos_x = 600
        p2.pos_y = 0
    if x == 22:
        p2.pos_x = 500
        p2.pos_y = 0
    if x == 23:
        p2.pos_x = 400
        p2.pos_y = 0
    if x == 24:
        p2.pos_x = 400
        p2.pos_y = 100
    if x == 25:
        p2.pos_x = 400
        p2.pos_y = 200
    if x == 26:
        p2.pos_x = 400
        p2.pos_y = 300
    if x == 27:
        p2.pos_x = 400
        p2.pos_y = 400
    if x == 28:
        p2.pos_x = 400
        p2.pos_y = 500
    if x == 29:
        p2.pos_x = 500
        p2.pos_y = 500
    if x == 30:
        p2.pos_x = 600
        p2.pos_y = 500
    if x == 31:
        p2.pos_x = 700
        p2.pos_y = 500
    if x == 32:
        p2.pos_x = 800
        p2.pos_y = 500
    if x == 33:
        p2.pos_x = 900
        p2.pos_y = 500
    if x == 34:
        p2.pos_x = 1000
        p2.pos_y = 500
    if x == 35:
        p2.pos_x = 1100
        p2.pos_y = 500
    if x == 36:
        p2.pos_x = 1100
        p2.pos_y = 400
    if x == 37:
        p2.pos_x = 1100
        p2.pos_y = 300
    if x == 38:
        p2.pos_x = 1100
        p2.pos_y = 200
    if x == 39:
        p2.pos_x = 1100
        p2.pos_y = 100
    if x == 40:
        p2.pos_x = 1000
        p2.pos_y = 100
    if x == 41:
        p2.pos_x = 900
        p2.pos_y = 100
    if x == 42:
        p2.pos_x = 800
        p2.pos_y = 100
    if x == 43:
        p2.pos_x = 700
        p2.pos_y = 100
    if x == 44:
        p2.pos_x = 600
        p2.pos_y = 100
    if x == 45:
        p2.pos_x = 500
        p2.pos_y = 100
    if x == 46:
        p2.pos_x = 500
        p2.pos_y = 200
    if x == 47:
        p2.pos_x = 500
        p2.pos_y = 300
    if x == 48:
        p2.pos_x = 500
        p2.pos_y = 400
    if x == 49:
        p2.pos_x = 600
        p2.pos_y = 400
    if x == 50:
        p2.pos_x = 700
        p2.pos_y = 400
    if x == 51:
        p2.pos_x = 800
        p2.pos_y = 400
    if x == 52:
        p2.pos_x = 900
        p2.pos_y = 400
    if x == 53:
        p2.pos_x = 1000
        p2.pos_y = 400
    if x == 54:
        p2.pos_x = 1000
        p2.pos_y = 300
    if x == 55:
        p2.pos_x = 1000
        p2.pos_y = 200
    if x == 56:
        p2.pos_x = 900
        p2.pos_y = 200
    if x == 57:
        p2.pos_x = 800
        p2.pos_y = 200
    if x == 58:
        p2.pos_x = 700
        p2.pos_y = 200
    if x == 59:
        p2.pos_x = 600
        p2.pos_y = 200
    if x == 60:
        p2.pos_x = 600
        p2.pos_y = 300
    if x == 61:
        p2.pos_x = 700
        p2.pos_y = 300
    if x == 62:
        p2.pos_x = 800
        p2.pos_y = 300
    if x == 63:
        p2.pos_x = 900
        p2.pos_y = 300
    if x > 63:
        p2.pos_x = 900
        p2.pos_y = 300