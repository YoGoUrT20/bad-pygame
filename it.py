import pygame
import sys



pygame.init()
pygame.display.set_caption("GAMINGGG")


fps = 30
p1 = 10
p2 = 10
speed = 10
event1 = False 
event2 = False
event3 = False
key_item = False
water_item = False
x = False
x2 = True
font = pygame.font.Font(None, 36)
fpsclock = pygame.time.Clock()
screen = pygame.display.set_mode((1024, 1024))
p1, p2 = 100, 100


while True:
    screen.fill((255, 255, 255))
    playerimg = pygame.image.load("player.png")
    if x2 == True:
        door = screen.blit(pygame.image.load("door.png"), (845, 590))
    else:
        door = screen.blit(pygame.image.load("door.png"), (1500, 1500))
    
    python = screen.blit(pygame.image.load("python.png"), (50, 590))
    if x == True:
        water = screen.blit(pygame.image.load("water.png"), (900, 200))
    else:
        water = screen.blit(pygame.image.load("water.png"), (1500, 1500))



    for eve in pygame.event.get():
        if eve.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    key_input = pygame.key.get_pressed()
    if key_input[pygame.K_LEFT]:
        p1 -= speed
    if key_input[pygame.K_UP]:
        p2 -= speed
    if key_input[pygame.K_RIGHT]:
        p1 += speed
    if key_input[pygame.K_DOWN]:
        p2 += speed


    player = screen.blit(playerimg, (p1, p2))
    player_pos = player.topleft

    if player.colliderect(door):
        if key_item == True:
            event3 = True
        else:
            text = font.render("You need a key!", True, (0, 0, 0))
            text_rect = text.get_rect()
            text_rect.center = (900, 600)
            screen.blit(text, text_rect)

    if player.colliderect(python):
        if water_item == True:
            key_item = True
            event2 = True
        else:
            text = font.render("I am so thirsty, gimme water", True, (0, 0, 0))
            text_rect = text.get_rect()
            text_rect.center = (200, 550)
            screen.blit(text, text_rect)
            event1 = True

    if event1 == True:
        text = font.render("How to get whatar?!?", True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (player_pos[0]+20, player_pos[1]-30)
        screen.blit(text, text_rect)
        x = True

    if event2 == True:
        text = font.render("Damn, i have a key rn", True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (player_pos[0]+20, player_pos[1]-30)
        screen.blit(text, text_rect)
        

    if event3 == True:
        event2 = False
        text = font.render("I escaped!", True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (player_pos[0]+20, player_pos[1]-30)
        screen.blit(text, text_rect)
        x2 = False


    if player.colliderect(water):
        x = False
        water_item = True
        event1 = False


    


    pygame.display.update()
    fpsclock.tick(fps)
