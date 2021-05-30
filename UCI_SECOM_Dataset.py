### Running pandas from a .py file ###

# import dependencies
import pandas as pd

# read the csv into a df
df = pd.read_csv('resources/data/UCI_SECOM_Dataset/uci-secom.csv')

# display the df
print(df)