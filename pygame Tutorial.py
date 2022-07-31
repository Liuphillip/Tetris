import pygame
import os

WIDTH, HEIGHT = 900,500
WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))
GREEN = (50,200,50)
BLACK = (0,0,0)
FPS = 60
SHIP_WIDTH, SHIP_HEIGHT = 55,40
VELOCITY = 5

MAX_BULLETS = 3
BULLET_VEL = 10

YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2

BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)

YELLOW_SHIP_IMAGE = pygame.image.load(
    os.path.join('Assets','spaceship_yellow.png'))
YELLOW_SHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SHIP_IMAGE, (SHIP_WIDTH,SHIP_HEIGHT)), 90)

RED_SHIP_IMAGE = pygame.image.load(
    os.path.join('Assets','spaceship_red.png'))
RED_SHIP = pygame.transform.rotate(pygame.transform.scale(
    RED_SHIP_IMAGE, (SHIP_WIDTH,SHIP_HEIGHT)), 90)

pygame.display.set_caption("The Game")


def draw_window(red,yellow, red_bullets, yellow_bullets):
    WINDOW.fill(GREEN)
    pygame.draw.rect(WINDOW, BLACK, BORDER)
    WINDOW.blit(YELLOW_SHIP,(yellow.x,yellow.y))
    WINDOW.blit(RED_SHIP,(red.x,red.y))

    for bullet in red_bullets:
        pygame.draw.rect(WINDOW, BLACK, bullet)
    for bullet in yellow_bullets:
        pygame.draw.rect(WINDOW, BLACK, bullet)

    pygame.display.update()


def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    for bullet in yellow_bullets:
        bullet.x -= BULLET_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        elif bullet.x < 0:
            yellow_bullets.remove(bullet)


    for bullet in red_bullets:
        bullet.x += BULLET_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            red_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            red_bullets.remove(bullet)

def yellow_movement(keys_pressed,yellow):
    if keys_pressed[pygame.K_a] and yellow.x - VELOCITY > BORDER.x:  # LEFT
        yellow.x -= VELOCITY
    if keys_pressed[pygame.K_d] and yellow.x + VELOCITY + yellow.width < WIDTH:  # RIGHT
        yellow.x += VELOCITY
    if keys_pressed[pygame.K_w] and yellow.y - VELOCITY > 0:  # UP
        yellow.y -= VELOCITY
    if keys_pressed[pygame.K_s] and yellow.y + VELOCITY + yellow.height < HEIGHT:  # DOWN
        yellow.y += VELOCITY


def red_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_LEFT] and yellow.x - VELOCITY > 0:  # LEFT
        yellow.x -= VELOCITY
    if keys_pressed[pygame.K_RIGHT] and yellow.x + VELOCITY + yellow.width < BORDER.x:  # RIGHT
        yellow.x += VELOCITY
    if keys_pressed[pygame.K_UP] and yellow.y - VELOCITY > 0:  # UP
        yellow.y -= VELOCITY
    if keys_pressed[pygame.K_DOWN] and yellow.y + VELOCITY + yellow.height < HEIGHT:  # DOWN
        yellow.y += VELOCITY


def main():
    red = pygame.Rect(100,300, SHIP_WIDTH,SHIP_HEIGHT)
    yellow = pygame.Rect(700, 300, SHIP_WIDTH, SHIP_HEIGHT)

    red_bullets = []
    yellow_bullets = []

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        #check events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height//2 - 2, 10, 5)
                    yellow_bullets.append(bullet)
                if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(red.x, red.y + red.height // 2 - 2, 10, 5)
                    red_bullets.append(bullet)
        # logic
        keys_pressed = pygame.key.get_pressed()
        yellow_movement(keys_pressed, yellow)
        red_movement(keys_pressed, red)
        handle_bullets(yellow_bullets, red_bullets, yellow, red)

        # update window
        draw_window(red, yellow, red_bullets, yellow_bullets)
    pygame.quit()


if __name__ == "__main__":
    main()