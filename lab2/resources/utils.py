import pickle
from pathlib import Path

this_folder = Path(__file__).parent

with open(this_folder/'data.pickle','rb') as f:
    DI, DImany, DII = pickle.load(f)

def draw_dataset_from_exponential():
    return DI

def draw_300datasets_from_exponential():
    return DImany

def draw_dataset_from_gaussian():
    return DII
