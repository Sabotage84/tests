import pygame as pygame
import random
import os
import sys
import time

WIDTH = 600  # ширина игрового окна
HEIGHT = 700  # высота игрового окна
FPS = 30  # частота кадров в секунду

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


class Player(pygame.sprite.Sprite):

    speed = 7
    right_move = 0
    left_move = 0

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.midbottom = ((WIDTH / 2) - 25, HEIGHT-10)

    def get_mid_point(self):
        return self.rect.midtop


    def update_speed(self):
        self.speed = 0

    def update_right_move(self):
        self.right_move += 1

    def update_left_move(self):
        self.left_move += 1

    def zero_left_move(self):
        self.left_move = 0

    def zero_right_move(self):
        self.right_move = 0

    def update(self):
        self.rect.x += self.speed * self.right_move - self.speed * self.left_move
        # self.right_move = 0
        # self.left_move = 0
        # if self.rect.left > WIDTH:
        #     self.rect.right = 0


class Bullet(pygame.sprite.Sprite):
    speed = 5

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((5, 15))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.midbottom = (x, HEIGHT-60)

    def update(self):
        self.rect.y -= self.speed
        # self.right_move = 0
        # self.left_move = 0
        # if self.rect.left > WIDTH:
        #     self.rect.right = 0


class Target(pygame.sprite.Sprite):
    speed = 1

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((40, 40))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.midbottom = (x, y)

    def update(self):
        self.rect.y += self.speed
        # self.right_move = 0
        # self.left_move = 0
        # if self.rect.left > WIDTH:
        #     self.rect.right = 0


# создаем игру и окно
pygame.init()
pygame.mixer.init()  # для звука
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game 1")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
player = Player()
pygame.time.set_timer(pygame.USEREVENT, 4000)
all_sprites.add(player)


# Цикл игры
running = True
while running:
    # держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # проверить закрытие окна
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.USEREVENT:
            # Сделать несколько функций разных формаций
            for i in range(1, 4):
                target = Target(10 + 50 + i * 100, 0)
                all_sprites.add(target)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pass
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.update_left_move()
            if event.key == pygame.K_RIGHT:
                player.update_right_move()
            if event.key == pygame.K_DOWN or event.key == pygame.K_SPACE:
                a, s = player.rect.midtop
                bull = Bullet(a, s)
                all_sprites.add(bull)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.zero_left_move()
            if event.key == pygame.K_RIGHT:
                player.zero_right_move()
    # Обновление
    all_sprites.update()

    # Отрисовка
    screen.fill(BLACK)
    all_sprites.draw(screen)

    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

    # Визуализация (сборка)

pygame.quit()





