class calculator:
#your code here
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        product = 0
        for i, j in zip(V1, V2):
            product += i * j
        print('Dot product is: {}'.format(product))

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        for i in range(len(V1)):
            V1[i] += V2[i]
        print('Add Vector is : {}'.format(V1))

    @staticmethod        
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        for i in range(len(V1)):
            V1[i] -= V2[i]
        print('Sous Vector is: {}'.format(V1))
