from random import randint

a=3
b=3


Voisins=[[0 for col in range(b)] for lig in range(a)]
Nouv=[[0 for col in range(b)] for lig in range(a)]

# Random_Grid
Liste=[[0 for col in range(b)] for lig in range(a)] # Fill Liste with Zeros
for lig in range(a):
  for col in range(b):
    Liste[lig][col]=randint(0,1) # Random initialisation with 0 & 1 (Too Long : randint(1,100)%2)
    if Liste[lig][col] == 1:   
        print(Liste)

for gen in range(2):
  for i in range(a):
    for j in range(b):
      Voisins[i][j]=0
      for k in [-1,0,1]:
        for l in [-1,0,1]:
          if (k,l)!=(0,0) and (0<=(i+k)<=(a-1) and 0<=(j+l)<=(b-1)):
            Voisins[i][j]+=Liste[(i+k)][(j+l)]

  for m in range(a):
    for n in range(b):
      if ( Liste[m][n]==0 and Voisins[m][n]==3 ) or ( Liste[m][n]==1 and Voisins[m][n] in [2,3] ): # Live or Death ?
        # Life
        Nouv[m][n]=1
        couleur=1
      else:
        Nouv[m][n]=0
        couleur=0
      if Nouv[m][n]!=Liste[m][n]: # or Nouv[m][n]==1: 
        print(Liste)
      Liste[m][n]=Nouv[m][n]
