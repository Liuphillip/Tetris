import pygame

WIDTH, HEIGHT = 900,500
WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))
GREEN = (0,150,0)
FPS = 60

YELLOW_SHIP_IMAGE = pygame.image.load('')

pygame.display.set_caption("The Game")


def draw_window():
    WINDOW.fill(GREEN)
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        #check events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


        #update window
        draw_window()
    pygame.quit()

if __name__ == "__main__":
    main()