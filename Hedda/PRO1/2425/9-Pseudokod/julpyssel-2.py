"""
Använd turtle för att rita ut en gran
"""

import turtle

"""
PSEUDOKOD

SET COLOR TO GREEN

SET n TO 1

begin fill

FUNCTION make_triangle(n):
    begin_fill
    FOR i IN range(3):
        FORWARD 50*n
        TURN 120 degrees left
    end_fill

FUNCTION setup_triangle(n):
    FORWARD 25*(n-1)

    TURN 90 degrees left
    FORWARD 25*(n-1)
    TURN 90 degrees right
    
    TURN 120 degrees right
    FORWARD 50*n
    TURN 120 degrees left

FUNCTION draw_foot():

    FORWARD 25*3-5
    TURN 90 degrees right
    
    SET COLOR TO BROWN

    begin fill
    FORWARD 25
    TURN 90 degrees left
    FORWARD 10
    TURN 90 degrees left
    FORWARD 25
    end fill

FUNCTION setup_star():
    pen up

    SET POSITION to (0,55)

    SET HEADING to 0

    pen down

FUNCTION draw_star():
    SET COLOR TO YELLOW

    begin fill

    FOR i IN range(5):
        FORWARD 50
        TURN 180-180/5 degrees RIGHT

    end fill
        
make_triangle(n)

n += 1

setup_triangle(n)
make_triangle(n)

n += 1

setup_triangle(n)
make_triangle(n)
    
"""



