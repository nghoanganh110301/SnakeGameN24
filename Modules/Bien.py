import pygame
from pygame.math import Vector2
pygame.init()
pygame.mixer.pre_init(frequency=44100, size = -16, channels=2, buffer=512)
SCREEN_WEIGHT = 800
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode((SCREEN_WEIGHT, SCREEN_HEIGHT))
FPS = pygame.time.Clock()
BLOCK_X = 40
BLOCK_Y = 30
BLOCKSIZE = 20

stone = pygame.image.load('image/warn/stone.png')
bush  = pygame.image.load('image/warn/bush2.png')
wall  = pygame.image.load('image/warn/wall.png')
stone_pos = [Vector2(5, 6), Vector2(20, 0), Vector2(38, 9), Vector2(15, 20), Vector2(30, 25)]
wall_pos = [Vector2(4, 24), Vector2(17, 9), Vector2(31, 20)]
bush_pos = [Vector2(9, 10), Vector2(2, 28), Vector2(30, 8), Vector2(0,5), Vector2(0,6),
            Vector2(25, 25), Vector2(25, 26), Vector2(26, 25), Vector2(26, 26),
            Vector2(32, 19), Vector2(33, 19), Vector2(34, 19), Vector2(35, 19)]

food1 = pygame.image.load('image/food/Mushroom_1.png')
food2 = pygame.image.load('image/food/Mushroom_2.png')
food3 = pygame.image.load('image/food/Mushroom_3.png')
bigFood = pygame.image.load('image/food/apple.png')

head_up    = pygame.image.load('image/snake/head_up.png')
head_down  = pygame.image.load('image/snake/head_down.png')
head_right = pygame.image.load('image/snake/head_right.png')
head_left  = pygame.image.load('image/snake/head_left.png')
tail_up    = pygame.image.load('image/snake/tail_up.png')
tail_down  = pygame.image.load('image/snake/tail_down.png')
tail_right = pygame.image.load('image/snake/tail_right.png')
tail_left  = pygame.image.load('image/snake/tail_left.png')
body_vertical   = pygame.image.load('image/snake/body_vertical.png')
body_horizontal = pygame.image.load('image/snake/body_horizontal.png')
body_tr = pygame.image.load('image/snake/body_tr.png')
body_tl = pygame.image.load('image/snake/body_tl.png')
body_br = pygame.image.load('image/snake/body_br.png')
body_bl = pygame.image.load('image/snake/body_bl.png')
bg = pygame.image.load('image/menu/bg.png')

eat_sound    = pygame.mixer.Sound('sound/sfx_point.wav')
hit_sound    = pygame.mixer.Sound('sound/sfx_hit.wav')
choose_sound = pygame.mixer.Sound('sound/beep.wav')