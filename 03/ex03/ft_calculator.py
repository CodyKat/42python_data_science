class calculator:
    def __init__(self, input_subject : list):
        self.subject = input_subject


    def __add__(self, object) -> None:
        for i in range(len(self.subject)):
            self.subject[i] += object
        print(self.subject)


    def __mul__(self, object) -> None:
        for i in range(len(self.subject)):
            self.subject[i] *= object
        print(self.subject)


    def __sub__(self, object) -> None:
        for i in range(len(self.subject)):
            self.subject[i] -= object
        print(self.subject)


    def __truediv__(self, object) -> None:
        for i in range(len(self.subject)):
            try:
                self.subject[i] /= object
            except ZeroDivisionError:
                print('You try to divide with zero!!')
        print(self.subject)