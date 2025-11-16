import pygame
import sys
pygame.init()
screen =pygame.display.set_mode(((600 , 400)))
pygame.display.set_caption("This is my game welcome")
Red =( 255,0,0)

player_size =50
player_x =400 //2
player_y =600 //2
player_speed =5

clock =pygame.time.Clock()



while True:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    screen.fill((234,234,234))
    pygame.draw.rect(screen,Red,(player_x,player_y,player_size,player_size))
    pygame.display.update()
            
    clock.tick(60)