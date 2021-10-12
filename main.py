from turtle import Screen
from keyboardturtle import KeyboardTurtle
from clickableturtle import ClickableTurtle
from movingturtle import MovingTurtle
from wall import Wall


# set up instance of the screen
window = Screen()
screen_width = 600
screen_height = 400
window.setup(screen_width, screen_height)

# set up clickable instance
button = ClickableTurtle()

#list setup
wall_list = []
#set up players
player_1 = KeyboardTurtle(window, walls = wall_list)
player_2 = KeyboardTurtle(window, "w","a", "s", "d")

player_1.goto(100,0)

# set target of other player(our collison check) to the opposite player
player_1.other_player = player_2
player_2.other_player = player_1

w1 = Wall(100,0,1,5)
wall_list.append(w1)
wall_list.append(Wall(0,100,5,1))
moveT = MovingTurtle(screen_width)

# This is needed to listen for inputs
window.listen()
window.mainloop()


# be CAREFUL. We aren't controlling the screen draws in this program, so NO while True loops

#TODO:  Check the classes and complete TODOs
#push to github repo.
#link repo to assignment