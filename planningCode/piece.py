class Piece():
    def __init__(self, pieceName, pieceColour):
        self.name = pieceName
        self.colour = pieceColour

    def setColour(self, pieceColour):
        self.colour = pieceColour

    def getColour(self):
        return self.colour

    def getName(self):
        return self.name
