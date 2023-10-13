import random,pygame,sys,time
#from raycasting import Boundary
sys.setrecursionlimit(30000)

GRID_SIZE = 60
multiplier = 10
secs = 0.001

class Cell:
	visited_colour = (255,255,255)
	unvisited_colour = (0,0,0)

	def __init__(self):
		self.current_colour = Cell.unvisited_colour
		self.visited = False
		self.val = 0
		self.rect = None
		self.center = None
		self.connected = []
		self.pos_dir = []

	def update_val(self):
		if self.visited:
			self.val = 1
			self.current_colour = Cell.visited_colour
		else:
			self.val = 0
			self.current_colour = Cell.unvisited_colour

	def add_rect(self,grid):
		index = self.index_2d(grid,self)
		self.rect = pygame.Rect(index[0]*multiplier,index[1]*multiplier,10,10)
		self.center = (self.rect.x+self.rect.width/2,self.rect.y+self.rect.height/2)

	def index_2d(self,myList, val):
	    for i, x in enumerate(myList):
	        if val in x:
	            return i, x.index(val)
class Search:
	def __init__(self):
		self.grid = [[Cell() for i in range(GRID_SIZE)] for j in range(GRID_SIZE)]
		for i in self.grid:
			for cell in i:
				cell.add_rect(self.grid)
		self.visited_cells = []
		self.lines = []

	def display_grid(self,window,line_size):
		for cell in self.visited_cells:
			#pygame.draw.rect(WIN,cell.current_colour,cell.rect)
			for node in cell.connected:
				time.sleep(secs)
				#self.lines.append(Boundary(cell.center,node.center))
				pygame.draw.line(window,Cell.visited_colour,cell.center,node.center,line_size)
			pygame.display.update()

	def get_rand_pnt(self):
		return (random.randint(0,GRID_SIZE-1),random.randint(0,GRID_SIZE-1))

	def get_dir(self,index):
		directions = [(1,0),(-1,0),(0,1),(0,-1)]
		pos_dir = []
		for direction in directions:
			if index[0]+direction[0] > -1 and index[0]+direction[0] < GRID_SIZE and index[1]+direction[1] > -1 and index[1]+direction[1] < GRID_SIZE and not self.grid[index[0]+direction[0]][index[1]+direction[1]].visited:
				pos_dir.append(direction)
		if len(pos_dir) == 0:
			return None
		else:
			return random.choice(pos_dir)

	def start(self):
		rand_pnt = self.get_rand_pnt()
		self.depth_first(self.grid[rand_pnt[0]][rand_pnt[1]])

	def depth_first(self,cell):
		#self.display_grid()
		cell.visited = True
		self.visited_cells.append(cell)
		cell.update_val()
		index = cell.index_2d(self.grid,cell)
		direction = self.get_dir(index)
		while direction is not None:
			cell.connected.append(self.grid[index[0]+direction[0]][index[1]+direction[1]])
			self.depth_first(self.grid[index[0]+direction[0]][index[1]+direction[1]])
			direction = self.get_dir(index)