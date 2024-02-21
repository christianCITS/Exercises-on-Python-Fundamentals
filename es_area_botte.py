# SVOLGIMENTO ESERCIZIO VOLUME BOTTE 


#inizializzo le variabili tramite output
r1 =int(input("inserire raggio 1:")) 
r2 =int(input("inserire raggio 2:"))
r3 =int(input("inserire raggio 3:"))
h  =int(input("inserire altezza:"))
π  = 3.1415

#inserisco formule per calcolo superfici
s1=π*(r1**2)  
s2=π*(r2**2)
s3=π*(r3**2)

#calcolo volume
v=1/6*h*(s1+4*s2+s3) 
#converto in litri
v=(v/1000) 
#stampo risultato in litri
print("il volume della botte è di : ",v, "litri" ) 

#impossibile calcolare area della botte essendo un oggetto 3d
