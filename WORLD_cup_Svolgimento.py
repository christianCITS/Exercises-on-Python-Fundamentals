# !!!! SONO TUTTE OPERAZIONI SU LISTE !!!!
# 1) contare quanti calciatori hanno giocato per l'Italia
# 2) contare quanti calciatori hanno giocato per il Brasile
# 3) contare quanti calciatori hanno giocato per l'Argentina
# 4) Indicare quali calciatori hanno giocato sia per il Brasile, sia per l'Italia
# 5) Indicare quali calciatori hanno giocato sia per l'Argentina, sia per l'Italia
# 6) Trovare qual'è il calciatore più giovane che ha partecipato alla coppa del mondo
# 7) Trovare qual'è il calciatore più anziano che ha partecipato alla coppa del mondo
# 8) Trovare quale calciatore ha partecipato a più edizioni della coppa del mondo
# 9) Trovare quale squadra di calcio ha fornito più calciatori per la coppa del mondo
# 10)  Organizzare per nazione. Cioè quale squadra italiana ha fornito più calciatori per la coppa del mondo e quanti, quale squadra francese, ...
import json



def  giocatorePiuEdizioni(w):
      gpd={}
      
      for v in w:
            if v["FullName"] in gpd.keys():
                  gpd[v["FullName"]]=gpd[v["FullName"]]+1
            else:
                  gpd[v["FullName"]]=1
      return gpd

            

           



def minore(a,b):
       ymda=a.split("-")
       ymdb=b.split("-")
       if ymda[0]< ymdb[0]:
              return False
       elif ymda[0]>ymdb[0]:
              return True
       elif ymda[0]==ymdb[0]:
            if ymda[1]< ymdb[1]:
              return False
            elif ymda[1]>ymdb[1]:
              return True
            elif ymda[1]==ymdb[1]:
                  if ymda[2]<ymdb[2]:
                        return False
                  else: 
                        return True
                  

def maggiore(a,b):
       ymda=a.split("-")
       ymdb=b.split("-")
       if ymda[0]< ymdb[0]:
              return True
       elif ymda[0]>ymdb[0]:
              return False
       elif ymda[0]==ymdb[0]:
            if ymda[1]< ymdb[1]:
              return True
            elif ymda[1]>ymdb[1]:
              return False
            elif ymda[1]==ymdb[1]:
                  if ymda[2]<ymdb[2]:
                        return True
                  else: 
                        return False
              
              
def dataMax(date):
      max=date[0]
      for d in date:
            if maggiore(d,max):
                  max=d
      return max

    
                  
               



def dataMin(date):
    min=date[10]
    for d in date:
              if minore(d,min):
                     
                     min=d
    return min
              

filejson = open("all-world-cup-players.json", "r")
worldcup = json.load(filejson)
filejson.close()

calciatoriita=[]
calciatoribra=[]
calciatoriarg=[]
eta=[]

for x in worldcup:
    if x["Team"]==("Italy"):
          calciatoriita.append(x["FullName"]) 
    elif x["Team"]==("Brazil"):
          calciatoribra.append(x["FullName"])
    elif x["Team"]==("Argentina"):
          calciatoriarg.append(x["FullName"])
    



print("Il numero di calciatori italiani è: ",len(calciatoriita))
print("Il numero di calciatori brasiliani è: ",len(calciatoribra))
print("Il numero di calciatori argentini è: ",len(calciatoriarg))

for calciatore in calciatoriita:
            if calciatore in calciatoribra:
                print("I calciatori che hanno giocato sia per il Brasile, sia per l'Italia sono: ",len(calciatore))
            
                         




for calciatore in calciatoriita:
    if calciatore in calciatoriarg:
                
                 print("I calciatori che hanno giocato sia per l'Argentina, sia per l'Italia sono: ",calciatore)



for g in worldcup:
      if g["DateOfBirth"]: eta.append(g["DateOfBirth"])


datmin=dataMin(eta)
datmax=dataMax(eta)


for g in worldcup:
      if g["DateOfBirth"]== datmin:
             print("il calciatore più giovane che ha partecipato alla coppa del mondo è: " , g["FullName"] ,datmin)


for g in worldcup:
      if g["DateOfBirth"]== datmax:
             print("il calciatore più anziano che ha partecipato alla coppa del mondo è: " , g["FullName"] ,datmax)




       

gpd=giocatorePiuEdizioni(worldcup)


#print(gpd)



        









    
    





        