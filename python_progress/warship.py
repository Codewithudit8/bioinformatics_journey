## making 5 rows and asking user to where my boat is located : guess colum name  and  row name 
from random import randint

board = []

for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print " ".join(row)

print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
print ship_row
print ship_col
guess_row = int(raw_input("Guess Row: "))
guess_col = int(raw_input("Guess Col: "))

# Write your code below!
if guess_row == ship_row and guess_col == ship_col:
  print "Congratulations! You sank my battleship!"  
else:
  print "You missed my battleship!"
  board[guess_row][guess_col] = "X"
  print_board(board)

## making function inside function 
n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
# Add your function here

def flatten(lists):
  results = []
  for i in lists:
    for j in i:
      results.append(j)
  return results

print flatten(n)
  ## iterating over loops

n = [3, 5, 7]

def total(numbers):
    result = 0
    for i in range(0,len(numbers)):
        result += numbers[i]
    return result
