import pygame,sys
from pygame.locals import*
pygame.init()                         #intialisation 
clock=pygame.time.Clock() 
clock.tick(0)

global globalbg

screen=pygame.display.set_mode((960,720),FULLSCREEN)              #screen size
pygame.display.set_caption('images/football fantasy')          #game name
bg = pygame.image.load('images/top cover.png')
highscore = pygame.image.load('images/highscore.png')
back = pygame.image.load('images/back.png')
instructions = pygame.image.load('images/how to play.png')
exitbutton = pygame.image.load('images/begex.png')
highscores = pygame.image.load('images/begsco.png')
control = pygame.image.load('images/begcon.png')
play = pygame.image.load('images/begplay.png')
lvlchoose = pygame.image.load('Images/choose_level.png')
lvlchoose1 = pygame.image.load('Images/choose_level1.png')
lvlchoose2 = pygame.image.load('Images/choose_level2.png')
lvlchoose3 = pygame.image.load('Images/choose_level3.png')
lvlchoose4 = pygame.image.load('Images/choose_level4.png')
lvlchoose5 = pygame.image.load('Images/choose_level5.png')
returntomenu = pygame.image.load('Images/returntomenu.png')
mousex,mousey = pygame.mouse.get_pos()
pygame.mouse.set_visible(True)


def exitgame():                                     #exit sequence function
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

def draw():
    screen.blit(bg,(0,0))
    mousex,mousey = pygame.mouse.get_pos()
    pygame.display.update()

while True:
    exitgame()
    mousex,mousey = pygame.mouse.get_pos()
    if mousex >= 245 and mousex <= 625:
        if mousey >= 280 and mousey <= 365:
            screen.blit(play,(0,0))
            mousex,mousey = pygame.mouse.get_pos()
            pygame.display.update()
            for event in pygame.event.get(): 
                if event.type==MOUSEBUTTONUP:
                    game = True
                    while game == True:
                        exitgame()
                        mousex,mousey = pygame.mouse.get_pos()
                        if mousex >= 0 and mousex <= 350:
                            if mousey >= 640 and mousey <= 690:
                                screen.blit(returntomenu,(0,0))
                                mousex,mousey = pygame.mouse.get_pos()
                                pygame.display.update()
                                for event in pygame.event.get(): 
                                    if event.type==MOUSEBUTTONUP:
                                        game = False
                        else:                
                            if mousex >= 375 and mousex <= 490:
                                if mousey >= 350 and mousey <= 420:
                                    screen.blit(lvlchoose1,(0,0))
                                    mousex,mousey = pygame.mouse.get_pos()
                                    pygame.display.update()
                                    for event in pygame.event.get(): 
                                        if event.type==MOUSEBUTTONUP:
                                            import game_extension
                            if mousex >= 375 and mousex <= 490:
                                if mousey >= 421 and mousey <= 468:
                                    screen.blit(lvlchoose2,(0,0))
                                    mousex,mousey = pygame.mouse.get_pos()
                                    pygame.display.update()
                            if mousex >= 375 and mousex <= 490:
                                if mousey >= 469 and mousey <= 520:
                                    screen.blit(lvlchoose3,(0,0))
                                    mousex,mousey = pygame.mouse.get_pos()
                                    pygame.display.update()
                            if mousex >= 375 and mousex <= 490:
                                if mousey >= 521 and mousey <= 580:
                                    screen.blit(lvlchoose4,(0,0))
                                    mousex,mousey = pygame.mouse.get_pos()
                                    pygame.display.update()
                            if mousex >= 375 and mousex <= 490:
                                if mousey >= 581 and mousey <= 650:
                                    screen.blit(lvlchoose5,(0,0))
                                    mousex,mousey = pygame.mouse.get_pos()
                                    pygame.display.update()        
                            else:
                                screen.blit(lvlchoose,(0,0))
                                pygame.display.update()
    if mousex >= 245 and mousex <= 625:
        if mousey >= 366 and mousey <= 450:
            screen.blit(control,(0,0))
            mousex,mousey = pygame.mouse.get_pos()
            pygame.display.update()
            for event in pygame.event.get(): 
                if event.type==MOUSEBUTTONUP:
                    run = True
                    while run==True:
                        for event in pygame.event.get(): 
                            exitgame()
                            screen.blit(instructions,(0,0))
                            mousex,mousey = pygame.mouse.get_pos()
                            pygame.display.update() 
                            if mousex >= 688 and mousex <= 959:
                                if mousey >= 630 and mousey <= 713:
                                      screen.blit(back,(0,0))
                                      pygame.display.update()
                                      if event.type==MOUSEBUTTONUP:
                                        run = False                     
    if mousex >= 245 and mousex <= 625:
        if mousey >= 451 and mousey <= 515:
            screen.blit(highscores,(0,0))
            mousex,mousey = pygame.mouse.get_pos()     
            pygame.display.update()
            for event in pygame.event.get(): 
                if event.type==MOUSEBUTTONUP:
                    run = True
                    while run==True:
                        for event in pygame.event.get(): 
                            exitgame()
                            screen.blit(highscore,(0,0))
                            mousex,mousey = pygame.mouse.get_pos()
                            pygame.display.update() 
                            if mousex >= 688 and mousex <= 959:
                                if mousey >= 630 and mousey <= 713:
                                      screen.blit(highscore,(0,0))
                                      pygame.display.update()
                                      if event.type==MOUSEBUTTONUP:
                                        run = False
    if mousex >= 245 and mousex <= 625:
        if mousey >= 516 and mousey <= 610:
            screen.blit(exitbutton,(0,0))
            mousex,mousey = pygame.mouse.get_pos()
            pygame.display.update()
            for event in pygame.event.get(): 
                if event.type==MOUSEBUTTONUP:
                    pygame.quit()
    else:
       draw()
