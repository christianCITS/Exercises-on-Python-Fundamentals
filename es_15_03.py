#Leggere da input una stringa, se minore di "lettera", stampare la stringa "minore", se maggiore di "lettera" e minore di 
#"tocco", stampare "intermedia", se maggiore di "tocco" e minore di "what" stampare "maggiore", altrimenti stampare "massima"

a=input(str("inserire stringa: "))
if a<"lettera":
    print("minore")
elif a>"lettera" and a<"tocco":
    print("intermedia")
elif a>"tocco"  and a<"what":
    print("maggiore")
else:print("massima")