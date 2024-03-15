#Leggere da un file (persone.txt) i nomi, cognomi e eta di un gruppo di persone. organizzarli in un dizionario la cui chiave 
#è il cognome e il cui valore è una t-upla contenente i tre valori letti.
fin=open("persone.csv", "r") #APRO FILE PERSONE.CSV
rig=fin.readlines() #LEGGO TUTTO IL CONTENUTO DEL FILE E LO METTO SOTTOFORMA DI SERIE DI STRINGHE
fin.close()#CHIUDERE SUBITO DOPO AVER FATTO LE PRECEDENTI COSE ( CI SI PUO CONTINUARE A LAVORARE TRANQUILLAMENTE NON CHIUDE NULLA SUL CODICE)
l=[]#CREO LISTA VUOTA
for i in rig:
    l=i.strip().split(",")#SPLIT SERVE PER DIVIDERE APPUNTO GLI ELEMENTI ALL'INTERNO DELLA LISTA METTENDO TRA PARENTESI DELLO SPLIT OGNI DOVE CI SI VUOLE SEGMENTARE (ESEMPIO QUI LA VIRGOLA)
                          # STRIP INVECE TOGLIE TUTTI GLI SPAZI BIANCHI E I "\N" CHE SI FORMANO NEGLI SPAZI VUOTI
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