import pygame
import sys
pygame.init()
screen =pygame.display.set_mode(((600 , 400)))
pygame.display.set_caption("This is my game welcome")

while True:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((234,234,234))
    pygame.display.update()
            
