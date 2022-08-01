import pygame

FPS = 60
WIDTH = 500
HEIGHT = 500
GRID_WIDTH, GRID_HEIGHT = 50, 50
WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))

GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
GREY = (100, 100, 100)

def draw_window():
    WINDOW.fill(GREY)
    pygame.display.update()
def main():
    clock = pygame.time.Clock()

    run = True
    while run:
        # sets fps
        clock.tick(FPS)

        # event polling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # logic

        # Render
        draw_window()

if __name__ == "__main__":
    main()