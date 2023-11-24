from random import choice

# Game Classes
class Player:
    def __init__(self, dice):
        self._dice = dice

    def tossDice(self):
        return self._dice

class Dice:
    def __init__(self):
        self._dice = [1, 2, 3, 4, 5, 6]
    
    def rollDice(self):
        return choice(self._dice)

class Board:
    def __init__(self, player, boardLocation, dice):
        self._player = player
        self._boardLocation = boardLocation
        self._dice = dice
        self._ladders = {"1": 38, "4": 14, "8": 30, "28": 76, "21": 42, "50": 67, "71": 92, "80": 99}
        self._snakes = {"97": 78, "95": 56, "88": 24, "62": 18, "48": 26, "36": 6, "32": 10}

    def move(self):
        boardLocation = self._boardLocation + self._dice

        # Dice Roll Message
        if boardLocation >= 100:
            print(f"{self._player} rolled the dice landed at '{self._dice}'\nNow {self._player} is moving forward from tile {self._boardLocation} to tile 100")
        else:
            print(f"{self._player} rolled the dice landed at '{self._dice}'\nNow {self._player} is moving forward from tile {self._boardLocation} to tile {boardLocation}")

        # Ladder Logic
        for tile in self._ladders:
            if str(boardLocation) == tile:
                print(f"{self._player} stepped on the bottom of a ladder in tile {boardLocation} and is now moving up to tile {self._ladders[tile]}")
                return self._ladders[tile]
            
        # Snake Logic
        for tile in self._snakes:
            if str(boardLocation) == tile:
                print(f"{self._player} stepped on the head of a snake in tile {boardLocation} and is now moving down to tile {self._snakes[tile]}")
                return self._snakes[tile]

        return (self._boardLocation + self._dice)

# In-Game Function
def rollDice(player, location):
    dice = Player(Dice().rollDice())
    board = Board(player, location, dice.tossDice())
    return board.move()

# Welcome Message
print("Welcome to Snake & Ladder created by Argal Games")

# In-Game Variables
playerName = input("Enter your name: ")
playerCurrentBoardLocation = 0
computerCurrentBoardLocation = 0
divider = "-"*50

# Game Mechanics Explanation
print("Game Mechanics:\n1. Each player puts their counter on board location 0.\n2. You will be playing against a computer and take it in turns to roll the dice. Move your counter forward the number of tiles shown on the dice.\n3. If your counter lands at the bottom of a ladder, you can move up to the top of the ladder.\n4. If your counter lands on the head of a snake, you must slide down to the bottom of the snake.\n5. The first player to get to the tile 100 is the winner.")

# Initial User Input
userInput = input("Roll Dice? (Y) Yes / (C) Concede: ")

# Game Logic
while True:

    print(divider)

    # Snake and Ladder Route Reference
    print("Board Reference:\nLadder Route: (1 -> 38) (4 -> 14) (8 -> 30) (28 -> 76) (21 -> 42) (50 -> 67) (71 -> 92) (80 -> 99)\nSnake Route: (97 -> 78) (95 -> 56) (88 -> 24) (62 -> 18) (48 -> 26) (36 -> 6) (32 -> 10)")

    print(divider)

    # Player Action
    if userInput.lower() == "y":
        playerCurrentBoardLocation = rollDice(playerName, playerCurrentBoardLocation)
        # Game Message For Player
        if playerCurrentBoardLocation >= 100:
            print(f"{playerName} current board location is at tile 100!\n{divider}")
        else:
            print(f"{playerName} current board location is at tile {playerCurrentBoardLocation}!\n{divider}")
    elif userInput.lower() == "c":
        print("Computer Wins!")
        break
    else:
        print("Invalid Input")
    
    # Player Winning Condition
    if playerCurrentBoardLocation >= 100:
        print(f"{playerName} Wins!")
        break

    if userInput.lower() != "y":
        pass
    else:
        # Computer Action and Player Winning Condition
        computerCurrentBoardLocation = rollDice("Computer", computerCurrentBoardLocation)
        if computerCurrentBoardLocation >= 100:
            print(f"Computer current board location is at tile 100!\n{divider}")
        else:
            print(f"Computer current board location is at tile {computerCurrentBoardLocation}!\n{divider}")

    # Computer Winning Condition
    if computerCurrentBoardLocation >= 100:
        print("Computer Wins!")
        break

    userInput = input("Roll Dice? (Y) Yes / (C) Concede: ")

# TODO: Add play again option
# TODO: Randomized which player gets to start to roll the dice
# TODO: Add multi player option
# TODO: Add graphical interface