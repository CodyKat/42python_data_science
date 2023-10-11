from abc import ABC, abstractmethod

class Character(ABC):
	"""docstring for Character"""
	@abstractmethod


class Stark(Character):
	"""docstring for Stark"""
	def __init__(self, first_name=None, is_alive=True):
		self.first_name = first_name
		self.is_alive = is_alive

	def print_house_words(self):
		print("Winter is coming")

	def die(self):
		self.is_alive = False