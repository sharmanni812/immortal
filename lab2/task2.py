import pygame
from pygame.draw import *

# Инициализация
pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 550))

def draw_background():
    """Рисует небо и землю"""
    rect(screen, (80, 80, 80), (0, 0, 600, 280))   # Серое небо
    rect(screen, (0, 0, 0), (0, 280, 600, 270))    # Черная земля

def draw_moon():
    """Рисует луну"""
    circle(screen, (240, 240, 240), (500, 70), 45)

def draw_cloud(x, y, w, h, color):
    """Рисует облако (эллипс) по заданным координатам"""
    ellipse(screen, color, (x, y, w, h))

def draw_house(shift_x):
    """Рисует дом со смещением shift_x (точно как во 2 задании)"""
    # 3. ДОМ (Стены и крыша)
    rect(screen, (50, 40, 0), (120 - shift_x, 200, 300, 220)) 
    # Крыша
    polygon(screen, (0, 0, 0), [
        (110 - shift_x, 200), 
        (430 - shift_x, 200), 
        (400 - shift_x, 170), 
        (140 - shift_x, 170)
    ])
    # Трубы
    rect(screen, (30, 30, 30), (150 - shift_x, 130, 15, 40))
    rect(screen, (30, 30, 30), (320 - shift_x, 140, 15, 30))

    # 4. ОКНА И БАЛКОН
    for i in range(4):
        rect(screen, (40, 30, 0), (150 - shift_x + i * 70, 210, 40, 80))
    rect(screen, (40, 25, 0), (160 - shift_x, 320, 60, 60))
    rect(screen, (35, 20, 0), (240 - shift_x, 320, 60, 60))
    rect(screen, (200, 160, 0), (320 - shift_x, 320, 60, 60))

    # Балкон
    line(screen, (0, 0, 0), (120 - shift_x, 300), (420 - shift_x, 300), 15)
    for i in range(10):
        line(screen, (0, 0, 0), (135 - shift_x + i * 30, 280), (135 - shift_x + i * 30, 300), 5)
    line(screen, (0, 0, 0), (120 - shift_x, 280), (420 - shift_x, 280), 7)

def draw_ghost(x_offset, y_offset):
    """Рисует привидение с возможностью небольшого смещения"""
    # Тело
    ghost_points = [
        (450 + x_offset, 480 + y_offset), (470 + x_offset, 430 + y_offset), 
        (500 + x_offset, 400 + y_offset), (540 + x_offset, 420 + y_offset), 
        (570 + x_offset, 460 + y_offset), (580 + x_offset, 500 + y_offset), 
        (550 + x_offset, 520 + y_offset), (500 + x_offset, 530 + y_offset), 
        (460 + x_offset, 510 + y_offset)
    ]
    polygon(screen, (180, 180, 180), ghost_points)
    # Глаза
    circle(screen, (150, 200, 255), (495 + x_offset, 435 + y_offset), 5)
    circle(screen, (150, 200, 255), (525 + x_offset, 435 + y_offset), 5)

# --- ВЫЗОВ ФУНКЦИЙ ---
draw_background()
draw_moon()

# Облака (теперь через одну функцию)
draw_cloud(20, 70, 440, 40, (50, 50, 50))
draw_cloud(245, 50, 360, 40, (60, 60, 60))
draw_cloud(350, 100, 300, 27, (60, 60, 60))
draw_cloud(280, 142, 600, 27, (0, 0, 0))

# Дом (передаем shift_x как аргумент)
draw_house(shift_x=100)

# Привидение (без смещения, как в оригинале)
draw_ghost(0, 0)

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