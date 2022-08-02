import pygame

S_1 = [[0, 0, 0, 0, 0],
     [],
     [],
     [],
     [0, 0, 0, 0, 0]]

FPS = 60
WIDTH = 300
HEIGHT = 600
GRID_BLOCK_SIZE = 30
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
GREY = (100, 100, 100)


# initialize matrix
# playing space is 10x20
# there is extra 5 rows at the top for spawning blocks
# there is extra 1 row at the bottom for detecting collisions
# total matrix size is 10x26
matrix = [[0 for n in range(10)] for n in range(25)]
# adding the extra 1 row to the bottom
matrix.append([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])


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
