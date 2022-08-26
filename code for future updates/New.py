import sys
import pygame

pygame.init()
x='Activision Logo HD.mpg'
video=pygame.movie.Movie(x)
w,h=1000,650
screen=pygame.display.set_mode((w,h))
video.set_display(screen,(0,0,w,h))
video.play()
pygame.time.wait(8000)
import game_extension


