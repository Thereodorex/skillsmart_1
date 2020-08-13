import unittest
from squirrel import squirrel

class TestSquirrel(unittest.TestCase):
	def test_100(self):
		cases = []
		current = 1
		for i in range(1, 1010):
			current *= i
			cases.append(current)
		for i, c in enumerate(cases):
			with self.subTest(case=c):
				self.assertEqual(int(str(c)[:1]), squirrel(i+1))

if __name__ == "__main__":
	unittest.main()