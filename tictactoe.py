from typing import List, Iterable

def input_candidate(prompt: str, candidates: Iterable[str]) -> str:
  while True:
    choice = input(prompt)
    if choice in candidates:
      return choice
    print('This is not an option.')

def is_not_marker(v):
  return v != 'X' and choice != 'O'

def get_winner(board): # return X if X win, return O if O win, return None if no winner
  bars = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [1,4,7],
    [2,5,8],
    [3,6,9],
    [1,5,9],
    [3,5,7]
  ]
  for [l, m, r] in bars:
    if board[l] == board[m] == board[r]:
      return board[l]
  return None


def test_get_winner():
  board = [ 0,
    0,0,1,
    0,0,1,
    0,0,1
  ]
  assert get_winner(board) == 1

def from_input_get_result(userinput: str, options):
  #
  if userinput <= 0 or type(userinput) != int or userinput >= len(options):
    return None
  else:
    return 

class TicTacToe:

  def __init__(self):
    self.p1_avatar = 'X'
    self.p2_avatar = 'O'
    self.board = list(range(10)) # reserve index 0 for simplicity in calculation

  def input_valid_choice(self, prompt):
    input_candidates("Choose: ", self.board.filter(is_not_marker))

  def choose_avatar(self, player_name):
    print(f'{player_name}, do you want to be X or O? Type X or O.')
    input_candidate("Choose: ",[ 'X', 'O' ])

  def menu(self):
    self.choose_avatar('Player 1')
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
      self.player_game(board)
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
      Email me at ebkzcontact@gmail.com
      ''')
      self.menu()
    #Easter Egg;)
    else:
      print('That is not an option')
      self.menu()
    #No Option

  def mutate(self, choice, value):
    pass
  
  #Player Game Function
  def player_game(self, board):
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
    choice = self.input_valid_choice('Player 1 enter (1-9): ')
    #Using Player Options to Change the board
    j = self.p1_avatar
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
    choice = input('Choose: ')
    input_1to9(choice)
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
    j = self.p2_avatar
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
    self.player_game(board)

  #CPU Game Function
  def cpugame(self,board):
    pass

if __name__ == '__main__':
  game = TicTacToe()
  game.menu()
  #Bug List
  '''
  Cannot type non integers in to player moves. If I typed fg in Player 1's Choice, I would receive an error
  Check if the boards look right.
  '''