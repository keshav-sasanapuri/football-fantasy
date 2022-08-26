import pygame,sys,random              #importing modules
from pygame.locals import*
pygame.init()#intialisation
pygame.mixer.quit()
pygame.mouse.set_visible(False)       #cursor visibiltity
clock=pygame.time.Clock() 
clock.tick(0)                         #FPS
global bomb, bom, burst #VARIABLES                            #global variables
global level, level_2, score, balls, dispsco, dispbal, life
global ready, ok, go
global boy, ball, cursor
global boy1_1, boy1_2, boy1_3
global ballposx, ballposy, centerx, centery
global rectcursor, cursortop, cursorbottom, cursorleft, cursorright   
global rectball, balltop, ballbottom, ballleft, ballright
life=5
score=0
balls=10
x = 30
y = 30
lvl = 1      #set level
kick = 1
ballposx = 450
ballposy = 350
boyposx =  410
boyposy = 260  #midx = 500  #midy = 325
screen=pygame.display.set_mode((1000,650))#SCREEN              #screen size
pygame.display.set_caption('football fantasy')          #game name
bg = pygame.image.load('Images/stadium.jpg')#INSERTING IMAGES                   #main background
glove1 = pygame.image.load('Images/glove1.png')                #gloves closed and open
glove2 = pygame.image.load('Images/glove2.png')
glove3 = pygame.image.load('Images/glove3.png')
glove4 = pygame.image.load('Images/glove4.png')
glove5 = pygame.image.load('Images/glove5.png')
glove1cl = pygame.image.load('Images/glove1cl.png')
glove2cl = pygame.image.load('Images/glove2cl.png')
glove3cl = pygame.image.load('Images/glove3cl.png')
glove4cl = pygame.image.load('Images/glove4cl.png')
glove5cl = pygame.image.load('Images/glove5cl.png')
boy1_1 = pygame.image.load('Images/boy1_1.png')               #players all motion
boy1_2 = pygame.image.load('Images/boy1_2.png')
boy1_3 = pygame.image.load('Images/boy1_3.png')
ball2 = pygame.image.load('Images/ball2.png')         #both balls
fireball = pygame.image.load('Images/fireball.png')
block1 = pygame.image.load('Images/block.png')         #blocked display
block2 = pygame.image.load('Images/block2.png')
block3 = pygame.image.load('Images/block3.png')
block4 = pygame.image.load('Images/block4.png')
block5 = pygame.image.load('Images/block5.png')
busted = pygame.image.load('Images/busted.png')       #busted display
heart1 = pygame.image.load('Images/1heart.png')         #heart for life
heart2 = pygame.image.load('Images/2heart.png')
heart3 = pygame.image.load('Images/3heart.png')
heart4 = pygame.image.load('Images/4heart.png')
heart5 = pygame.image.load('Images/5heart.png')
xtralife = pygame.image.load('Images/extralife.png')
gameover = pygame.image.load('Images/gameover.png')
bomb = pygame.image.load('Images/bomb.png')
boom1=pygame.image.load('Images/boom1.png')
boom2=pygame.image.load('Images/boom2.png')
boom3=pygame.image.load('Images/boom3.png')
boom4=pygame.image.load('Images/boom4.png')
boom5=pygame.image.load('Images/boom5.png')
boom6=pygame.image.load('Images/boom6.png')
boom7=pygame.image.load('Images/boom7.png')
boom8=pygame.image.load('Images/boom8.png')
boom9=pygame.image.load('Images/boom9.png')
boom10=pygame.image.load('Images/boom10.png')
boom11=pygame.image.load('Images/boom11.png')
boom12=pygame.image.load('Images/boom12.png')
boom13=pygame.image.load('Images/boom13.png')
boom14=pygame.image.load('Images/boom14.png')
boom15=pygame.image.load('Images/boom15.png')
boom16=pygame.image.load('Images/boom16.png')
boom17=pygame.image.load('Images/boom17.png')
boom18=pygame.image.load('Images/boom18.png')
boom19=pygame.image.load('Images/boom19.png')
boom20=pygame.image.load('Images/boom20.png')
boom21=pygame.image.load('Images/boom21.png')
boom22=pygame.image.load('Images/boom22.png')
boom23=pygame.image.load('Images/boom23.png')
surc1=pygame.image.load('Images/surc1.png')
surc2=pygame.image.load('Images/surc2_1.png')
surc3=pygame.image.load('Images/surc3.png')
surc4=pygame.image.load('Images/surc5.png')
ready = pygame.image.load('Images/ready.png')#get set go
ok = pygame.image.load('Images/set.png')
go = pygame.image.load('Images/go.png')
level1 = pygame.image.load('Images/level 1.png')   #level up
level1_2 = pygame.image.load('Images/level 1_2.png')
level2 = pygame.image.load('Images/level 2.png')
level2_2 = pygame.image.load('Images/level 2_2.png')
level3 = pygame.image.load('Images/level 3.png')
level3_2 = pygame.image.load('Images/level 3_2.png')
level4 = pygame.image.load('Images/level 4.png')
level4_2 = pygame.image.load('Images/level 4_2.png')
level5 = pygame.image.load('Images/level 5.png')
level5_2 = pygame.image.load('Images/level 5_2.png')
missed = pygame.image.load('Images/missed.png')
lvlchoose = pygame.image.load('Images/choose_level.png')
lvlchoose1 = pygame.image.load('Images/choose_level1.png')
lvlchoose2 = pygame.image.load('Images/choose_level2.png')
lvlchoose3 = pygame.image.load('Images/choose_level3.png')
lvlchoose4 = pygame.image.load('Images/choose_level4.png')
lvlchoose5 = pygame.image.load('Images/choose_level5.png')
incomingfire = pygame.image.load('Images/fireballcoming.png')
text=pygame.font.Font('Fonts/digital.ttf',50)
boom1 = pygame.transform.scale(boom1,(300,300))
boom2 = pygame.transform.scale(boom2,(300,300))
boom3 = pygame.transform.scale(boom3,(300,300))
boom4 = pygame.transform.scale(boom4,(300,300))
boom5 = pygame.transform.scale(boom5,(300,300))
boom6 = pygame.transform.scale(boom6,(300,300))
boom7 = pygame.transform.scale(boom7,(300,300))
boom8 = pygame.transform.scale(boom8,(300,300))
boom9 = pygame.transform.scale(boom9,(300,300))
boom10 = pygame.transform.scale(boom10,(300,300))
boom11 = pygame.transform.scale(boom11,(300,300))
boom12 = pygame.transform.scale(boom12,(300,300))
boom13 = pygame.transform.scale(boom13,(300,300))
boom14 = pygame.transform.scale(boom14,(300,300))
boom15 = pygame.transform.scale(boom15,(300,300))
boom16 = pygame.transform.scale(boom16,(300,300))
boom17 = pygame.transform.scale(boom17,(300,300))
boom18 = pygame.transform.scale(boom18,(300,300))
boom19 = pygame.transform.scale(boom19,(300,300))
boom20 = pygame.transform.scale(boom20,(300,300))
boom21 = pygame.transform.scale(boom21,(300,300))
boom22 = pygame.transform.scale(boom22,(300,300))
boom23 = pygame.transform.scale(boom23,(300,300))
burst=[boom1,boom2,boom3,boom4,boom5,boom6,boom7,boom8,boom9,boom10,boom11,boom12,boom13,boom14,boom15,boom16,boom17,boom18,boom19,boom20,boom21,boom22,boom23]
bg = pygame.transform.scale(bg,(1000,650))#scaling background
gameover = pygame.transform.scale(gameover,(1000,650)) 
glove1 = pygame.transform.scale(glove1,(100,100))                 #scaling gloves  
glove2 = pygame.transform.scale(glove2,(100,100))
glove3 = pygame.transform.scale(glove3,(100,100))
glove4 = pygame.transform.scale(glove4,(100,100))
glove5 = pygame.transform.scale(glove5,(130,130))
glove1cl = pygame.transform.scale(glove1cl,(100,100))
glove2cl = pygame.transform.scale(glove2cl,(100,100))
glove3cl = pygame.transform.scale(glove3cl,(100,100))
glove4cl = pygame.transform.scale(glove4cl,(100,100))
glove5cl = pygame.transform.scale(glove5cl,(130,130))
boy1_1 = pygame.transform.scale(boy1_1,(150,150))                 #scaling players
boy1_2 = pygame.transform.scale(boy1_2,(150,150))
boy1_3 = pygame.transform.scale(boy1_3,(150,150))
level1 = pygame.transform.scale(level1,(1000,650))
level1_2 = pygame.transform.scale(level1_2,(1000,650))
level2 = pygame.transform.scale(level2,(1000,650))
level2_2 = pygame.transform.scale(level2_2,(1000,650))
level3 = pygame.transform.scale(level3,(1000,650))
level3_2 = pygame.transform.scale(level3_2,(1000,650))
level4 = pygame.transform.scale(level4,(1000,650))
level4_2 = pygame.transform.scale(level4_2,(1000,650))
level5 = pygame.transform.scale(level5,(1000,650))
level5_2 = pygame.transform.scale(level5_2,(1000,650))
missed = pygame.transform.scale(missed,(450,200))
#incomingfire = pygame.transform.scale(incomingfire,(450,200))
boy = boy1_1 #assigning images
ball = pygame.transform.scale(ball2,(30,30))
cursor = glove1
bomb = pygame.transform.scale(bomb,(30,30))
class displaylife():
    def displife(self):
        if life==5:
           screen.blit(heart5,(800,1))
           pygame.display.update()
        elif life==4:
            screen.blit(heart4,(800,1))
            pygame.display.update()
        elif life==3:
            screen.blit(heart3,(800,1))
            pygame.display.update()
        elif life==2:
            screen.blit(heart2,(800,1))
            pygame.display.update()
        elif life==1:
            screen.blit(heart1,(800,1))
            pygame.display.update()
        elif life==0:
            screen.blit(gameover,(0,0))
            displayscore()
            pygame.display.update()
            pygame.time.delay(5000)
            pygame.quit()
            pygame.display.update()          
