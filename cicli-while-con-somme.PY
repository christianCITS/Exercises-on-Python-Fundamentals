virgola=False
prob=","
numero=""
while True:
    c = input("Digita 0-9,+-/=: ")
    if len(c)>0:
        c=c[0]
    if len(c)==0:
        continue
     # dovete leggere un numero sia intero, sia decimale
     # e stamparlo nella sua interezza quando viene
     # digitato un simbolo non numerico (+-/=)
    
     # Terminerete quando varrà la
    if c not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ","]:
        # Stampate il numero letto
        print("il numero è: ",numero)
        break
    elif prob==c and virgola==False :
        numero=numero+c
        virgola=True
    elif prob==c and virgola:
        continue
    else: 
        numero=numero+c
        
    
        



