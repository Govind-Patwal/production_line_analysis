### Running pandas from a .py file ###

# importing dependencies
import pandas as pd

# reading the csv into a df
df = pd.read_csv('resources/data/UCI_SECOM_Dataset/uci-secom.csv')

# displaying the df
print(df)