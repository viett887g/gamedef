import pygame
import constant as c
from enemys import Enemy
from turet import Turret
from regame_defense.button_2 import Button_1
pygame.init()
screen = pygame.display.set_mode((c.SCREEN_WIDTH +300,c.SCREEN_HEIGHT))
enemy_image = pygame.image.load('E:/tower_defence_tut-main/Part 1/assets/images/enemies/enemy_1.png').convert_alpha()
dino_image= pygame.transform.scale(pygame.image.load('C:/Users/vcd09/Pictures/goblin.png').convert_alpha(),(80,65))
turret_sheet = pygame.image.load('E:/tower_defence_tut-main/Part 1/assets/images/turrets/turret_1.png').convert_alpha()
cursor_turret = pygame.image.load('E:/tower_defence_tut-main/Part 1/assets/images/turrets/cursor_turret.png').convert_alpha()
turret_sprite_sheet =[]
for x in range(1,c.TURRET_LEVELS+1):
    turret_sheet = pygame.image.load(f'E:/tower_defence_tut-main/Part 1/assets/images/turrets/turret_{x}.png').convert_alpha()
    turret_sprite_sheet.append(turret_sheet)
cursor_turret_brown= pygame.image.load('C:/Users/vcd09/Downloads/ground_shaker_asset/Purple/Weapons/turret_01_mk1.gif').convert_alpha()

map_image = pygame.image.load('E:/tower_defence_tut-main/Part 1/levels/level.png').convert_alpha()
map_image_1 = pygame.transform.scale(pygame.image.load('C:/Users/vcd09/Pictures/map_game.png'),(c.SCREEN_WIDTH,c.SCREEN_HEIGHT)).convert_alpha()

cancel_image=pygame.image.load('E:/tower_defence_tut-main/Part 6/assets/images/buttons/cancel.png').convert_alpha()
buy_turret_image=pygame.image.load('E:/tower_defence_tut-main/Part 6/assets/images/buttons/buy_turret.png').convert_alpha()
upgrade_button=pygame.image.load('E:/tower_defence_tut-main/Part 6/assets/images/buttons/upgrade_turret.png').convert_alpha()

enemy_image_2 = pygame.transform.scale(pygame.image.load('E:/Castle_Defender-main/img/enemies/knight/attack/1.png'),(75,65)).convert_alpha()
waypoints=[(709, 111), (517, 113), (292, 117), (246, 171), (240, 231), (251, 277), (273, 334), (327, 371), (369, 439), (368, 528), (307, 563), (278, 630), (277, 698)]

#create group for enemy and Turret
enemy_group = pygame.sprite.Group()
enemy = Enemy(waypoints,dino_image)
turret_group = pygame.sprite.Group()

# # button
buy_turret_button = Button_1( c.SCREEN_WIDTH+80 ,80, buy_turret_image,True)
cancel_button = Button_1(c.SCREEN_WIDTH+80,150,cancel_image,True)
upgrade_button = Button_1(c.SCREEN_WIDTH+80,150,upgrade_button,True)
def create_turret(mouse_pos):
    mouse_tile_x = mouse_pos[0] // c.TILE_SIZE
    mouse_tile_y = mouse_pos[1] // c.TILE_SIZE
    space_is_free = True
    for turret in turret_group:
      if (mouse_tile_x, mouse_tile_y) == (turret.tile_x, turret.tile_y):
        space_is_free = False
    #if it is a free space then create turret
    if space_is_free == True:
      new_turret = Turret(turret_sprite_sheet, mouse_tile_x, mouse_tile_y)
      turret_group.add(new_turret)

def select_turret(mouse_pos):
    mouse_tile_x = mouse_pos[0] // c.TILE_SIZE
    mouse_tile_y = mouse_pos[1] // c.TILE_SIZE
    for turret in turret_group:
      if (mouse_tile_x, mouse_tile_y) == (turret.tile_x, turret.tile_y):
        return turret

def clear_selection():
    for turret in turret_group:
        turret.selected = False

enemy_group.add(enemy)
# avable
placing_turret= False
selected_turret = None
click =[]


clock=pygame.time.Clock()
run= True
while run:
    screen.fill('grey')
    clock.tick(c.FPS)
    screen.blit(map_image_1, (0, 0))
    enemy_group.draw(screen)
    enemy.move()

    for turret in turret_group:
        turret.draw(screen)
    if selected_turret:
        selected_turret.selected = True

    turret_group.update(enemy_group)
    # button in game
    if buy_turret_button.draw(screen):

        placing_turret =True
    if placing_turret ==True:
        cursor_image = cursor_turret.get_rect()
        cursor_pos = pygame.mouse.get_pos()
        cursor_image.center = cursor_pos

        if cursor_pos[0]<c.SCREEN_WIDTH:
            screen.blit(cursor_turret, cursor_image)
        if cancel_button.draw(screen):

            placing_turret=False
    if selected_turret:
        if selected_turret.upgrade_level < c.TURRET_LEVELS:
            if upgrade_button.draw(screen):
                selected_turret.upgrade()





    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()



            if mouse_pos[0]<c.SCREEN_WIDTH and mouse_pos[1]<c.SCREEN_HEIGHT:
                selected_turret = False
                clear_selection()

                if placing_turret==True:
                    create_turret(mouse_pos)
                else:
                    selected_turret = select_turret(mouse_pos)


    pygame.display.flip()
pygame.quit()