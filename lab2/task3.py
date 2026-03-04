import pygame
from pygame.draw import *

# Инициализация
pygame.init()

FPS = 30
screen = pygame.display.set_mode((800, 600))

# --- ФУНКЦИИ ---

def draw_house(x, y, width, height):
    """
    Рисует дом. x, y — координаты левого верхнего угла стены.
    """
    # Основной корпус
    rect(screen, (50, 40, 0), (x, y, width, height)) 
    
    # Крыша
    polygon(screen, (0, 0, 0), [
        (x - 10, y), 
        (x + width + 10, y), 
        (x + width - 30, y - 40), 
        (x + 30, y - 40)
    ])
    
    # Трубы
    rect(screen, (30, 30, 30), (x + 30, y - 55, 15, 45))
    rect(screen, (30, 30, 30), (x + width - 60, y - 45, 15, 35))

    # Окна второго этажа
    for i in range(4):
        window_x = x + (width / 5) * (i + 1) - 15
        rect(screen, (40, 30, 0), (window_x, y + 15, 30, 70))

    # Окна первого этажа
    rect(screen, (40, 25, 0), (x + 30, y + 130, 50, 50))
    rect(screen, (35, 20, 0), (x + width // 2 - 25, y + 130, 50, 50))
    rect(screen, (200, 160, 0), (x + width - 80, y + 130, 50, 50)) 

    # Балкон
    line(screen, (0, 0, 0), (x, y + 110), (x + width, y + 110), 12) # Основание
    for i in range(10):
        step = (width / 10) * i
        line(screen, (0, 0, 0), (x + step, y + 90), (x + step, y + 110), 4) # Перила
    line(screen, (0, 0, 0), (x, y + 90), (x + width, y + 90), 6) # Поручень

def draw_ghost(x, y, scale):
    """Рисует привидение с масштабированием"""
    ghost_points = [
        (x, y), (x + 20*scale, y - 30*scale), (x + 50*scale, y - 50*scale),
        (x + 90*scale, y - 30*scale), (x + 120*scale, y + 10*scale),
        (x + 130*scale, y + 50*scale), (x + 100*scale, y + 70*scale),
        (x + 50*scale, y + 80*scale), (x + 10*scale, y + 60*scale)
    ]
    polygon(screen, (180, 180, 180), ghost_points)
    # Глаза
    circle(screen, (150, 200, 255), (int(x + 45*scale), int(y - 15*scale)), int(5*scale))
    circle(screen, (150, 200, 255), (int(x + 75*scale), int(y - 15*scale)), int(5*scale))

def draw_cloud(x, y, w, h):
    """Рисует облако"""
    ellipse(screen, (60, 60, 60), (x, y, w, h))

# --- ОСНОВНАЯ ОТРИСОВКА ---

# 1. Фон (Слой 0)
rect(screen, (80, 80, 80), (0, 0, 800, 300))   # Небо
rect(screen, (0, 0, 0), (0, 300, 800, 300))    # Земля
circle(screen, (240, 240, 240), (700, 80), 50) # Луна

# 2. Облака (Слой 1)
draw_cloud(50, 50, 300, 40)
draw_cloud(400, 100, 250, 35)
draw_cloud(150, 150, 400, 45)
draw_cloud(600, 40, 180, 30)

# 3. Дома (Слой 2)
# Левый дом (средний)
draw_house(50, 300, 220, 200)   
# Центральный дом (большой, на переднем плане)
draw_house(300, 240, 250, 230)  
# Правый дом (маленький, вдали)
draw_house(580, 280, 180, 180) 

# 4. Привидения (Слой 3 - самый верхний)
draw_ghost(100, 520, 0.6)
draw_ghost(400, 540, 0.8)
draw_ghost(650, 500, 0.5)
draw_ghost(250, 480, 0.4)



# Обновление экрана
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