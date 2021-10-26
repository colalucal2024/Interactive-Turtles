from turtle import Turtle


#setup class for clickable turtle on staring screen
class KeyboardTurtle(Turtle):
  # our 'wrapper' class of the Turtle class
  def __init__(self, 
               window,  
               straight = "Up", 
               turn_right = "Right",
               not_straight = "Down",
               turn_left = "Left",
               other_player = None,
               walls = None,
               winningwall = None):
    # Runs Keyboard Turtle Constructor as well as the Turtle Constructor
    Turtle.__init__(self)
    
    # Sets up incoming variables
    self.window = window
    self.straight = straight
    self.not_straight = not_straight
    self.turn_right = turn_right
    self.turn_left = turn_left
    self.other_player = other_player
    self.walls = walls
    self.winningwall = winningwall
    self.shape("turtle")
    self.color("blue")
    self.penup()

    # Sets up keyboard command examples
    self.window.onkey(self.go_right, self.turn_right)
    self.window.onkey(self.go_forward, self.straight)
    self.window.onkey(self.go_left, self.turn_left)
    self.window.onkey(self.go_backward, self.not_straight)

    #sets up controlling variables (y not implemented)
    self.movement_speed = 5
    self.turn_speed = 45
    self.collision_distance = 20

  # Movement Methods
  def go_forward(self):
    collided=False
    self.forward(self.movement_speed)


#hit winning wall
    if self.check_collision(self.winningwall):
      print("***YOU WIN***")
      quit()

  
#when not touching a wall
    if self.walls != None:
      for wall in self.walls:
        if self.check_collision(wall):
          collided = True
          break
      if collided :
        self.goto(-270, -170)

  
  #def backwards
  def go_backward(self):
    collided=False
    self.backward(self.movement_speed)


#hit winning wall
    if self.check_collision(self.winningwall):
      print("***YOU WIN***")
      quit()

  
#when not touching a wall
    if self.walls != None:
      for wall in self.walls:
        if self.check_collision(wall):
          collided = True
          break
      if collided :
        self.goto(-270, -170)

  def go_right(self):
    self.right(self.turn_speed)

  def go_left(self):
    self.left(self.turn_speed)

# def collision checker
  def check_collision(self, obj_to_check):
    turtle_rad = 10
    wall_rad = 10
    distance_x = obj_to_check.xcor() - self.xcor()
    distance_x = abs(distance_x)

    distance_y = obj_to_check.ycor() - self.ycor()
    distance_y = abs(distance_y)

    if distance_x < turtle_rad + (wall_rad * obj_to_check.x_size) and distance_y < turtle_rad + (wall_rad * obj_to_check.y_size):
      return True
    else:
      return False
      
