picas = ["Picas",]
diamantes = ["Diamantes"]
corazones = ["Corazones"] 
treboles = ["Treboles"]
def deck(i): 
    limiss= 

    while 0 < i <=10:
        picas.append(i)
        i = i+1            
    while 10 < i <= 20:
        corazones.append(i)
        i=i+1
    while 20 < i <= 30:
        diamantes.append(i)
        i=i+1
    while 30 < i <= 40:
        treboles.append(i)
        i=i+1
        
deck(i=1)
print(picas, diamantes, corazones, treboles)



def algo(i,limi, lims, lista):
    while limi < i < lims:
        lista.append(i)

