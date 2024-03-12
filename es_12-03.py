'''var=10
nome=0
numero= "Altro"

ottimo=[1,2,3,4,5]
esempio=("uno",nome,var,ottimo)
print(esempio)
nome="nome propexit(-1) exit(-1) ARIAMENTE A QUANTO SI PUO PENSARE USCIRA NEL PRINT LA LISTA [1,2,3,4,] POICHE ANCHE SE ABBIAMO ASSEGNATO UNALTRO VALORE AD "a"
           #NON ABBIAMO ANCORA INIZZIALIZZATO NUOVAMENTE LA VARIABILE B E PERCIÒ IL PC STAMPERÀ QUELLA PRECEDENTE 
b=a
a=100
print(b)

a=10
b=20
c=30
if a % 2==0:   #si puo anche scrivere if a & 1==0 per dichiarare: IF A È PARO QUINDI "A" MODULO(%)DI 2 
    print(b+c)
else:
    print(b-c)


a=13
b=7
c=2
if a % 2==0:   
    print(b+c)
else:
    print(b-c)


a=int(input())
b=int(input())
c=int(input())
if a % 2==0:   
    print(b+c)
else:
    print(b-c)
    #come pèosso evitare di copiare di continuo?
    #sempre lo stesso pezzo di codice?
    #con le funzioni!
    def Arit(a,b,c):
        if a%2==0:  
            print(b+c)
        else: 
            print(b-c)

Arit(10,11,12)
Arit(11,2,3)
Arit(101,1000,2)
a,b,c=10,20,30
Arit(b,c,a)



def cambia (a,b):
    a=print(a)


a=100
b=200
cambia(a,b)
print(a)print(Maggiore())



def Somma (a,b):
    c=a+b
    return c
print(Somma(1,2))
print(Somma("a","b"))
a,b,c=1,2,3
def Divisione(a,b):
    return a//b,a%b
h,i=a//b,a%b
###############


import random

def ColoreCasuale():
    a=["rosso","verde","giallo","blu","arancio","ciano"]
    return a [random.randint(0, len(a)-1)]#con return torno alla stringa precedente e attraverso la funzione random randint assegno un numero casuale da 0 alla lunghezza della lista in questa caso "a"che contiene 8 elementi


print(ColoreCasuale())
print(ColoreCasuale())
print(ColoreCasuale())
print(ColoreCasuale())



#CERCA IL PIU GRANDE ELEMENTO DI UNA LISTA:
def Maggiore(lista):
    if len(lista)==0:
        return None
    else:
        magg=lista[0]
        for i in lista[1:]:
            if magg<i:
                magg=i
        return magg
print(Maggiore([3,67,5,34,10,32,100,456]))'''


def GeneralListaDigit():
    lista=[]
    for i in range(0,10000):
        s=str(i)
        while len(s)<4:
            s="0"+s
        lista.append(s)
    return lista
print(GeneralListaDigit())



def StringDigitsToList(sd):
    lista=[]
    for c in sd:
        c=int
        lista.append(c)
        print(StringDigitsToList("19834"))
        































