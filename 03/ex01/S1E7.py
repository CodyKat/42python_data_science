from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""

    def __init__(self, first_name=None, is_alive=True):
        """constructor of Stark"""
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = 'Baratheon'
        self.eyes = 'brown'
        self.hairs = 'dark'

    def __str__(self) -> str:
        """this function return string when use str(Baratheon)"""
        return 'Baratheon'

    def __repr__(self) -> str:
        """detail information in class"""
        return "Vector: ('{}', '{}', '{}')"\
            .format(self.family_name, self.eyes, self.hairs)

    @staticmethod
    def create_baratheon(first_name, is_alive):
        """make new Baratheon object"""
        new_baratheon = Baratheon(first_name, is_alive)
        return new_baratheon

    def die(self):
        """make me die"""
        self.is_alive = False


class Lannister(Character):
    """Representing the Baratheon family."""

    def __init__(self, first_name=None, is_alive=True):
        """constructor of Stark"""
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = 'Lannister'
        self.eyes = 'brown'
        self.hairs = 'dark'

    def __str__(self) -> str:
        """this function return string when use str(Lannister)"""
        return 'Lannister'

    def __repr__(self) -> str:
        """detail information in class"""
        return 'Vector: ({}, {}, {})'\
            .format(self.family_name, self.eyes, self.hairs)

    @staticmethod
    def create_lannister(first_name, is_alive):
        """make new Lannister object"""
        new_lannister = Lannister(first_name, is_alive)
        return new_lannister

    def die(self):
        """make me die"""
        self.is_alive = False
