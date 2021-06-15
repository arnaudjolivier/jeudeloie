import random
import os

class oie:
    def __init__(self):
        self.pos = 0
        self.img = 0
        self.timer = 0
        self.attendre = 0

def des():
    des1 = random.randrange(1,7)
    des2 = random.randrange(1,7)
    if prem_tour == 0:
        if des1 == 6:
            if des2 ==3:
                print('Case 26')
                return 26
        if des1 == 3:
            if des2 == 6:
                print('Case 26')
                return 26
        if des1 == 5:
            if des2 ==4:
                print('Case 52')
                return 52
        if des1 == 4:
            if des2 == 5:
                print('Case 52')
                return 52
    add = des1 + des2
    return add
tour = 0
p1 = oie()
p2 = oie()
p3 = oie()
p4 = oie()
p5 = oie()
p6 = oie()
continuer = 0
os.system('cls')
prem_tour = 0
tour_jeux = 0
input('Lancez les des\n')
while continuer == 0:
    avance = des()
    print('Avancez de ' + str(avance))
    if tour == 0:
        if p1.attendre == 0:
            if p1.timer == 0:
                p1.pos += avance
                if p1.pos % 9 == 0:
                    print('Et c\'est partit les copains')
                    p1.pos += avance
                if p1.pos == 31:
                    print('En prison')
                    p1.attendre = 1
                if p1.pos == 52:
                    print('En prison aussi')
                    p1.attendre = 1
                if p1.pos == 42:
                    print('Et bah non')
                    p1.pos = 30
                if p1.pos == 58:
                    print('Retour a la case départ')
                    p1.pos = 1
                if p1.pos == 6:
                    print('Pont a 12')
                    p1.pos = 12
                if p1.pos == 19:
                    print('Bienvenue a l\'hotel ibis')
                    p1.timer = 2
                if p1.pos == 63:
                    continuer = 1
                    print('P1 Win')
                if p1.pos > 63:
                    recule = p1.pos - 63
                    p1.pos = 63 - recule
                    if p1.pos % 9 == 0:
                        p1.pos-=recule
                if p1.pos == p2.pos:
                    p2.pos -= avance
                if p1.pos == p3.pos:
                    p3.pos -= avance
                if p1.pos == p4.pos:
                    p4.pos -= avance
                if p1.pos == p5.pos:
                    p5.pos -= avance
                if p1.pos == p6.pos:
                    p6.pos -= avance
                print(str(p1.pos) + ' P1')
            else:
                print('Vous avez oubliez de payez, la Stonks Industries vous charge de dormir et de payer une nuit supplementaire')
                p1.timer -=1
        if p1.attendre == 1 and (p2.pos >= p1.pos or p3.pos >= p1.pos or p4.pos >= p1.pos or p5.pos >= p1.pos or p6.pos >= p1.pos):
            p1.attendre = 0
        elif p1.attendre == 1:
            print('Prisonnier reste la')
            p1.attendre = 1
        tour += 1      
    elif tour == 1: 
        if p2.attendre == 0:
            if p2.timer == 0:
                p2.pos += avance
                if p2.pos % 9 == 0:
                    print('Et c\'est partit les copains')
                    p2.pos += avance
                if p2.pos == 31:
                    print('En prison')
                    p2.attendre = 1
                if p2.pos == 52:
                    print('En prison aussi')
                    p2.attendre = 1
                if p2.pos == 42:
                    print('Et bah non')
                    p2.pos = 30
                if p2.pos == 58:
                    print('Retour a la case départ')
                    p2.pos = 1
                if p2.pos == 6:
                    print('Pont a 12')
                    p2.pos = 12
                if p2.pos == 19:
                    print('Bienvenue a l\'hotel ibis')
                    p2.timer = 2
                if p2.pos == 63:
                    continuer = 1
                    print('P2 Win')
                if p2.pos > 63:
                    recule = p2.pos - 63
                    p2.pos = 63 - recule
                    if p2.pos % 9 == 0:
                        p2.pos-=recule
                if p2.pos == p1.pos:
                    p1.pos -= avance
                if p2.pos == p3.pos:
                    p3.pos -= avance
                if p2.pos == p4.pos:
                    p4.pos -= avance
                if p2.pos == p5.pos:
                    p5.pos -= avance
                if p2.pos == p6.pos:
                    p6.pos -= avance
                print(str(p2.pos) + ' P2')
            else:
                print('Vous avez oubliez de payez, la Stonks Industries vous charge de dormir et de payer une nuit supplementaire')
                p2.timer -=1
        if p2.attendre == 1 and (p1.pos >= p2.pos or p3.pos >= p2.pos or p4.pos >= p2.pos or p5.pos >= p2.pos or p6.pos >= p2.pos):
            p2.attendre = 0
        elif p2.attendre == 1:
            print('Prisonnier reste la')
            p2.attendre = 1
        tour += 1 
    elif tour == 2:
        if p3.attendre == 0:
            if p3.timer == 0:
                p3.pos += avance
                if p3.pos % 9 == 0:
                    print('Et c\'est partit les copains')
                    p3.pos += avance
                if p3.pos == 31:
                    print('En prison')
                    p3.attendre = 1
                if p3.pos == 52:
                    print('En prison aussi')
                    p3.attendre = 1
                if p3.pos == 42:
                    print('Et bah non')
                    p3.pos = 30
                if p3.pos == 58:
                    print('Retour a la case départ')
                    p3.pos = 1
                if p3.pos == 6:
                    print('Pont a 12')
                    p3.pos = 12
                if p3.pos == 19:
                    print('Bienvenue a l\'hotel ibis')
                    p3.timer = 2
                if p3.pos == 63:
                    continuer = 1
                    print('P3 Win')
                if p3.pos > 63:
                    recule = p3.pos - 63
                    p3.pos = 63 - recule
                    if p3.pos % 9 == 0:
                        p3.pos-=recule
                if p3.pos == p2.pos:
                    p2.pos -= avance
                if p3.pos == p1.pos:
                    p1.pos -= avance
                if p3.pos == p4.pos:
                    p4.pos -= avance
                if p3.pos == p5.pos:
                    p5.pos -= avance
                if p3.pos == p6.pos:
                    p6.pos -= avance
                print(str(p3.pos) + ' P3')
            else:
                print('Vous avez oubliez de payez, la Stonks Industries vous charge de dormir et de payer une nuit supplementaire')
                p3.timer -=1
        if p3.attendre == 1 and (p2.pos >= p3.pos or p1.pos >= p3.pos or p4.pos >= p3.pos or p5.pos >= p3.pos or p6.pos >= p3.pos):
            p3.attendre = 0
        elif p3.attendre == 1:
            print('Prisonnier reste la')
            p3.attendre = 1
        tour += 1
    elif tour == 3:
        if p4.attendre == 0:
            if p4.timer == 0:
                p4.pos += avance
                if p4.pos % 9 == 0:
                    print('Et c\'est partit les copains')
                    p4.pos += avance
                if p4.pos == 31:
                    print('En prison')
                    p4.attendre = 1
                if p4.pos == 52:
                    print('En prison aussi')
                    p4.attendre = 1
                if p4.pos == 42:
                    print('Et bah non')
                    p4.pos = 30
                if p4.pos == 58:
                    print('Retour a la case départ')
                    p4.pos = 1
                if p4.pos == 6:
                    print('Pont a 12')
                    p4.pos = 12
                if p4.pos == 19:
                    print('Bienvenue a l\'hotel ibis')
                    p4.timer = 2
                if p4.pos == 63:
                    continuer = 1
                    print('P4 Win')
                if p4.pos > 63:
                    recule = p4.pos - 63
                    p4.pos = 63 - recule
                    if p4.pos % 9 == 0:
                        p4.pos-=recule
                if p4.pos == p2.pos:
                    p2.pos -= avance
                if p4.pos == p3.pos:
                    p3.pos -= avance
                if p4.pos == p5.pos:
                    p5.pos -= avance
                if p4.pos == p1.pos:
                    p1.pos -= avance
                if p4.pos == p6.pos:
                    p6.pos -= avance
                print(str(p4.pos) + ' P4')
            else:
                print('Vous avez oubliez de payez, la Stonks Industries vous charge de dormir et de payer une nuit supplementaire')
                p4.timer -=1
        if p4.attendre == 1 and (p2.pos >= p4.pos or p3.pos >= p4.pos or p1.pos >= p4.pos or p5.pos >= p4.pos or p6.pos >= p4.pos):
            p4.attendre = 0
        elif p4.attendre == 1:
            print('Prisonnier reste la')
            p4.attendre = 1
        tour += 1
    elif tour == 4:
        if p5.attendre == 0:
            if p5.timer == 0:
                p5.pos += avance
                if p5.pos % 9 == 0:
                    print('Et c\'est partit les copains')
                    p5.pos += avance
                if p5.pos == 31:
                    print('En prison')
                    p5.attendre = 1
                if p5.pos == 52:
                    print('En prison aussi')
                    p5.attendre = 1
                if p5.pos == 42:
                    print('Et bah non')
                    p5.pos = 30
                if p5.pos == 58:
                    print('Retour a la case départ')
                    p5.pos = 1
                if p5.pos == 6:
                    print('Pont a 12')
                    p5.pos = 12
                if p5.pos == 19:
                    print('Bienvenue a l\'hotel ibis')
                    p5.timer = 2
                if p5.pos == 63:
                    continuer = 1
                    print('P5 Win')
                if p5.pos > 63:
                    recule = p5.pos - 63
                    p5.pos = 63 - recule
                    if p5.pos % 9 == 0:
                        p5.pos-=recule
                if p5.pos == p2.pos:
                    p2.pos -= avance
                if p5.pos == p3.pos:
                    p3.pos -= avance
                if p5.pos == p4.pos:
                    p4.pos -= avance
                if p5.pos == p1.pos:
                    p1.pos -= avance
                if p5.pos == p6.pos:
                    p6.pos -= avance
                print(str(p5.pos) + ' P5')
            else:
                print('Vous avez oubliez de payez, la Stonks Industries vous charge de dormir et de payer une nuit supplementaire')
                p5.timer -=1
        if p5.attendre == 1 and (p2.pos >= p5.pos or p3.pos >= p5.pos or p4.pos >= p5.pos or p1.pos >= p5.pos or p6.pos >= p5.pos):
            p5.attendre = 0
        elif p5.attendre == 1:
            print('Prisonnier reste la')
            p5.attendre = 1
        tour += 1
    elif tour == 5:
        if p6.attendre == 0:
            if p6.timer == 0:
                p6.pos += avance
                if p6.pos % 9 == 0:
                    print('Et c\'est partit les copains')
                    p6.pos += avance
                if p6.pos == 31:
                    print('En prison')
                    p6.attendre = 1
                if p6.pos == 52:
                    print('En prison aussi')
                    p6.attendre = 1
                if p6.pos == 42:
                    print('Et bah non')
                    p6.pos = 30
                if p6.pos == 58:
                    print('Retour a la case départ')
                    p6.pos = 1
                if p6.pos == 6:
                    print('Pont a 12')
                    p6.pos = 12
                if p6.pos == 19:
                    print('Bienvenue a l\'hotel ibis')
                    p6.timer = 2
                if p6.pos == 63:
                    continuer = 1
                    print('P6 Win')
                if p6.pos > 63:
                    recule = p6.pos - 63
                    p6.pos = 63 - recule
                    if p6.pos % 9 == 0:
                        p6.pos-=recule
                if p6.pos == p2.pos:
                    p2.pos -= avance
                if p6.pos == p3.pos:
                    p3.pos -= avance
                if p6.pos == p4.pos:
                    p4.pos -= avance
                if p6.pos == p5.pos:
                    p5.pos -= avance
                if p6.pos == p1.pos:
                    p1.pos -= avance
                print(str(p6.pos) + ' P6')
            else:
                print('Vous avez oubliez de payez, la Stonks Industries vous charge de dormir et de payer une nuit supplementaire')
                p6.timer -=1
        if p6.attendre == 1 and (p2.pos >= p6.pos or p3.pos >= p6.pos or p4.pos >= p6.pos or p5.pos >= p6.pos or p1.pos >= p6.pos):
            p6.attendre = 0
        elif p6.attendre == 1:
            print('Prisonnier reste la')
            p6.attendre = 1
        tour = 0
        prem_tour = 1
    tour_jeux +=1
    print('tour ' + str(tour_jeux))