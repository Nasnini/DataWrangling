import pandas as pd

df = pd.read_csv("personality_scores.csv" , sep=";")
df.head(5)

# 1. 
#Checking any duplications in ID
def check_dup_in_id(ID):
    boolean = not df["ID"].is_unique
    boolean = df['ID'].duplicated().any() 
print(boolean)

# First store boolean array, check then remove
duplicate_in_id = df.duplicated(subset=['ID'])
if duplicate_in_id.any():
    print(df.loc[~duplicate_in_id], end = '\n\n')
    

# Use drop_duplicates method
df.drop_duplicates(subset=['id'], inplace=True)
print(df)


#1 Merge department into personality score dataframe
frames = [new_df1, new_df2]
concat_frames = pd.concat(frames)

new_df1 = pd.read_csv("personality_scores.csv" , sep=";")
new_df2 = pd.read_csv("departments.csv" , sep=";")

new_df1.head(5)
new_df2.head(5)

#Checking the length of both dataframes
new_df1.shape #1555row 70col
new_df2. #1555row 2col

# Now assert that the 1555row length are still consistant




# Reading certain indexes - predefined functions
# print(df.head(3))
# print(df.tail())

# Read the headers on the file
    #df.columns

# read each column
    #print(df['Name_of column'][0:5])

# Read a specific location
    #