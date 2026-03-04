import pygame
from pygame.draw import *

# Инициализация
pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 550))

# 1. ФОН (Небо и Земля)
rect(screen, (80, 80, 80), (0, 0, 600, 280))   # Серое небо
rect(screen, (0, 0, 0), (0, 280, 600, 270))    # Черная земля

# 2. ЛУНА И ОБЛАКА
circle(screen, (240, 240, 240), (500, 70), 45) # Луна
# Рисуем облака серыми эллипсами
ellipse(screen, (50, 50, 50), (20, 70, 440, 40))
ellipse(screen, (60, 60, 60), (245, 50, 360, 40))
ellipse(screen, (60, 60 ,60), (350, 100, 300, 27))
ellipse(screen, (0, 0, 0), (280, 142, 600, 27))

shift_x=100
# 3. ДОМ (Стены и крыша)
# Основной корпус
rect(screen, (50, 40, 0), (120-shift_x, 200, 300, 220)) 
# Крыша (трапеция через polygon)
polygon(screen, (0, 0, 0), 
        [(110-shift_x, 200), 
         (430-shift_x, 200), 
         (400-shift_x, 170), 
         (140-shift_x, 170)
])
# Трубы
rect(screen, (30, 30, 30), (150-shift_x, 130, 15, 40))
rect(screen, (30, 30, 30), (320-shift_x, 140, 15, 30))

# 4. ОКНА И БАЛКОН
# Окна второго этажа (используем цикл для повторения)
for i in range(4):
    rect(screen, (40, 30, 0), (150 - shift_x + i*70, 210, 40, 80)) # Темные окна
# Окна первого этажа
rect(screen, (40, 25, 0), (160-shift_x, 320, 60, 60))
rect(screen, (35, 20, 0), (240-shift_x, 320, 60, 60))
rect(screen, (200, 160, 0), (320-shift_x, 320, 60, 60)) # Светящееся окно

# Балкон (линии)
line(screen, (0, 0, 0), (120-shift_x, 300), (420-shift_x, 300), 15) # Основание
for i in range(10):
    line(screen, (0, 0, 0), (135 - shift_x + i*30, 280), (135 - shift_x + i*30, 300), 5) # Перила
line(screen, (0,0,0), (120-shift_x, 280), (420-shift_x, 280), 7)

# 5. ПРИВИДЕНИЕ
# Рисуем тело через polygon (координаты точек по контуру)
ghost_points = [(450, 480), (470, 430), (500, 400), (540, 420), 
                (570, 460), (580, 500), (550, 520), (500, 530), (460, 510)]
polygon(screen, (180, 180, 180), ghost_points)
# Глаза привидения
circle(screen, (150, 200, 255), (495, 435), 5)
circle(screen, (150, 200, 255), (525, 435), 5)

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