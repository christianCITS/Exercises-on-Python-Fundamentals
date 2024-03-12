import random
import time

start=time.time_ns()
lista=[]
for v in range(1,10000000):
    lista.append(random.randint(1,1000000000))
end=time.time_ns()

print(f"il tempo richiesto è: {(end-start)/1000000000}")




#ricerca nella lista
start=time.time_ns()
trovati=0
for v in range(1,10000000):
    if random.randint(1,1000000000)in lista:
        trovati+= 1
end=time.time_ns()

print(f"il tempo richiesto è: {(end-start)/1000000000} e ne ha trovati: {trovati}")



#########################################################################################
#costruzione del set
start=time.time_ns()
aSet=set()
for v in range(1,10000000):
    aSet.add(random.randint(1,1000000000))
end=time.time_ns()

print(f"il tempo richiesto è: {(end-start)/1000000000}")




#ricerca nel SET
start=time.time_ns()
trovati=0
for v in range(1,10000000):
    if random.randint(1,1000000000)in aSet:
        trovati+= 1
end=time.time_ns()

print(f"il tempo richiesto è: {(end-start)/1000000000} e ne ha trovati: {trovati}")


###################################################################################################
print(hash("Mario")%17)#GENERO L'HASH DELLA STRINGA MARIO E FACCIO IL MODULO(%) IN QUESTO CASO 17 POICHE VOGLIAMO CHE IL RISULTATO
                       # ENTRI IN UN VETTORE DI 16 ELEMENTI
print(hash("Rossi")%17)
print(hash("Verdi")%17)
print(hash("Bianchi")%17)
print(hash("Neri")%17)
print(hash("Bianchini")%17)