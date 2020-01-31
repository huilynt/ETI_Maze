import mock
from src.main import *

maze = [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'O', 'O', 'O', 'X', 'O', 'A', 'X'],
        ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'X'],
        ['X', 'O', 'X', 'O', 'X', 'O', 'O', 'X'],
        ['X', 'O', 'X', 'O', 'X', 'X', 'O', 'X'],
        ['X', 'O', 'X', 'O', 'X', 'O', 'O', 'X'],
        ['X', 'O', 'X', 'O', 'O', 'O', 'X', 'X'],
        ['X', 'B', 'X', 'X', 'X', 'X', 'X', 'X']]


def test_read_file():
    with mock.patch('builtins.input', return_value="maze.csv"):
        assert maze == read_file()
