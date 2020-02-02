import pytest
import sys
import builtins
import os
import mock
import io

from src.maze_functions import *


# Test that the menu is returned as expected
def test_display_menu():
    menu = display_menu()
    assert '''
    MAIN MENU
    =========
    [1] Read and load maze from file
    [2] View maze
    [3] Play maze game
    [4] Configure current maze

    [0] Exit maze
    ''' == menu


# Test that the get_option function takes in an input and evaluates if it is valid or invalid
def test_get_option():
    # Test that option inputs from 0 to 4 will be return as is
    for i in range(0, 5):
        with mock.patch('builtins.input', return_value=str(i)):
            assert i == get_option()

    # Test that option inputs not 0 to 4 will return -1 as invalid response
    invalid_array = ['a', '!', 5]
    for option in invalid_array:
        with mock.patch('builtins.input', return_value=str(option)):
            assert -1 == get_option()


# Test that the option_function takes in an input and gives out the correct print() output
def test_option_function():
    # Array mapping option number as array index to expected print() output
    option_array = [
        'Exit maze', 'Read and load maze from file', 'View maze',
        'Play maze game', 'Configure current maze'
    ]
    # Array of invalid option input()
    invalid_array = ['a', '!', 5]

    # Test that the option input will result in the correct print() output
    # Strip '\n' as print always append a newline
    for i, option in enumerate(option_array):
        with mock.patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            option_functions(i)
        assert option == fake_stdout.getvalue().strip('\n')

    # Test that all invalid option input() will result in the same invalid error message
    # Strip '\n' as print always append a newline
    for option in invalid_array:
        with mock.patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            option_functions(option)
        assert 'Invalid option! Please try again!' == fake_stdout.getvalue(
        ).strip('\n')
