import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """just slice your matrix from start to end"""
    assert isinstance(family, list), 'family must be list'
    assert isinstance(start, int), 'start index must be int'
    assert isinstance(end, int), 'end index must be int'

    print('My shap is : ', np.shape(family))
    new_shape = family[start:end]
    print('My new shape is : ', np.shape(new_shape))
    return new_shape
