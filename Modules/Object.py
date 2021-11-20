import pygame
from Modules.Bien import *
def draw_text(text, x, y, font_size):
    font_word = pygame.font.Font('8-BIT WONDER.TTF', font_size)
    textobj = font_word.render(text, 1, (0, 0, 0))
    text_rect = textobj.get_rect()
    text_rect.topleft = (x, y)
    SCREEN.blit(textobj, text_rect)
class Button():
	def __init__(self, x, y, image, scale):
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False
	def draw(self):
		action = False
		pos = pygame.mouse.get_pos()
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				choose_sound.play()
				self.clicked = True
				action = True
		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False
		SCREEN.blit(self.image, (self.rect.x, self.rect.y))
		return action

play_img       = pygame.image.load('image/menu/play.png')
difficulty_img = pygame.image.load('image/menu/dificulty.png')
credit_img     = pygame.image.load('image/menu/credit.png')
exit_img       = pygame.image.load('image/menu/exit.png')
easy_img       = pygame.image.load('image/menu/easy.png')
normal_img     = pygame.image.load('image/menu/normal.png')
hard_img       = pygame.image.load('image/menu/hard.png')
restart_img    = pygame.image.load('image/menu/restart.png')
menu_img       = pygame.image.load('image/menu/menu.png')
rank_img       = pygame.image.load('image/menu/rank.png')
back_img       = pygame.image.load('image/menu/back.png')

play_button       = Button(320,200, play_img , 1)
difficulty_button = Button(250,275, difficulty_img , 1)
rank_button       = Button(320,350, rank_img , 1)
credit_button     = Button(290,420, credit_img , 1)
exit_button       = Button(325,500, exit_img , 1)

easy_button       = Button(310,250, easy_img , 1)
normal_button     = Button(280,320, normal_img , 1)
hard_button       = Button(310,390, hard_img , 1)
restart_button    = Button(290,180, restart_img , 1)
menu_button       = Button(320,240, menu_img , 1)
back_button       = Button(40,40, back_img , 1)
