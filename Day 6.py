def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def clearing():
    if right_is_clear():
            turn_right()
    while wall_on_right():
        if right_is_clear():
            turn_right()
        if front_is_clear():
            move()
        elif not(front_is_clear()):
            turn_left()
        
        else:
            move()
    
   
while not at_goal():
    if front_is_clear():
        move()
    else:
        clearing()

    
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
