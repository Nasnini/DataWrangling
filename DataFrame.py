import pandas as pd

df = pd.read_csv('personality_scores.csv')

print(df)

# Reading certain indexes - predefined functions
# print(df.head(3))
# print(df.tail())

# Read the headers on the file
    #df.columns

# read each column
    #print(df['Name_of column'][0:5])

# Read a specific location
    #