import pygame,sys
from pygame.locals import*
pygame.init()                         #intialisation 
clock=pygame.time.Clock() 
clock.tick(0)

screen=pygame.display.set_mode((610,460))
pygame.display.set_caption('football fantasy')  

global bg1
global bgleft
global bg
bg1 = pygame.image.load('player selection.png')
bg1 = pygame.transform.scale(bg1,(610,460))#610 460
bgleft = pygame.image.load('leftplayer.png')
bgleft = pygame.transform.scale(bgleft,(610,460))#610 460
bgright = pygame.image.load('rightplayer.png')
bgright = pygame.transform.scale(bgright,(610,460))#610 460
select = pygame.image.load('selectplayer.png')
select = pygame.transform.scale(select,(610,460))#610 460
#boy2
b1 = pygame.image.load('boy1.jpg')
b2 = pygame.image.load('boy2.jpg')
b3 = pygame.image.load('boy3.jpg')
b4 = pygame.image.load('boy4.jpg')
b5 = pygame.image.load('boy5.jpg')
b6 = pygame.image.load('boy6.jpg')
b7 = pygame.image.load('boy7.jpg')
b8 = pygame.image.load('boy8.jpg')
b9 = pygame.image.load('boy9.jpg')
b10 = pygame.image.load('boy10.jpg')
b11 = pygame.image.load('boy11.jpg')
b12 = pygame.image.load('boy12.jpg')
b13 = pygame.image.load('boy13.jpg')
b14 = pygame.image.load('boy14.jpg')
b15 = pygame.image.load('boy15.jpg')
b16 = pygame.image.load('boy16.jpg')
b17 = pygame.image.load('boy17.jpg')
b18 = pygame.image.load('boy18.jpg')
#boy1
a1 = pygame.image.load('1.png')
a1 = pygame.transform.scale(a1,(200,200))
a2 = pygame.image.load('2.png')
a2 = pygame.transform.scale(a2,(200,200))
a3 = pygame.image.load('3.png')
a3 = pygame.transform.scale(a3,(200,200))
a4 = pygame.image.load('4.png')
a4 = pygame.transform.scale(a4,(200,200))
a5 = pygame.image.load('5.png')
a5 = pygame.transform.scale(a5,(200,200))
a6 = pygame.image.load('6.png')
a6 = pygame.transform.scale(a6,(200,200))
a7 = pygame.image.load('7.png')
a7 = pygame.transform.scale(a7,(200,200))
a8 = pygame.image.load('8.png')
a8 = pygame.transform.scale(a8,(200,200))
a9 = pygame.image.load('9.png')
a9 = pygame.transform.scale(a9,(200,200))
#boy3
c1 = pygame.image.load('boy3-1.png')
c1 = pygame.transform.scale(c1,(150,200))
c2 = pygame.image.load('boy3-2.png')
c2 = pygame.transform.scale(c2,(150,200))
c3 = pygame.image.load('boy3-3.png')
c3 = pygame.transform.scale(c3,(150,200))
c4 = pygame.image.load('boy3-4.png')
c4 = pygame.transform.scale(c4,(150,200))
c5 = pygame.image.load('boy3-5.png')
c5 = pygame.transform.scale(c5,(150,200))
c6 = pygame.image.load('boy3-6.png')
c6 = pygame.transform.scale(c6,(150,200))
c7 = pygame.image.load('boy3-7.png')
c7 = pygame.transform.scale(c7,(150,200))
c8 = pygame.image.load('boy3-8.png')
c8 = pygame.transform.scale(c8,(150,200))
c9 = pygame.image.load('boy3-9.png')
c9 = pygame.transform.scale(c9,(150,200))
c10 = pygame.image.load('boy3-10.png')
c10 = pygame.transform.scale(c10,(150,200))
c11 = pygame.image.load('boy3-11.png')
c11 = pygame.transform.scale(c11,(150,200))
c12 = pygame.image.load('boy3-12.png')
c12 = pygame.transform.scale(c12,(150,200))
c13 = pygame.image.load('boy3-13.png')
c13 = pygame.transform.scale(c13,(150,200))
c14 = pygame.image.load('boy3-14.png')
c14 = pygame.transform.scale(c14,(150,200))
c15 = pygame.image.load('boy3-15.png')
c15 = pygame.transform.scale(c15,(150,200))
c16 = pygame.image.load('boy3-16.png')
c16 = pygame.transform.scale(c16,(150,200))
c17 = pygame.image.load('boy3-17.png')
c17 = pygame.transform.scale(c17,(150,200))
c18 = pygame.image.load('boy3-18.png')
c18 = pygame.transform.scale(c18,(150,200))
b=[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18]
a=[a1,a2,a3,a4,a5,a6,a7,a8,a9]
c=[c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15,c16,c17,c18]
def exitgame():                                     #exit sequence function
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
def getmouse():
    centerx,centery=pygame.mouse.get_pos()
            
class boy1:
    
class boy2:
    
class boy3: 
    
    
    
while True:
    exitgame()
    player=1 
    index=0
    centerx,centery=pygame.mouse.get_pos()
    for event in  pygame.event.get():
        if uni==1:
        
        if uni==2:
        if uni==3:
        if uni==4:
    
        if centerx>=144 and centerx<=181 and centery>=350 and centery<=370:
            bg=bgleft
            pygame.display.update() 
            if uni>1:
                uni-=1
        else:
            bg=bg1
    '''while indexa<9 and uni==1:
        screen.blit(bg,(0,0))
        screen.blit(a[indexa],(200,140))
        pygame.time.delay(90)
        indexa+=1      
        pygame.display.update()
    while indexa<18 and uni==2:
        screen.blit(bg,(0,0))
        screen.blit(b[indexb],(223,140))
        pygame.time.delay(150)
        indexb+=1      
        pygame.display.update()'''        
    '''while indexb<18 and uni==2:
        screen.blit(bg,(0,0))
        screen.blit(b[indexb],(223,140))
        pygame.time.delay(150)
        indexb+=1
        pygame.display.update()'''
    '''while indexc<18 and uni==3:
        screen.blit(bg,(0,0))
        screen.blit(c[indexc],(220,140))
        pygame.time.delay(150)
        indexc+=1
        pygame.display.update()'''        