def exitgame():                                     #exit sequence function
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
def draw():        #function                                              #main draw function used frequently     
    global ball,dispsco,dispbal,score,balls,life  
    screen.blit(bg,(0,0))
    screen.blit(boy,(boyposx,boyposy))
    screen.blit(ball,(ballposx,ballposy))
    centerx,centery = pygame.mouse.get_pos()
    screen.blit(cursor,(centerx,centery))
    pygame.display.update()
def displayscore():
    dispsco=str(score)
    disptext=text.render('Score:',True,(0,0,0))    
    dispscore=text.render(dispsco,True,(0,0,0)) 
    screen.blit(disptext,(400,5))
    screen.blit(dispscore,(570,5))
    pygame.display.update()
def dispblock():
    if lvl==5:
        screen.blit(block5,(300,100))
    elif lvl==4:
        screen.blit(block4,(300,100))
    elif lvl==3: 
        screen.blit(block3,(300,100)) 
    elif lvl==2:
        screen.blit(block2,(300,100)) 
    elif lvl==1:
        screen.blit(block1,(300,100))
def aftercoll():                                                 #function used for showing movment of ball after collision  
    ball = pygame.transform.scale(ball2,(x,y))
    screen.blit(bg,(0,0))
    screen.blit(boy,(boyposx,boyposy)) 
    screen.blit(ball,(ballposx,ballposy)) 
    screen.blit(cursor,(centerx,centery))
    if lvl==5:
        screen.blit(block5,(300,100))
    elif lvl==4:
        screen.blit(block4,(300,100))
    elif lvl==3: 
        screen.blit(block3,(300,100)) 
    elif lvl==2:
        screen.blit(block2,(300,100)) 
    elif lvl==1:
        screen.blit(block1,(300,100))
    pygame.display.update()
