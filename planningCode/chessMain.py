from square import Square

def makeBoard(): 
    #how to create a new square instance:
    #a1 = Square('a1')
    #position = a1.getSquare()
    #is position really needed?? ^^

    files = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    ranks = ['1', '2', '3', '4', '5', '6', '7', '8']
    squares = []

    #creates all possible squares on the chess board
    for i in range(0, 8):
        for count in range(0, 8):
            newSquare = files[i] + ranks[count]
            squares.append(newSquare)
    print(squares)
    
    #creates an instance of Square for each 
    boardSquares = []
    for item in squares:
        boardSquares.append(Square(item))
    #print(boardSquares[0].name)

    #to getSquare
    #position = boardSquares[0].getSquare()

    #checking which square matched to which index number
    #for i in range(0, len(boardSquares)):
        #print(i, end='')
        #print(boardSquares[i].name, end='  ')

    #link board squares, e.g. :
    #a1
    boardSquares[0].linkSquare(boardSquares[1], 'north')
    boardSquares[0].linkSquare(boardSquares[9], 'north east')
    boardSquares[0].linkSquare(boardSquares[8], 'east')
    #a2
    boardSquares[1].linkSquare(boardSquares[2], 'north')
    boardSquares[1].linkSquare(boardSquares[10], 'north east')
    boardSquares[1].linkSquare(boardSquares[9], 'east')
    boardSquares[1].linkSquare(boardSquares[8], 'south east')
    boardSquares[1].linkSquare(boardSquares[0], 'south')
    #a3
    boardSquares[2].linkSquare(boardSquares[3], 'north')
    boardSquares[2].linkSquare(boardSquares[11], 'north east')
    boardSquares[2].linkSquare(boardSquares[10], 'east')
    boardSquares[2].linkSquare(boardSquares[9], 'south east')
    boardSquares[2].linkSquare(boardSquares[1], 'south')
    #a4
    boardSquares[3].linkSquare(boardSquares[4], 'north')
    boardSquares[3].linkSquare(boardSquares[12], 'north east')
    boardSquares[3].linkSquare(boardSquares[11], 'east')
    boardSquares[3].linkSquare(boardSquares[10], 'south east')
    boardSquares[3].linkSquare(boardSquares[2], 'south')
    #a5
    boardSquares[4].linkSquare(boardSquares[5], 'north')
    boardSquares[4].linkSquare(boardSquares[13], 'north east')
    boardSquares[4].linkSquare(boardSquares[12], 'east')
    boardSquares[4].linkSquare(boardSquares[11], 'south east')
    boardSquares[4].linkSquare(boardSquares[3], 'south')
    #is it better to link pieces to board squares?
    #or, can link squares when a piece is on square?
    return boardSquares

def main():
    #maybe use boardSquares as a local variable
    #maybe have directions for each piece as a different subroutine
    boardSquares = makeBoard()
    print()
    boardSquares[0].describeSquare()
    print()
    boardSquares[1]. describeSquare()
    print()
    boardSquares[2]. describeSquare()
    print()
    boardSquares[3]. describeSquare()
    print()
    boardSquares[4]. describeSquare()
    
main()

