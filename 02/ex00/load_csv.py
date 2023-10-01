import pandas as pd

def load(path: str):
    csv_file: any
    if path.split('.')[-1] != 'csv':
        return None
    try:
        csv_file = pd.read_csv(path, sep=',')
    except FileNotFoundError:
        return None
    print('Loading dataset of dimensions', csv_file.shape)
    return csv_file
