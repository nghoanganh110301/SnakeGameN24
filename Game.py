import pygame,sys
from Modules.Bien import *
from Modules.Object import *
from Modules.Event import *
pygame.init()
class main_Menu:
    def __init__(self):
        self.snake_speed = 10
        self.hard_mode = 'EASY'
        self.bxh = []
    def menu(self):
        while True:
            SCREEN.blit(bg, (0,0))
            draw_text('MAIN MENU', 250, 100, 35)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()                
            if play_button.draw():
                self.Play()
            if difficulty_button.draw():
                self.difficulty()
            if rank_button.draw():
                self.show_rank()
            if credit_button.draw():
                self.credit()
            if exit_button.draw():
                pygame.quit()
                sys.exit()
            pygame.display.update()  
    def Play(self):
        gl = GamePlay()
        run = True,
        lose = False
        pause = False
        tmp = self.snake_speed
        while run:
            SCREEN.fill((255, 255, 153))
            gl.set_barrier()
            gl.print_score()
            while lose:
                SCREEN.blit(bg, (0,0))
                draw_text('Your score: ', 300, 120, 15)
                draw_text(str(gl.score), 460, 120, 15)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()  
                if restart_button.draw():
                    self.Play()
                if menu_button.draw():
                    self.menu()
                pygame.display.update()
            while pause:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()  
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            pause = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        pause = True
                    if event.key == pygame.K_UP and gl.snake.before_direction != 'DOWN':
                        gl.snake.direction = Vector2(0, -1)
                        gl.snake.before_direction = 'UP'
                    elif event.key == pygame.K_DOWN and gl.snake.before_direction != 'UP':
                        gl.snake.direction = Vector2(0, 1)
                        gl.snake.before_direction = 'DOWN'
                    elif event.key == pygame.K_LEFT and gl.snake.before_direction != 'RIGHT':
                        gl.snake.direction = Vector2(-1, 0)
                        gl.snake.before_direction = 'LEFT'
                    elif event.key == pygame.K_RIGHT and gl.snake.before_direction != 'LEFT':
                        gl.snake.direction = Vector2(1, 0)
                        gl.snake.before_direction = 'RIGHT'
            gl.move()
            gl.eat()
            gl.draw()
            if gl.count == 4:
                tmp += 1
                gl.count = 0
            if gl.check_touch(): 
                hit_sound.play()
                self.bxh.append(gl.score)
                self.bxh_update()
                lose = True
            pygame.display.update()
            FPS.tick(tmp)
    def difficulty(self):
        while True:
            SCREEN.blit(bg, (0,0))   
            draw_text('DIFFICULTY:', 250, 150, 20)
            draw_text(self.hard_mode, 450, 150, 20)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()        
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.menu()
            if back_button.draw(): self.menu()
            if easy_button.draw():
                self.snake_speed = 10
                self.hard_mode = 'EASY'
            if normal_button.draw():
                self.snake_speed = 15
                self.hard_mode = 'NORMAL'
            if hard_button.draw():
                self.snake_speed = 20
                self.hard_mode = 'HARD'
            pygame.display.update() 
    def show_rank(self):
        with open('bxh.txt', 'r') as f:
            l = ([int(i) for i in f.readline().split()])
        while True:
            SCREEN.blit(bg, (0,0)) 
            draw_text('Rank     Score', 280, 150, 20)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()        
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.menu()
            if back_button.draw(): self.menu()
            for i in range(5):
                draw_text(str(i+1)+"           "+str(l[i]), 300, 180+i*30, 20)
            pygame.display.update() 
    def credit(self):
        while True:
            SCREEN.blit(bg, (0,0))
            draw_text('CREDITS', 320, 120, 20)
            draw_text('MADE BY N24', 290, 550, 20)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()        
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.menu()
            if back_button.draw(): self.menu()
            pygame.display.update()    
    def bxh_update(self):
        with open('bxh.txt', 'r') as f:
            self.bxh += ([int(i) for i in f.readline().split()])
            self.bxh.sort(reverse=True)
            self.bxh.pop()
        s = ""
        for i in self.bxh:
            s = s + str(i) + " "
        with open('bxh.txt', 'w') as f:
            f.write(s)
        self.bxh = []
a = main_Menu()
a.menu()