def evaluerUnePiece(frais):
    recevable = frais in (500, 200, 100, 50, 20, 10, 5)
    return recevable

def demanderPiece():
    frais = input('Deposez une piece:')
    return (evaluerUnePiece(int(frais)), int(frais))

def obtenirPieceCorrecte():
    pieceCorrecte = demanderPiece()
    while not pieceCorrecte[0]:
      pieceCorrecte = demanderPiece()
    return pieceCorrecte[1]

def oPSOE():
    print('entrez le prix par piece: 750')
    piece = obtenirPieceCorrecte()
    while piece < 750 :
       piece = obtenirPieceCorrecte()
       piece = piece + piece
    return piece

print(oPSOE())

#def rendreMonnaie():
#    monnaie = oPSOE()
#    if monnaie > 750:
#       print('Votre monnaie est:', monnaie - 750)
#    else:
#       print("Vous n'avez pas de monnaie")
