import pygame
import sys
import random 
pygame.init()
screen =pygame.display.set_mode(((600 , 400)))
pygame.display.set_caption("This is my game welcome")
BLUE =( 255,0,0)

player_size =50
player_x =400 //2import pygame
player_y =600 //2
player_speed =5

clock =pygame.time.Clock()

bg_color =(255,255,255)
def random_color():
    return(
        random.randint(0,255),
        random.randint(0,255),
        random.randint(0,255)
        
    )


while True:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed

    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    touched_edge = False

    if player_x <= 0:
        player_x = 10
        touched_edge = True

    if player_x + player_size >= 600:
        player_x = 600 - player_size - 10
        touched_edge = True

    if touched_edge:
        bg_color = random_color()

    screen.fill(bg_color) # White background

    pygame.draw.rect(screen,BLUE,(player_x,player_y,player_size,player_size))

    pygame.display.update()

    clock.tick(60)