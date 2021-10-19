from turtle import Screen
from clickableturtle import ClickableTurtle


window = Screen()
screen_width = 600
screen_height = 400
window.setup(screen_width, screen_height)

start_button = ClickableTurtle(window)


window.listen()
window.mainloop()