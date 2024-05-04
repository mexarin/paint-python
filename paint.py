import pygame

WIDTH = 1920
HEIGHT = 1080
FPS = 120
prs = False

#Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (188, 25, 255)
colors = {1: WHITE, 2: BLACK, 3: RED, 4: GREEN, 5: BLUE, 6: YELLOW, 7: PURPLE}
color = colors[7]
color_str="фиолетовый"
size = 30
geometry="circle"

#Создаем игру и окно
pygame.font.init()
font_name = pygame.font.match_font('arial')
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Игра")
clock = pygame.time.Clock()
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, 30)
    if color != BLACK:
        text_surface = font.render(text, True, color)
    else:
        text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)
    pygame.font.Font()

#Цикл игры
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            prs = True
        if event.type == pygame.MOUSEBUTTONUP:
            prs = False

    keystate = pygame.key.get_pressed()
    if keystate[pygame.K_1]:
        color = colors[1]
        color_str = "белый"
    if keystate[pygame.K_2]:
        color = colors[2]
        color_str = "ластик"
    if keystate[pygame.K_3]:
        color = colors[3]
        color_str = "красный"
    if keystate[pygame.K_4]:
        color = colors[4]
        color_str = "зелёный"
    if keystate[pygame.K_5]:
        color = colors[5]
        color_str = "синий"
    if keystate[pygame.K_6]:
        color = colors[6]
        color_str = "жёлтый"
    if keystate[pygame.K_7]:
        color = colors[7]
        color_str ="фиолетовый"
    if keystate[pygame.K_EQUALS]:
        size += 1
    if keystate[pygame.K_MINUS] and size > 2:
        size -= 1
    if keystate[pygame.K_u]:
        pygame.draw.rect(screen, BLACK, (0, 0, WIDTH, HEIGHT))
    if keystate[pygame.K_r]:
        geometry="rect"
    if keystate[pygame.K_c]:
        geometry="circle"

    if prs == True and geometry=="circle":
        pygame.draw.circle(screen, color, pygame.mouse.get_pos(), size/2)
    if prs == True and geometry=="rect":
        pygame.draw.rect(screen, color, (pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1], size, size))
    pygame.draw.rect(screen, BLACK, (WIDTH/2-73, 8, 146, 28))
    draw_text(screen, color_str, 18, WIDTH / 2, 1)
    pygame.display.flip()

pygame.quit()
