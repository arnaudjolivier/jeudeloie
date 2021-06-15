import pygame
import random
import sys

des1 = random.randrange(1,7)
des2 = random.randrange(1,7)
avance = des1 + des2

class joueur:
    def __init__(self):
        self.pos = 1
        self.pos_x = 400
        self.pos_y = 600
        self.timer1 = 0
        self.mouve = 0
        self.attendre = 0
#def des cases a effet spéciaux
def pos_speciale1():
    if p1.pos % 9 == 0:
        p1.pos += p1.mouve
        print('oie')

    if p1.pos == 6:
        p1.pos = 12
        print('pont')

    if p1.pos == 19:
        p1.timer1 = 2
        print('hotel ibis')

    if p1.pos == 42:
        p1.pos = 30
        print('tuut police')

    if p1.pos == 58:
        p1.pos = 1
        print('pouf tu es mort')
    
    if p1.pos == 31 or p1.pos == 52:
        p1.attendre = 1
        print('emprisonné')


def pos_speciale2():
    if p2.pos % 9 == 0:
        p2.pos += p2.mouve
        print('oie')

    if p2.pos == 6:
        p2.pos = 12
        print('pont')

    if p2.pos == 19:
        p2.timer1 = 2
        print('hotel ibis')

    if p2.pos == 42:
        p2.pos = 30
        print('tuut police')

    if p2.pos == 58:
        p2.pos = 1
        print('pouf tu es mort')
    
    if p2.pos == 31 or p2.pos == 52:
        p2.attendre = 1
        print('emprisonné')
#def des lancer de dés spéciaux sur le tour 1
def des_premtour1(x,y):
    if x == 6 and y ==3:
        print('Case 26')
        p1.pos = 26
        return True
    if x == 3 and y == 6:
        print('Case 26')
        p1.pos = 26
        return True
    if x == 5 and y ==4:
        print('Case 52')
        p1.pos = 52
        p1.attendre = 1
        return True
    if x == 4 and y == 5:
        print('Case 52')
        p1.pos = 52
        p1.attendre = 1
        return True
    else:
        return False
def des_premtour2(x,y):
    if x == 6 and y ==3:
        print('Case 26')
        p2.pos = 26
        return True
    if x == 3 and y == 6:
        print('Case 26')
        p2.pos = 26
        return True
    if x == 5 and y ==4:
        print('Case 52')
        p2.pos = 52
        p2.attendre = 1
        return True
    if x == 4 and y == 5:
        print('Case 52')
        p2.pos = 52
        p2.attendre = 1
        return True
    else:
        return False
p1 = joueur()
p2 = joueur()
pos_speciale1()
pos_speciale2()