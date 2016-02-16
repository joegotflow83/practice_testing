import unittest

from conversion import Money


class ConversionTest(unittest.TestCase):


	def setUp(self):
		"""Set up testing env"""
		self.conversion = Money([20, 75, 650, 12000])


	def tearDown(self):
		"""Tear down testing env"""
		self.conversion = None


	def test_conversion_of_USD_to_EUR(self):
		"""Test that dollars are converted into euros"""
		self.assertEquals(self.conversion.usd_to_eur(20), 18)
		self.assertEquals(self.conversion.usd_to_eur(75), 68)
		self.assertEquals(self.conversion.usd_to_eur(650), 585)
		self.assertEquals(self.conversion.usd_to_eur(12000), 10800)


	def test_error_occurs_if_not_int_USD(self):
		"""Test that an error occurs if arg not int"""
		with self.assertRaises(TypeError):
			self.conversion.usd_to_eur(("20", [1,2,3], {'joe': 'isawesome'}))


	def test_conversion_of_EUR_to_USD(self):
		"""Test that euros are converted to dollars"""
		self.assertEquals(self.conversion.eur_to_usd(9), 10)
		self.assertEquals(self.conversion.eur_to_usd(78), 87)
		self.assertEquals(self.conversion.eur_to_usd(423), 474)
		self.assertEquals(self.conversion.eur_to_usd(10000), 11200)


	def test_error_occurs_if_not_int_for_EUR(self):
		"""Test that an error occurs if arg not int"""
		with self.assertRaises(TypeError):
			self.conversion.eur_to_usd(("20", [1,2,3], {'joe': 'likestests'}))


	def test_list_of_numbers_are_converted_to_USD(self):
		"""Test that a list of numbers can be converted to USD"""
		self.assertEquals(self.conversion.mul_convert_usd([34, 5, 124]), [31, 4, 112])


	def test_error_occurs_if_not_list_for_USD(self):
		"""Test that an error occurs if arg not list"""
		with self.assertRaises(TypeError):
			self.conversion.mul_convert_usd((1, "350", {'doesnt': 'work'}))


	def test_list_of_numbers_are_converted_to_EUR(self):
		"""Test that a list of numbers can be converted to EUR"""
		self.assertEquals(self.conversion.mul_convert_eur([47, 12, 111]), [53, 13, 124])


	def test_error_occurs_if_not_list_for_EUR(self):
		"""Test that an error occurs if arg not list"""
		with self.assertRaises(TypeError):
			self.conversion.mul_convert_eur((90, "4", {'need': 'morecoverage'}))