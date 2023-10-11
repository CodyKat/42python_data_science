import pandas as pd

def load(path: str):
    try:
        if not isinstance(path, str):
            raise AssertionError('path must be a string')
        if path.split('.')[-1] != 'csv':
            raise AssertionError('path must be a csv file')
        csv_file = pd.read_csv(path, sep=',')
    except FileNotFoundError:
        print('Error: file not found')
        return None
    except AssertionError as e:
        print(e)
        return None
    print('Loading dataset of dimensions', csv_file.shape)
    return csv_file
