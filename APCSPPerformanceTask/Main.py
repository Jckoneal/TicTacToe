from colored import Fore, Back, Style
import random

winX = False
winO = False
i = 0
#Define function Check if win conditions are met for player X
def checkWinX():
    # Check if player X has won
    for line in win_combinations:
        if all(squares[i] == "X" for i in line):
            return True
    return False

def checkWinO():
    # Check if player O has won
    for line in win_combinations:
        if all(squares[i] == "O" for i in line):
            return True
    return False

def whoWon(position):
    # Check if the specified player has won
    for line in win_combinations:
        if all(squares[i] == position for i in line):
            return True
    return False

win_combinations = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
    [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
    [0, 4, 8], [2, 4, 6]              # Diagonals
]


def checkDraw():
    for (ind, s) in enumerate(squares):
        if s == squaresC[ind] and winX == False and winO == False:
            continue
        else:
            return False
    return True
#Make list of Squares and a list of squares that doesnt change
squares = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
squaresC = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

#Define function to Print board
def printSquares():
    string=squares[0] + "|" + squares[1] + "|" + squares[2] + "\n" + squares[3] + "|" + squares[4] + "|" + squares[5] + "\n" + squares[6] + "|" + squares[7] + "|" + squares[8]

    string = string.replace("X", f"{Fore.red}X{Fore.white}")
    string = string.replace("O", f"{Fore.blue}O{Fore.white}")

    print(f"{Style.bold + string + Style.reset}")
  
#Ask for the input
def playerMove():
  global i
  if i < 9 and winO == False and winX == False:
    move=''
    while type(move) is not int:
      try:
        move = int(input("What square would you like to choose? ")) 
      except:
        print("Please enter a number: ")
    move = move-1
  # if move >= 8 and move <= 0:
  #   move = int(input("Try again, that square is not on the board: "))
  #   move = move-1
  # else:
  #   move = int(input("Try again, that square is taken: "))
  squares[move] = playerPosition
  i = i+1

# ComputerMove
def computerMove():
    global i
    if i >= 1:
      if computerPosition == "X":
        bestScore = -1000 # Adjust initial bestScore
        bestMove = 0
        for (ind, s) in enumerate(squares):
            if s == squaresC[ind]:
                squares[ind] = computerPosition
                score = minimax(squares, 0, False, computerPosition)
                squares[ind] = s
                if bestScore < score:
                  bestScore = score
                  bestMove = ind
            

        if i < 9:
            squares[bestMove] = computerPosition
      else:
        bestScore = -1000 # Adjust initial bestScore
        bestMove = 0
        for (ind, s) in enumerate(squares):
            if s == squaresC[ind]:
                squares[ind] = computerPosition
                score = minimax(squares, 0, False, computerPosition)
                squares[ind] = s
                if bestScore < score:
                  bestScore = score
                  bestMove = ind
                

        if i < 9:
            squares[bestMove] = computerPosition
    else:
       bestMove = random.randint(0,8)
       squares[bestMove] = computerPosition
    i += 1

# minimax algorithm
def minimax(squares, depth, isMaximizing, computerPosition):
    if computerPosition == "X":
      if whoWon(computerPosition):
          return 10 - depth  # Adjust the score to favor shorter paths
      elif whoWon(playerPosition):
          return  -depth - 10  # Adjust the score to favor shorter paths
      elif checkDraw():
          return 0

      if isMaximizing:
          bestScore = -1000
          for (ind, s) in enumerate(squares):
              if s == squaresC[ind]:
                  squares[ind] = computerPosition
                  score = minimax(squares, depth + 1, False, computerPosition)
                  squares[ind] = s
                  if bestScore < score:
                    bestScore = score
          return bestScore
      else:
          bestScore = 1000
          for (ind, s) in enumerate(squares):
              if s == squaresC[ind]:
                  squares[ind] = playerPosition
                  score = minimax(squares, depth + 1, True, computerPosition)
                  squares[ind] = s
                  if bestScore > score:
                    bestScore = score
          return bestScore
    else:
      if whoWon(computerPosition):
          return 10 - depth  # Adjust the score to favor shorter paths
      elif whoWon(playerPosition):
          return  -depth - 10  # Adjust the score to favor shorter paths
      elif checkDraw():
          return 0
      if isMaximizing:
          bestScore = -1000
          for (ind, s) in enumerate(squares):
              if s == squaresC[ind]:
                  squares[ind] = computerPosition
                  score = minimax(squares, depth + 1, False, computerPosition)
                  squares[ind] = s
                  if bestScore < score:
                    bestScore = score
          return bestScore
      else:
        bestScore = 1000
        for (ind, s) in enumerate(squares):
            if s == squaresC[ind]:
                squares[ind] = playerPosition
                score = minimax(squares, depth + 1, True, computerPosition)
                squares[ind] = s
                if bestScore > score:
                  bestScore = score
        return bestScore




#Game starts:  
#Asks player to start as O or X
playerPosition = str.upper(input("Welcome to Tic Tac Toe! Would you like to start as X or O? "))
while playerPosition != "X" and playerPosition != "O":
  playerPosition = str.upper(input("Please pick X or O. "))
#
if playerPosition == "X":
  print("You will go first.")
  computerPosition = "O"
  printSquares()
  i = 0

  while winO == False and winX == False and i < 9:
    playerMove()
    if whoWon(playerPosition):
       printSquares()
       print("You won!")
       break
    if checkDraw():
      print("Draw")
    computerMove()
    if whoWon (computerPosition):
       printSquares()
       print("Computer won!")
       break
    if checkDraw():
      print("Draw")
    printSquares()
    
else:
  print("I will go first.")
  computerPosition = "X"
  i = 0
  while winO == False and winX == False and i < 9:
    computerMove()
    if whoWon (computerPosition):
       printSquares()
       print("Computer won!")
       break
    if checkDraw():
      print("Draw")
    printSquares()
    playerMove()
    if whoWon(playerPosition):
       printSquares()
       print("You won!")
       break
    if checkDraw():
      print("Draw")
    
if checkDraw():
  print("Draw")
#Game is over