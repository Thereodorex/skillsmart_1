def squirrel(n):
	"""
	получает параметром целое неотрицательное число N,
	возвращает первую цифру факториала N
	"""
	res = 1
	for i in range(2, n+1):
		res *= i
	return int(str(res)[:1])