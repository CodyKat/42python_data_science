def give_bmi(height: list[int | float], weight: list[int | float])\
      -> list[int | float]:
    """calculate bmi"""

    assert len(height) == len(weight), \
        'sizeof height and sizeof weight is different'

    if all(isinstance(h, (int, float)) and isinstance(w, (int, float))
           for h, w in zip(height, weight)):
        bmi = [w / (h**2) for w, h in zip(weight, height)]
    else:
        raise ValueError('height and weight must be int or float')
    return bmi


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """check that bmi is over the limit"""
    if not all(isinstance(value, (int, float)) for value in bmi) \
            or not isinstance(limit, (int, float)):
        raise ValueError('Invalid Value. bmi must be int or float')
    output = [value > limit for value in bmi]
    return output
