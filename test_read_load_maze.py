import mock
from src.maze_functions import *

maze = [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'O', 'O', 'O', 'X', 'O', 'A', 'X'],
        ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'X'],
        ['X', 'O', 'X', 'O', 'X', 'O', 'O', 'X'],
        ['X', 'O', 'X', 'O', 'X', 'X', 'O', 'X'],
        ['X', 'O', 'X', 'O', 'X', 'O', 'O', 'X'],
        ['X', 'O', 'X', 'O', 'O', 'O', 'X', 'X'],
        ['X', 'B', 'X', 'X', 'X', 'X', 'X', 'X']]

maze_no_location = [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
                    ['X', 'O', 'O', 'O', 'X', 'O', 'O', 'X'],
                    ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'X'],
                    ['X', 'O', 'X', 'O', 'X', 'O', 'O', 'X'],
                    ['X', 'O', 'X', 'O', 'X', 'X', 'O', 'X'],
                    ['X', 'O', 'X', 'O', 'X', 'O', 'O', 'X'],
                    ['X', 'O', 'X', 'O', 'O', 'O', 'X', 'X'],
                    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']]

maze_start = [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
              ['X', 'O', 'O', 'O', 'X', 'A', 'O', 'X'],
              ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'X'],
              ['X', 'O', 'X', 'O', 'X', 'O', 'O', 'X'],
              ['X', 'O', 'X', 'O', 'X', 'X', 'O', 'X'],
              ['X', 'O', 'X', 'O', 'X', 'O', 'O', 'X'],
              ['X', 'O', 'X', 'O', 'O', 'O', 'X', 'X'],
              ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']]

maze_end = [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
            ['X', 'O', 'O', 'O', 'X', 'O', 'O', 'X'],
            ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'X'],
            ['X', 'O', 'X', 'O', 'X', 'O', 'O', 'X'],
            ['X', 'O', 'X', 'O', 'X', 'X', 'O', 'X'],
            ['X', 'O', 'X', 'O', 'X', 'O', 'O', 'X'],
            ['X', 'O', 'X', 'O', 'O', 'O', 'X', 'X'],
            ['X', 'B', 'X', 'X', 'X', 'X', 'X', 'X']]


# Test that maze is returned when file given is csv file
def test_read_file_valid():
    with mock.patch('builtins.input', return_value='maze.csv'):
        assert maze == read_file()


# Test that -1 is return as error when file given is not csv file
def test_read_file_invalid():
    with mock.patch('builtins.input', return_value='maze.txt'):
        assert -1 == read_file()


# Test correct coordinates are returned when maze has start A and end B
def test_store_location_valid():
    start, end = store_location(maze)
    assert [7, 2] == start and [2, 8] == end


# Test -1 coordinates are returned when maze has does not have a start, end or both
def test_store_location_invalid():
    invalid_maze = [maze_no_location, maze_end, maze_start]
    for m in invalid_maze:
        start, end = store_location(m)
        assert start == -1 and end == -1