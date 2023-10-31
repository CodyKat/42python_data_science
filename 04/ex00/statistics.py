def ft_statistics(*args: any, **kwargs: any) -> None:
    def calculate_mean() -> int:
        sum = 0
        for i in args:
            sum += i
        return sum / len(args)

    def calculate_median() -> int | float:
        sorted_values = sorted(args)
        return sorted_values[len(sorted_values) // 2]

    def calculate_quartile() -> list:
        sorted_values = sorted(args)
        quartile = []
        quartile.append(sorted_values[len(sorted_values) // 4])
        quartile.append(sorted_values[int(len(sorted_values) * (3/4))])
        return quartile

    def calculate_var() -> int | float:
        mean = calculate_mean()
        diff_square = [(i - mean) ** 2 for i in args]
        diff_square_sum = 0
        for i in diff_square:
            diff_square_sum += i
        return diff_square_sum / len(diff_square)

    def calculate_std() -> int | float:
        var = calculate_var()
        std = var ** (1 / 2)
        return std

    for key, value in kwargs.items():
        if (len(args) == 0):
            print('ERROR')
            continue
        match (value):
            case ('mean'):
                print('mean : ', calculate_mean())
            case ('median'):
                print('median : ', calculate_median())
            case ('quartile'):
                print('quartile : ', calculate_quartile())
            case ('var'):
                print('var : ', calculate_var())
            case ('std'):
                print('std : ', calculate_std())
