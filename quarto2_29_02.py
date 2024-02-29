import random
#sapendo che la funzione random.randint(|start| |end| esempio 1,10)
#genera un numento intero compreso tra start e end, end compreso
#costruire una lista di numeri casuali lunga 100 e stampare a schermo la somma di tutti i suoi numeri

l=[]
for c in range(100):#vuoldire che tutto quello che ce all'interno del for sarà ripetuto in questo caso per 100 volte
    l.append(random.randint(1,10))
print(l)
totale=0
for c in l:
        totale=totale+c
print("totale: ",totale)
    
#costruire due liste la prima che contiene i numeri pari fino a 1000
#la sec che contiene i numeri dispari fino a 1000
#a partire dalle prime due liste costruire una terza lista che contenga tutti i pari e i dispari delle due liste precedenti

l1=[]
l2=[]
for i in range(0,501):
      
      l1.append(i*2)
      l2.append(i*2+1)
      print(l1)
      print(l2)
      
