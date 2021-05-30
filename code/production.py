# import dependencies
import pandas as pd
import zipfile as zf

# # read the zip file as a pandas df
# zip_file = zf.ZipFile('../resources/data/Production_Quality_Prediction/data_X.zip') 
# df_X = pd.read_csv(zip_file.open('data_X.csv'))
# # display df_X
# print(df_X)

# import csv file as a df
df_Y = pd.read_csv('../resources/data/Production_Quality_Prediction/data_Y.csv')
# display # display df_Y
print(df_Y)
