def odometer(l):
	"""
	Получает параметром массив N целых чисел (N >= 2) с индексацией с нуля,
	в котором каждый чётный элемент содержит скорость в километрах в час,
	а каждый нечётный элемент содержит время, прошедшее с начала поездки, в часах.
	Возвращает общее пройденное расстояние.
	Например, на входе массив [10,1,20,2], на выходе расстояние 30
	"""
	res = 0
	prev_time = 0
	for i in range(0, len(l), 2):
		res += l[i] * (l[i+1] - prev_time)
		prev_time = l[i+1]
	return res