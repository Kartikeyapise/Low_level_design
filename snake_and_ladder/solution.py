class Player:
    def __init__(self, id, playerName):
        self.__playerName = playerName
        self.__id = id

    def getPlayerName(self):
        return self.__playerName

    def getPlayerId(self):
        return self.__id

    @staticmethod
    def createSamplePlayers():
        return [Player(1, "alex"), Player(2, "bob"), Player(3, "caddy"), Player(4, "demic")]


class Dice:
    def __init__(self, numberOfDice):
        self.__numberOfDice = numberOfDice

    def getNumberOfDice(self):
        return self.__numberOfDice

    def rollDice(self):
        import random
        return random.randint(self.__numberOfDice, self.__numberOfDice * 6)


class Jumper:
    def __init__(self, jumperMap):
        self.__jumperMap = jumperMap


class Board:
    def __init__(self, boardSize, jumpers):
        self.__boardSize = boardSize
        self.__jumpers = jumpers

    def getJumpers(self):
        return self.__jumpers

    @staticmethod
    def createSampleBoard():
        boardSize = 100
        jumpers = {1: 10, 21: 94, 99: 0, 22: 6}
        return Board(boardSize, jumpers)


class Game:
    def __init__(self, dice, players, board):
        self.__dice = dice
        self.__players = players
        self.__board = board
        playersCurrentPositions = {}
        for player in players:
            playersCurrentPositions[player] = 0
        self.__playersCurrentPositions = playersCurrentPositions

    def startGame(self):
        from collections import deque
        playerQueue = deque(self.__players)
        winnerList = []
        while len(playerQueue) > 1:
            currentPlayer = playerQueue.pop()
            isWinner = self.rollDice(self.__dice, currentPlayer, self.__board.getJumpers())
            if isWinner:
                winnerList.append(currentPlayer)
                print(currentPlayer.getPlayerName() + " won")
            else:
                playerQueue.appendleft(currentPlayer)

        winnerList.append(playerQueue.pop())
        print("\ngave over. Following is the ranking:")
        for i, player in enumerate(winnerList):
            print(str(i + 1) + ": " + player.getPlayerName())

    def rollDice(self, dice, currentPlayer, jumperMap):
        print(currentPlayer.getPlayerName()+" is rolling.....")
        nextPosition = dice.rollDice() + self.__playersCurrentPositions[currentPlayer]
        if nextPosition > 100:
            nextPosition = self.__playersCurrentPositions[currentPlayer]
        nextPosition = jumperMap.get(nextPosition, nextPosition)
        self.__playersCurrentPositions[currentPlayer] = nextPosition
        print(currentPlayer.getPlayerName() + ": " + str(nextPosition))
        if nextPosition == 100:
            return True
        return False


if __name__ == "__main__":
    print("Executed when invoked directly")
    demoPlayers = Player.createSamplePlayers()
    demoDice = Dice(2)
    demoBoard = Board.createSampleBoard()
    demoGame = Game(demoDice, demoPlayers, demoBoard)
    demoGame.startGame()
