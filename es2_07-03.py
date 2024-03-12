#comprehension
lista=[1,2,3,4,5]

lista2=[x*x for x in lista]#con questo comando prende ciascun elemento(x) della lista precedente(lista) e li eleva al quadrato (moltiplicandoli per se stesso ovvero per x)
print(lista2) 
#LA RIGA 4 POTREBBE ESSERE ANCHE SCRITTA COSI:
#lista2=[]
#for x in lista:
    #lista2.append(x*x)

lista=[2,3,4]
lista3=[y for x in lista for y in range(1,x)]
print(lista3)



lista_dispari=[x*2+1 for x in range(0,5)]#attraverso la comprension genero 5 numeri dispari casuali (x*2+1) se avessi voluto numeri pari stessa operazione ma solamente (x*2)
lista_numeri=[x for x in range (0,5)]
print(lista_numeri)
print(lista_dispari)
print(list(zip(lista_numeri,lista_dispari)))#attraverso il comando zip unisco le due liste assocciando primo elemento di una con il primo dell'altra e cosi via
 