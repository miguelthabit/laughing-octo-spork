import pygame
import sys
import random 
pygame.init()
WIDTH , HEIGHT =600,400
screen =pygame.display.set_mode(((600 , 400)))
pygame.display.set_caption("This is my game welcome")
BG =( 255,0,0)
SHIP =(30,144,255)
TRIM =(255,255,255)


player_x =WIDTH//2
player_y =HEIGHT =80
player_w =60
Player_h =15

clock =pygame.time.Clock()
def draw_ship(surface,x,y,w,h):
    points =[(x,y),(x+w,y),(x+w//2,y - h)]
    pygame.draw.polygon(surface,SHIP,points)

    Cockpit_center =(x+w//2,y-h//3)
    pygame.draw.circle(surface,TRIM,Cockpit_center,6)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill(BG)
    draw_ship(screen,player_x - player_w//2,player_y,player_w,Player_h)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()


    
