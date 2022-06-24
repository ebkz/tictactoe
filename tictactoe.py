from random import randint

class TicTacToe:
  def __init__(self):
    self.xo = 'X'
    self.ox = 'O'

  def xoro(self):
    #Allows Player to Choose X or O.
    print('Player, do you want to be X or O? Type X or O. Note: If you choose multiplayer mode, Player 1 will be what you select.')
    self.xo = input('Choose: ')
    if self.xo == 'X':
      self.ox = 'O'
    elif self.xo == 'O':
      self.ox = 'X'
    else:
      print('That is not an option. We will choose X for you. ')
      self.xo = 'X'
      self.ox = 'O'
    #Making self.ox based on self.xo. You will see this later in the playergame() function.
    self.xo = self.xo
    self.ox = self.ox
  def menu(self):
    self.xoro()
    board = [0,1,2,3,4,5,6,7,8,9]
    print('''
    Welcome to TicTacToe!
    MAIN MENU:
    1: Play the Game with another player.
    2: Play the Game with the CPU.
    3: Exit TicTacToe.
    ''')
    #Main Menu
    menuchoice = input('Choose an option: ')
    if menuchoice == '1':
      print('Ok, taking you to the game...')
      print('Welcome to the player game of TicTacToe!')
      self.playergame(board)
    elif menuchoice == '2':
      print('Ok, taking you to the game...')
      print('Welcome to the CPU game of TicTacToe!')
      self.cpugame(board)
    elif menuchoice == '3':
      print('Taking you to the command line...')
      pass
    #Menu Choices
    elif menuchoice == 'bobthebuilder':
      print('''
      Bob The Builder, Can he do it. Bob The Builder, Yes He Can!
      CREDITS!
      ebkz Group
      Me
      And... of course, Bob The Builder because he can do EVERYTHING!
      Email me at [censored email adress.] Just find it on github
      ''')
      self.menu()
    #Easter Egg;)
    else:
      print('That is not an option')
      self.menu()
    #No Option

  #Player Game Function
  def playergame(self, board):
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
    #Board Layout
    print("Player 1's Turn!")
    choice = input('Choose: ')
    if int(choice) > 9 or int(choice) < 1:
      print('That is not an option. Restarting Turn...')
      self.playergame(board)
    elif int(choice) < 10 and int(choice) > 0 and board[int(choice)] != 'X' and board[int(choice)] != 'O':
      print(f'You Chose Spot {choice}')
      board[int(choice)] = self.xo
    elif board[int(choice)] == 'X' or board[int(choice)] == 'O':
      print('That is not an option. Restarting Turn...')
      self.playergame(board)
    #Using Player Options to Change the board
    j = self.xo
    a = board[1]
    b = board[2]
    c = board[3]
    d = board[4]
    e = board[5]
    f = board[6]
    g = board[7]
    h = board[8]
    i = board[9]
    if (
      j == a and j == b and j == c or 
      j == a and j == d and j == g or 
      j == a and j == e and j == i or 
      j == b and j == e and j == h or 
      j == c and j == f and j == i or
      j == d and j == e and j == f or 
      j == g and j == h and j == i
    ):
      print('Player 1 Won!')
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
            |         |''')
      self.menu()
    #Check if player 1 won
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
    #board layout again
    print("Player 2's Turn!")
    choice2 = input('Choose: ')
    if int(choice2) > 9 or int(choice2) < 1:
      print('That is not an option. Restarting Turn...')
      board[int(choice)] = int(choice)
      self.playergame(board)
    elif int(choice2) < 10 and int(choice2) > 0 and board[int(choice2)] != 'X' and board[int(choice2)] != 'O':
      print(f'You Chose Spot {choice2}')
      board[int(choice2)] = self.ox
    elif board[int(choice2)] == 'X' or board[int(choice2)] == 'O':
      print('That is not an option. Restarting Turn...')
      board[int(choice)] = int(choice)
      self.playergame(board)
    #Changing the board, again
    a = board[1]
    b = board[2]
    c = board[3]
    d = board[4]
    e = board[5]
    f = board[6]
    g = board[7]
    h = board[8]
    i = board[9]
    j = self.ox
    #Since all the variables I used for the checking win for player 1 are still there, I only need to change the x into o or the o into x to check if player 2 won.
    if j == a and j == b and j == c or j == a and j == d and j == g or j == a and j == e and j == i or j == b and j == e and j == h or j == c and j == f and j == i or j == d and j == e and j == f or j == g and j == h and j == i:
      print('Player 2 Won!')
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
            |         |''')
      self.menu()
    self.playergame(board)

  #CPU Game Function
  def cpugame(self,board):
    pass


game = TicTacToe()
game.menu()