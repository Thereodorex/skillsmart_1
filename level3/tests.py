import unittest
from ConquestCampaign import ConquestCampaign

class TestGame(unittest.TestCase):
	def test_3_4(self):
		cases = [[1, 1], [2, 2], [1, 1, 3, 4]]
		results = [6, 4, 3]
		for i, c in enumerate(cases):
			with self.subTest(case=c):
				self.assertEqual(ConquestCampaign(3, 4, len(c), c), results[i])

if __name__ == "__main__":
	unittest.main()