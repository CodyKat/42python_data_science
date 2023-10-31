from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """king from Baratheon, Lannister"""

    def __init__(self, first_name=None, is_alive=True):
        """constructor of Stark"""
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = Baratheon.family_name
        self.eyes = Baratheon.eyes
        self.hairs = Baratheon.hairs

    def set_eyes(self, eyes_color):
        """set eyes color"""
        self.eyes = eyes_color

    def set_hairs(self, hairs_color):
        """set hairs color"""
        self.hairs = hairs_color

    def get_eyes(self) -> str:
        """get eyes color"""
        return self.eyes

    def get_hairs(self) -> str:
        """get hairs color"""
        return self.hairs
