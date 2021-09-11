# -*- coding: utf-8 -*-
"""trab_atualizado.ipynb"""

# import thread
import pygame, random
from pygame.locals import *
from threading import Semaphore, Thread
from threading import Lock

# Número máximo de threads a serem execultadas simultaneamente
control_threads = Semaphore(4)

# mutex3 = Lock()
# mutex4 = Lock()
# mutex5 = Lock()

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('Trens')

clock = pygame.time.Clock()

# speed
speed_verde = 2
class MyGame():
    def __init__(self):
        self.mutex1 = Lock()
        self.mutex2 = Lock()
        self.direction_verde = RIGHT
        self.direction_roxo = RIGHT
        self.direction_laranja = RIGHT
        # self.direction_azul = LEFT

        self.trem_verde_pos = (100, 100)
        self.trem_verde = pygame.Surface((10,10))
        self.trem_verde.fill((0,255,0))

        self.trem_roxo_pos = (200, 100)
        self.trem_roxo = pygame.Surface((10,10))
        self.trem_roxo.fill((128,0,255))

        # self.trem_laranja_pos = (300, 100)
        # self.trem_laranja = pygame.Surface((10,10))
        # self.trem_laranja.fill((255,128,0))

        # self.trem_azul_pos = (100, 200)
        # self.trem_azul = pygame.Surface((10,10))
        # self.trem_azul.fill((0,0,255))

        self.t_v = Thread(target=self.trem_verde_)
        self.t_r = Thread(target=self.trem_roxo_)
        # self.t_a = threading.Thread(target=self.trem_laranja_)
        # self.t_z = threading.Thread(target=self.trem_azul_)
        self.t_v.start()
        self.t_r.start()
        # self.t_a.start()
        # self.t_z.start()
    #Direção de acordo com a posição

    
    #Movimento de acordo com posição
    def L1(self):
        if self.direction_verde == UP:
            self.trem_verde_pos = (self.trem_verde_pos[0], self.trem_verde_pos[1] - speed_verde)

    def L2(self):
        if self.direction_verde == RIGHT:
            self.trem_verde_pos = (self.trem_verde_pos[0] + speed_verde, self.trem_verde_pos[1])

    def L3(self):
        if self.direction_verde == DOWN:
            self.trem_verde_pos = (self.trem_verde_pos[0], self.trem_verde_pos[1] + speed_verde)
        if self.direction_roxo == UP:
            self.trem_roxo_pos = (self.trem_roxo_pos[0], self.trem_roxo_pos[1] - 10)

    def L4(self):
        if self.direction_verde == LEFT:
            self.trem_verde_pos = (self.trem_verde_pos[0] - speed_verde, self.trem_verde_pos[1])
        # if self.direction_azul == RIGHT:
        #     self.trem_azul_pos = (self.trem_azul_pos[0] + 10, self.trem_azul_pos[1])

    def L5(self):
        if self.direction_roxo == DOWN:
            self.trem_roxo_pos = (self.trem_roxo_pos[0], self.trem_roxo_pos[1] + 10)
        # if self.direction_laranja == UP:
        #     self.trem_laranja_pos = (self.trem_laranja_pos[0], self.trem_laranja_pos[1] - 10)

    def L6(self):
        if self.direction_roxo == LEFT:
            self.trem_roxo_pos = (self.trem_roxo_pos[0] - 10, self.trem_roxo_pos[1])
        # if self.direction_azul == RIGHT:
        #     self.trem_azul_pos = (self.trem_azul_pos[0] + 10, self.trem_azul_pos[1])

    def L7(self):
        if self.direction_roxo == RIGHT:
            self.trem_roxo_pos = (self.trem_roxo_pos[0] + 10, self.trem_roxo_pos[1])

    def L8(self):
        if self.direction_laranja == RIGHT:
            self.trem_laranja_pos = (self.trem_laranja_pos[0] + 10, self.trem_laranja_pos[1])

    def L9(self):
        if self.direction_laranja == DOWN:
            self.trem_laranja_pos = (self.trem_laranja_pos[0], self.trem_laranja_pos[1] + 10)

    def L10(self):
        if self.direction_laranja == LEFT:
            self.trem_laranja_pos = (self.trem_laranja_pos[0] - 10, self.trem_laranja_pos[1])
        if self.direction_azul == RIGHT:
            self.trem_azul_pos = (self.trem_azul_pos[0] + 10, self.trem_azul_pos[1])

    def L11(self):
        if self.direction_azul == UP:
            self.trem_azul_pos = (self.trem_azul_pos[0], self.trem_azul_pos[1] - 10)

    def L12(self):
        if self.direction_azul == DOWN:
            self.trem_azul_pos = (self.trem_azul_pos[0], self.trem_azul_pos[1] + 10)

    def L13(self):
        if self.direction_azul == LEFT:
            self.trem_azul_pos = (self.trem_azul_pos[0] - 10, self.trem_azul_pos[1])


    def trem_verde_(self):
        if self.trem_verde_pos == (100, 100):
            self.direction_verde = RIGHT
        if self.trem_verde_pos == (200, 100):
            self.direction_verde = DOWN
        if self.trem_verde_pos == (200, 200):
           self.direction_verde = LEFT
        if self.trem_verde_pos == (100, 200):
            self.direction_verde = UP
        # print("posiciton verde: ", self.trem_verde_pos )
        self.L1()
        self.L2()
        
        self.mutex1.acquire(True)
        # self.mutex2.acquire(False)
        print('Região crita com verde')
        self.L3()
        self.mutex1.release()
        # self.mutex2.release()
        # mutex2.acquire()
        # mutex1.release()
        self.L4()
        # mutex2.release()
        screen.fill((0,0,0))
        screen.blit(self.trem_verde, self.trem_verde_pos)
        screen.blit(self.trem_roxo, self.trem_roxo_pos)
        # screen.blit(self.trem_laranja, self.trem_laranja_pos)
        # screen.blit(self.trem_azul, self.trem_azul_pos)

    def trem_roxo_(self):
        if self.trem_roxo_pos == (200, 100):
            self.direction_roxo = RIGHT
        if self.trem_roxo_pos == (300, 100):
            self.direction_roxo = DOWN
        if self.trem_roxo_pos == (300, 200):
            self.direction_roxo = LEFT
        if self.trem_roxo_pos == (200, 200):
            self.direction_roxo = UP

        self.L7()
        # mutex4.acquire()
        self.L5()
        # mutex3.acquire()
        # mutex4.release()
        self.L6()
        
        self.mutex2.acquire(True)
        self.mutex1.acquire(False)
        print('Região crita com roxa')
        self.L3()
        self.mutex2.release()
        self.mutex1.release()
        screen.fill((0,0,0))
        screen.blit(self.trem_verde, self.trem_verde_pos)
        screen.blit(self.trem_roxo, self.trem_roxo_pos)
        # screen.blit(self.trem_laranja, self.trem_laranja_pos)
        # screen.blit(self.trem_azul, self.trem_azul_pos)

    def trem_laranja_(self):
        if self.trem_laranja_pos == (300, 100):
            self.direction_laranja = RIGHT
        if self.trem_laranja_pos == (400, 100):
            self.direction_laranja = DOWN
        if self.trem_laranja_pos == (400, 200):
            self.direction_laranja = LEFT
        if self.trem_laranja_pos == (300, 200):
            self.direction_laranja = UP

        self.L8()
        self.L9()
        mutex5.acquire()
        self.L10()
        mutex4.acquire()
        mutex5.release()
        self.L5()
        mutex4.release()
        screen.fill((0,0,0))
        screen.blit(self.trem_verde, self.trem_verde_pos)
        screen.blit(self.trem_roxo, self.trem_roxo_pos)
        screen.blit(self.trem_laranja, self.trem_laranja_pos)
        screen.blit(self.trem_azul, self.trem_azul_pos)        

    def trem_azul_(self):
        if self.trem_azul_pos == (100, 200):
            self.direction_azul = RIGHT
        if self.trem_azul_pos == (400, 200):
            self.direction_azul = DOWN
        if self.trem_azul_pos == (400, 300):
            self.direction_azul = LEFT
        if self.trem_azul_pos == (100, 300):
            self.direction_azul = UP

        mutex3.acquire()
        mutex2.acquire()
        mutex5.acquire()
        self.L4()
        mutex2.release()
        self.L6()
        mutex3.release()
        self.L10()
        mutex5.release()
        self.L12()
        self.L13()
        self.L11()
        screen.fill((0,0,0))

        screen.blit(self.trem_verde, self.trem_verde_pos)
        screen.blit(self.trem_roxo, self.trem_roxo_pos)
        screen.blit(self.trem_laranja, self.trem_laranja_pos)
        screen.blit(self.trem_azul, self.trem_azul_pos)

if __name__ == '__main__':
    mygame = MyGame()
    while True:
        clock.tick(10)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
        
        mygame.trem_roxo_()
        mygame.trem_verde_()
        # mygame.trem_laranja_()
        # mygame.trem_azul_()
        
        pygame.draw.rect(screen, (255,255,255), [100, 100, 100, 100], 5)
        pygame.draw.rect(screen, (255,255,255), [200, 100, 100, 100], 5)
        pygame.draw.rect(screen, (255,255,255), [300, 100, 100, 100], 5)
        pygame.draw.rect(screen, (255,255,255), [100, 200, 300, 100], 5)

        pygame.display.update()