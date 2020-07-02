

from dq_calendar import DQCalendar as cal
import unittest

class Test(unittest.TestCase):
	
	def setUp(self):
		self.curr_date = '05/22'
		self.curr_num = 143
		self.day_one = '01/01'
		self.day_one_num = 1
		self.heb_date = 'H'
		self.heb_num = 91
		self.fion_date = 'F'
		self.fion_num = 182
		self.dai_date = 'D'
		self.dai_num = 273
		self.bayur_date = 'B'
		self.bayur_num = 364
		self.iters = 10

	def tearDown(self):
		pass

	def add_year(year, date):
		return f'{year}/{date}'

	def num_year(year, num):
		return (year)*cal.YEAR_LENGTH+num

	def test_dse_day_one_not_fest(self):
		self.assertEqual(
				cal.date_to_dse(Test.add_year(0, self.day_one)),
				self.day_one_num)

	def test_dse_day_one_reflective(self):
		for i in range(0, self.iters):
			with self.subTest(i=i):
				date = Test.add_year(i, self.day_one)
				num = Test.num_year(i, self.day_one_num)
				self.assertEqual(
						cal.date_to_dse(date),
						num)
				self.assertEqual(
						cal.dse_to_date(num),
						date)



	def test_dse_fest_heb_reflective(self):
		for i in range(0, self.iters):
			with self.subTest(i=i):
				date = Test.add_year(i, self.heb_date)
				num = Test.num_year(i, self.heb_num)
				self.assertEqual(
						cal.date_to_dse(date),
						num)
				self.assertEqual(
						cal.dse_to_date(num),
						date)



	def test_dse_fest_fion_reflective(self):
		for i in range(0, self.iters):
			with self.subTest(i=i):
				date = Test.add_year(i, self.fion_date)
				num = Test.num_year(i, self.fion_num)
				self.assertEqual(
						cal.date_to_dse(date),
						num)
				self.assertEqual(
						cal.dse_to_date(num),
						date)



	def test_dse_fest_dai_reflective(self):
		for i in range(0, self.iters):
			with self.subTest(i=i):
				date = Test.add_year(i, self.dai_date)
				num = Test.num_year(i, self.dai_num)
				self.assertEqual(
						cal.date_to_dse(date),
						num)
				self.assertEqual(
						cal.dse_to_date(num),
						date)


	def test_dse_fest_bayur_reflective(self):
		for i in range(0, self.iters):
			with self.subTest(i=i):
				date = Test.add_year(i, self.bayur_date)
				num = Test.num_year(i, self.bayur_num)
				self.assertEqual(
						cal.date_to_dse(date),
						num)
				self.assertEqual(
						cal.dse_to_date(num),
						date)


	def test_dse_convert_is_refective(self):
		for i in range(0, self.iters):
			with self.subTest(i=i):
				date = Test.add_year(i, self.curr_date)
				num = Test.num_year(i, self.curr_num)
				self.assertEqual(
						cal.date_to_dse(date),
						num)
				self.assertEqual(
						cal.dse_to_date(num),
						date)

	def test_all_for_year_reflective(self):
		for day in range(1, 31):
			for month in range(1, 13):
				with self.subTest(day=day, month=month):
					date = Test.add_year(0, f'{str(month).zfill(2)}/{str(day).zfill(2)}')
					self.assertEqual(
							cal.dse_to_date(cal.date_to_dse(date)),
							date)

	def test_nums_for_year_reflective(self):
		for i in range(1, cal.YEAR_LENGTH+1):
			with self.subTest(i = i):
				self.assertEqual(
						cal.date_to_dse(cal.dse_to_date(i)),
						i)



if __name__=='__main__':
	unittest.main()
