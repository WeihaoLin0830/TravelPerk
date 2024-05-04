import pandas as pd

# Replace 'path_to_csv_file' with the actual path to your CSV file
file_path = 'C:/Users/weiha/Documents/UPC/Programación/hackupc/hackupc-travelperk-dataset.csv'

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(file_path)

df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})

# Añadimos el DataFrame df2 al final de df1
df1 = df1.append(df2, ignore_index=True)

print(df1)
