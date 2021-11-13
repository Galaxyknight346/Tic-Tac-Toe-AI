# main.py
#Import Neccesary Files/Libraries
import functions
import random
import time

#Make the board
a = functions.makeBoard()

#Choose who is going to play first
c = random.randint(0,1)
#Print Beggining Information
print("You are playing as X\nThe computer is O.")
print("The max value for both row and column is 3. If you put anything above or below those, values, an error will be reached. Good luck beating my AI and have fun! :)")
time.sleep(10)


#Loop the game:
while True:
  print('\033c')
  functions.printBoard(a)
  if c%2 == 0: functions.getInput(a)
  else: functions.ai(a)
  b = functions.check(a)
  if b == "X":
    print("User Wins! :D\n Final Board: ")
    functions.printBoard(a)
    break
  elif b == "O":
    print("Computer Wins. :(\n Final Board: ")
    functions.printBoard(a)
    break
  elif b =="t":
    print("Tie! :/")
    break
  c += 1
  
