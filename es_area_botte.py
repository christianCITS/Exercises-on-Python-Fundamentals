



r1 =int(input("inserire raggio 1:"))
r2 =int(input("inserire raggio 2:"))
r3 =int(input("inserire raggio 3:"))
h  =int(input("inserire altezza:"))
π  = 3.1415

s1=(π*r1)**2
s2=(π*r2)**2
s3=(π*r3)**2

v=1/6*h*(s1*4*s2+s3)
v=(v/1000)
print("il volume della botte è di : "+str(v)+" litri" )






