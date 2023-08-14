import random

import pygame as pygame
from enemy_data import ENEMY_SPAWN_DATA
class World():
    def __init__(self,map_image):
        self.image= map_image

    def draw(self,sunface):
        sunface.blit(self.image,(0,0))
