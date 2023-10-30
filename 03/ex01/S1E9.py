from abc import ABC, abstractmethod

class Character(ABC):
	"""Character can die"""
	@abstractmethod
	def die(self):
		pass


class Stark(Character):
	"""Stark is derived from Character"""
	def __init__(self, first_name=None, is_alive=True):
		"""constructor of Stark"""
		self.first_name = first_name
		self.is_alive = is_alive

	def die(self):
		"""make me die"""
		self.is_alive = False