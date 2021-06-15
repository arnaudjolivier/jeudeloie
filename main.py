import random
import sys
import pygame
import os
from jeu import *
from pos import *

os.system('cls')
pygame.init()
clock = pygame.time.Clock()
# definition des couleurs
white = (255, 255, 255) 
green = (0, 255, 0) 
blue = (0, 0, 128)
black = (0,0,0)
color = (255,255,255) 
color_light = (170,170,170)  
color_dark = (100,100,100) 
# mise en place de la taille de l'écran
fenetre=pygame.display.set_mode((1300,900))
# load toutes les images et les textes
background = pygame.image.load("Map_oie.png")
j1 = pygame.image.load("J1.png").convert_alpha()
j1 = pygame.transform.scale(j1,(100 , 100))
j2 = pygame.image.load("J2.png").convert_alpha()
j2 = pygame.transform.scale(j2,(100 , 100))
font = pygame.font.Font('freesansbold.ttf', 32) 
width = fenetre.get_width()  
height = fenetre.get_height() 
smallfont = pygame.font.SysFont('Corbel',35)  
Lancedes = smallfont.render('Lancer les dés' , True , color)
reset = smallfont.render('New Game' , True , color)
Quitte = smallfont.render('Quitter' , True , color)
Win = font.render('Win' , True , color)
'''p2.pos_x = 400
p2.pos_y = 600'''
# declare les variables
tours = 0
avance = 0
tour_jeux = 1
spe_act = False
End = False
continuer=True
des_enprem = False

while continuer == True:
    clock.tick(60)
    fenetre.blit(background,(400,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 20 <= mouse[0] <= 20+200 and 650 <= mouse[1] <= 650+40:
                End = False         # reinnitialisation pour recommencer la game
                tours = 0
                tour_jeux = 1
                p1.pos = 0
                p2.pos = 0
                pygame.draw.rect(fenetre,black,[250,250,150,50])    # cache nombre tours
                pygame.draw.rect(fenetre,black,[100,100,150,50])    # cache nombre win
            if End == False:    # disable button
                if 20 <= mouse[0] <= 20+200 and 750 <= mouse[1] <= 750+40:
                        des1 = random.randrange(1,7)
                        des2 = random.randrange(1,7)
                        if tours == 0:      # tours joueur 1
                            text5 = font.render('Joueur 1', True,white)
                            if p1.timer1 == 0:        #hôtel
                                if p1.attendre == 0:    # prison
                                    p1.mouve = des1 + des2  # mouvement aves les dés
                                    if tour_jeux == 1:      # compteur de tours
                                        des_premtour1(des1,des2)    
                                        if p1.pos > 12:
                                            case1(p1.pos) 
                                        else:
                                            p1.pos = p1.mouve
                                            pos_speciale1()        # check si case special
                                            if p1.pos != 1:
                                                case1(p1.pos)
                                    else:
                                        p1.pos += p1.mouve
                                        case1(p1.pos)
                                        pos_speciale1()          # check si case special ensuite 
                                        case1(p1.pos)             # affiche la case
                                        if p1.pos >= 63:            #regarde si le joueur 1 arrive a la fin
                                            p1.pos = 63
                                            End = True
                                            print('P1 Win')
                                elif p2.pos >= p1.pos :         #regarde si le joueur 2 est sur la case ou a dépasser le joueur 1
                                    p1.attendre = 0
                                else:
                                    p1.attendre = 1
                            else:
                                p1.timer1 -= 1           #timer hôtel
                            if p1.pos == p2.pos:         #recule le joueur 2 si sur la meme case
                                p2.pos -= p1.mouve
                                case2(p2.pos)
                            tours = 1                    #set tour à 1
                            text7 = font.render('Case : '+ str(p1.pos), True,white)
                            pygame.draw.rect(fenetre,black,[250,350,150,40])    # cache joueur 1
                            fenetre.blit(text5, (250,350))
                            pygame.draw.rect(fenetre,black,[250,450,150,40])    
                            fenetre.blit(text7, (250,450))
                        elif tours == 1:
                            text6 = font.render('Joueur 2', True,white)
                            if p2.timer1 == 0:
                                if p2.attendre == 0:
                                    p2.mouve = des1 + des2
                                    if tour_jeux == 1:
                                        des_premtour2(des1,des2)    
                                        if p2.pos > 12:
                                            case2(p2.pos) 
                                        else:
                                            p2.pos = p2.mouve
                                            pos_speciale2()
                                            if p2.pos != 1:
                                                case2(p2.pos)
                                    else:
                                        p2.pos += p2.mouve
                                        case2(p2.pos)
                                        pos_speciale2()
                                        case2(p2.pos)
                                        
                                        if p2.pos >= 63:
                                            p2.pos = 63
                                            End = True
                                            print('P2 Win')
                                elif p1.pos >= p2.pos :
                                    p2.attendre = 0
                                else:
                                    p2.attendre = 1
                            else:
                                p2.timer1 -= 1
                            if p1.pos == p2.pos:
                                p1.pos -= p2.mouve
                                case1(p1.pos)
                            tours = 0
                            tour_jeux += 1
                            text8 = font.render('Case : '+ str(p2.pos), True,white)
                            pygame.draw.rect(fenetre,black,[250,350,150,40])
                            fenetre.blit(text6, (250,350))
                            pygame.draw.rect(fenetre,black,[250,450,150,40])
                            fenetre.blit(text8, (250,450))
                        print(des1,des2) 
                        print(tour_jeux)
            #boutton quitter
            if 240 <= mouse[0] <= 240+140 and 750 <= mouse[1] <= 750+40:
                pygame.quit()       # button quit
                
    text = font.render('Tour : ' + str(tour_jeux), True, green, blue)   
    mouse = pygame.mouse.get_pos()
    #affichage bouttons
    if 20 <= mouse[0] <= 20+200 and 750 <= mouse[1] <= 750+40: 
        pygame.draw.rect(fenetre,color_light,[20,750,200,40])
    else: 
        pygame.draw.rect(fenetre,color_dark,[20,750,200,40])
    if 240 <= mouse[0] <= 240+100 and 750 <= mouse[1] <= 750+40: 
        pygame.draw.rect(fenetre,color_light,[240,750,100,40]) 
    else:
        pygame.draw.rect(fenetre,color_dark,[240,750,100,40])
    if 20 <= mouse[0] <= 20+200 and 650 <= mouse[1] <= 650+40: 
        pygame.draw.rect(fenetre,color_light,[20,650,200,40]) 
    else:
        pygame.draw.rect(fenetre,color_dark,[20,650,200,40])
    if End == True:
        fenetre.blit(Win,(100,100))
    fenetre.blit(text, (250,250))
    fenetre.blit(reset, (20,650))               # affiche tout les textes et les buttons
    fenetre.blit(Lancedes , (20,750))
    fenetre.blit(Quitte,(240,750))
    fenetre.blit(j1,(p1.pos_x,p1.pos_y))
    fenetre.blit(j2,(p2.pos_x,p2.pos_y))
    pygame.display.update()                     # update la fenetre