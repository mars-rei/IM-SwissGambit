# importing pygame and initialising pygame's library
import pygame

# imports actions to detect
from pygame.locals import (
    MOUSEBUTTONUP,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

pygame.init()

# setting up initial display variables
screenWidth, screenHeight = 600, 600
squareSide = int(screenWidth / 8)

# draws window display
display = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('Gambit')

#creates class player
class Player:
    def __init__(self, colour, playerKind):
        self._playerColour = colour
        self._playerPiecesOnBoard = []
        self._playerType = playerKind

    def getPlayerDetails(self):
        print('player is a:', self._playerType)
        print('player is:', self._playerColour)
        print('player has these pieces on board:', self._playerPiecesOnBoard)
        print()

    def updatePiecesOnBoard(self, piecesOn):
        self._playerPiecesOnBoard = piecesOn
        print(self._playerType, 'has these pieces on board:', self._playerPiecesOnBoard)

    def getPlayerColour(self):
        return self._playerColour

    def getPlayerType(self):
        return self._playerType

#creates class board
class Board:
    def __init__(self, squareSide):
        # for the coordinates of squares
        self._x = 0
        self._y = 0
        # side size to draw squares
        self._side = squareSide
        # names of board squares from white's point of view
        self._boardSquares = [
            ['a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8'],
            ['a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7'],
            ['a6', 'b6', 'c6', 'd6', 'e6', 'f6', 'g6', 'h6'],
            ['a5', 'b5', 'c5', 'd5', 'e5', 'f5', 'g5', 'h5'],
            ['a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4', 'h4'],
            ['a3', 'b3', 'c3', 'd3', 'e3', 'f3', 'g3', 'h3'],
            ['a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2'],
            ['a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1']
        ]
        # a dictionary of the squares and their square coordinates
        self._squareCoordinates = {}
        # a dictionary of the squares and their colours
        self._squareColour = {}
        # setting the status of a square when clicked
        self._lastHighlightedSquare = False
        # dictionary of pieces on each square and all their details
        self._pieceOnSquare = {}

    # draws board
    def drawBoard(self):
        x = y = 0
        # could add white and black if they want a more contrasted display
        # also can add other colours / player can customise!
        dimmerWhite = (163, 163, 163)
        dimmerBlack = (84, 84, 84)
        #decides what colour a square will be
        for i in range(0, 8):
            if i % 2 == 0:
                colour1 = dimmerWhite
                colour2 = dimmerBlack
            else:
                colour1 = dimmerBlack
                colour2 = dimmerWhite
            for count in range(0, 8):
                # attaches squares onto the board via coordinates with given colours
                surf = pygame.Surface((squareSide, squareSide))
                squareLocation = self._boardSquares[i][count]
                # print(squareLocation)
                self._squareCoordinates[squareLocation] = x, y
                # print(self._squareCoordinates[squareLocation])
                if count % 2 == 0:
                    surf.fill(colour1)
                    self._squareColour[squareLocation] = colour1
                else:
                    surf.fill(colour2)
                    self._squareColour[squareLocation] = colour2
                rect = surf.get_rect()
                display.blit(surf, (x, y))
                # pygame.display.flip()
                # shifts one square coordinates to the right (new file)
                x += squareSide
            # resets x coordinate for next rank
            x = 0
            y += squareSide

    # locates the mouse's position and finds which square the mouse is on
    def getMouseSquare(self, pos):
        mousePosition = pos
        xCoord = mousePosition[0]
        yCoord = mousePosition[1]
        # print(xCoord, yCoord)

        squaresMouseCouldBeOn = []

        # need to call boardSquares to get key name for each
        # square to access value for square coordinates
        for i in range(0, 8):
            for count in range(0, 8):
                possibleBoardSquare = self._boardSquares[i][count]
                getPossibleSquareCoordinates = \
                    self._squareCoordinates[possibleBoardSquare]
                if getPossibleSquareCoordinates[1] < yCoord \
                        and getPossibleSquareCoordinates[0] < xCoord:
                    # print()
                    # print(possibleBoardSquare)
                    # print(getPossibleSquareCoordinates)
                    squaresMouseCouldBeOn.append(possibleBoardSquare)
                    yDifference = yCoord - getPossibleSquareCoordinates[1]
                    # print('y difference =', yDifference)
                    xDifference = xCoord - getPossibleSquareCoordinates[0]
                    # print('x difference =', xDifference)
                    # print()
                    if yDifference > squareSide or xDifference > squareSide:
                        squaresMouseCouldBeOn.remove(possibleBoardSquare)
                # if yDifference > squareSide or xDifference >squareSide:
                # squaresMouseCouldBeOn.remove(possibleBoardSquare)

        # print('mouse is on', squaresMouseCouldBeOn[0])
        return squaresMouseCouldBeOn[0]

    def highlightSquareClicked(self, squareMouseOn):
        if squareMouseOn == self._lastHighlightedSquare:
            colour = self._squareColour[squareMouseOn]
            self._lastHighlightedSquare = False
            # print(squareMouseOn, 'is unhighlighted')
        else:
            colour = (124, 113, 127)
            # print(squareMouseOn, 'is highlighted')

            if self._lastHighlightedSquare != False:
                previousSquareCoords = self._squareCoordinates[self._lastHighlightedSquare]
                surf = pygame.Surface((squareSide, squareSide))
                refill = self._squareColour[self._lastHighlightedSquare]
                surf.fill(refill)
                rect = surf.get_rect()
                display.blit(surf, previousSquareCoords)
                # pygame.display.flip()

            self._lastHighlightedSquare = squareMouseOn

        startingSquareCoord = self._squareCoordinates[squareMouseOn]
        x = startingSquareCoord[0]
        y = startingSquareCoord[1]
        surf = pygame.Surface((squareSide, squareSide))
        surf.fill(colour)
        display.blit(surf, (x, y))

    def kingInCheckHighlight(self, squareKingOn, highlightStatus):
        if highlightStatus == True:
            colour = self._squareColour[squareKingOn]
        else:
            colour = (180, 129, 123)

        startingSquareCoord = self._squareCoordinates[squareKingOn]
        x = startingSquareCoord[0]
        y = startingSquareCoord[1]
        surf = pygame.Surface((squareSide, squareSide))
        surf.fill(colour)
        display.blit(surf, (x, y))

    #updates board when a square is highlighted so pieces stay on (also when a piece is moved)
    def keepPiecesOn(self):
        piecesOnBoard = self._pieceOnSquare
        for i in range(len(piecesOnBoard)):
            # piecesOnBoard = self._pieceOnSquare
            # print(self._pieceOnSquare)
            squareKey = list(piecesOnBoard.keys())[i]
            # print(piecesOnBoard[squareKey])
            if piecesOnBoard[squareKey] != False:
                piecePng = piecesOnBoard[squareKey][1]
                pieceCoord = piecesOnBoard[squareKey][2]
                pieceToKeepOn = pygame.image.load(piecePng)
                display.blit(pieceToKeepOn, (pieceCoord))

    # setup for pieces - places pieces on the board
    def setupPieces(self, setup):
        # print(setup)
        boardSquareCoords = self._squareCoordinates
        # for i in range(0, 64):
        square = list(boardSquareCoords.keys())[i]
        # print(square)
        xCoord = boardSquareCoords[square][0] + 5
        # print(xCoord)
        yCoord = boardSquareCoords[square][1] + 5
        # print(yCoord)
        coordToPlace = xCoord, yCoord
        piece = setup
        # print(piece)
        if piece != False:
            if piece == 'BR':
                piece = 'black rook'
                imgFile = "dbR.png"
                colour = "black"
            elif piece == 'BN':
                piece = 'black knight'
                imgFile = "dbN.png"
                colour = "black"
            elif piece == 'BB':
                piece = 'black bishop'
                imgFile = "dbB.png"
                colour = "black"
            elif piece == 'BQ':
                piece = 'black queen'
                imgFile = "dbQ.png"
                colour = "black"
            elif piece == 'BK':
                piece = 'black king'
                imgFile = "dbK.png"
                colour = "black"
            elif piece == 'Bp':
                piece = 'black pawn'
                imgFile = "dbp.png"
                colour = "black"
            elif piece == 'WR':
                piece = 'white rook'
                imgFile = "dwR.png"
                colour = "white"
            elif piece == 'WN':
                piece = 'white knight'
                imgFile = "dwN.png"
                colour = "white"
            elif piece == 'WB':
                piece = 'white bishop'
                imgFile = "dwB.png"
                colour = "white"
            elif piece == 'WQ':
                piece = 'white queen'
                imgFile = "dwQ.png"
                colour = "white"
            elif piece == 'WK':
                piece = 'white king'
                imgFile = "dwK.png"
                colour = "white"
            elif piece == 'Wp':
                piece = 'white pawn'
                imgFile = "dwp.png"
                colour = "white"

            #added colour to help with blocked pieces and not taking one's own!!
            self._pieceOnSquare[square] = piece, imgFile, coordToPlace, colour
            loadPiece = pygame.image.load(imgFile)
            display.blit(loadPiece, (coordToPlace))
        else:
            self._pieceOnSquare[square] = False

    # place pieces
    def promotionPieces(self, pieceToPlace, squareToPlaceOn):
        print('piece to place is', pieceToPlace)
        print('square to place piece on is', squareToPlaceOn)

        boardSquareCoords = self._squareCoordinates
        squareDetails = boardSquareCoords[squareToPlaceOn]
        print(squareDetails)
        xCoord = squareDetails[0] + 5
        yCoord = squareDetails[1] + 5
        coordToPlace = xCoord, yCoord
        if pieceToPlace == 'BR':
            piece = 'black rook'
            imgFile = "dbR.png"
            colour = "black"
        elif pieceToPlace == 'BN':
            piece = 'black knight'
            imgFile = "dbN.png"
            colour = "black"
        elif pieceToPlace == 'BB':
            piece = 'black bishop'
            imgFile = "dbB.png"
            colour = "black"
        elif pieceToPlace == 'BQ':
            piece = 'black queen'
            imgFile = "dbQ.png"
            colour = "black"
        elif pieceToPlace == 'WR':
            piece = 'white rook'
            imgFile = "dwR.png"
            colour = "white"
        elif pieceToPlace == 'WN':
            piece = 'white knight'
            imgFile = "dwN.png"
            colour = "white"
        elif pieceToPlace == 'WB':
            piece = 'white bishop'
            imgFile = "dwB.png"
            colour = "white"
        elif pieceToPlace == 'WQ':
            piece = 'white queen'
            imgFile = "dwQ.png"
            colour = "white"

        self._pieceOnSquare[squareToPlaceOn] = piece, imgFile, coordToPlace, colour
        loadPiece = pygame.image.load(imgFile)
        display.blit(loadPiece, (coordToPlace))

    # returns the starting setup of a normal game of chess for the above subroutine to use
    def setupStart(self):
        startDetails = ['BR', 'BN', 'BB', 'BQ', 'BK', 'BB', 'BN', 'BR',
                        'Bp', 'Bp', 'Bp', 'Bp', 'Bp', 'Bp', 'Bp', 'Bp',
                        False, False, False, False, False, False, False, False,
                        False, False, False, False, False, False, False, False,
                        False, False, False, False, False, False, False, False,
                        False, False, False, False, False, False, False, False,
                        'Wp', 'Wp', 'Wp', 'Wp', 'Wp', 'Wp', 'Wp', 'Wp',
                        'WR', 'WN', 'WB', 'WQ', 'WK', 'WB', 'WN', 'WR']
        return startDetails

    #checks if a piece is on the square the mouse is on
    def checkIfPieceOnSquare(self, squareMouseOn):
        pieceThere = self._pieceOnSquare[squareMouseOn]
        # print(pieceThere)
        if pieceThere != False:
            return True
        else:
            return False

    # if previous click was on a square with a piece and current click
    # is on a vacant square, statement is true!
    def checkIfMoving(self, current, past, moveStatus):
        # print('current square has piece?', current)
        # print('past square has piece?', past)
        # print(moveStatus)

        if moveStatus == 'just moved':
            return False

        # to move a piece to an empty square
        elif current == False and past == True:
            return True
        elif current == False and past == False:
            return False
        # to move a piece to a square with a piece already on it
        elif current == True and past == True:
            return True
        # i think i've solved sticky pieces!!

    # removes piece from board - for en passant or promotion!
    def removePiece(self, removeFromSquare):
        print('the piece on', removeFromSquare, 'needs to be removed from the board')
        self._pieceOnSquare[removeFromSquare] = False

    # moves pieces to square they have been relocated to
    def movePiece(self, current, past):
        # print('current square is', current)
        # print('past square is', past)
        pieceDetails = self._pieceOnSquare[past]
        # print(past, 'past square details', pieceDetails)

        boardSquareCoords = self._squareCoordinates
        # for i in range(0, 64):
        xCoord = boardSquareCoords[current][0] + 5
        # print(xCoord)
        yCoord = boardSquareCoords[current][1] + 5
        # print(yCoord)
        coordToPlace = xCoord, yCoord
        piece = pieceDetails[0]
        # print(piece)
        img = pieceDetails[1]
        # print(img)
        colour = pieceDetails[3]
        # print(colour)

        self._pieceOnSquare[current] = piece, img, coordToPlace, colour
        self._pieceOnSquare[past] = False

        loadPiece = pygame.image.load(img)
        display.blit(loadPiece, (coordToPlace))

        # self._pieceOnSquare[current] = pieceDetails
        # self._pieceOnSquare[past] = False

    # to replace checkLegal to check and return piece that wants to move
    def checkPiece(self, pastSquare):
        pieceToMove = self._pieceOnSquare[pastSquare][0]
        return pieceToMove

    #check colour of piece that is moving
    def checkPieceColour(self, pieceSquare):
        pieceColour = self._pieceOnSquare[pieceSquare][3]
        # print(pieceColour)
        return pieceColour

    def checkPiecesOnBoard(self, currentColour):
        piecesOnBoard = []
        if currentColour == 'white':
            opponentsColour = 'black'
        else:
            opponentsColour = 'white'

        for i in range(0, 8):
            for count in range(0, 8):
                square = self._boardSquares[i][count]
                # print(square)
                squareDetails = self._pieceOnSquare[square]
                # print(squareDetails)
                if squareDetails != False:
                    if squareDetails[3] == opponentsColour:
                        pieceOnSquare = self._pieceOnSquare[square][0]
                        # print(square, 'has an opposing piece: a', pieceOnSquare)
                        piecesOnBoard.append((square, pieceOnSquare))
                    if squareDetails[3] == currentColour:
                        pieceOnSquare = self._pieceOnSquare[square][0]
                        if pieceOnSquare == 'white king' or pieceOnSquare == 'black king':
                            currentKingSquare = square


        return currentKingSquare, piecesOnBoard

    # checks if the move the player has requested is a legal move according to chess rules
    # need to check boundaries!
    def checkWhitePawnMoves(self, currentSquare, pastSquare, pawnColour, previousMove, previousMoveFrom, checking):
        moveEnPassant = False
        enPassantPossible = False
        enPassantMove = None
        # print('the previous move went to', previousMove)
        if previousMove != '' and checking == False:
            pieceMovedPreviously = self._pieceOnSquare[previousMove][0]
            #print('the piece that moved to', previousMove, 'was a', pieceMovedPreviously)
            if pieceMovedPreviously == 'black pawn' and previousMoveFrom[1] == '7':
                enPassantPossible = True
        legalMoves = []
        squares = self._boardSquares
        for i in range(0, 8):
            for count in range(0, 8):
                checkingSquare = squares[i][count]
                # print(checkingSquare)
                if checkingSquare == pastSquare:
                    # print('found', pastSquare)
                    squareIndex = i, count
                    # print(squareIndex)
                    # print(squares[squareIndex[0]][squareIndex[1]])
                    rank = squareIndex[0]
                    # print(rank)
                    file = squareIndex[1]
                    # print(file)
                    if rank == 6 and checking != True:
                        for i in range(1, 3):
                            rank -= 1
                            addLegalMove = squares[rank][file]
                            legalMoves.append(addLegalMove)
                            checkPieceBlocking = self._pieceOnSquare[addLegalMove]
                            # print(checkPieceBlocking)
                            if checkPieceBlocking != False:
                                legalMoves.remove(addLegalMove)
                                break
                    elif rank < 6 and checking != True:
                        rank -= 1
                        addLegalMove = squares[rank][file]
                        legalMoves.append(addLegalMove)
                        checkPieceBlocking = self._pieceOnSquare[addLegalMove]
                        # print(checkPieceBlocking)
                        if checkPieceBlocking != False:
                            legalMoves.remove(addLegalMove)
                    rank = squareIndex[0]

                    # for taking left adjacent
                    if file - 1 > -1 and rank != 7:
                        addLegalMove = squares[rank - 1][file - 1]
                        canCapture = self._pieceOnSquare[addLegalMove]
                        if canCapture != False:
                            legalMoves.append(addLegalMove)
                            if pawnColour == self._pieceOnSquare[addLegalMove][3]:
                                legalMoves.remove(addLegalMove)
                        if rank == 3 and enPassantPossible == True and previousMove[0] == addLegalMove[0]:
                            print('en passant may be legal on', addLegalMove)
                            enPassantMove = addLegalMove
                            moveEnPassant = True
                            legalMoves.append(addLegalMove)

                    # for taking right adjacent
                    if file + 1 < 8 and rank != 7:
                        addLegalMove = squares[rank - 1][file + 1]
                        canCapture = self._pieceOnSquare[addLegalMove]
                        if canCapture != False:
                            legalMoves.append(addLegalMove)
                            if pawnColour == self._pieceOnSquare[addLegalMove][3]:
                                legalMoves.remove(addLegalMove)
                        if rank == 3 and enPassantPossible == True and previousMove[0] == addLegalMove[0]:
                            print('en passant may be legal on', addLegalMove)
                            enPassantMove = addLegalMove
                            moveEnPassant = True
                            legalMoves.append(addLegalMove)

        if checking == True:
            return legalMoves
        else:
            print('pawn can go to:', legalMoves)
        for i in range(0, len(legalMoves)):
            if currentSquare == legalMoves[i]:
                print('move is legal!')
                if moveEnPassant == True and enPassantMove == currentSquare:
                    return True, 'en passant'
                if currentSquare[1] == '8':
                    print('promotion is possible!')
                    return True, 'promotion'
                return True
        print('move isn\'t legal!')

    def checkBlackPawnMoves(self, currentSquare, pastSquare, pawnColour, previousMove, previousMoveFrom, checking):
        moveEnPassant = False
        enPassantPossible = False
        enPassantMove = None
        #print('the previous move went to', previousMove)
        if previousMove != '' and checking == False:
            pieceMovedPreviously = self._pieceOnSquare[previousMove][0]
            print('the piece that moved to', previousMove, 'was a', pieceMovedPreviously)
            if pieceMovedPreviously == 'white pawn' and previousMoveFrom[1] == '2':
                enPassantPossible = True
        legalMoves = []
        squares = self._boardSquares
        for i in range(0, 8):
            for count in range(0, 8):
                checkingSquare = squares[i][count]
                if checkingSquare == pastSquare:
                    squareIndex = i, count
                    rank = squareIndex[0]
                    file = squareIndex[1]
                    if rank == 1 and checking != True:
                        for i in range(1, 3):
                            rank += 1
                            addLegalMove = squares[rank][file]
                            legalMoves.append(addLegalMove)
                            checkPieceBlocking = self._pieceOnSquare[addLegalMove]
                            # print(checkPieceBlocking)
                            if checkPieceBlocking != False:
                                legalMoves.remove(addLegalMove)
                                break
                    elif rank > 1 and checking != True:
                        rank += 1
                        addLegalMove = squares[rank][file]
                        legalMoves.append(addLegalMove)
                        checkPieceBlocking = self._pieceOnSquare[addLegalMove]
                        # print(checkPieceBlocking)
                        if checkPieceBlocking != False:
                            legalMoves.remove(addLegalMove)
                    rank = squareIndex[0]
                    if file - 1 > -1 and rank != 0:
                        addLegalMove = squares[rank + 1][file - 1]
                        canCapture = self._pieceOnSquare[addLegalMove]
                        if canCapture != False:
                            legalMoves.append(addLegalMove)
                            if pawnColour == self._pieceOnSquare[addLegalMove][3]:
                                legalMoves.remove(addLegalMove)
                        if rank == 4 and enPassantPossible == True and previousMove[0] == addLegalMove[0]:
                            print('en passant may be legal on', addLegalMove)
                            enPassantMove = addLegalMove
                            moveEnPassant = True
                            legalMoves.append(addLegalMove)

                    if file + 1 < 8 and rank != 0:
                        addLegalMove = squares[rank + 1][file + 1]
                        canCapture = self._pieceOnSquare[addLegalMove]
                        if canCapture != False:
                            legalMoves.append(addLegalMove)
                            if pawnColour == self._pieceOnSquare[addLegalMove][3]:
                                legalMoves.remove(addLegalMove)
                        if rank == 4 and enPassantPossible == True and previousMove[0] == addLegalMove[0]:
                            print('en passant may be legal on', addLegalMove)
                            enPassantMove = addLegalMove
                            moveEnPassant = True
                            legalMoves.append(addLegalMove)

        if checking == True:
            return legalMoves
        else:
            print('pawn can go to:', legalMoves)
        for i in range(0, len(legalMoves)):
            if currentSquare == legalMoves[i]:
                print('move is legal!')
                if moveEnPassant == True and enPassantMove == currentSquare:
                    return True, 'en passant'
                if currentSquare[1] == '1':
                    print('promotion is possible!')
                    return True, 'promotion'
                return True
        print('move isn\'t legal!')

    def checkQueenMoves(self, currentSquare, pastSquare, queenColour, checking):
        if queenColour == 'white':
            oppositionColour = 'black'
        else:
            oppositionColour = 'white'
        legalMoves = []
        squares = self._boardSquares
        # for ranks and files
        # program boundaries!!
        for i in range(0, 8):
            for count in range(0, 8):
                checkingSquare = squares[i][count]
                # better logic is to add squares in order of how close they are to the moving piece
                if checkingSquare == pastSquare:
                    squareIndex = i, count
                    rank = squareIndex[0]
                    # print('piece\'s rank is', rank)
                    file = squareIndex[1]
                    # print('piece\'s file is', file)

                    # check from piece to left
                    l = file
                    for repeat in range(0, 8):
                        addLegalMove = squares[rank][l]
                        l = l - 1
                        if l < -1:
                            break
                        legalMoves.append(addLegalMove)
                        if addLegalMove == checkingSquare:
                            legalMoves.remove(addLegalMove)
                        if self._pieceOnSquare[addLegalMove] != False:
                            if queenColour == self._pieceOnSquare[addLegalMove][3] and addLegalMove != pastSquare:
                                legalMoves.remove(addLegalMove)
                                # print('the queen can take a piece of its own colour on', addLegalMove)
                                break
                            elif oppositionColour == self._pieceOnSquare[addLegalMove][3]:
                                if self._pieceOnSquare[addLegalMove][0] == 'white king' and oppositionColour == 'white' and checking == True:
                                    pass
                                elif self._pieceOnSquare[addLegalMove][0] == 'black king' and oppositionColour == 'black' and checking == True:
                                    pass
                                else:
                                    break

                    # check from piece to right
                    r = file
                    for repeat in range(0, 8):
                        if r > 7:
                            break
                        addLegalMove = squares[rank][r]
                        r = r + 1
                        legalMoves.append(addLegalMove)
                        if addLegalMove == checkingSquare:
                            legalMoves.remove(addLegalMove)
                        if self._pieceOnSquare[addLegalMove] != False:
                            if queenColour == self._pieceOnSquare[addLegalMove][3] and addLegalMove != pastSquare:
                                legalMoves.remove(addLegalMove)
                                # print('the queen can take a piece of its own colour on', addLegalMove)
                                break
                            elif oppositionColour == self._pieceOnSquare[addLegalMove][3]:
                                if self._pieceOnSquare[addLegalMove][0] == 'white king' and oppositionColour == 'white' and checking == True:
                                    pass
                                elif self._pieceOnSquare[addLegalMove][0] == 'black king' and oppositionColour == 'black' and checking == True:
                                    pass
                                else:
                                    break

                    # check from piece to up
                    u = rank
                    for repeat in range(0, 8):
                        addLegalMove = squares[u][file]
                        u = u - 1
                        if u < -1:
                            break
                        legalMoves.append(addLegalMove)
                        if addLegalMove == checkingSquare:
                            legalMoves.remove(addLegalMove)
                        if self._pieceOnSquare[addLegalMove] != False:
                            if queenColour == self._pieceOnSquare[addLegalMove][3] and addLegalMove != pastSquare:
                                legalMoves.remove(addLegalMove)
                                # print('the queen can take a piece of its own colour on', addLegalMove)
                                break
                            elif oppositionColour == self._pieceOnSquare[addLegalMove][3]:
                                if self._pieceOnSquare[addLegalMove][0] == 'white king' and oppositionColour == 'white' and checking == True:
                                    pass
                                elif self._pieceOnSquare[addLegalMove][0] == 'black king' and oppositionColour == 'black' and checking == True:
                                    pass
                                else:
                                    break

                    # check from piece to down
                    d = rank
                    for repeat in range(0, 8):
                        if d > 7:
                            break
                        addLegalMove = squares[d][file]
                        d = d + 1
                        legalMoves.append(addLegalMove)
                        if addLegalMove == checkingSquare:
                            legalMoves.remove(addLegalMove)
                        if self._pieceOnSquare[addLegalMove] != False:
                            if queenColour == self._pieceOnSquare[addLegalMove][3] and addLegalMove != pastSquare:
                                legalMoves.remove(addLegalMove)
                                # print('the queen can take a piece of its own colour on', addLegalMove)
                                break
                            elif oppositionColour == self._pieceOnSquare[addLegalMove][3]:
                                if self._pieceOnSquare[addLegalMove][0] == 'white king' and oppositionColour == 'white' and checking == True:
                                    pass
                                elif self._pieceOnSquare[addLegalMove][0] == 'black king' and oppositionColour == 'black' and checking == True:
                                    pass
                                else:
                                    break

        # for diagonals
        for i in range(0, 8):
            for count in range(0, 8):
                checkingSquare = squares[i][count]
                if checkingSquare == pastSquare:
                    squareIndex = i, count
                    rank = squareIndex[0]
                    file = squareIndex[1]
                    for i in range(0, 8):
                        if rank - i > -1 and file - i > - 1:
                            addLegalMove = squares[rank - i][file - i]
                            legalMoves.append(addLegalMove)
                            if self._pieceOnSquare[addLegalMove] != False:
                                if queenColour == self._pieceOnSquare[addLegalMove][3] and addLegalMove != pastSquare:
                                    legalMoves.remove(addLegalMove)
                                    # print('the queen can take a piece of its own colour on', addLegalMove)
                                    break
                                elif oppositionColour == self._pieceOnSquare[addLegalMove][3]:
                                    if self._pieceOnSquare[addLegalMove][0] == 'white king' and oppositionColour == 'white' and checking == True:
                                        pass
                                    elif self._pieceOnSquare[addLegalMove][0] == 'black king' and oppositionColour == 'black' and checking == True:
                                        pass
                                    else:
                                        break
                    for i in range(0, 8):
                        if rank - i > - 1 and file + i < 8:
                            addLegalMove = squares[rank - i][file + i]
                            legalMoves.append(addLegalMove)
                            if self._pieceOnSquare[addLegalMove] != False:
                                if queenColour == self._pieceOnSquare[addLegalMove][3] and addLegalMove != pastSquare:
                                    legalMoves.remove(addLegalMove)
                                    # print('the queen can take a piece of its own colour on', addLegalMove)
                                    break
                                elif oppositionColour == self._pieceOnSquare[addLegalMove][3]:
                                    if self._pieceOnSquare[addLegalMove][0] == 'white king' and oppositionColour == 'white' and checking == True:
                                        pass
                                    elif self._pieceOnSquare[addLegalMove][0] == 'black king' and oppositionColour == 'black' and checking == True:
                                        pass
                                    else:
                                        break
                    for i in range(0, 8):
                        if rank + i < 8 and file + i < 8:
                            addLegalMove = squares[rank + i][file + i]
                            legalMoves.append(addLegalMove)
                            if self._pieceOnSquare[addLegalMove] != False:
                                if queenColour == self._pieceOnSquare[addLegalMove][3] and addLegalMove != pastSquare:
                                    legalMoves.remove(addLegalMove)
                                    # print('the queen can take a piece of its own colour on', addLegalMove)
                                    break
                                elif oppositionColour == self._pieceOnSquare[addLegalMove][3]:
                                    if self._pieceOnSquare[addLegalMove][0] == 'white king' and oppositionColour == 'white' and checking == True:
                                        pass
                                    elif self._pieceOnSquare[addLegalMove][0] == 'black king' and oppositionColour == 'black' and checking == True:
                                        pass
                                    else:
                                        break
                    for i in range(0, 8):
                        if rank + i < 8 and file - i > -1:
                            addLegalMove = squares[rank + i][file - i]
                            legalMoves.append(addLegalMove)
                            if self._pieceOnSquare[addLegalMove] != False:
                                if queenColour == self._pieceOnSquare[addLegalMove][3] and addLegalMove != pastSquare:
                                    legalMoves.remove(addLegalMove)
                                    # print('the queen can take a piece of its own colour on', addLegalMove)
                                    break
                                elif oppositionColour == self._pieceOnSquare[addLegalMove][3]:
                                    if self._pieceOnSquare[addLegalMove][0] == 'white king' and oppositionColour == 'white' and checking == True:
                                        pass
                                    elif self._pieceOnSquare[addLegalMove][0] == 'black king' and oppositionColour == 'black' and checking == True:
                                        pass
                                    else:
                                        break

        extra = []
        for i in range(0, len(legalMoves)):
            if legalMoves[i] == pastSquare:
                extra.append(legalMoves[i])
        for count in range(0, len(extra)):
            legalMoves.remove(extra[count])

        if checking == True:
            return legalMoves
        else:
            print('queen can go to:', legalMoves)
        for i in range(0, len(legalMoves)):
            if currentSquare == legalMoves[i]:
                print('move is legal!')
                return True
        print('move isn\'t legal!')

    def checkBishopMoves(self, currentSquare, pastSquare, bishopColour, checking):
        if bishopColour == 'white':
            oppositionColour = 'black'
        else:
            oppositionColour = 'white'
        legalMoves = []
        squares = self._boardSquares
        for i in range(0, 8):
            for count in range(0, 8):
                checkingSquare = squares[i][count]
                if checkingSquare == pastSquare:
                    squareIndex = i, count
                    rank = squareIndex[0]
                    file = squareIndex[1]
                    for i in range(0, 8):
                        if rank - i > -1 and file - i > - 1:
                            addLegalMove = squares[rank - i][file - i]
                            legalMoves.append(addLegalMove)
                            if self._pieceOnSquare[addLegalMove] != False:
                                if bishopColour == self._pieceOnSquare[addLegalMove][3] and addLegalMove != pastSquare:
                                    legalMoves.remove(addLegalMove)
                                    # print('the bishop can take a piece of its own colour on', addLegalMove)
                                    break
                                elif oppositionColour == self._pieceOnSquare[addLegalMove][3]:
                                    if self._pieceOnSquare[addLegalMove][0] == 'white king' and oppositionColour == 'white' and checking == True:
                                        pass
                                    elif self._pieceOnSquare[addLegalMove][0] == 'black king' and oppositionColour == 'black' and checking == True:
                                        pass
                                    else:
                                        break
                    for i in range(0, 8):
                        if rank - i > - 1 and file + i < 8:
                            addLegalMove = squares[rank - i][file + i]
                            legalMoves.append(addLegalMove)
                            if self._pieceOnSquare[addLegalMove] != False:
                                if bishopColour == self._pieceOnSquare[addLegalMove][3] and addLegalMove != pastSquare:
                                    legalMoves.remove(addLegalMove)
                                    # print('the bishop can take a piece of its own colour on', addLegalMove)
                                    break
                                elif oppositionColour == self._pieceOnSquare[addLegalMove][3]:
                                    if self._pieceOnSquare[addLegalMove][0] == 'white king' and oppositionColour == 'white' and checking == True:
                                        pass
                                    elif self._pieceOnSquare[addLegalMove][0] == 'black king' and oppositionColour == 'black' and checking == True:
                                        pass
                                    else:
                                        break
                    for i in range(0, 8):
                        if rank + i < 8 and file + i < 8:
                            addLegalMove = squares[rank + i][file + i]
                            legalMoves.append(addLegalMove)
                            if self._pieceOnSquare[addLegalMove] != False:
                                if bishopColour == self._pieceOnSquare[addLegalMove][3] and addLegalMove != pastSquare:
                                    legalMoves.remove(addLegalMove)
                                    # print('the bishop can take a piece of its own colour on', addLegalMove)
                                    break
                                elif oppositionColour == self._pieceOnSquare[addLegalMove][3]:
                                    if self._pieceOnSquare[addLegalMove][0] == 'white king' and oppositionColour == 'white' and checking == True:
                                        pass
                                    elif self._pieceOnSquare[addLegalMove][0] == 'black king' and oppositionColour == 'black' and checking == True:
                                        pass
                                    else:
                                        break
                    for i in range(0, 8):
                        if rank + i < 8 and file - i > -1:
                            addLegalMove = squares[rank + i][file - i]
                            legalMoves.append(addLegalMove)
                            if self._pieceOnSquare[addLegalMove] != False:
                                if bishopColour == self._pieceOnSquare[addLegalMove][3] and addLegalMove != pastSquare:
                                    legalMoves.remove(addLegalMove)
                                    # print('the bishop can take a piece of its own colour on', addLegalMove)
                                    break
                                elif oppositionColour == self._pieceOnSquare[addLegalMove][3]:
                                    if self._pieceOnSquare[addLegalMove][0] == 'white king' and oppositionColour == 'white' and checking == True:
                                        pass
                                    elif self._pieceOnSquare[addLegalMove][0] == 'black king' and oppositionColour == 'black' and checking == True:
                                        pass
                                    else:
                                        break

        extra = []
        for i in range(0, len(legalMoves)):
            if legalMoves[i] == pastSquare:
                extra.append(legalMoves[i])
        for count in range(0, len(extra)):
            legalMoves.remove(extra[count])

        if checking == True:
            return legalMoves
        else:
            print('bishop can go to:', legalMoves)
        for i in range(0, len(legalMoves)):
            if currentSquare == legalMoves[i]:
                print('move is legal!')
                return True
        print('move isn\'t legal!')

    def checkRookMoves(self, currentSquare, pastSquare, rookColour, checking):
        if rookColour == 'white':
            oppositionColour = 'black'
        else:
            oppositionColour = 'white'
        legalMoves = []
        squares = self._boardSquares
        #program boundaries!!
        for i in range(0, 8):
            for count in range(0, 8):
                checkingSquare = squares[i][count]
                # better logic is to add squares in order of how close they are to the moving piece
                if checkingSquare == pastSquare:
                    squareIndex = i, count
                    rank = squareIndex[0]
                    # print('piece\'s rank is', rank)
                    file = squareIndex[1]
                    # print('piece\'s file is', file)

                    # check from piece to left
                    l = file
                    for repeat in range(0, 8):
                        addLegalMove = squares[rank][l]
                        l = l-1
                        if l < -1:
                            break
                        legalMoves.append(addLegalMove)
                        if addLegalMove == checkingSquare:
                            legalMoves.remove(addLegalMove)
                        if self._pieceOnSquare[addLegalMove] != False:
                            if rookColour == self._pieceOnSquare[addLegalMove][3] and addLegalMove != pastSquare:
                                legalMoves.remove(addLegalMove)
                                # print('the rook can take a piece of its own colour on', addLegalMove)
                                break
                            elif oppositionColour == self._pieceOnSquare[addLegalMove][3]:
                                if self._pieceOnSquare[addLegalMove][0] == 'white king' and oppositionColour == 'white' and checking == True:
                                    pass
                                elif self._pieceOnSquare[addLegalMove][0] == 'black king' and oppositionColour == 'black' and checking == True:
                                    pass
                                else:
                                    break

                    # check from piece to right
                    r = file
                    for repeat in range(0, 8):
                        if r > 7:
                            break
                        addLegalMove = squares[rank][r]
                        r = r+1
                        legalMoves.append(addLegalMove)
                        if addLegalMove == checkingSquare:
                            legalMoves.remove(addLegalMove)
                        if self._pieceOnSquare[addLegalMove] != False:
                            if rookColour == self._pieceOnSquare[addLegalMove][3] and addLegalMove != pastSquare:
                                legalMoves.remove(addLegalMove)
                                # print('the rook can take a piece of its own colour on', addLegalMove)
                                break
                            elif oppositionColour == self._pieceOnSquare[addLegalMove][3]:
                                if self._pieceOnSquare[addLegalMove][0] == 'white king' and oppositionColour == 'white' and checking == True:
                                    pass
                                elif self._pieceOnSquare[addLegalMove][0] == 'black king' and oppositionColour == 'black' and checking == True:
                                    pass
                                else:
                                    break

                    # check from piece to up
                    u = rank
                    for repeat in range(0, 8):
                        addLegalMove = squares[u][file]
                        u = u - 1
                        if u < -1:
                            break
                        legalMoves.append(addLegalMove)
                        if addLegalMove == checkingSquare:
                            legalMoves.remove(addLegalMove)
                        if self._pieceOnSquare[addLegalMove] != False:
                            if rookColour == self._pieceOnSquare[addLegalMove][3] and addLegalMove != pastSquare:
                                legalMoves.remove(addLegalMove)
                                # print('the rook can take a piece of its own colour on', addLegalMove)
                                break
                            elif oppositionColour == self._pieceOnSquare[addLegalMove][3]:
                                if self._pieceOnSquare[addLegalMove][0] == 'white king' and oppositionColour == 'white' and checking == True:
                                    pass
                                elif self._pieceOnSquare[addLegalMove][0] == 'black king' and oppositionColour == 'black' and checking == True:
                                    pass
                                else:
                                    break

                    # check from piece to down
                    d = rank
                    for repeat in range(0, 8):
                        if d > 7:
                            break
                        addLegalMove = squares[d][file]
                        d = d + 1
                        legalMoves.append(addLegalMove)
                        if addLegalMove == checkingSquare:
                            legalMoves.remove(addLegalMove)
                        if self._pieceOnSquare[addLegalMove] != False:
                            if rookColour == self._pieceOnSquare[addLegalMove][3] and addLegalMove != pastSquare:
                                legalMoves.remove(addLegalMove)
                                # print('the rook can take a piece of its own colour on', addLegalMove)
                                break
                            elif oppositionColour == self._pieceOnSquare[addLegalMove][3]:
                                if self._pieceOnSquare[addLegalMove][0] == 'white king' and oppositionColour == 'white' and checking == True:
                                    pass
                                elif self._pieceOnSquare[addLegalMove][0] == 'black king' and oppositionColour == 'black' and checking == True:
                                    pass
                                else:
                                    break

        if checking == True:
            return legalMoves
        else:
            print('rook can go to:', legalMoves)
        for i in range(0, len(legalMoves)):
            if currentSquare == legalMoves[i]:
                print('move is legal!')
                return True
        print('move isn\'t legal!')

    def checkKingMoves(self, currentSquare, pastSquare, kingColour, whiteMoved, blackMoved, checking):
        if whiteMoved == False and kingColour == 'white':
            # print('condition for castling met')
            castle = True
        elif blackMoved == False and kingColour == 'black':
            # print('condition for castling met')
            castle = True
        else:
            castle = False
        legalMoves = []
        squares = self._boardSquares
        #program boundaries!!
        for i in range(0, 8):
            for count in range(0, 8):
                checkingSquare = squares[i][count]
                if checkingSquare == pastSquare:
                    squareIndex = i, count
                    rank = squareIndex[0]
                    file = squareIndex[1]
                    if rank + 1 < 8:
                        addLegalMove = squares[rank + 1][file]
                        legalMoves.append(addLegalMove)
                        if self._pieceOnSquare[addLegalMove] != False:
                            if kingColour == self._pieceOnSquare[addLegalMove][3]:
                                legalMoves.remove(addLegalMove)
                    if file + 1 < 8:
                        addLegalMove = squares[rank][file + 1]
                        legalMoves.append(addLegalMove)
                        if self._pieceOnSquare[addLegalMove] != False:
                            if kingColour == self._pieceOnSquare[addLegalMove][3]:
                                legalMoves.remove(addLegalMove)
                        if castle == True:
                            # checking if can castle kingside
                            addLegalMove = squares[rank][file + 2]
                            legalMoves.append(addLegalMove)
                            if self._pieceOnSquare[addLegalMove] != False:
                                legalMoves.remove(addLegalMove)
                            else:
                                pass
                                #print('can maybe castle kingside')

                    if rank - 1 > -1:
                        addLegalMove = squares[rank - 1][file]
                        legalMoves.append(addLegalMove)
                        if self._pieceOnSquare[addLegalMove] != False:
                            if kingColour == self._pieceOnSquare[addLegalMove][3]:
                                legalMoves.remove(addLegalMove)

                    if file - 1 > -1:
                        addLegalMove = squares[rank][file - 1]
                        legalMoves.append(addLegalMove)
                        if self._pieceOnSquare[addLegalMove] != False:
                            if kingColour == self._pieceOnSquare[addLegalMove][3]:
                                legalMoves.remove(addLegalMove)
                        if castle == True:
                            # checking if can castle queenside
                            addLegalMove = squares[rank][file - 2]
                            legalMoves.append(addLegalMove)
                            if self._pieceOnSquare[addLegalMove] != False:
                                legalMoves.remove(addLegalMove)
                            else:
                                pass
                                #print('can maybe castle queenside')

                    if rank + 1 < 8 and file + 1 < 8:
                        addLegalMove = squares[rank + 1][file + 1]
                        legalMoves.append(addLegalMove)
                        if self._pieceOnSquare[addLegalMove] != False:
                            if kingColour == self._pieceOnSquare[addLegalMove][3]:
                                legalMoves.remove(addLegalMove)
                    if rank - 1 > -1 and file - 1 > - 1:
                        addLegalMove = squares[rank - 1][file - 1]
                        legalMoves.append(addLegalMove)
                        if self._pieceOnSquare[addLegalMove] != False:
                            if kingColour == self._pieceOnSquare[addLegalMove][3]:
                                legalMoves.remove(addLegalMove)
                    if rank - 1 > -1 and file + 1 < 8:
                        addLegalMove = squares[rank - 1][file + 1]
                        legalMoves.append(addLegalMove)
                        if self._pieceOnSquare[addLegalMove] != False:
                            if kingColour == self._pieceOnSquare[addLegalMove][3]:
                                legalMoves.remove(addLegalMove)
                    if rank + 1 < 8 and file - 1 > - 1:
                        addLegalMove = squares[rank + 1][file - 1]
                        legalMoves.append(addLegalMove)
                        if self._pieceOnSquare[addLegalMove] != False:
                            if kingColour == self._pieceOnSquare[addLegalMove][3]:
                                legalMoves.remove(addLegalMove)

        if checking == True:
            return legalMoves
        else:
            print('king can go to:', legalMoves)
        for i in range(0, len(legalMoves)):
            if currentSquare == legalMoves[i]:
                if castle == True:
                    print('castling is legal')
                    return True, 'castle'
                print('move is legal!')
                return True
        print('move isn\'t legal!')

    def checkKnightMoves(self, currentSquare, pastSquare, knightColour, checking):
        legalMoves = []
        squares = self._boardSquares
        #program not to take its own pieces!
        for i in range(0, 8):
            for count in range(0, 8):
                checkingSquare = squares[i][count]
                if checkingSquare == pastSquare:
                    squareIndex = i, count
                    rank = squareIndex[0]
                    file = squareIndex[1]
                    if rank - 1 > - 1 and file - 2 > - 1:
                        addLegalMove = squares[rank - 1][file - 2]
                        legalMoves.append(addLegalMove)
                        if self._pieceOnSquare[addLegalMove] != False:
                            # print('the', knightColour, 'knight can take a', self._pieceOnSquare[addLegalMove][3], 'piece on', addLegalMove)
                            if knightColour == self._pieceOnSquare[addLegalMove][3]:
                                # print('this move is illegal')
                                legalMoves.remove(addLegalMove)
                        # print('down 1, left 2')
                    if rank - 2 > - 1 and file - 1 > -1:
                        addLegalMove = squares[rank - 2][file - 1]
                        legalMoves.append(addLegalMove)
                        if self._pieceOnSquare[addLegalMove] != False:
                            if knightColour == self._pieceOnSquare[addLegalMove][3]:
                                legalMoves.remove(addLegalMove)
                        # print('down 2, left 1')
                    if rank - 2 > - 1 and file + 1 < 8:
                        addLegalMove = squares[rank - 2][file + 1]
                        legalMoves.append(addLegalMove)
                        if self._pieceOnSquare[addLegalMove] != False:
                            if knightColour == self._pieceOnSquare[addLegalMove][3]:
                                legalMoves.remove(addLegalMove)
                        # print('down 2, right 1')
                    if rank - 1 > - 1 and file + 2 < 8:
                        addLegalMove = squares[rank - 1][file + 2]
                        legalMoves.append(addLegalMove)
                        if self._pieceOnSquare[addLegalMove] != False:
                            if knightColour == self._pieceOnSquare[addLegalMove][3]:
                                legalMoves.remove(addLegalMove)
                        # print('down 1, right 2')
                    if rank + 1 < 8 and file + 2 < 8:
                        addLegalMove = squares[rank + 1][file + 2]
                        legalMoves.append(addLegalMove)
                        if self._pieceOnSquare[addLegalMove] != False:
                            if knightColour == self._pieceOnSquare[addLegalMove][3]:
                                legalMoves.remove(addLegalMove)
                        # print('up 1, right 2')
                    if rank + 2 < 8 and file + 1 < 8:
                        addLegalMove = squares[rank + 2][file + 1]
                        legalMoves.append(addLegalMove)
                        if self._pieceOnSquare[addLegalMove] != False:
                            if knightColour == self._pieceOnSquare[addLegalMove][3]:
                                legalMoves.remove(addLegalMove)
                        # print('up 2, right 1')
                    if rank + 2 < 8 and file - 1 > - 1:
                        addLegalMove = squares[rank + 2][file - 1]
                        legalMoves.append(addLegalMove)
                        if self._pieceOnSquare[addLegalMove] != False:
                            if knightColour == self._pieceOnSquare[addLegalMove][3]:
                                legalMoves.remove(addLegalMove)
                        # print('up 2, left 1')
                    if rank + 1 < 8 and file - 2 > - 1:
                        addLegalMove = squares[rank + 1][file - 2]
                        legalMoves.append(addLegalMove)
                        if self._pieceOnSquare[addLegalMove] != False:
                            if knightColour == self._pieceOnSquare[addLegalMove][3]:
                                legalMoves.remove(addLegalMove)
                        # print('up 1, left 2')

        if checking == True:
            return legalMoves
        else:
            print('knight can go to:', legalMoves)
        for i in range(0, len(legalMoves)):
            if currentSquare == legalMoves[i]:
                print('move is legal!')
                return True
        print('move isn\'t legal!')

playerColour = input('what colour do you want to play as? white or black?: ')
while playerColour != 'white' and playerColour != 'black':
    print('enter a valid colour: white or black')
    playerColour = input('what colour do you want to play as? white or black?: ')
if playerColour == 'white':
    playerHuman = Player('white', 'human')
    playerComp = Player('black', 'computer')
elif playerColour == 'black':
    playerHuman = Player('black', 'human')
    playerComp = Player('white', 'computer')
players = [playerHuman, playerComp]

#playerHuman.getPlayerDetails()
#playerComp.getPlayerDetails()

chessBoard = Board(squareSide)
chessBoard.drawBoard()
setup = chessBoard.setupStart()
for i in range(0, 64):
    setPiece = setup[i]
    chessBoard.setupPieces(setPiece)

# update screen
pygame.display.flip()
pygame.display.update()

# runs until user quits
running = True

currentSquareHasPiece = ''
pastSquareHasPiece = ''
pastSquare = ''
moveNum = 1
move = ''
moveFrom = ''
moveStatus = 'not yet moved'
whoseMove = 'white'

for i in range(len(players)):
    colour = players[i].getPlayerColour()
    if colour == whoseMove:
        playerWhoseMove = players[i].getPlayerType()
        print('it is the', playerWhoseMove + '\'s turn')

whiteKingMoved = False
blackKingMoved = False
rooksMoved = {'a8': False, 'h8': False, 'a1': False, 'h1': False}
# print(rooksMoved)
promotion = False
currentKingInCheck = False
opposingKingInCheck = False
checking = False
checkmate = False
pastMovesCount = {}
opponentMovesCount = {}

#might need to do:
whiteMovesCount = {}
blackMovesCount = {}
pastWhiteMovesCount = {}
pastBlackMovesCount = {}

print('it is', whoseMove, 'to play')
print()

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            # if user presses escape key, quit program
            if event.key == K_ESCAPE:
                running = False
        if event.type == MOUSEBUTTONUP:

            pos = pygame.mouse.get_pos()
            # print(pos)
            squareMouseOn = chessBoard.getMouseSquare(pos)
            # print(squareMouseOn)

            pieceMouseOn = chessBoard.checkIfPieceOnSquare(squareMouseOn)
            currentSquareHasPiece = pieceMouseOn

            if currentSquareHasPiece == True:
                pieceMovingColour = chessBoard.checkPieceColour(squareMouseOn)

                # make sure only the colour whose move it is has their pieces clicked!
                #if pieceMovingColour != whoseMove:
                    #print()
                    #print('it is', whoseMove, 'to play')
                    #print('move a piece of the opposite colour')
                    #print()
                    #break

            playerMove = chessBoard.checkIfMoving(currentSquareHasPiece, pastSquareHasPiece, moveStatus)

            chessBoard.drawBoard()
            highlight = chessBoard.highlightSquareClicked(squareMouseOn)

            # testing to highlight square where this king is!
            # chessBoard.kingInCheckHighlight('e8', kingInCheck)
            # kingInCheck = True

            # makes pieces move
            if playerMove == True:
                piece = chessBoard.checkPiece(pastSquare)
                # print(piece)
                pieceMovingColour = piece[0:5]
                if pieceMovingColour != whoseMove:
                    print('it is', whoseMove, 'to play. you have tried to move the opponent\'s piece')
                    legal = False
                    piece = False

                #print('the piece moving is', pieceMovingColour)
                if piece == 'white pawn':
                    legal = chessBoard.checkWhitePawnMoves(squareMouseOn, pastSquare, pieceMovingColour, move, moveFrom, checking)
                    #print(legal)
                    if legal != True and legal != None:
                        if legal[1] == 'en passant':
                            print('en passant!')
                            chessBoard.removePiece(move)
                            legal = True
                        elif legal[1] == 'promotion':
                            promotion = True
                            legal = True
                elif piece == 'black pawn':
                    legal = chessBoard.checkBlackPawnMoves(squareMouseOn, pastSquare, pieceMovingColour, move, moveFrom, checking)
                    #print(legal)
                    if legal != True and legal != None:
                        if legal[1] == 'en passant':
                            print('en passant!')
                            chessBoard.removePiece(move)
                            legal = True
                        elif legal[1] == 'promotion':
                            promotion = True
                            legal = True
                    # promotionPieces(self, pieceToPlace, squareToPlaceOn)
                elif piece == 'white queen' or piece == 'black queen':
                    legal = chessBoard.checkQueenMoves(squareMouseOn, pastSquare, pieceMovingColour, checking)
                elif piece == 'white bishop' or piece == 'black bishop':
                    legal = chessBoard.checkBishopMoves(squareMouseOn, pastSquare, pieceMovingColour, checking)
                elif piece == 'white rook' or piece == 'black rook':
                    legal = chessBoard.checkRookMoves(squareMouseOn, pastSquare, pieceMovingColour, checking)
                    if legal == True:
                        rookThatJustMoved = pastSquare
                        if rookThatJustMoved == 'a8':
                            rooksMoved[pastSquare] = True
                        elif rookThatJustMoved == 'h8':
                            rooksMoved[pastSquare] = True
                        elif rookThatJustMoved == 'a1':
                            rooksMoved[pastSquare] = True
                        elif rookThatJustMoved == 'h1':
                            rooksMoved[pastSquare] = True
                elif piece == 'white king' or piece == 'black king':
                    legal = chessBoard.checkKingMoves(squareMouseOn, pastSquare, pieceMovingColour, whiteKingMoved, blackKingMoved, checking)
                    if legal == (True, 'castle'):
                        # kings can castle now - have to check if rook has moved yet though!
                        legal = True
                        if squareMouseOn[0] == 'g':
                            kingRank = squareMouseOn[1]
                            rookMove = 'f' + kingRank
                            rookOn = 'h' + kingRank
                            if rooksMoved[rookOn] == True:
                                legal = False
                                print('can\'t castle because rook on', rookOn, 'has already moved')
                            else:
                                chessBoard.movePiece(rookMove, rookOn)
                                if pieceMovingColour == 'white':
                                    whiteKingMoved = True
                                else:
                                    blackKingMoved = True
                        elif squareMouseOn[0] == 'c':
                            kingRank = squareMouseOn[1]
                            rookMove = 'd' + kingRank
                            rookOn = 'a' + kingRank
                            if rooksMoved[rookOn] == True:
                                legal = False
                                print('can\'t castle because rook on', rookOn, 'has already moved')
                            else:
                                chessBoard.movePiece(rookMove, rookOn)
                                if pieceMovingColour == 'white':
                                    whiteKingMoved = True
                                else:
                                    blackKingMoved = True
                        else:
                            if pieceMovingColour == 'white':
                                whiteKingMoved = True
                            else:
                                blackKingMoved = True

                elif piece == 'white knight' or piece == 'black knight':
                    legal = chessBoard.checkKnightMoves(squareMouseOn, pastSquare, pieceMovingColour, checking)

                if legal == True:

                    if promotion == True:
                        print('options to promote to')
                        print('1 queen')
                        print('2 rook')
                        print('3 bishop')
                        print('4 knight')
                        userChoosesPromotion = input('enter which number you\'d like to promote into: ')
                        while userChoosesPromotion.isdigit() == False and userChoosesPromotion < 1 and userChoosesPromotion > 4:
                            print('enter a valid number')
                            userChoosesPromotion = input('enter which number you\'d like to promote into')
                        if pieceMovingColour == 'white':
                            if int(userChoosesPromotion) == 1:
                                pieceToPlace = 'WQ'
                            elif int(userChoosesPromotion) == 2:
                                pieceToPlace = 'WR'
                            elif int(userChoosesPromotion) == 3:
                                pieceToPlace = 'WB'
                            elif int(userChoosesPromotion) == 4:
                                pieceToPlace = 'WN'
                        if pieceMovingColour == 'black':
                            if int(userChoosesPromotion) == 1:
                                pieceToPlace = 'BQ'
                            elif int(userChoosesPromotion) == 2:
                                pieceToPlace = 'BR'
                            elif int(userChoosesPromotion) == 3:
                                pieceToPlace = 'BB'
                            elif int(userChoosesPromotion) == 4:
                                pieceToPlace = 'BN'

                        chessBoard.promotionPieces(pieceToPlace, squareMouseOn)
                        chessBoard.removePiece(pastSquare)
                        promotion = False
                    else:
                        chessBoard.movePiece(squareMouseOn, pastSquare)

                    #check if current player is in check
                    #print()
                    #print('CHECKING IF THE CURRENT KING IS IN CHECK')
                    #print(whoseMove, 'just played their move')
                    if whoseMove == 'white':
                        opponentColour = 'black'
                        pastMovesCount = pastWhiteMovesCount
                    else:
                        opponentColour = 'white'
                        pastMovesCount = pastBlackMovesCount

                    piecesOnBoardCurrentPlayer = chessBoard.checkPiecesOnBoard(whoseMove)[1]
                    for i in range(len(players)):
                        colour = players[i].getPlayerColour()
                        if colour == whoseMove:
                            players[i].updatePiecesOnBoard(piecesOnBoardCurrentPlayer)
                    #print(piecesOnBoardCurrentPlayer)
                    kingPosCurrentPlayer = chessBoard.checkPiecesOnBoard(whoseMove)[0]
                    #print('current king is on', kingPosCurrentPlayer)

                    playerLegalMoves = None
                    for i in range(len(piecesOnBoardCurrentPlayer)):
                        squareCheckingCurrent = piecesOnBoardCurrentPlayer[i][0]
                        pieceToCheckCurrent = piecesOnBoardCurrentPlayer[i][1]

                        # checking if opposing pieces are checking the current king
                        if pieceToCheckCurrent == 'white pawn':
                            checking = True
                            playerLegalMoves = chessBoard.checkWhitePawnMoves(kingPosCurrentPlayer, squareCheckingCurrent, 'white', move, moveFrom, checking)
                            # print('legal white pawn moves are:', playerLegalMoves)
                            checking = False
                        elif pieceToCheckCurrent == 'black pawn':
                            checking = True
                            playerLegalMoves = chessBoard.checkBlackPawnMoves(kingPosCurrentPlayer, squareCheckingCurrent, 'black', move, moveFrom, checking)
                            # print('legal black pawn moves are:', playerLegalMoves)
                            checking = False
                        elif pieceToCheckCurrent == 'white queen' or pieceToCheckCurrent == 'black queen':
                            checking = True
                            playerLegalMoves = chessBoard.checkQueenMoves(kingPosCurrentPlayer, squareCheckingCurrent, opponentColour, checking)
                            # print('legal queen moves are:', playerLegalMoves)
                            checking = False
                        elif pieceToCheckCurrent == 'white bishop' or pieceToCheckCurrent == 'black bishop':
                            checking = True
                            playerLegalMoves = chessBoard.checkBishopMoves(kingPosCurrentPlayer, squareCheckingCurrent, opponentColour, checking)
                            # print('legal bishop moves are:', playerLegalMoves)
                            checking = False
                        elif pieceToCheckCurrent == 'white rook' or pieceToCheckCurrent == 'black rook':
                            checking = True
                            playerLegalMoves = chessBoard.checkRookMoves(kingPosCurrentPlayer, squareCheckingCurrent, opponentColour, checking)
                            # print('legal rook moves are:', playerLegalMoves)
                            checking = False
                        elif pieceToCheckCurrent == 'white knight' or pieceToCheckCurrent == 'black knight':
                            checking = True
                            playerLegalMoves = chessBoard.checkKnightMoves(kingPosCurrentPlayer, squareCheckingCurrent, opponentColour, checking)
                            # print('legal knight moves are:', playerLegalMoves)
                            checking = False
                        elif pieceToCheckCurrent == 'white king' or pieceToCheckCurrent == 'black king':
                            checking = True
                            playerLegalMoves = chessBoard.checkKingMoves(kingPosCurrentPlayer, squareCheckingCurrent, opponentColour, whiteKingMoved, blackKingMoved, checking)
                            # print('legal king moves are:', playerLegalMoves)
                            checking = False

                        if playerLegalMoves != None:
                            for count in range(len(playerLegalMoves)):
                                if playerLegalMoves[count] == kingPosCurrentPlayer:
                                    print(opponentColour, 'put', whoseMove, 'into check!')
                                    currentKingInCheck = True
                            if currentKingInCheck == True:
                                #print('THE', whoseMove, 'KING IS IN CHECK. THE LOOP SHOULD HAVE ENDED NOW!')
                                chessBoard.kingInCheckHighlight(kingPosCurrentPlayer, False)
                                # print('make another move, you are in check!')
                                break
                            #else:
                                #print('the current player\'s king is not in check')

                    # print('current player\'s king is in check?:', currentKingInCheck)
                    # print()
                    if currentKingInCheck == True:
                        chessBoard.movePiece(pastSquare, squareMouseOn)
                        break

                    #print('CHECKING IF THE OPPOSING KING IS IN CHECK')

                    piecesOnBoardOpposing = chessBoard.checkPiecesOnBoard(opponentColour)[1]
                    for i in range(len(players)):
                        colour = players[i].getPlayerColour()
                        if colour != whoseMove:
                            players[i].updatePiecesOnBoard(piecesOnBoardOpposing)
                    # print(piecesOnBoardOpposing)
                    #print(piecesOnBoardOpposing)
                    kingPosOpposing = chessBoard.checkPiecesOnBoard(opponentColour)[0]
                    #print('the opposing king is on', kingPosOpposing)

                    opponentKingHasMoves = False
                    checking = True
                    checkOppKingMoves = chessBoard.checkKingMoves(squareMouseOn, kingPosOpposing, opponentColour, whiteKingMoved, blackKingMoved, checking)
                    checking = False
                    if checkOppKingMoves == []:
                        squaresOpposingKingCanGoTo = 0
                        checkOppKingMoves = 0
                    else:
                        squaresOpposingKingCanGoTo = len(checkOppKingMoves)
                        opponentKingHasMoves = True
                    # print('the opponent\'s king can go to this number of squares:', squaresOpposingKingCanGoTo)
                    # print('the opponent\'s king could possibly go to these squares:', checkOppKingMoves)

                    opponentMoves = []
                    opponentMovesCount = {}

                    for i in range(len(piecesOnBoardOpposing)):
                        opposingLegalMoves = None
                        squareCheckingOpposing = piecesOnBoardOpposing[i][0]
                        pieceToCheckOpposing = piecesOnBoardOpposing[i][1]

                        # checking if current player's pieces are checking the opposing king
                        if pieceToCheckOpposing == 'white pawn':
                            checking = True
                            opposingLegalMoves = chessBoard.checkWhitePawnMoves(kingPosOpposing, squareCheckingOpposing, 'white', move, moveFrom, checking)
                            # print('legal white pawn moves are:', opposingLegalMoves)
                            checking = False
                        elif pieceToCheckOpposing == 'black pawn':
                            checking = True
                            opposingLegalMoves = chessBoard.checkBlackPawnMoves(kingPosOpposing, squareCheckingOpposing, 'black', move, moveFrom, checking)
                            # print('legal black pawn moves are:', opposingLegalMoves)
                            checking = False
                        elif pieceToCheckOpposing == 'white queen' or pieceToCheckOpposing == 'black queen':
                            checking = True
                            opposingLegalMoves = chessBoard.checkQueenMoves(kingPosOpposing, squareCheckingOpposing, whoseMove, checking)
                            # print('legal queen moves are:', opposingLegalMoves)
                            checking = False
                        elif pieceToCheckOpposing == 'white bishop' or pieceToCheckOpposing == 'black bishop':
                            checking = True
                            opposingLegalMoves = chessBoard.checkBishopMoves(kingPosOpposing, squareCheckingOpposing, whoseMove, checking)
                            # print('legal bishop moves are:', opposingLegalMoves)
                            checking = False
                        elif pieceToCheckOpposing == 'white rook' or pieceToCheckOpposing == 'black rook':
                            checking = True
                            opposingLegalMoves = chessBoard.checkRookMoves(kingPosOpposing, squareCheckingOpposing, whoseMove, checking)
                            # print('legal rook moves are:', opposingLegalMoves)
                            checking = False
                        elif pieceToCheckOpposing == 'white knight' or pieceToCheckOpposing == 'black knight':
                            checking = True
                            opposingLegalMoves = chessBoard.checkKnightMoves(kingPosOpposing, squareCheckingOpposing, whoseMove, checking)
                            # print('legal knight moves are:', opposingLegalMoves)
                            checking = False

                        # opponentMoves.append(squareCheckingOpposing)

                        #print('in opposing legal moves:', opposingLegalMoves)
                        #print('in opponent moves:', opponentMoves)

                        if opposingLegalMoves != None:
                            for a in range(len(opponentMoves)):
                                for b in range(len(opposingLegalMoves)):
                                    if opponentMoves[a] == opposingLegalMoves[b]:
                                        #print('moves match! this square is protected!')
                                        #print(opponentMoves[a], 'matches with', opposingLegalMoves[b])
                                        if opponentMoves[a] in opponentMovesCount:
                                            repeated = opponentMovesCount[opponentMoves[a]] + 1
                                            opponentMovesCount.update({opponentMoves[a]: repeated})
                                        else:
                                            opponentMovesCount.update({opponentMoves[a]: 1})

                        #print('in repeated opponent moves count:', opponentMovesCount)
                        #print()

                        # print('piece checking is on:', squareCheckingOpposing)

                        if opposingLegalMoves != None:
                            for count in range(len(opposingLegalMoves)):
                                opponentMoves.append(opposingLegalMoves[count])
                                if opposingLegalMoves[count] == kingPosOpposing:
                                    print(whoseMove, 'put', opponentColour, 'into check!')
                                    opposingKingInCheck = True
                            if opposingKingInCheck == True and currentKingInCheck == False:
                                #print('THE', opponentColour, 'KING IS IN CHECK. THE LOOP SHOULD HAVE ENDED NOW!')
                                chessBoard.kingInCheckHighlight(kingPosOpposing, False)
                                break
                            #else:
                                #print('the opposing player\'s king is not in check')

                    #print('in opponentMoves:', opponentMoves)
                    #print(opponentMovesCount)

                    if opposingKingInCheck == True:
                        bothKingAndPlayerMoves = []
                        for x in range(squaresOpposingKingCanGoTo):
                            # print('king can go to', checkOppKingMoves[x])
                            for y in range(len(opponentMoves)):
                                if opponentMoves[y] == checkOppKingMoves[x]:
                                    #print('opponent move and king move matches!')
                                    bothKingAndPlayerMoves.append(opponentMoves[y])
                            if checkOppKingMoves[x] in pastMovesCount:
                                bothKingAndPlayerMoves.append(checkOppKingMoves[x])
                                #print(checkOppKingMoves[x], 'is protected how many times?:', pastMovesCount[checkOppKingMoves[x]])
                        #print(squaresOpposingKingCanGoTo)
                        #print('the opposing king and the current player can both go to these squares:', bothKingAndPlayerMoves)

                        if squaresOpposingKingCanGoTo == len(bothKingAndPlayerMoves):
                            print('CHECKMATE!')
                            print(whoseMove, 'wins!')
                            checkmate = True

                    if checkmate == True:
                        running = False
                        break

                    #print('opposing king is in check?:', opposingKingInCheck)
                    #print()

                    #check what has been moved
                    print(piece, 'moved from', pastSquare, 'to', squareMouseOn)
                    if currentKingInCheck == True:
                        print('make another move, you are in check!')
                    else:
                        move = squareMouseOn
                        moveFrom = pastSquare
                        moveStatus = 'just moved'
                        moveNum += 0.5
                        if whoseMove == 'white':
                            pastWhiteMovesCount = opponentMovesCount
                            whoseMove = 'black'
                            print()
                        else:
                            pastBlackMovesCount = opponentMovesCount
                            whoseMove = 'white'
                            print()

                    print('it is', whoseMove, 'to play')
                    for i in range(len(players)):
                        colour = players[i].getPlayerColour()
                        if colour == whoseMove:
                            playerWhoseMove = players[i].getPlayerType()
                            print('it is the', playerWhoseMove + '\'s turn')


                    if whoseMove == 'white':
                        print('this is move number', int(moveNum))

            else:
                moveStatus = 'not yet moved'

            if currentKingInCheck == False:
                pastSquareHasPiece = currentSquareHasPiece
                pastSquare = squareMouseOn
                pastMove = move
                pastMoveFrom = moveFrom
                pastMovesCount = opponentMovesCount

            currentKingInCheck = False
            opposingKingInCheck = False

            chessBoard.keepPiecesOn()
            pygame.display.flip()
            pygame.display.update()

        elif event.type == pygame.QUIT:
            running = False