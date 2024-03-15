#Leggere da un file (persone.txt) i nomi, cognomi e eta di un gruppo di persone. organizzarli in un dizionario la cui chiave 
#è il cognome e il cui valore è una t-upla contenente i tre valori letti.
fin=open("persone.csv", "r")
rig=fin.readlines()
fin.close()
l=[]
for i in rig:
    l=i.strip().split(",")
    
print("nome: " ,l[0] , "cognome: " ,l[1], "età: " ,l[2] )

dizionario=dict()
for v in rig:
    persona=v.strip().split(",")
    dizionario[persona[1]]=(persona[0],persona[1], persona[2])
    print (dizionario)
for e in dizionario:
    print("Key: ", e, "Value: ",dizionario[e])









    


































#Leggere da input una stringa, se minore di "lettera", stampare la stringa "minore", se maggiore di "lettera" e minore di 
#"tocco", stampare "intermedia", se maggiore di "tocco" e minore di "what" stampare "maggiore", altrimenti stampare "massima"

'''a=input(str("inserire stringa: "))
if len(a)<len("lettera"):
    print("minore")
elif len(a)>len("lettera") and len(a)<len("tocco"):
    print("intermedia")
elif len(a)>("tocco")  and len(a)<len("what"):
    print("maggiore")
else:print("massima")'''