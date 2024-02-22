x, y, *z = "apple", "banana", "straberry", "orange"
print(x, y, z)

x, y, *z = ["apple", "banana", "straberry", "orange"]
print(x, y, z)

x, y, *z = ("apple", "banana", "straberry", "orange")
print(x, y, z)

lista = ["apple", "banana", "straberry", "orange"]
tupla = ("apple", "banana", "straberry", "orange")

print(lista[3])
print(tupla[3])

print(lista)
print(lista[2:])
print(lista[1:3])

print(lista[-1:])
print(lista[-2:])

l = [1, 2, 3, 4, 5, "sei" "sette", 8, [9, 10, 11], "dodici"]
for v in l:
    print(v)
print("fine")

for v in tupla:
    print(v)

for v in "Ciao come stai":
    print(v)


for i in range(10):
    print(i)

for i in range(4, 20, 3):
    print(i)

# Stampare la tabellina del 13
for i in range(13, 131, 13):
    print(i, end=" ")
print()

# a = range(100)
# print(a)

print(len("C i a o"))
print(len(tupla))
print(len([1, 2, 3, 4, 5, "a         ", 6, 5, 4, 3, 2, 1]))
a = [1]
a.append(2)
print(a)

a = "aaa"
b = "bbb"
c = a + b

a = [11, 22]

a.append(10)
print(a)

a.sort()
print(a)

print(a)
a.append(1000)
a.pop()
print(a)

# In una stanza entrano, uno dopo l'altro, 10 persone, rispettivamente:
# antonio, marco, andrea, luigi, tony, bruno, laura, anita, annarita, lucia
# le prime due vanno via dopo un pochino di tempo ma entrano altre tre persone
# john, alice, mary
# altre due vanno via, sempre in ordine di ingresso (primo entrato, primo a uscire)
# stampare l'elenco delle persone presenti

lista=["antonio", "marco", "andrea", "luigi", "tony", "bruno", "laura", "anita", "annarita", "lucia"]
print(lista)
lista.pop(0)
lista.pop(0)
lista.append("john")
lista.append("alice")
lista.append("mary")
print(lista)
lista.pop(0)
lista.pop(0)
lista.sort()
print(lista)
