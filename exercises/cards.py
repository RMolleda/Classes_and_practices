picas = ["Picas",]
diamantes = ["Diamantes"]
corazones = ["Corazones"] 
treboles = ["Treboles"]
def deck(i): 

    while 0 < i <=10:
        picas.append(i)
        diamantes.append(i)
        corazones.append(i)
        treboles.append(i)
        i = i+1  
    return picas, diamantes, corazones, treboles          
    
print(deck(i=1))




def algo(i,limi, lims, lista):
    while limi < i < lims:
        lista.append(i)

