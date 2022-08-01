import pygame

FPS = 60
WIDTH = 300
HEIGHT = 600
BLOCK_WIDTH, BLOCK_HEIGHT = 30, 30
GRID_WIDTH, GRID_HEIGHT = WIDTH/BLOCK_WIDTH, HEIGHT/BLOCK_HEIGHT
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

GRID_ARRAY = [[0] * int(GRID_WIDTH) for n in range(int(GRID_HEIGHT))]

GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
GREY = (100, 100, 100)


def create_grid(locked_pos = {}):
    grid = [[(0,0,0) for n in range(GRID_WIDTH)] for n in range(GRID_HEIGHT)]

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if (col, row) in locked_pos:
                color = locked_pos[(col, row)]
                grid[col][row] = color

    return grid


def grid():
    x, y = 0, 0
    for row in GRID_ARRAY:
        for col in row:
            block = pygame.Rect(x, y, BLOCK_WIDTH, BLOCK_HEIGHT)
            pygame.draw.rect(WINDOW, GREEN, block)
            x += BLOCK_WIDTH
            # print("x : " + str(x))
        y += BLOCK_HEIGHT
        # print("y : " + str(y))
        x = 0

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
