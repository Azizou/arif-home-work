#resultat ={ -10:-8,-9:-7,-8:-6,-7:-5,-6:-4,-5:-3,-4:-2,-3:-1,-2:0,-1:1,0:2,1:3,2:4,3:5,4:6,5:7,6:8,7:9,8:10,9:11,10:12}

def fonction():
    resultat = {}
    variable = 'x + 2'
    for x in range(-10,11):
      resultat[x] = eval(variable)
    for y in range(-10,11):
      for x in range(-10,11):
         if resultat[x] == y :
           print("o",end="")
         elif x == 0 and y == 0 :
           print("+",end="")
         elif y == 0:
           print("-",end="")
         elif x == 0:
           print("|",end="")
           print(" ",end="") 
         print(" ",end="") 
      print()
 
fonction()



                                                                                

