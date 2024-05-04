import pandas as pd
import random

# Replace 'path_to_csv_file' with the actual path to your CSV file
file_path = 'C:/Users/weiha/Documents/UPC/Programación/hackupc/hackupc-travelperk-dataset-extended.csv'

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
    
"""llista = [43, 140, 177, 245, 279, 408, 442, 488, 510, 515, 630, 665, 685, 828, 987, 43, 111, 132, 133, 140, 177, 279, 360, 442, 510, 515, 622, 630, 685, 768, 807, 987, 43, 111, 132, 177, 245, 279, 360, 442, 510, 622, 665, 685, 768, 828, 43, 140, 160, 177, 279, 408, 442, 488, 515, 630, 685, 768, 807, 987, 132, 133, 140, 160, 360, 442, 488, 510, 515, 630, 685, 768, 807, 111, 132, 133, 140, 160, 245, 408, 442, 488, 510, 622, 630, 665, 685, 768, 807, 828, 987]

no_reps = len(set(llista))

print(no_reps)"""
"""
for i in range(len(df)):
    if df.iloc[i,4] == df.iloc[i,5]:
        print(i)
        print(df.iloc[i,4])
        print(df.iloc[i,5])
        df.drop(i)
    df.to_csv(file_path, index=False)
"""  