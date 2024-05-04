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

        if max(start1, start2) <= min(end1, end2):
            if sortida1==sortida2 or sortida1==desti2 or desti1==desti2 or desti1==sortida2:

                if desti1 != desti2 and sortida1 != sortida2:
                    if (sortida1 > sortida2 and end1 > end2) or (sortida1 < sortida2 and end1 < end2):
                        return False

                else:
                    return True
    
    llista = []

    for i in range(1,len(df)+1):
        if i != trip_id:
            if coincidencia(i):
                llista.append(df.iloc[i-1,0])

    return llista