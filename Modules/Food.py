import pygame, random
from Modules.Bien import *
from pygame.math import Vector2
class Food:
    def __init__(self):
        self.random_pos()
    def draw(self):
        food_rect = pygame.Rect(self.pos.x*BLOCKSIZE, self.pos.y*BLOCKSIZE, BLOCKSIZE, BLOCKSIZE)
        SCREEN.blit(self.food_image, food_rect)
    def random_pos(self):
        self.pos = Vector2(random.randint(0, BLOCK_X-1), random.randint(0, BLOCK_Y-1))
        while not self.check_pos(): self.random_pos()
        self.food_image = random.choice([food1, food2, food3])
    def check_pos(self):
        for block in stone_pos:
            if block == self.pos:
                return False
        for block in wall_pos:
            if self.pos.y == block.y:
                if self.pos.x >= block.x and self.pos.x <= block.x + 5:
                    return False
        return True