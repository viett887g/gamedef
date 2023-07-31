import pygame
import constant as c
from enemys import Enemy
from turet import Turret
pygame.init()
screen = pygame.display.set_mode((c.SCREEN_WIDTH,c.SCREEN_HEIGHT))
enemy_image = pygame.image.load('E:/tower_defence_tut-main/Part 1/assets/images/enemies/enemy_1.png').convert_alpha()
turret_sheet = pygame.image.load('E:/tower_defence_tut-main/Part 1/assets/images/turrets/turret_1.png').convert_alpha()
cursor_turret = pygame.image.load('E:/tower_defence_tut-main/Part 1/assets/images/turrets/cursor_turret.png').convert_alpha()
cursor_turret_brown= pygame.image.load('C:/Users/vcd09/Downloads/ground_shaker_asset/Purple/Weapons/turret_01_mk1.gif').convert_alpha()

map_image = pygame.image.load('E:/tower_defence_tut-main/Part 1/levels/level.png').convert_alpha()
map_image_1 = pygame.transform.scale(pygame.image.load('C:/Users/vcd09/Pictures/pic (2).png'),(c.SCREEN_WIDTH,c.SCREEN_HEIGHT)).convert_alpha()

cancel_image=pygame.image.load('E:/tower_defence_tut-main/Part 6/assets/images/buttons/cancel.png').convert_alpha()
buy_turret_image=pygame.image.load('E:/tower_defence_tut-main/Part 6/assets/images/buttons/buy_turret.png').convert_alpha()
enemy_image_2 = pygame.transform.scale(pygame.image.load('E:/Castle_Defender-main/img/enemies/knight/attack/1.png'),(75,65)).convert_alpha()
waypoints=[(25, 477), (300, 471), (331, 388), (371, 301), (428, 294), (460, 348), (468, 431), (525, 475), (681, 475)]
#create group for enemy and Turret
enemy_group = pygame.sprite.Group()
enemy = Enemy(waypoints,enemy_image_2)
turret_group = pygame.sprite.Group()




click=[]
enemy_group.add(enemy)

clock=pygame.time.Clock()
run= True
while run:
    clock.tick(c.FPS)
    screen.blit(map_image_1, (0, 0))
    enemy_group.draw(screen)
    enemy.move()
    turret_group.draw(screen)
    # pygame.draw.lines(screen,'black',False,waypoints)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            # turret = Turret(cursor_turret_brown,mouse_pos)
            # turret_group.add(turret)
    pygame.display.flip()
pygame.quit()

