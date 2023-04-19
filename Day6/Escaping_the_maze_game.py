#Escaping the Maze Game
#Built by Drayerh
#Visit the folowing website to run the code. https://reeborg.ca/reeborg.html 
#Choose maze in the option of challenges. 
#Hope you have fun escaping the maze home!

def turn_right():
    turn_left()
    turn_left()
    turn_left()

    
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()

#To debug infinite loop error on Day 15
#When Reeborg starts from the center an infinite loop can be encountered