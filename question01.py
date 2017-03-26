""" Cette fonction permet de tracer la courbe de la fonction fx = x + 3 """

def fonction():
    resultat = {}
    variable = 'x + 2'
    for x in range(-10,11):
      resultat[x] = eval(variable)
    for x in range(-10,11):
      for y in range(-10,11):
         if resultat[x] == y :
           print("o",end="")
         elif x == 0 and y == 0 :
           print("+",end="")
         elif x == 0:
           print("-",end="")
         elif y == 0:
           print("|",end="")
         print(" ",end="") 
      print()
 
fonction()



                                                                                


