from turtle import Turtle
from random import choice

class BorderTurtle(Turtle):
  def __init__(self,
                name = "turtle",
               x = -190 , 
               y = 160):
    # Runs Keyboard Turtle Constructor as well as the Turtle Constructor
    Turtle.__init__(self)
    
  

    #set turtle starting states
    self.shape("turtle")
    self.shapesize(1,1,1)
    self.color(self.randcolor())
    self.penup()
    self.setx(self.x)
    self.sety(self.y)
    self.draw_title(self.name, self.x, self.y)
    self.window.onscreenclick(None)


  def randcolor(self):
    colors = ["red","yellow","orange","pink"]
    return choice(colors)