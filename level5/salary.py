def SynchronizingTables(n, ids, salary):
	"""
	получает параметром N длину обоих массивов. Параметр ids -- массив,содержащий номера сотрудников,
	параметр salary -- массив, содержащий зарплаты.
	Возвращает функция массив, содержащий переупорядоченные зарплаты.
	"""
	ids_c = ids.copy()
	salary = salary.copy()
	ids_c.sort()
	salary.sort()
	d = dict(zip(ids_c, salary))
	for i in range(n):
		salary[i] = d[ids[i]]
	return salary