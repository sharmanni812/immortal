import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

# 1. Заливка фона (светло-серый)
screen.fill((200, 200, 200))

# 2. Голова (желтый круг с черным контуром)
circle(screen, (255, 255, 0), (200, 200), 100)
circle(screen, (0, 0, 0), (200, 200), 100, 1)

# 3. Глаза (красные круги с черным контуром)
# Левый глаз
circle(screen, (255, 0, 0), (160, 170), 20)
circle(screen, (0, 0, 0), (160, 170), 20, 1)
circle(screen, (0, 0, 0), (160, 170), 8) # Зрачок
# Правый глаз
circle(screen, (255, 0, 0), (240, 170), 15)
circle(screen, (0, 0, 0), (240, 170), 15, 1)
circle(screen, (0, 0, 0), (240, 170), 6) # Зрачок

# 4. Брови (черные линии под наклоном)
line(screen, (0, 0, 0), (120, 130), (190, 180), 10) # Левая
line(screen, (0, 0, 0), (280, 130), (210, 180), 10) # Правая

# 5. Рот (черный прямоугольник)
rect(screen, (0, 0, 0), (150, 240, 100, 20))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()