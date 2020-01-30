import pytest
import sys
import builtins
import os
import mock

from src.main import *


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


def test_get_option():
    with mock.patch('builtins.input', return_value="0"):
        assert 0 == get_option()
    with mock.patch('builtins.input', return_value="a"):
        assert -1 == get_option()


def test_option_function():
    option_array = [
        'Exit maze', 'Read and load maze from file', 'View maze',
        'Play maze game', 'Configure current maze'
    ]
    for i, option in enumerate(option_array):
        assert option == option_functions(i)
    assert 'Invalid option!' == option_functions('a')
