def give_bmi(height: list[int | float], weight: list[int | float])\
      -> list[int | float]:
    """calculate bmi"""
    for value in height:
        if not isinstance(value, (int, float)):
            raise ValueError('Invalid Value... height must be int or float')
    for value in weight:
        if not isinstance(value, (int, float)):
            raise ValueError('Invalid Value... weight must be int or float')
    assert len(height) == len(weight), \
        'sizeof height and sizeof weight is different'

    bmi = []
    for i in range(len(height)):
        bmi.append(weight[i] / (height[i]**2))
    return bmi


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """check that bmi is over the limit"""
    for value in bmi:
        if not isinstance(value, (int, float)):
            raise ValueError('Invalid Value... bmi must be int or float')
    output = []
    for value in bmi:
        if value < limit:
            output.append(True)
        else:
            output.append(False)
    return output
