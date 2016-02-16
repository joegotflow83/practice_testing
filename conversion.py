"""This is practice writing unit tests and using TDD

Author: Joseph Moran
Created: 02/16/2016

!/usr/local/env python3.5
"""
class Money:


	def __init__(self, amount, currency):
		"""Initialize variables"""
		self.amount = amount
		self.currency = currency


	def usd_to_eur(self, amount):
		"""Convert USD to EUR"""
		return round(amount * 0.9)


	def eur_to_usd(self, amount):
		"""Convert EUR to USD"""
		return round(amount * 1.12)


	def mul_convert_usd(self, amount):
		"""Convert a list of USD's to EUR"""
		# If user only lists one number, convert to list so program doesn't crash
		amount = list(amount)
		return [self.usd_to_eur(money) for money in amount]


	def mul_convert_eur(self, amount):
		"""Convert a list of EUR's to USD"""
		# If user only lists one number, convert to list so program doesn't crash
		amount = list(amount)
		return [self.eur_to_usd(money) for money in amount]


	def __add__(self, other):
		"""Override add func to add classes"""
		if self.currency == "EUR":
			self.amount = self.eur_to_usd(self.amount)
			return ((self.amount + other.amount), "USD")
		elif other.currency == "EUR":
			other.amount = other.eur_to_usd(other.amount)
			return ((self.amount + other.amount), "USD")

