# Документация: python -m pygame.docs
import random
import pygame


def draw(screen):
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 50)
    text = font.render("Hello, Pygame!",
                       True,
                       (100, 255, 100))
    text_x = width // 2 - text.get_width() // 2
    text_y = height // 2 - text.get_height() // 2
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y))
    pygame.draw.rect(screen, (0, 255, 0),
                (text_x - 10, text_y - 10,
                 text_w + 20, text_h + 20), 1)


def draw2(screen):
    for i in range(1000):
        screen.fill(pygame.Color('white'),
                    (random.random() * width,
                     random.random() * height, 10, 2))


def draw3(screen):
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0, 255, 0),
                     (100, 100,
                      200, 200), 1)
    pygame.draw.polygon(screen, pygame.Color('orange'), [(0, 0), (150, 50), (50, 150)], 0)


if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)
    dt = 0.01
    v = 200
    running = True
    pygame.display.set_caption("Херня")
    player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
    # Смена кадров (обновление экрана)

    running = True

    while running:
        screen.fill('purple')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        key = pygame.key.get_pressed()
        if key[pygame.K_w]:
            player_pos.y -= v * dt
        elif key[pygame.K_s]:
            player_pos.y += v * dt
        pygame.draw.circle(screen, 'red', player_pos, 10)
        pygame.display.flip()

    pygame.quit()

