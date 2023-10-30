from abc import ABC, abstractmethod

class Character(ABC):
	"""Character has frist_name, is_alive attribute"""
	@abstractmethod
	def __init__(self, first_name=None, is_alive=True):
		self.first_name = first_name
		self.is_alive = is_alive


class Stark(Character):
	"""Stark is derived from Character"""
	def __init__(self, first_name=None, is_alive=True):
		"""constructor of Stark"""
		super().__init__(first_name, is_alive)

	def die(self):
		"""make me die"""
		self.is_alive = False