def sarcasm():
    screen.blit(bg,(0,0))
    screen.blit(boy,(boyposx,boyposy)) 
    screen.blit(ball,(ballposx,ballposy)) 
    screen.blit(cursor,(centerx,centery))
    if lvl==1: 
        screen.blit(surc1,(60,150))
    elif lvl==2: 
        screen.blit(surc2,(80,150))
    elif lvl==3: 
        screen.blit(surc3,(100,100))
    elif lvl==4: 
        screen.blit(surc4,(100,100))    
    pygame.display.update()
    pygame.time.delay(3000)
def bombcoll():
    global ball, b
    ball = pygame.transform.scale(bomb,(x,y))
    screen.blit(bg,(0,0))
    screen.blit(boy,(boyposx,boyposy))
    centerx,centery = pygame.mouse.get_pos()
    screen.blit(cursor,(centerx,centery))
    pygame.display.update() 
    screen.blit(busted,(ballposx,ballposy))
    pygame.display.update()
def ballsize():                                                  #function used for making the ball appear to come towards screen
    global ball
    ball = pygame.transform.scale(ball,(x,y))
    screen.blit(bg,(0,0))
    screen.blit(boy,(boyposx,boyposy)) 
    screen.blit(ball,(ballposx,ballposy)) 
    screen.blit(cursor,(centerx,centery))
