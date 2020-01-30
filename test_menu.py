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
    '''
    
    '''
    with mock.patch('builtins.input', return_value="0"):
        assert 0 == get_option()


def test_option_function():
    assert 'Exit maze' == option_functions(0)
