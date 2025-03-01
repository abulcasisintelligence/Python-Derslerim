import pygame
import time
import random

# Pygame'i başlat
pygame.init()

# Renkler
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)

# Ekran boyutu
WIDTH = 600
HEIGHT = 400

# Yılan özellikleri
SNAKE_BLOCK = 20
SNAKE_SPEED = 10
MAX_LENGTH = (WIDTH // SNAKE_BLOCK) * (HEIGHT // SNAKE_BLOCK)

# Fontlar
font = pygame.font.SysFont("bahnschrift", 25)

# Ekran oluştur
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Yılan Oyunu")

# Skor gösterme fonksiyonu
def show_score(score):
    value = font.render(f"Skor: {score}", True, WHITE)
    screen.blit(value, [10, 10])

# Yılanı çizen fonksiyon
def draw_snake(snake_list):
    for block in snake_list:
        pygame.draw.rect(screen, GREEN, [block[0], block[1], SNAKE_BLOCK, SNAKE_BLOCK])

# Oyun döngüsü
def game_loop():
    game_over = False
    game_close = False
    auto_collect = False
    
    x, y = WIDTH // 2, HEIGHT // 2
    x_change, y_change = 0, 0
    
    snake_list = []
    snake_length = 1
    
    food_x = random.randrange(0, WIDTH - SNAKE_BLOCK, SNAKE_BLOCK)
    food_y = random.randrange(0, HEIGHT - SNAKE_BLOCK, SNAKE_BLOCK)
    
    clock = pygame.time.Clock()
    
    while not game_over:
        while game_close:
            screen.fill(BLACK)
            msg1 = font.render("Kaybettin!", True, RED)
            msg2 = font.render("Yeniden başlamak için R'ye, çıkmak için Q'ya bas.", True, RED)
            msg1_rect = msg1.get_rect(center=(WIDTH // 2, HEIGHT // 3))
            msg2_rect = msg2.get_rect(center=(WIDTH // 2, HEIGHT // 3 + 30))
            screen.blit(msg1, msg1_rect)
            screen.blit(msg2, msg2_rect)
            show_score(snake_length - 1)
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_r:
                        game_loop()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and not auto_collect:
                    x_change = -SNAKE_BLOCK
                    y_change = 0
                elif event.key == pygame.K_RIGHT and not auto_collect:
                    x_change = SNAKE_BLOCK
                    y_change = 0
                elif event.key == pygame.K_UP and not auto_collect:
                    y_change = -SNAKE_BLOCK
                    x_change = 0
                elif event.key == pygame.K_DOWN and not auto_collect:
                    y_change = SNAKE_BLOCK
                    x_change = 0
                elif event.key == pygame.K_a:  # 'A' tuşuna basıldığında otomatik toplama başlar veya durur
                    auto_collect = not auto_collect
        
        if auto_collect:
            if x < food_x:
                x_change = SNAKE_BLOCK
                y_change = 0
            elif x > food_x:
                x_change = -SNAKE_BLOCK
                y_change = 0
            elif y < food_y:
                y_change = SNAKE_BLOCK
                x_change = 0
            elif y > food_y:
                y_change = -SNAKE_BLOCK
                x_change = 0
        
        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_close = True
        
        x += x_change
        y += y_change
        screen.fill(BLACK)
        pygame.draw.rect(screen, RED, [food_x, food_y, SNAKE_BLOCK, SNAKE_BLOCK])
        
        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)
        
        if len(snake_list) > snake_length:
            del snake_list[0]
        
        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True
        
        draw_snake(snake_list)
        show_score(snake_length - 1)
        pygame.display.update()
        
        if x == food_x and y == food_y:
            food_x = random.randrange(0, WIDTH - SNAKE_BLOCK, SNAKE_BLOCK)
            food_y = random.randrange(0, HEIGHT - SNAKE_BLOCK, SNAKE_BLOCK)
            snake_length += 1
        
        if snake_length == MAX_LENGTH:
            screen.fill(BLACK)
            msg = font.render("Kazandınız!", True, GREEN)
            msg_rect = msg.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            screen.blit(msg, msg_rect)
            pygame.display.update()
            time.sleep(3)
            game_over = True
        
        clock.tick(SNAKE_SPEED)
    
    pygame.quit()
    quit()

# Oyunu başlat
game_loop()