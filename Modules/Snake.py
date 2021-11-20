import pygame
from Modules.Bien import *
from pygame.math import Vector2
class Snake:
    def __init__(self):
        self.body = [Vector2(20,15), Vector2(19,15), Vector2(18,15)]
        self.length = 3
        self.direction = Vector2(1,0)
        self.before_direction = 'RIGHT'
    def draw(self):
        self.update_head()
        self.update_tail()
        for i, block in enumerate(self.body):
            ok = True
            for block_a in bush_pos:
                if block_a == block:
                    ok = False
            if ok:
                x_pos = block.x * BLOCKSIZE
                y_pos = block.y * BLOCKSIZE
                block_rect = pygame.Rect(x_pos, y_pos, BLOCKSIZE, BLOCKSIZE)
                if i == 0:
                    SCREEN.blit(self.head, block_rect)
                elif i == len(self.body) - 1:
                    SCREEN.blit(self.tail, block_rect)
                else:
                    before_block = self.body[i+1] - block
                    after_block = self.body[i-1] - block
                    if before_block.x == after_block.x: SCREEN.blit(body_vertical, block_rect)
                    elif before_block.y == after_block.y: SCREEN.blit(body_horizontal, block_rect)
                    else: 
                        if (before_block.x == -1 and after_block.y == -1) or (before_block.y == -1 and after_block.x == -1):
                            SCREEN.blit(body_tl, block_rect)
                        elif (before_block.x == -1 and after_block.y == 1) or (before_block.y == 1 and after_block.x == -1):
                            SCREEN.blit(body_bl, block_rect)
                        elif (before_block.x == 1 and after_block.y == -1) or (before_block.y == -1 and after_block.x == 1):
                            SCREEN.blit(body_tr, block_rect)
                        elif (before_block.x == 1 and after_block.y == 1) or (before_block.y == 1 and after_block.x == 1):
                            SCREEN.blit(body_br, block_rect)   
    def update_head(self):
        head_direction = self.body[1] - self.body[0]
        if head_direction == Vector2(1, 0): self.head = head_left
        if head_direction == Vector2(-1, 0): self.head = head_right
        if head_direction == Vector2(0, 1): self.head = head_up
        if head_direction == Vector2(0, -1): self.head = head_down  
    def update_tail(self):
        tail_direction = self.body[-2] - self.body[-1]
        if tail_direction == Vector2(1, 0): self.tail = tail_left
        if tail_direction == Vector2(-1, 0): self.tail = tail_right
        if tail_direction == Vector2(0, 1): self.tail = tail_up
        if tail_direction == Vector2(0, -1): self.tail = tail_down 
    def move(self):
        pos_x = int(self.body[0].x + self.direction.x) % BLOCK_X
        pos_y = int(self.body[0].y + self.direction.y) % BLOCK_Y
        self.body.insert(0, Vector2(pos_x, pos_y))
        if(len(self.body) > self.length): self.body.pop()
 