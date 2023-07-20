import numpy as np
import pandas as pd


def load_extracted_data(filename):
    return pd.DataFrame(dict(np.load(filename, allow_pickle=True)))