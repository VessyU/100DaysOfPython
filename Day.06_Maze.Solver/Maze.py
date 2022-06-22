#Tested on https://reeborg.ca/reeborg.html for hurdle 1-4 and maze - Can import
def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal() is True:    
    while front_is_clear() is True:
        if at_goal() is True:
                    break
        turn_right()
        while wall_in_front() is True:
            if at_goal() is True:
                    break
            turn_left()
            while front_is_clear() is True:
                if at_goal() is True:
                    break
                move()
                turn_right()
                if front_is_clear() is not True:
                    break
                turn_right 
        while wall_in_front() is not True:
            if at_goal() is True:
                    break
            turn_left()
            move()
    if front_is_clear() is not True:
        if at_goal() is True:
                    break
        turn_left()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
