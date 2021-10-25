from turtle import Screen
from clickableturtle import ClickableTurtle

#screen setup
window = Screen()
screen_width = 600
screen_height = 400
window.setup(screen_width, screen_height)

#starting menu and instructions
print("*** WELCOME TO THE MAZE OF DEATH ***")
print("USE YOUR ARROW KEYS TO NAVIGATE THROUGH THE MAZE")
print("CLICK THE SHAPES IN THE TOP LEFT OF THE SCREEN TO CHANGE THE SHAPE OF YOUR PLAYER") 
print("REACH THE BLUE AND YOU WIN... DONT TOUCH THE RED...") 
print("CLICK THE BUTTON ABOVE TO START!")

#start button and instructions
start_button = ClickableTurtle("Look below for the instructions... Click me when you are ready!")


window.listen()
window.mainloop()