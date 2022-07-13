from typing import List, Iterable
from .tictactoe import get_winner


def test_get_winner_col():
  board = [-1,
    1,2,0,
    4,5,0,
    7,8,0
  ]
  assert get_winner(board) == 0

def test_get_winner_diag():
  board = [-1,
    1,2,3,
    4,1,6,
    7,8,1
  ]
  assert get_winner(board) == 1

