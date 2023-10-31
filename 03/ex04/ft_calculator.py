class calculator:
    """static vector calculator"""
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """dotproduct with two Vectors"""
        product = 0
        for i, j in zip(V1, V2):
            product += i * j
        print('Dot product is: {}'.format(product))

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """add two Vectors"""
        result = []
        for i in range(len(V1)):
            result.append(V1[i] + V2[i])
        print('Add Vector is : {}'.format(result))

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """sub two Vectors"""
        result = []
        for i in range(len(V1)):
            result.append(V1[i] - V2[i])
        print('Sous Vector is: {}'.format(result))
