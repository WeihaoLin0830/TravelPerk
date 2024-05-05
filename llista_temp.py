def llista_coincidencies(trip_id):

    start1 = df.iloc[trip_id-1,2]
    end1 = df.iloc[trip_id-1,3]

    sortida1 = df.iloc[trip_id-1,4]
    desti1 = df.iloc[trip_id-1,5]

    def coincidencia(other):
        start2 = df.iloc[other-1,2]
        end2 = df.iloc[other-1,3]

        sortida2 = df.iloc[other-1,4]
        desti2 = df.iloc[other-1,5]

        if sortida1 == sortida2:
            return False, [], [] 
        else:
            if max(start1, start2) <= min(end1, end2):
                if desti1==desti2:
                    return True, [max(start1, start2),min(end1, end2)],True ##
                else:
                    if desti1==sortida2:
                        if start1 < start2 or end1 > end2:
                            return True, [max(start1, start2),min(end1, end2)], True ##
                        else:
                            return False, [], []

                    elif desti2==sortida1:
                        if start1 > start2 or end1 < end2:
                            return True, [max(start1, start2),min(end1, end2)],False
                        else:
                            return False, [], []
                           
                    else:
                        return False, [], []
                    
            else:
                if sortida1==desti2:
                    return True, [start2, end2], False
                
                elif desti1==sortida2:
                    return True, [start1,end1], True ##
                
                else:
                    return False, [], []  
    
    llista = []
    llista_data = {}
    si_local = {}

    for i in range(1,len(df)+1):
        if i != trip_id:

            indicador, data, local = coincidencia(i)

            if indicador:
                llista.append(df.iloc[i-1,0])
                llista_data[i-1]=data
                si_local[i-1]= local


    return llista, llista_data, si_local

def gustos(trip_id):
    coin = {}
    llista, llista_data, si_local = llista_coincidencies(trip_id)
    
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
    
    return sort_coin, llista_data, si_local


def coincidencias_orden(trip_id, local):

    if local:
        llista, llista_data, si_local = gustos(trip_id)

        presu = {key: [df.iloc[key-1,1],value, df.iloc[key-1,7], llista_data[key-1],si_local[key-1]] for key, value, in llista.items()}
        sorted_presu = dict(sorted(presu.items(), key=lambda item: (item[1][4], item[1][1], abs(item[1][2] - df.iloc[trip_id-1,7])),reverse=True)) 

    else:

        llista, llista_data, si_local = gustos(trip_id)

        presu = {key: [df.iloc[key-1,1],value, df.iloc[key-1,7], llista_data[key-1]] for key, value, in llista.items()}
        sorted_presu = dict(sorted(presu.items(), key=lambda item: (item[1][1], -abs(item[1][2] - df.iloc[trip_id-1,7])), reverse=True))

    return sorted_presu
