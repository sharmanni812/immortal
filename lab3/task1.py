import pygame
from pygame.draw import *

def draw_richard(surface, x, y, width):
    '''
    Рисует Ричарда Уоттерсона без лишних розовых деталей внизу.
    Задание для напарника: разбить на draw_head, draw_body, draw_arms, draw_legs.
    '''
    # Цвета
    PINK = (255, 192, 203)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    BROWN = (101, 67, 33)
    GRAY = (60, 60, 60)
    DARK_PINK = (255, 150, 170)

    # --- ТУЛОВИЩЕ И ОДЕЖДА (Строго по контуру) ---
    # 1. Основная рубашка (закрывает все розовое тело сверху)
    # Плечевая часть (скругление)
    ellipse(surface, WHITE, (x - width // 2, y + width // 2.5, width, width // 2.5))
    # Основной прямоугольник рубашки
    rect(surface, WHITE, (x - width // 2, y + width // 2, width, width // 1.8))
    
    # 2. Брюки (коричневые штаны, закрывающие низ)
    # Пояс
    rect(surface, BROWN, (x - width // 2, y + width // 1.05, width, width // 6))
    # Левая штанина
    rect(surface, BROWN, (x - width // 2, y + width // 1.1 + width // 8, width // 2.5, width // 2.2))
    # Правая штанина
    rect(surface, BROWN, (x + width // 10, y + width // 1.1 + width // 8, width // 2.5, width // 2.2))

    # 3. Аксессуары
    # Галстук (магические числа для координат)
    ellipse(surface, GRAY, (x - 8, y + width // 2 + 15, 16, 22))
    polygon(surface, GRAY, [(x - 8, y + width // 2 + 35), (x + 8, y + width // 2 + 35), 
                            (x + 12, y + width // 2 + 130), (x, y + width // 2 + 150), (x - 12, y + width // 2 + 130)])
    # Воротник
    line(surface, BLACK, (x, y + width // 2), (x - 65, y + width // 2 + 45), 2)
    line(surface, BLACK, (x, y + width // 2), (x + 65, y + width // 2 + 45), 2)

    # --- КОНЕЧНОСТИ (Плавный переход к рукам) ---
    # Левая рука (Рукав + Лапа)
    ellipse(surface, WHITE, (x - width * 0.85, y + width // 2, width // 2.5, width // 3.8))
    ellipse(surface, PINK, (x - width * 0.95, y + width // 1.6, width // 3.5, width // 5))
    # Правая рука
    ellipse(surface, WHITE, (x + width // 2.2, y + width // 2, width // 2.5, width // 3.8))
    ellipse(surface, PINK, (x + width * 0.7, y + width // 1.6, width // 3.5, width // 5))

    # Ступни
    ellipse(surface, PINK, (x - width // 1.8, y + width * 1.5, width // 2, width // 6))
    ellipse(surface, BLACK, (x - width // 1.8, y + width * 1.5, width // 2, width // 6), 2)
    ellipse(surface, PINK, (x + width // 12, y + width * 1.5, width // 2, width // 6))
    ellipse(surface, BLACK, (x + width // 12, y + width * 1.5, width // 2, width // 6), 2)

    # --- ГОЛОВА ---
    draw_head(surface, x, y, width, PINK, WHITE, BLACK, DARK_PINK)

def draw_head(surface, x, y, width, PINK, WHITE, BLACK, DARK_PINK):
    '''Рисует голову Ричарда с щеками и ушами'''
    circle(surface, PINK, (x, y), width // 2)
    ellipse(surface, PINK, (x - width // 1.8, y - width // 10, width * 1.1, width // 1.5))
    
    # Уши
    ear = pygame.Surface((100, 200), pygame.SRCALPHA)
    ellipse(ear, PINK, (0, 0, 42, 165))
    surface.blit(pygame.transform.rotate(ear, 12), (x - width // 3, y - width // 1.1))
    surface.blit(pygame.transform.rotate(ear, -12), (x + width // 12, y - width // 1.1))

    # Глаза и лицо
    circle(surface, WHITE, (x - 45, y - 40), 40); circle(surface, BLACK, (x - 45, y - 40), 40, 2)
    circle(surface, WHITE, (x + 45, y - 40), 40); circle(surface, BLACK, (x + 45, y - 40), 40, 2)
    circle(surface, BLACK, (x - 35, y - 35), 7); circle(surface, BLACK, (x + 35, y - 35), 7)
    
    ellipse(surface, DARK_PINK, (x - 20, y + 5, 40, 25)); ellipse(surface, BLACK, (x - 20, y + 5, 40, 25), 1)
    
    for i in range(2): # Усы
        line(surface, BLACK, (x - 140, y + 35 + i*20), (x - 175, y + 30 + i*30), 2)
        line(surface, BLACK, (x + 140, y + 35 + i*20), (x + 175, y + 30 + i*30), 2)

    # Улыбка и зубы
    arc(surface, BLACK, (x - 70, y + 10, 140, 75), 3.14, 0, 2)
    rect(surface, WHITE, (x - 18, y + 75, 18, 26)); rect(surface, BLACK, (x - 18, y + 75, 18, 26), 1)
    rect(surface, WHITE, (x + 2, y + 75, 18, 26)); rect(surface, BLACK, (x + 2, y + 75, 18, 26), 1)

# Старт
pygame.init()
screen = pygame.display.set_mode((800, 1000))
screen.fill((253, 235, 208)) 

draw_richard(screen, 400, 300, 280)

pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: finished = True
pygame.quit()