def bombsize():
    ball = pygame.transform.scale(bomb,(x,y))
    screen.blit(bg,(0,0))
    screen.blit(boy,(boyposx,boyposy)) 
    screen.blit(ball,(ballposx,ballposy)) 
    screen.blit(cursor,(centerx,centery))
    pygame.display.update()
def getmouse():
    global centerx
    global centery
    centerx,centery = pygame.mouse.get_pos()
def blast():
    global b
    global ball
    burst=[boom1,boom2,boom3,boom4,boom5,boom6,boom7,boom8,boom9,boom10,boom11,boom12,boom13,boom14,boom15,boom16,boom17,boom18,boom19,boom20,boom21,boom22,boom23]
    index=0
    while index<23:
        screen.blit(burst[index],(ballposx,ballposy))
        pygame.display.update()   
        pygame.time.delay(40)
        screen.blit(bg,(0,0))
        screen.blit(boy,(boyposx,boyposy))
        centerx,centery = pygame.mouse.get_pos()
        screen.blit(cursor,(centerx,centery))
        pygame.display.update() 
        index+=1
def collision():                                                 #function recognises collision between gloves and ball and returns boolean value
    global rectcursor, cursortop, cursorbottom, cursorleft, cursorright   
    global rectball, balltop, ballbottom, ballleft, ballright
    if ((cursorleft > ballleft and cursorleft < ballright) and (cursortop > balltop and cursortop < ballbottom)):  
        return True     
    elif ((cursorleft > ballleft and cursorleft < ballright) and (cursorbottom > balltop and cursorbottom < ballbottom)):
        return True    
    elif ((cursorright > ballleft and cursorright < ballright) and (cursorbottom > balltop and cursorbottom < ballbottom)): 
        return True    
    elif ((cursorright > ballleft and cursorright < ballright) and (cursortop > balltop and cursortop < ballbottom)):
        return True    
    elif (cursortop > balltop and cursorbottom < ballbottom) and (cursorleft > ballleft and cursorright < ballright):
        return True    
    elif (cursortop < balltop and cursorbottom > ballbottom) and (cursorleft < ballleft and cursorright > ballright):
        return True 
def levelpt():
    pygame.mouse.set_visible(True)
    run = True
    while run==True:
        for event in pygame.event.get(): 
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            screen.blit(level,(0,0))
            centerx,centery = pygame.mouse.get_pos() 
            pygame.display.update() 
            if centerx >= 720 and centerx <= 1000:
                if centery >= 556 and centery <= 638:
                    screen.blit(level_2,(0,0))
                    if event.type==MOUSEBUTTONUP:
                        run = False    
        pygame.display.update()     
def start():
    screen.blit(bg,(0,0))
    pygame.display.update()
    pygame.time.delay(500)
    screen.blit(bg,(0,0))
    screen.blit(ready,(300,300))
    pygame.display.update()
    pygame.time.delay(1000)
    screen.blit(bg,(0,0))
    screen.blit(ok,(400,300))
    pygame.display.update()
    pygame.time.delay(1000)
    screen.blit(bg,(0,0))
    screen.blit(go,(400,300))
    pygame.display.update()
    pygame.time.delay(1000)
def boykick():
    global boy
    b=[boy1_1,boy1_2,boy1_3] 
    index=0
    count=1
    boy=b[index]
    while index<3:
        draw()
        boy=b[index]
        if count==2:
            pygame.time.delay(150)
        draw()    
        index+=1
        count+=1
def makerect():
    global rectcursor, cursortop, cursorbottom, cursorleft, cursorright   
    global rectball, balltop, ballbottom, ballleft, ballright
    rectcursor = cursor.get_rect()          #giving rect attribute to cursor
    rectcursor.topleft = (centerx,centery)  
    rectball = ball2.get_rect()             #giving rect attribute to ball
    rectball.topleft = (ballposx,ballposy)  
    balltop = rectball.top                  #getting ball coordinates
    ballbottom = rectball.bottom
    ballleft = rectball.left
    ballright = rectball.right
    cursortop = rectcursor.top              #getting cursor coordinates  
    cursorbottom = rectcursor.bottom
    cursorleft = rectcursor.left
    cursorright = rectcursor.right
