from turtle import Screen
from keyboardturtle import KeyboardTurtle
from clickableturtle import ClickableTurtle
from borders import BorderTurtle





# set up instance of the screen
window = Screen()
screen_width = 600
screen_height = 400
window.setup(screen_width, screen_height)

# set up clickable instance
button = ClickableTurtle()
border = BorderTurtle()


player_1 = KeyboardTurtle(window)
player_2 = KeyboardTurtle(window, "w","a","s", "d")

player_1.goto(100,0)

# set target of other player(our collison check) to the opposite player
player_1.other_player = player_2
player_2.other_player = player_1



# This is needed to listen for inputs
window.listen()
window.mainloop()
