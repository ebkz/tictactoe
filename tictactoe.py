def menu():
  print('''
  Welcome to TicTacToe!
  Options:
  1. Play The Game
  2. Exit
  ''')
  choice = input("Choose: ")
  if choice == "1":
    print("Ok, Taking you to the game...")
    tictactoe2()
  elif choice == "2":
    print("Returning you to the Command Line...")
  else:
    print("That's not an option.")
board = [1,2,3,4,5,6,7,8,9]
def tictactoe2():
  print(f'''
            |         |         
       {board[0]}    |    {board[1]}    |    {board[2]}   
            |         |   
   ---------|---------|---------
            |         |   
       {board[3]}    |    {board[4]}    |    {board[5]}
            |         |         
   ---------|---------|---------
            |         |   
       {board[6]}    |    {board[7]}    |    {board[8]}
            |         |
  ''')
  player1()
def tictactoe1():
  print(f'''
            |         |         
       {board[0]}    |    {board[1]}    |    {board[2]}   
            |         |   
   ---------|---------|---------
            |         |   
       {board[3]}    |    {board[4]}    |    {board[5]}
            |         |         
   ---------|---------|---------
            |         |   
       {board[6]}    |    {board[7]}    |    {board[8]}
            |         |
  ''')
  player2()
def player2():
  choice = input('Player 2, Choose where to place your marker: ')
  if choice == "1":
    print('Player 2 placed his or her marker on spot 1.')
    board[0] = "O"
  if choice == "2":
    print('Player 2 placed his or her marker on spot 2.')
    board[1] = "O"
  if choice == "3":
    print('Player 2 placed his or her marker on spot 3.')
    board[2] = "O"
  if choice == "4":
    print('Player 2 placed his or her marker on spot 4.')
    board[3] = "O"
  if choice == "5":
    print('Player 2 placed his or her marker on spot 5.')
    board[4] = "O"
  if choice == "6":
    print('Player 2 placed his or her marker on spot 6.')
    board[5] = "O"
  if choice == "7":
    print('Player 2 placed his or her marker on spot 7.')
    board[6] = "O"
  if choice == "8":
    print('Player 2 placed his or her marker on spot 8.')
    board[7] = "O"
  if choice == "9":
    print('Player 2 placed his or her marker on spot 9.')
    board[8] = "O"
  checkwin2()
def player1():
  choice = input('Player 1, Choose where to place your marker: ')
  if choice == "1":
    print('Player 1 placed his or her marker on spot 1.')
    board[0] = "X"
  if choice == "2":
    print('Player 1 placed his or her marker on spot 2.')
    board[1] = "X"
  if choice == "3":
    print('Player 1 placed his or her marker on spot 3.')
    board[2] = "X"
  if choice == "4":
    print('Player 1 placed his or her marker on spot 4.')
    board[3] = "X"
  if choice == "5":
    print('Player 1 placed his or her marker on spot 5.')
    board[4] = "X"
  if choice == "6":
    print('Player 1 placed his or her marker on spot 6.')
    board[5] = "X"
  if choice == "7":
    print('Player 1 placed his or her marker on spot 7.')
    board[6] = "X"
  if choice == "8":
    print('Player 1 placed his or her marker on spot 8.')
    board[7] = "X"
  if choice == "9":
    print('Player 1 placed his or her marker on spot 9.')
    board[8] = "X"
  checkwin1()
def checkwin1():
  x = 'X'
  a = board[0]
  b = board[1]
  c = board[2]
  d = board[3]
  e = board[4]
  f = board[5]
  g = board[6]
  h = board[7]
  i = board[8]
  if a == x and b == x and c == x or a == x and d == x and g == x or a == x and e == x and i == x or b == x and e == x and h == x or c == x and f == x and i == x or c == x and e == x and g == x or d == x and e == x and f == x or g == x and h == x and i == x:
    print('Player 1 Won!')
    menu()
  else:
    tictactoe1()
def checkwin2():
  x = 'O'
  a = board[0]
  b = board[1]
  c = board[2]
  d = board[3]
  e = board[4]
  f = board[5]
  g = board[6]
  h = board[7]
  i = board[8]
  if a == x and b == x and c == x or a == x and d == x and g == x or a == x and e == x and i == x or b == x and e == x and h == x or c == x and f == x and i == x or c == x and e == x and g == x or d == x and e == x and f == x or g == x and h == x and i == x:
    print('Player 2 Won!')
    menu()
  else:
    tictactoe2()

menu()