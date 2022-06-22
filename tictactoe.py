from random import randint
def menu():
  board = [0,1,2,3,4,5,6,7,8,9]
  print('''
Welcome to TicTacToe!
MAIN MENU:
1: Play the Game with another player.
2: Play the Game with the CPU.
3: Exit TicTacToe.
  ''')
  menuchoice = input('Choose an option: ')
  if menuchoice == '1':
    print('Ok, taking you to the game...')
    print('Welcome to the player game of TicTacToe!')
    playergame(board)
  elif menuchoice == '2':
    print('Ok, taking you to the game...')
    board = [0,1,2,3,4,5,6,7,8,9]
    cpugame(board)
  elif menuchoice == '3':
    print('Taking you to the command line...')
    pass
  else:
    print('That is not an option')
    menu()

def playergame(board):
  print(f'''
           |         |         
      {board[1]}    |    {board[2]}    |    {board[3]}
           |         |
  ---------|---------|---------
           |         |         
      {board[4]}    |    {board[5]}    |    {board[6]}
           |         |
  ---------|---------|---------
           |         |         
      {board[7]}    |    {board[8]}    |    {board[9]}
           |         |
  ''')
  print("Player 1's Turn!")
  choice = input('Choose: ')
  if int(choice) > 9 or int(choice) < 1:
    print('That is not an option. Restarting Turn...')
    playergame(board)
  elif int(choice) < 10 and int(choice) > 0 and board[int(choice)] != 'X' and board[int(choice)] != 'O':
    print(f'You Chose Spot {choice}')
    board[int(choice)] = 'X'
  elif board[int(choice)] == 'X' or board[int(choice)] == 'O':
    print('That is not an option. Restarting Turn...')
    playergame(board)
  j = 'X'
  a = board[1]
  b = board[2]
  c = board[3]
  d = board[4]
  e = board[5]
  f = board[6]
  g = board[7]
  h = board[8]
  i = board[9]
  if j == a and j == b and j == c or j == a and j == d and j == g or j == a and j == e and j == i or j == b and j == e and j == h or j == c and j == f and j == i or j == d and j == e and j == f or j == g and j == h and j == i:
    print('Player 1 Won!')
    menu()
  print(f'''
           |         |         
      {board[1]}    |    {board[2]}    |    {board[3]}
           |         |
  ---------|---------|---------
           |         |         
      {board[4]}    |    {board[5]}    |    {board[6]}
           |         |
  ---------|---------|---------
           |         |         
      {board[7]}    |    {board[8]}    |    {board[9]}
           |         | ''')
  print("Player 2's Turn!")
  choice2 = input('Choose: ')
  if int(choice2) > 9 or int(choice2) < 1:
    print('That is not an option. Restarting Turn...')
    board[int(choice)] = int(choice)
    playergame(board)
  elif int(choice2) < 10 and int(choice2) > 0 and board[int(choice2)] != 'X' and board[int(choice2)] != 'O':
    print(f'You Chose Spot {choice2}')
    board[int(choice2)] = 'O'
  elif board[int(choice2)] == 'X' or board[int(choice2)] == 'O':
    print('That is not an option. Restarting Turn...')
    board[int(choice)] = int(choice)
    playergame(board)
  j = 'O'
  if j == a and j == b and j == c or j == a and j == d and j == g or j == a and j == e and j == i or j == b and j == e and j == h or j == c and j == f and j == i or j == d and j == e and j == f or j == g and j == h and j == i:
    print('Player 2 Won!')
    menu()
  playergame(board)

def cpugame():
  print('Welcome to the CPU game of TicTacToe!')
menu()