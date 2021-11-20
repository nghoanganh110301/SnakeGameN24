import pygame
from Modules.Snake import *
from Modules.Food import *
pygame.init()
class GamePlay:
    def __init__(self):
        self.food = Food()
        self.snake = Snake()
        self.score = 0
        self.count = 0
    def draw(self):
        self.food.draw()
        self.snake.draw()
    def move(self):
        self.snake.move()
    def eat(self):
        if self.snake.body[0] == self.food.pos:
            eat_sound.play()
            self.food.random_pos()
            self.snake.length += 1
            self.score += 1
            self.count += 1
    def check_touch(self):
        for block in self.snake.body[3:]:
            if block == self.snake.body[0]:
                return True
        for block in stone_pos:
            if block == self.snake.body[0]:
                return True
        for block in wall_pos:
            if block.y == self.snake.body[0].y:
                tmp = block.x
                if self.snake.body[0].x >= tmp and self.snake.body[0].x <= tmp + 5:
                    return True
    def print_score(self):
        font_word = pygame.font.SysFont(None, 25)
        s = font_word.render("Score: " + str(self.score), True, (0,0,0))
        SCREEN.blit(s, [0, 0])
    def set_barrier(self):
        for block in stone_pos:
            stone_rect = pygame.Rect(block.x*BLOCKSIZE, block.y*BLOCKSIZE, BLOCKSIZE, BLOCKSIZE)
            SCREEN.blit(stone, stone_rect)
        for block in bush_pos:
            bush_rect = pygame.Rect(block.x*BLOCKSIZE, block.y*BLOCKSIZE, BLOCKSIZE, BLOCKSIZE)
            SCREEN.blit(bush, bush_rect)
        for block in wall_pos:
            wall_rect = pygame.Rect(block.x*BLOCKSIZE, block.y*BLOCKSIZE, BLOCKSIZE, BLOCKSIZE)
            SCREEN.blit(wall, wall_rect)
