import pandas as pd
from datetime import datetime
from flask import Flask, request
import cgitb

cgitb.enable()
print("Content-type: text/html\n\n")
import sys
sys.path.append('/mnt/web305/c1/31/53991431/htdocs/.local/lib/python3.8/site-packages')


app = Flask(__name__)

# Replace 'path_to_csv_file' with the actual path to your CSV file
file_path = './hackupc-travelperk-dataset-extended.csv'

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(file_path)

# Display the DataFrame
def afegir():
    global df
    traveller_name = input("Nom: ")
    departure_date = input("Dia de sortida (dd/mm/yyyy): ")
    return_date = input("Dia de tornada(dd/mm/yyyy): ")
    departure_city = input("Ciutat de partida: ")
    arrival_city = input("Ciutat que viatge: ")
    likes = [like.strip() for like in input("Gustos (separats amb coma): ").split(',')]
    budget = input("El presupost que disposa: ")
    new_row = {'Trip ID': len(df)+1, 'Traveller Name': traveller_name, 'Departure Date': departure_date, 'Return Date': return_date, 'Departure City': departure_city, 'Arrival City': arrival_city, 'Likes': likes, 'Budget': budget}
    df = df._append(new_row, ignore_index=True)
    df.to_csv(file_path, index=False)


def overlap_fecha(trip_id):

    overlap_list = []
    total_overlap_list = []

    def coincide(other):

        # -1 is because the index to search the names and id doesn't match

        start1 = df.iloc[trip_id-1,2]
        end1 = df.iloc[trip_id-1,3]

        start2 = df.iloc[other-1,2]
        end2 = df.iloc[other-1,3]
        
        # Convert string dates to datetime objects if inputs are strings
        if isinstance(start1, str):
            start1 = datetime.strptime(start1, "%d/%m/%Y")
        if isinstance(end1, str):
            end1 = datetime.strptime(end1, "%d/%m/%Y")
        if isinstance(start2, str):
            start2 = datetime.strptime(start2, "%d/%m/%Y")
        if isinstance(end2, str):
            end2 = datetime.strptime(end2, "%d/%m/%Y")

        # Check if the two ranges overlap
        return max(start1, start2) <= min(end1, end2), start1 == start2 and end1 == end2
    
    for i in range(1,len(df)+1):
        if i != trip_id:
            parcial, total = coincide(i)

            if total:
                total_overlap_list.append(df.iloc[i-1,0])

            elif parcial:
                overlap_list.append(df.iloc[i-1,0])
            
                
    return overlap_list, total_overlap_list


def overlap_places(trip_id):

    overlap_list = []
    total_overlap_list =  []
    llista_fechas = overlap_fecha(trip_id)
    llista_p, llista_t = llista_fechas
    

    def coincide(other):

        start1 = df.iloc[trip_id-1,4]
        end1 = df.iloc[trip_id-1,5]

        start2 = df.iloc[other-1,4]
        end2 = df.iloc[other-1,5]

        return start1 == start2 or start1 == end2 or end1 == start2 or end1 == end2, start1 == start2 or end1 == end2 #balgase la redundancia por vaga


    for i in llista_t:
        if i != trip_id:
            parcial, total = coincide(i)

            if total:
                total_overlap_list.append(df.iloc[i-1,0])

    for n in llista_p:
        if n != trip_id:
            parcial, total = coincide(n)

            if parcial:
                overlap_list.append(df.iloc[n-1,0])
                
    return overlap_list + total_overlap_list
    
    
def gustos(trip_id):
    coin = {}
    llista = overlap_places(trip_id)
    
    for gustos in eval(df.iloc[trip_id-1,6]):
        for j in llista:
            
            numero_conincidencias = 0
            
            if gustos in eval(df.iloc[j-1,6]):
                for i in range(len(eval(df.iloc[trip_id-1,6]))):
                    for k in range(len(eval(df.iloc[j-1,6]))):
                        if eval(df.iloc[trip_id-1,6])[i] == eval(df.iloc[j-1,6])[k]:
                            numero_conincidencias += 1
                
                coin[j] = numero_conincidencias
    
    sort_coin = dict(sorted(coin.items(), key=lambda x: x[1], reverse=True))
    
    return sort_coin


def presupost(trip_id):
    presu = {key: [df.iloc[key-1,1],value, df.iloc[key-1,7]] for key, value in gustos(trip_id).items()}
    sorted_presu = dict(sorted(presu.items(), key=lambda item: (item[1][1], -abs(item[1][2] - df.iloc[trip_id-1,7])), reverse=True))
    return sorted_presu


def dies_coin(trip_id):
    
    ids_coins = overlap_places(trip_id)
    llista_dies_coins = []
    
    for ids in ids_coins:
        
        start1 = df.iloc[trip_id-1,2]
        end1 = df.iloc[trip_id-1,3]

        start2 = df.iloc[ids-1,2]
        end2 = df.iloc[ids-1,3]
        
        # Convert string dates to datetime objects if inputs are strings
        if isinstance(start1, str):
            start1 = datetime.strptime(start1, "%d/%m/%Y")
        if isinstance(end1, str):
            end1 = datetime.strptime(end1, "%d/%m/%Y")
        if isinstance(start2, str):
            start2 = datetime.strptime(start2, "%d/%m/%Y")
        if isinstance(end2, str):
            end2 = datetime.strptime(end2, "%d/%m/%Y")
        
        if start1 >= start2:
            if end1 <= end2:
                llista_dies_coins.append([df.iloc[ids-1,1], start1.strftime("%d/%m/%Y"), end1.strftime("%d/%m/%Y")])
            
            elif end1 > end2:
                llista_dies_coins.append([df.iloc[ids-1,1], start1.strftime("%d/%m/%Y"), end2.strftime("%d/%m/%Y")])
            
            
        elif start1 < start2:
            if end1 <= end2:
                llista_dies_coins.append([df.iloc[ids-1,1], start2.strftime("%d/%m/%Y"), end1.strftime("%d/%m/%Y")])
            
            elif end1 > end2:
                llista_dies_coins.append([df.iloc[ids-1,1], start2.strftime("%d/%m/%Y"), end2.strftime("%d/%m/%Y")])
                
    return llista_dies_coins
        
print(dies_coin(1))

"""@app.route('/compatible', methods=['GET'])
def newgroup():

    id = request.args.get("id")
    print(int(id))
    print(str(df.iloc[int(id)-1]))
    print(str(presupost(int(id))))

    return str(presupost(int(id)))


if __name__ == "__main__":
    app.run()
"""