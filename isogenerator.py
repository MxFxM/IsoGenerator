import pandas as pd
import matplotlib.pyplot as plt

#
# SETTINGS AND OPTIONS
#
INPUT_FILENAME = "testfile"

input_data = pd.read_csv(f"./input_data/{INPUT_FILENAME}.csv", header=0, sep=';')
print(input_data.head())
