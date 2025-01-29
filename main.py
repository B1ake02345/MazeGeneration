import pygame
from mazeGen import *

BLACK = (0,0,0)
dimension = 60*10
WINDOW = pygame.display.set_mode((dimension,dimension))
clock = pygame.time.Clock()


def update(current_search):
	WINDOW.fill(BLACK)
	if len(current_search.lines) > 0:
		for wall in current_search.lines:
			wall.update(WINDOW)

	pygame.display.update()

def main():
	search = Search()
	while True:
		clock.tick(30)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				WINDOW.fill(BLACK)
				search = Search()
				search.start()
				search.display_grid(WINDOW,1)

if __name__ == "__main__":
	main()