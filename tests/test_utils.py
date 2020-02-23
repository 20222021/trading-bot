import unittest

from trade.signal_generation import *


class UtilsTestCase(unittest.TestCase):

	def setUp(self):
		pass

	def test_signal_generation(self):
		data = [
			(222, 1, 2),
			(333, 2, 1),
			(444, 0, 1),
		]
		df = pd.DataFrame(data, columns=["aaa", "high_60_20", "low_60_04"])

		models = {
			"buy": {"high_60_20": 1, "low_60_04": 1},  # All higher
			"sell": {"high_60_20": 1, "low_60_04": 1},  # All lower
		}

		signals = generate_signals(df, models)

		# Check existence
		self.assertTrue("buy" in df.columns.to_list())
		self.assertTrue("sell" in df.columns.to_list())

		# Check values of signal columns
		self.assertListEqual([1,1,0], list(df["buy"]))
		self.assertListEqual([0,0,1], list(df["sell"]))


if __name__ == '__main__':
	unittest.main()