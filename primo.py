print("hello world")
print(3**1001)
from math import asin, cos, radians, sin, sqrt
dat=(sqrt((10.123**2)+(30.456**2)))
print("La lunghezza dell'ipotenusa è di "+str(dat)) 




raggio=6371
ϕ1=(59.9)
λ1=(10.8)
ϕ2=(49.3)
λ2=(-123.1)

ϕ1=radians(ϕ1)
λ1=radians(λ1)
ϕ2=radians(ϕ2)
λ2=radians(λ2)

d= 2*raggio*asin(sqrt(sin(1/2*(ϕ2-ϕ1))**2+cos(ϕ1)*cos(ϕ2)*sin(1/2*(λ2-λ1))**2))

print (d)