def miss():
    global life
    life-=1
    screen.blit(missed,(300,250))
    pygame.display.update()
    pygame.time.delay(300)
while True:    #main game loop
    clock.tick(0) 
    exitgame()
    live=displaylife()
    while lvl == 1:                                 #LEVEL 1 BEGINS....           
        level = level1
        level_2 = level1_2
        levelpt()
        life=5     
        pygame.mouse.set_visible(False) 
        exitgame()
        start()
        displayscore()
        live.displife() 
        for kick in range (1,11):                   #number of kicks in each level
            cursor = glove1   
            exitgame()  
            x,y = 30,30  
            boykick()
            draw()
            displayscore()
            live.displife()
            a = random.randint(-10,10)              #a and b give randomness to the direction of the kick
            b = random.randint(-10,10)
            for x in range (30,210,8):         
                ball=ball2
                exitgame()  
                y+=8                                # x and y determine the size of the ball
                ballposy -=a        
                ballposx -=b                        # ballposx and ballposy determine position of ball during movement    
                if ballposy<100 or ballposy>550 or ballposx<50 or ballposx>900:         #does not allow ball to go outside screen or goalkey 
                    break     
                getmouse()
                displayscore()
                live.displife()
                pygame.time.delay(10)               #gives speed of ball movement  
                ballsize()
                makerect()
            if collision() == True:                 #if collision...
                score+=10
                cursor = glove1cl                   #glove gets closed
                a = random.randint(-10,10)          # a and b give randomness to the direction of the kick
                b = random.randint(-10,10)
                x = 210
                y = 210
                for x in range (210,30,-8):         
                    exitgame()  
                    dispblock()
                    y-=8                            # x and y determine the size of the ball
                    ballposy -=a        
                    ballposx -=b                    # ballposx and ballposy determine position of ball during movement    
                    if ballposy<100 or ballposy>550 or ballposx<50 or ballposx>900:      #keeps ball within goal key and screen limits    
                        break
                    displayscore()
                    live.displife()
                    getmouse()
                    dispblock()
                    pygame.time.delay(10)           #gives speed of ball movement
                    aftercoll()
            else:
                miss()
            x=30
            y=30
            ball = pygame.transform.scale(ball,(x,y))       
            draw()
            ballposx,ballposy = 450,350
        sarcasm()
        lvl = 2                                 #level upgrade...   
    pygame.display.update()
    while lvl == 2:                                 #LEVEL 2 BEGINS...
        level = level2
        level_2 = level2_2
        levelpt()
        if life<5:     
            life+=1 
        pygame.mouse.set_visible(False) 
        exitgame()
        start()
        displayscore()
        live.displife()
        for kick in range (1,11):                   #number of kicks        
            cursor = glove2
            exitgame()  
            x,y = 30,30
            boykick()
            draw()
            displayscore()
            live.displife()
            a = random.randint(-15,15)              # a and b give randomness to the direction of the kick
            b = random.randint(-15,15)
            for x in range (30,210,5):         
                ball=ball2   
                exitgame()  
                y+=5                                # x and y determine the size of the ball
                ballposy -=a        
                ballposx -=b                        # ballposx and ballposy determine position of ball during movement    
                if ballposy<100 or ballposy>550 or ballposx<50 or ballposx>900:     #keeps ball within limits of screen and goalkey     
                    break                
                if x == 80:
                    a = random.randint(-10,10)      # a and b give randomness to the direction of the kick
                    b = random.randint(-10,10)
                getmouse()
                displayscore()
                live.displife()
                pygame.time.delay(9)                #speed of ball movement
                ballsize()   
                makerect()
                pygame.display.update()
            if collision() == True:                 #if collision...
                score+=15
                cursor = glove2cl                   #glove closes
                a = random.randint(-10,10)          # a and b give randomness to the direction of the kick
                b = random.randint(-10,10)
                x = 210
                y = 210
                for x in range (210,30,-8):         
                    exitgame()  
                    y-=8                            # x and y determine the size of the ball
                    ballposy -=a        
                    ballposx -=b                    # ballposx and ballposy determine position of ball during movement    
                    if ballposy<100 or ballposy>550 or ballposx<50 or ballposx>900:        #keeps ball within goalkey and screen limits  
                        break                
                    getmouse()
                    displayscore()
                    live.displife()
                    pygame.time.delay(10)           #gives speed of ball movement 
                    aftercoll()
            else:
                miss() 
            x=30
            y=30
            ball = pygame.transform.scale(ball,(x,y))
            draw()
            ballposx,ballposy = 450,350
            pygame.display.update()
        sarcasm() 
        lvl = 3        #level upgrade
    while lvl == 3:                                 #LEVEL 3 BEGINS.....
        level = level3
        level_2 = level3_2
        levelpt()
        if life<5: 
            life+=1 
        pygame.mouse.set_visible(False)                                     
        exitgame()
        start()
        displayscore()
        live.displife()
        for kick in range (1,11):                   #number of kicks
            cursor = glove3
            exitgame()  
            x,y = 30,30
            boykick()
            displayscore()
            live.displife()
            draw()
            a = random.randint(-15,15)             # a and b give randomness to the direction of the kick
            b = random.randint(-15,15)
            c=random.randint(1,3)
            for x in range (30,210,5):           
                if c!=2:
                    ball=ball2  
                elif c==2:
                    ball=bomb  
                exitgame()  
                y+=5                               # x and y determine the size of the ball
                ballposy -=a        
                ballposx -=b                       # ballposx and ballposy determine position of ball during movement    
                if ballposy<100 or ballposy>550 or ballposx<50 or ballposx>900:          #keeps ball within goal and screen 
                    break
                if x == 80:                        #makes the ball turn in the air
                    a = random.randint(-10,10)     # a and b give randomness to the direction of the kick
                    b = random.randint(-10,10)
                getmouse()
                displayscore()
                live.displife()
                pygame.time.delay(8)                #gives speed to the ball
                ballsize()
                makerect()
            if collision() == True:                 #if collision...
                cursor = glove3cl                   #glove closes
                a = random.randint(-10,10)          # a and b give randomness to the direction of the kick
                b = random.randint(-10,10)
                x = 210
                y = 210
                if c!=2:
                    score+=20 
                    for x in range (210,30,-8):         
                            exitgame()  
                            y-=8                            # x and y determine the size of the ball
                            ballposy -=a        
                            ballposx -=b                    # ballposx and ballposy determine position of ball during movement    
                            if ballposy<100 or ballposy>550 or ballposx<50 or ballposx>900:      #keeps ball within gaolkey and screen    
                                break
                            getmouse()
                            pygame.time.delay(10)           #gives speed of the ball
                            aftercoll()
                            displayscore()
                            live.displife()
                elif c==2:
                    score-=40
                    life-=1
                    blast()
                    bombcoll()
                    displayscore()
                    live.displife()
                    pygame.time.delay(1000)
            else:
                if c!=2:
                    miss()
            x=30
            y=30
            ball = pygame.transform.scale(ball,(x,y)) 
            draw()
            displayscore()
            live.displife()
            ballposx,ballposy = 450,350
            pygame.display.update()
        sarcasm()   
        lvl = 4    #level upgrade
    while lvl==4:
        level = level4
        level_2 = level4_2
        levelpt()
        if life<5: 
            life+=1 
        pygame.mouse.set_visible(False)                                     
        exitgame()
        start()
        displayscore()
        live.displife()
        for kick in range (1,11):                   #number of kicks
            cursor = glove4
            exitgame()  
            x,y = 30,30
            boykick()
            displayscore()
            live.displife()
            draw()
            a = random.randint(-15,15)             # a and b give randomness to the direction of the kick
            b = random.randint(-15,15)
            c=random.randint(1,5)
            for x in range (30,210,5):           
                if c!=2:
                    ball=ball2
                elif c==2:
                    ball=bomb  
                exitgame()  
                y+=5                               # x and y determine the size of the ball
                ballposy -=a        
                ballposx -=b                       # ballposx and ballposy determine position of ball during movement    
                if ballposy<100 or ballposy>550 or ballposx<50 or ballposx>900:          #keeps ball within goal and screen 
                    break
                if x == 80:                        #makes the ball turn in the air
                    a = random.randint(-10,10)     # a and b give randomness to the direction of the kick
                    b = random.randint(-10,10)
                if x == 100:
                    a = random.randint(-20,20)     # a and b give randomness to the direction of the kick
                    b = random.randint(-20,20) 
                getmouse()
                displayscore()
                live.displife()
                pygame.time.delay(10)                #gives speed to the ball
                ballsize()
                makerect()
            if collision() == True:                 #if collision...
                cursor = glove4cl                   #glove closes
                a = random.randint(-10,10)          # a and b give randomness to the direction of the kick
                b = random.randint(-10,10)
                x = 210
                y = 210
                if c!=2:
                    d=1
                    score+=30
                    for x in range (210,30,-8):         
                            exitgame()  
                            y-=8                            # x and y determine the size of the ball
                            ballposy -=a        
                            ballposx -=b                    # ballposx and ballposy determine position of ball during movement    
                            if ballposy<100 or ballposy>550 or ballposx<50 or ballposx>900:      #keeps ball within gaolkey and screen    
                                break
                            getmouse()
                            pygame.time.delay(10)           #gives speed of the ball
                            aftercoll()
                            displayscore()
                            live.displife()
                elif c==2:
                    score-=40
                    life-=1
                    blast()
                    bombcoll()
                    displayscore()
                    live.displife()
                    pygame.time.delay(1000)  
            else:
                if c!=2:
                    miss()
            x=30
            y=30
            ball = pygame.transform.scale(ball,(x,y)) 
            draw()
            displayscore()
            ballposx,ballposy = 450,350
            pygame.display.update()
        sarcasm() 
        lvl = 5    #level upgrade
    while lvl==5:
        level = level5
        level_2 = level5_2
        levelpt()
        if life<5: 
            life+=1 
        pygame.mouse.set_visible(False)                                     
        exitgame()
        start()
        displayscore()
        live.displife()
        for kick in range (1,11):                   #number of kicks
            cursor = glove5
            exitgame()  
            x,y = 30,30
            boykick()
            displayscore()
            live.displife()
            draw()
            a = random.randint(-20,20)             # a and b give randomness to the direction of the kick
            b = random.randint(-20,20)
            c=random.randint(1,5)
            d=random.randint(1,5) 
            if d==2:
                screen.blit(incomingfire,(300,50))
                pygame.display.update()
                pygame.time.delay(1000)
                draw()
            for x in range (30,210,5):           
                if c!=2:
                    ball=ball2 
                if d==2:
                    ball=fireball
                elif c==2:
                    ball=bomb
                exitgame()  
                y+=5                               # x and y determine the size of the ball
                ballposy -=a        
                ballposx -=b                       # ballposx and ballposy determine position of ball during movement    
                if ballposy<100 or ballposy>550 or ballposx<50 or ballposx>900:          #keeps ball within goal and screen 
                    break
                if x == 80:                        #makes the ball turn in the air
                    a = random.randint(-10,10)     # a and b give randomness to the direction of the kick
                    b = random.randint(-10,10)
                if x == 100:
                    a = random.randint(-20,20)     # a and b give randomness to the direction of the kick
                    b = random.randint(-20,20) 
                getmouse()
                displayscore()
                live.displife()
                pygame.time.delay(15)                #gives speed to the ball
                ballsize()
                makerect()
            if collision() == True:                 #if collision... 
                cursor = glove5cl                   #glove closes
                a = random.randint(-10,10)          # a and b give randomness to the direction of the kick
                b = random.randint(-10,10)
                x = 210
                y = 210
                if d==2:
                    if life<5: 
                        life+=1
                    score+=50
                    screen.blit(xtralife,(100,200))
                    pygame.display.update() 
                    pygame.time.delay(2000)
                elif c!=2:
                    score+=30 
                    for x in range (210,30,-8):         
                            exitgame()  
                            y-=8                            # x and y determine the size of the ball
                            ballposy -=a        
                            ballposx -=b                    # ballposx and ballposy determine position of ball during movement    
                            if ballposy<100 or ballposy>550 or ballposx<50 or ballposx>900:      #keeps ball within gaolkey and screen    
                                break
                            getmouse()
                            pygame.time.delay(10)           #gives speed of the ball
                            aftercoll()
                            displayscore()
                            live.displife() 
                elif c==2:
                    score-=40
                    life-=1
                    blast()
                    bombcoll()
                    displayscore()
                    live.displife()
                    pygame.time.delay(1000)  
            else:
                if c!=2:
                    miss()
            x=30
            y=30
            ball = pygame.transform.scale(ball,(x,y)) 
            draw()
            displayscore()
            ballposx,ballposy = 450,350
            pygame.display.update()
        lvl = 5    #level upgrade         
pygame.quit()
       

        
   
