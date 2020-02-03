import mock
import io

from src.maze_functions import *

maze = [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'O', 'O', 'O', 'X', 'O', 'A', 'X'],
        ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'X'],
        ['X', 'O', 'X', 'O', 'X', 'O', 'O', 'X'],
        ['X', 'O', 'X', 'O', 'X', 'X', 'O', 'X'],
        ['X', 'O', 'X', 'O', 'X', 'O', 'O', 'X'],
        ['X', 'O', 'X', 'O', 'O', 'O', 'X', 'X'],
        ['X', 'B', 'X', 'X', 'X', 'X', 'X', 'X']]


# Test that the maze is correctly printed out
def test_view_maze():
    with mock.patch('sys.stdout', new=io.StringIO()) as fake_stdout:
        display_maze(maze)

    maze_result = '\n'.join(str(row) for row in maze)
    assert maze_result == fake_stdout.getvalue()