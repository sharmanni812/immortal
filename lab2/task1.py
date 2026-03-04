import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

def draw_angry_face(x, y, scale):
    """
    Рисует злое лицо.
    x, y — центр головы.
    scale — масштаб (1.0 — оригинальный размер).
    """
    # 2. Голова (желтый круг с черным контуром)
    radius = int(100 * scale)
    circle(screen, (255, 255, 0), (x, y), radius)
    circle(screen, (0, 0, 0), (x, y), radius, 1)

    # 3. Глаза (красные круги с черным контуром)
    # Левый глаз (смещен влево на 40 и вверх на 30 относительно центра x, y)
    circle(screen, (255, 0, 0), (int(x - 40*scale), int(y - 30*scale)), int(20*scale))
    circle(screen, (0, 0, 0), (int(x - 40*scale), int(y - 30*scale)), int(20*scale), 1)
    circle(screen, (0, 0, 0), (int(x - 40*scale), int(y - 30*scale)), int(8*scale)) # Зрачок
    
    # Правый глаз (смещен вправо на 40 и вверх на 30)
    circle(screen, (255, 0, 0), (int(x + 40*scale), int(y - 30*scale)), int(15*scale))
    circle(screen, (0, 0, 0), (int(x + 40*scale), int(y - 30*scale)), int(15*scale), 1)
    circle(screen, (0, 0, 0), (int(x + 40*scale), int(y - 30*scale)), int(6*scale)) # Зрачок

    # 4. Брови (черные линии)
    # Используем смещения от центра для каждой точки линии
    line(screen, (0, 0, 0), (int(x - 80*scale), int(y - 70*scale)), 
         (int(x - 10*scale), int(y - 20*scale)), int(10*scale)) # Левая
    line(screen, (0, 0, 0), (int(x + 80*scale), int(y - 70*scale)), 
         (int(x + 10*scale), int(y - 20*scale)), int(10*scale)) # Правая

    # 5. Рот (черный прямоугольник)
    # Центрируем прямоугольник: x - половина ширины
    rect(screen, (0, 0, 0), (int(x - 50*scale), int(y + 40*scale), int(100*scale), int(20*scale)))

# --- ВЫЗОВ ФУНКЦИИ ---

# Заливка фона
screen.fill((200, 200, 200))

# Рисуем наше лицо в центре экрана
draw_angry_face(200, 200, 1.0)

pygame.display.update()

# Основной цикл
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()