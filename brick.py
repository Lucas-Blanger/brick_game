import pygame
import sys
import random

# Inicialização do pygame
pygame.init()

# Configurações da tela
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Brick Breaker')

# Configurações de cores
black = (0, 0, 0)
white = (255, 255, 255)
green = (34, 139, 34)
yelow = (223, 255, 0)

# Configurações da raquete
paddle_width = 100
paddle_height = 10
paddle_x = (screen_width - paddle_width) // 2
paddle_y = screen_height - 30
paddle_speed = 6

# Configurações da bola
ball_radius = 10
ball_x = screen_width // 2
ball_y = paddle_y - ball_radius
ball_speed_x = 3
ball_speed_y = -3

# Configurações dos tijolos
brick_width = 75
brick_height = 20
brick_color = green

# Criar matriz de tijolos
bricks = []
rows = 5
cols = screen_width // (brick_width + 10)

for row in range(rows):
    brick_row = []
    for col in range(cols):
        brick_x = col * (brick_width + 10) + 35
        brick_y = row * (brick_height + 10) + 50
        brick_rect = pygame.Rect(brick_x, brick_y, brick_width, brick_height)
        brick_row.append(brick_rect)
    bricks.append(brick_row)

# Variável de pontuação
score = 0

# Fonte para exibir a pontuação
font = pygame.font.SysFont('Arial', 24)

# Função para desenhar a raquete
def draw_paddle():
    pygame.draw.rect(screen, white, (paddle_x, paddle_y, paddle_width, paddle_height))

# Função para desenhar a bola
def draw_ball():
    pygame.draw.circle(screen, yelow, (ball_x, ball_y), ball_radius)

# Função para desenhar os tijolos
def draw_bricks():
    for row in bricks:
        for brick in row:
            pygame.draw.rect(screen, brick_color, brick)

# Função para exibir a pontuação
def draw_score():
    score_text = font.render(f'Score: {score}', True, white)
    screen.blit(score_text, (10, 10))

# Função para exibir mensagem de vitória
def draw_victory_message():
    victory_text = font.render('Parabéns, Você Venceu!', True, white)
    text_rect = victory_text.get_rect(center=(screen_width / 2, screen_height / 2))
    screen.blit(victory_text, text_rect)
    pygame.display.flip()
    pygame.time.wait(3000)

# Loop principal do jogo
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle_x < screen_width - paddle_width:
        paddle_x += paddle_speed

    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Colisão com as paredes
    if ball_x <= ball_radius or ball_x >= screen_width - ball_radius:
        ball_speed_x *= -1
    if ball_y <= ball_radius:
        ball_speed_y *= -1
    if ball_y >= screen_height - ball_radius:
        running = False  # Fim do jogo se a bola passar da raquete

    # Colisão com a raquete
    if ball_y + ball_radius >= paddle_y and paddle_x <= ball_x <= paddle_x + paddle_width:
        ball_speed_y *= -1

    # Colisão com os tijolos
    for row in bricks:
        for brick in row:
            if brick.collidepoint(ball_x, ball_y):
                ball_speed_y *= -1
                row.remove(brick)
                score += 10  # Incrementa a pontuação
                break

    # Desenhar elementos na tela
    screen.fill(black)
    draw_paddle()
    draw_ball()
    draw_bricks()
    draw_score()
    pygame.display.flip()
    pygame.time.Clock().tick(60)

        # Verificar se todos os tijolos foram destruídos
    if all(not row for row in bricks):
        draw_victory_message()
        running = False

# Esperar um momento antes de fechar
pygame.quit()
sys.exit()
