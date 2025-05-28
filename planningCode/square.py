class Square():
    def __init__(self, squareName):
        self.name = squareName
        self.adjacentSquares = {}

    def getSquare(self):
        return self.name
    
    def describeSquare(self):
        print('This square is {}.'.format(self.name))
        for i in self.adjacentSquares:
            square = self.adjacentSquares[i]
            print('The ' + square.getSquare() + ' is to the ' +i)

    def linkSquare(self, squareToLink, direction):
        self.adjacentSquares[direction] = squareToLink
