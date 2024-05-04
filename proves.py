import pandas as pd
import random

# Replace 'path_to_csv_file' with the actual path to your CSV file
file_path = 'C:/Users/weiha/Documents/UPC/Programación/hackupc/hackupc-travelperk-dataset.csv'

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(file_path)

llista_de_gustos = ["Cultura","Aire lliure","Història","Compres","Ciència","Familiar","Relax","Festa"]

#holacaracola
"""for i in range(len(df)):
    likes = []
    for nombre_de_gustos in range(len(llista_de_gustos)):
        gust_rand = random.choice(llista_de_gustos)
        if gust_rand not in likes:
            likes.append(gust_rand)
    df.iloc[i,6] = str(likes)
    df.to_csv(file_path, index=False)"""

"""for i in range(len(df)):
    presupost = random.choice(range(0,250))
    df.iloc[i,7] = presupost
    df.to_csv(file_path, index=False)"""

print(df.iloc[1,7])