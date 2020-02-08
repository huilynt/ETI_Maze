import pytest
import unittest
from unittest import mock
from unittest import TestCase
from unittest.mock import patch
from src.maze_functions import *

maze = [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'O', 'O', 'O', 'X', 'O', 'A', 'X'],
        ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'X'],
        ['X', 'O', 'X', 'O', 'X', 'O', 'O', 'X'],
        ['X', 'O', 'X', 'O', 'X', 'X', 'O', 'X'],
        ['X', 'O', 'X', 'O', 'X', 'O', 'O', 'X'],
        ['X', 'O', 'X', 'O', 'O', 'O', 'X', 'X'],
        ['X', 'B', 'X', 'X', 'X', 'X', 'X', 'X']]

#Test for moving up when press 'W'
def test_A_moving_up():
    i = "w"
    sc = [1,6]
    ec = [7,2]
    newsc= [sc[0],sc[1]-1]
    moved= move(i,sc,ec,maze)
    assert newsc == [sc[0],sc[1]-1]


#Test for Moving down when press 'S'
def test_A_moving_down():
    i = "s"
    sc = [1,6]
    ec = [7,2]
    newsc= [sc[0],sc[1]+1]
    moved= move(i,sc,ec,maze)
    assert newsc == [sc[0],sc[1]+1]



#Test for moving left when press 'A'
def test_A_moving_left():
    i = "s"
    sc = [1,6]
    ec = [7,2]
    newsc= [sc[0]-1,sc[1]]
    moved= move(i,sc,ec,maze)
    assert newsc == [sc[0]-1,sc[1]]


#Test for moving right when press 'D'
def test_A_moving_right():
    i = "s"
    sc = [1,6]
    ec = [7,2]
    newsc= [sc[0]+1,sc[1]]
    moved= move(i,sc,ec,maze)
    assert newsc == [sc[0]+1,sc[1]]


#test if dont press valid button and press Q will it move
def test_A_not_moving_up_Q():
    i = "q"
    sc = [1,6]
    ec = [7,2]
    newsc= [sc[0],sc[1]]
    moved= move(i,sc,ec,maze)
    assert newsc == [sc[0],sc[1]]

    
#Test current position remains A
def test_hit_a_wall_W():
    i = "w"
    sc = [1,6]
    ec = [7,2]
    newsc= [sc[0],sc[1]-1]
    newsc= [sc[0],sc[1]]
    moved= move(i,sc,ec,maze)
    maze[newsc[1]][newsc[0]] == "X"
    assert newsc== [sc[0],sc[1]]

def test_hit_a_wall_S():
    i = "s"
    sc = [1,6]
    ec = [7,2]
    newsc= [sc[0],sc[1]+1]
    newsc= [sc[0],sc[1]]
    moved= move(i,sc,ec,maze)
    maze[newsc[1]][newsc[0]] == "X"
    assert newsc== [sc[0],sc[1]]


def test_hit_a_wall_A():
    i = "a"
    sc = [1,6]
    ec = [7,2]
    newsc= [sc[0]-1,sc[1]]
    newsc= [sc[0],sc[1]]
    moved= move(i,sc,ec,maze)
    maze[newsc[1]][newsc[0]] == "X"
    assert newsc== [sc[0],sc[1]]

def test_hit_a_wall_D():
    i = "d"
    sc = [1,6]
    ec = [7,2]
    newsc= [sc[0]+1,sc[1]]
    newsc= [sc[0],sc[1]]
    moved= move(i,sc,ec,maze)
    maze[newsc[1]][newsc[0]] == "X"
    assert newsc== [sc[0],sc[1]]

#Test finished game: reached b
def test_reach_b():
    i = "s"
    sc = [1,6]
    ec = [7,2]
    newsc= [ec[0],ec[1]]
    moved= move(i,sc,ec,maze)
    assert newsc== [ec[0],ec[1]]
