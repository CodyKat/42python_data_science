from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""
    family_name = 'Baratheon'
    eyes = 'brown'
    hairs = 'dark'

    def __init__(self, first_name=None, is_alive=True):
        """constructor of Stark"""
        self.first_name = first_name
        self.is_alive = is_alive

    def __str__(self) -> str:
        return 'Baratheon'

    def __repr__(self) -> str:
        return "Vector: ('{}', '{}', '{}')"\
            .format(self.family_name, self.eyes, self.hairs)

    @classmethod
    def create_baratheon(cls, first_name, is_alive):
        new_baratheon = Baratheon(first_name, is_alive)
        return new_baratheon

    def die(self):
        """make me die"""
        self.is_alive = False


class Lannister(Character):
    """Representing the Baratheon family."""
    family_name = 'Lannister'
    eyes = 'brown'
    hairs = 'dark'

    def __init__(self, first_name=None, is_alive=True):
        """constructor of Stark"""
        self.first_name = first_name
        self.is_alive = is_alive

    def __str__(self) -> str:
        return 'Lannister'

    def __repr__(self) -> str:
        return 'Vector: ({}, {}, {})'.format(self.family_name, self.eyes, self.hairs)

    @classmethod
    def create_lannister(cls, first_name, is_alive):
        new_lannister = Lannister(first_name, is_alive)
        return new_lannister

    def die(self):
        """make me die"""
        self.is_alive = False
