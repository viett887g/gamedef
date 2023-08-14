import pygame
class Button_1():
    def __init__(self,x,y,image,single_click):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

        self.clicked =False
        self.single_click = single_click
    def draw(self,surface):
        # draw image in screen
        pos = pygame.mouse.get_pos()
        action= False
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]==1 and self.clicked ==False:
                action=True
                if self.single_click:
                    self.clicked = True
        if pygame.mouse.get_pressed()[0]==0:
            self.clicked = False



        surface.blit(self.image,self.rect)
        return action
