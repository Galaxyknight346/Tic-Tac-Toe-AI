import random

def makeBoard():
  a = " "
  board = [[a for i in range(3)]for j in range(3)]
  return board

def printBoard(board):
  c = 0
  for i in range(5):
    if i%2 == 0:
      print(" "+" | ".join(board[c]))
      c += 1
    else:
      print("---+---+---")
    
def getInput(board):
  userrow = int(input("Row(1-3): "))
  userrow -= 1
  usercol = int(input("Column(1-3): "))
  usercol -= 1
  if(board[userrow][usercol] == "X" or board[userrow][usercol]== "O" ):
    getInput(board)
  else:
    board[userrow][usercol] = "X"
  
def compInput(board):
  comprow = random.randint(1,3)
  compcol = random.randint(1,3)
  comprow -= 1
  compcol -= 1
  while board[comprow][compcol] != " ":
    comprow = random.randint(1,3)
    compcol = random.randint(1,3)
    comprow -= 1
    compcol -= 1
  board[comprow][compcol] = "X"
  
def check(board):
  for i in range(len(board)):
    if (board[i][0] == board[i][1] == board[i][2]) and board[i][0] != " ":
      return board[i][0]
    if (board[0][i] == board[1][i] == board[2][i]) and board[0][i] != " ":
      return board[0][i]
  if (board[2][0] == board[1][1] == board[0][2]) and board[2][0] != " ":
    return board[2][0]
  if (board[0][0] == board[1][1] == board[2][2]) and board[0][0] != " ":
    return board[0][0]
  for i in range(len(board)):
    for j in range(len(board[i])):
      if board[i][j] == " ":
        return "in progress"
  return "t"

def ai(board):
  cornerCoords = [[1,1],[0,0],[0,2],[2,2],[2,0],[0,1],[1,2],[2,1],[1,0]]
  for i in range(len(board)):
    for j in range(len(board[i])):
      if board[i][j] == " ":
        board[i][j] = "O"
        if check(board) == "O":
          return board[i][j]
        board[i][j] = " "
  for c in range(len(board)):
    for b in range(len(board[c])):
      if board[c][b] == " ":
        board[c][b] = "X"
        if check(board) == "X":
          board[c][b] = "O"
          return
        board[c][b] = " "
  for i,j in cornerCoords:
    if board[i][j] == " ":
      board[i][j] = "O"
      return
