from turtle import Screen
from keyboardturtle import KeyboardTurtle
from clickableturtle import ClkTurt
from clickableturtle import ClkSqu
from clickableturtle import ClkCir
from clickableturtle import ClkArr
from winningwall import Winningwall
from wall import Wall


# set up instance of the screen
window = Screen()
screen_width = 600
screen_height = 400
window.setup(screen_width, screen_height)
window.bgpic("baw.png")

#define walls
wall_list = []
player_1 = KeyboardTurtle(window, walls = wall_list)

#clickable turtle
turt = ClkTurt(window, player=player_1)
turt.shape("turtle")
turt.shapesize(2)
turt.goto(-260,155)

#clickable circle
cir = ClkCir(window, player=player_1)
cir.shape("circle")
cir.shapesize(2)
cir.goto(-185,155)

#clickable arrow
arr = ClkArr(window, player=player_1)
arr.shape("arrow")
arr.shapesize(2)
arr.goto(-110,155)

#clickable square
squ = ClkSqu(window, player=player_1)
squ.shape("square")
squ.shapesize(2)
squ.goto(-35,155)

#player starting state
player_1.goto(-270, -170)


#list of walls in maze
w1 = Wall(-300,-180,.5,200)
wall_list.append(w1)
wall_list.append(Wall(-50,200,29,.5))
wall_list.append(Wall(50,-200,35,1))
wall_list.append(Wall(300,180,1,100))
wall_list.append(Wall(-130, -200,.5,26))
wall_list.append(Wall(-160,120,15.5,.5))
wall_list.append(Wall(0,160,.5,4.5))
wall_list.append(Wall(-180,-65,4.5,.5)) #vertical
wall_list.append(Wall(-220,-90,.5,3)) #horizontal
wall_list.append(Wall(-130,0,6,.5)) 
wall_list.append(Wall(-220,85,.5,4))
wall_list.append(Wall(0,-25,.5,3.0))
wall_list.append(Wall(85,0,9,.5))
wall_list.append(Wall(65,125,.5,12))
wall_list.append(Wall(35,65,8,.5))
wall_list.append(Wall(-30,-50,3.5,.5))
wall_list.append(Wall(-65,-75,.5,3))
wall_list.append(Wall(-30,-100,3.5,.5))
wall_list.append(Wall(65,-205,.5,12))
wall_list.append(Wall(175,-5,.5,10))
wall_list.append(Wall(175,-100,5,.5))
wall_list.append(Wall(300,0,6,.5))
wall_list.append(Wall(280,145,12,.5))

#list for winning wall in maze
w2 = Winningwall(270,200,3,1)
player_1.winningwall = w2

# This is needed to listen for inputs
window.listen()
window.mainloop()
