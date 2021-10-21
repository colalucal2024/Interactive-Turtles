from turtle import Turtle, Screen
from random import choice
from keyboardturtle import KeyboardTurtle
from wall import Wall
import os


class ClickableTurtle(Turtle):
  # our 'wrapper' class of the Turtle class
  def __init__(self, 
               name = "click me",
              
               x = 0 , 
               y = -100):
    # Runs Keyboard Turtle Constructor as well as the Turtle Constructor
    Turtle.__init__(self)
    
    # Sets up incoming variables
    self.name = name
    self.x = x
    self.y = y
    self.window = Screen()

    #set turtle starting states
    self.shape("square")
    self.shapesize(1,3,1)
    self.color(self.randcolor())
    self.penup()
    self.setx(self.x)
    self.sety(self.y)
    self.draw_title(self.name, self.x, self.y)
    self.window.onscreenclick(None)
    self.onclick(self.click)

  # Draws the button name above the button
  def draw_title(self, text, x, y):
    self.goto(self.x, self.y + 17)
    self.write(text, move=False, align='center', font=('Arial', 10, 'normal'))
    self.goto(self.x, self.y)

  # tells what happens when button is clicked
  def click(self, x, y):
    # This is Placeholder:  What should this button do?
    os.system("python3 main.py")


  def randcolor(self):
    colors = ["sky blue","powder blue","dodger blue","light sky blue"]
    return choice(colors)


class ClkSqu(Turtle):
  # our 'wrapper' class of the Turtle class
  def __init__(self, 
               name = "square", 
               x = 0 , 
               y = -100,
               player = None):
    # Runs Keyboard Turtle Constructor as well as the Turtle Constructor
    Turtle.__init__(self)
    
    # Sets up incoming variables
    self.name = name
    self.x = x
    self.y = y
    self.player = player
    self.window = Screen()

    #set turtle starting states
    self.shape("square")
    self.shapesize(1,3,1)
    self.color(self.randcolor())
    self.penup()
    self.setx(self.x)
    self.sety(self.y)
    self.draw_title(self.name, self.x, self.y)
    self.window.onscreenclick(None)
    self.onclick(self.click)

  # Draws the button name above the button
  def draw_title(self, text, x, y):
    self.goto(self.x, self.y + 17)
    self.write(text, move=False, align='center', font=('Arial', 10, 'normal'))
    self.goto(self.x, self.y)

  # tells what happens when button is clicked
  def click(self, x, y):
    # This is Placeholder:  What should this button do?
    self.player.shape("square")


  def randcolor(self):
    colors = ["sky blue","powder blue","dodger blue","light sky blue"]
    return choice(colors)

