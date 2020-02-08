import pytest

#Test to display maze game with start and end location
def test_display_maze_game():
    displayed= display_maze()
    assert displayed == disp_maze


#Test for moving up when press 'W'
def test_A_moving_up():
    moved= move()
    assert move == mazeup


#Test for Moving down when press 'S'
def test_A_moving_down():
    moved= move()
    assert moved == mazedown


#Test for moving left when press 'A'
def test_A_moving_left():
    moved= move()
    assert moved == mazeleft


#Test for moving right when press 'D'
def test_A_moving_right():
    moved= move()
    assert moved == mazeright


#Test that A has moved position
def test_A_not_in_same_position():
    moved= move()
    assert moved == True

#test if dont press valid button and press Q will it move
def test_A_not_moving_up_Q():
    moved= move()
    assert moved == False

    
#Test that error message prompted 
def test_hit_a_wall():
    invalidmovement= move()
    assert invalidmovement == "Invalid"
