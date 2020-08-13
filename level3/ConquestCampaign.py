class Game:

	def __init__(self, n, m):
		self.n = n
		self.m = m
		self.board = [[0] * m for i in range(n)]
		self.day = 0
		self.free = n * m

	def start(self, battalion):
		self.day = 1
		for i in range(0, len(battalion), 2):
			if self.board[battalion[i]-1][battalion[i+1]-1] == 0:
				self.board[battalion[i]-1][battalion[i+1]-1] = 1
				self.free -= 1

	def run(self):
		while self.free != 0:
			self.day += 1
			for y, line in enumerate(self.board):
				for x, v in enumerate(line):
					if v == 1:
						pass
						self.board[y][x] = 2
			for y, line in enumerate(self.board):
				for x, v in enumerate(line):
					if v == 2:
						self.step(y, x)
		return self.day


	def step(self, y, x):
		self.step_to_point(y - 1, x)
		self.step_to_point(y + 1, x)
		self.step_to_point(y, x - 1)
		self.step_to_point(y, x + 1)

	def step_to_point(self, y, x):
		if y >= 0 and y < self.n and x >= 0 and x < self.m:
			if self.board[y][x] == 0:
				self.board[y][x] = 1
				self.free -= 1

def ConquestCampaign(n, m, l, battalion):
	"""
	Десантники в день 1 высаживаются в L областей, заданных их координатами (x1, y1),
	(x2,y2), ... , (xl, yl) и защищают их от бунтовщиков. На следующий день (день 2)
	они захватывают все соседние области, прилегающие к этим областям с четырёх сторон
	(по вертикали и горизонтали), и далее каждый следующий день этот процесс повторяется,
	пока не будут взяты под контроль все бунтующие области без исключения.
	Функция получает первыми двумя параметрами размер Государства Квадратов NxM,
	а battalion содержит массив из L*2 целых чисел (L >= 1) с индексацией с нуля,
	в котором каждый чётный элемент содержит очередную координату области высадки
	по первому измерению N, а каждый нечётный элемент содержит очередную координату
	области высадки по второму измерению M. Не исключено, что в связи с неразберихой
	в командовании координаты областей высадки могут дублироваться.
	Возвращает день, начиная с 1, когда все области будут взяты под контроль.
	"""
	game = Game(n, m)
	game.start(battalion)
	return game.run()