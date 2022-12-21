#!/bin/python3

######################################################
# Assignment: Project 2
# UIN: <663809723>
# URL to your assignment: https://trinket.io/library/trinkets/982c6f7390
######################################################

import turtle
import random
import math

#sets up screen with 500*500 dimension
s = turtle.Screen()
s.setup(500, 500)
s.bgpic("deepspace.png") #background image 


#represents image game character as amongus
#shape for character image file
#score and lives for the game 
amongus = {"turtle": turtle.Turtle(), "shape": "amongus.png", "radius": 10, "score": 0, "lives": 3};
s.addshape(amongus["shape"])
amongus["turtle"].shape(amongus["shape"])

#represents benefit greenball to increase score
#shape for the benefit character image 
#radius when checking the collision
greenball = {"turtle": turtle.Turtle(), "shape": "greenball.jpg", "radius": 50};
s.addshape(greenball["shape"])
greenball["turtle"].shape(greenball["shape"])

blueball = {"turtle": turtle.Turtle(), "shape": "Blueball.jpg", "radius": 50};
s.addshape(blueball["shape"])
blueball["turtle"].shape(blueball["shape"])

#represents harm redball to reduce lives
#shape for the harm character image
redball = {"turtle": turtle.Turtle(), "shape": "RedBall.jpg", "radius": 50};
s.addshape(redball["shape"])
redball["turtle"].shape(redball["shape"])

#t2 turtle to keep track of score in a game
t2 = turtle.Turtle()
t2.hideturtle()
t2.goto(150,230)
t2.color("white")
t2.write("Score: " + str(amongus["score"]), font=('Arial', 12))

#t3 turtle to keep track of lives left in a game
t3 = turtle.Turtle()
t3.hideturtle()
t3.goto(150,210)
t3.color("white")
t3.write("Lives: " + str(amongus["lives"]), font=('Arial', 12))

#t4 turtle to display GAME OVER! when lives is 0
t4 = turtle.Turtle()
t4.hideturtle()
t4.color("white")
t4.penup()
t4.goto(-75,210)

#sets the amongus character to inital position
amongus["turtle"].tracer(0)
amongus["turtle"].sety(0)
amongus["turtle"].setx(-150)
  
#sets the greenball benefit to intial postion
greenball["turtle"].tracer(0)
greenball["turtle"].setx(250)
greenball["turtle"].sety(50)

blueball["turtle"].tracer(0)
blueball["turtle"].setx(250)
blueball["turtle"].sety(150)

#sets the redball harm to inital postion
redball["turtle"].tracer(0)
redball["turtle"].setx(250)
redball["turtle"].sety(-100)


#move_distane to control the distance travelled by character everytime it moves
move_distance = 7
s_width = 500

#up function moves game character up the screen
def up():
  amongus["turtle"].clear()
  current_y = amongus["turtle"].ycor() + move_distance
  #move distance to the current y
  amongus["turtle"].sety(current_y)
up()

#down function moves game character down the screen
def down():  
  amongus["turtle"].clear()
  current_y = amongus["turtle"].ycor() - move_distance
  amongus["turtle"].sety(current_y)
down()



#are_colliding to check if the character collides with other balls
def are_colliding (obj_1, obj_2):
  #uses coodinate to check if objects collide
  dx = obj_1["turtle"].xcor() - obj_2["turtle"].xcor()
  dy = obj_1["turtle"].ycor() - obj_2["turtle"].ycor()
  distance = math.sqrt(dx*dx + dy*dy)
  if distance < obj_1["radius"] + obj_2["radius"]:
    collision_detected = True
  else:
    collision_detected = False
  return collision_detected

#main() runs the program
def main():
  #hooks up key event handlers so that arrow keys trigger appropriate function
  s.onkey(up, "Up")
  s.onkey(down, "Down")
  s.listen()
  
  greenballcollided = False #changes to true everytime score updates 
  blueballcollided = False
  redballcollided = True #true until the redballcollides with the character
  
  #checks the lives before proceeding to next step
  while amongus["lives"] >= 1:
    greenball["turtle"].clear()
    blueball["turtle"].clear()
    redball["turtle"].clear()
    greenball["turtle"].setx(greenball["turtle"].xcor()-6) #controls the movement of greenball
    blueball["turtle"].setx(blueball["turtle"].xcor()-1)
    redball["turtle"].setx(redball["turtle"].xcor()-5) #for movement of redball
    
    if(-greenball["turtle"].xcor() >= s_width/2): #if the greenball exceeds the screen width
      greenball["turtle"].sety(random.randrange(-220,200)) #returns back from right randomly
      greenball["turtle"].setx(s_width)
      greenballcollided = False
    greenball["turtle"].update()
    
    if(-blueball["turtle"].xcor() >= s_width/2): #if the greenball exceeds the screen width
      blueball["turtle"].sety(random.randrange(-220,200)) #returns back from right randomly
      blueball["turtle"].setx(s_width)
      blueballcollided = False
    blueball["turtle"].update()
    
    if(-redball["turtle"].xcor() >= s_width/2):#if the redball exceeds the screen width
      redball["turtle"].sety(random.randrange(-220,200))#returns back from right randomly
      redball["turtle"].setx(s_width)
      redballcollided = False
    redball["turtle"].update()
    
    #colliders list to use for are_colliding function's parameters
    colliders = [amongus, greenball, redball, blueball]
    
    #if greenball collides, the score increases by 10
    if are_colliding(colliders[0], colliders[1]):
      if greenballcollided == False:
        amongus["score"] += 10 #increases the score by 10 when benefit hits
        t2.clear()
        t2.update()
        #updates the score everytime collides with benefit
        t2.write("Score: " + str(amongus["score"]), font=('Arial', 12))
        greenballcollided = True
    elif are_colliding(colliders[0], colliders[3]):
      if blueballcollided == False:
        amongus["score"] += 20 #increases the score by 10 when benefit hits
        t2.clear()
        t2.update()
        #updates the score everytime collides with benefit
        t2.write("Score: " + str(amongus["score"]), font=('Arial', 12))
        blueballcollided = True
        
    #if redball collides, the lives decreases by 1 
    #else if the lives get to zero, Game over message is displayed
    elif are_colliding(colliders[0],colliders[2]):
      if redballcollided == False:
        amongus["lives"] -= 1 #decreases lives by 1 lif redball collides with amongus
        if (amongus["lives"] == 0): #once the lives is zero, the Game over is displayed
          t3.clear()
          t3.update()
          t3.write("Lives: " + str(amongus["lives"]), font=('Arial', 12))
          t4.clear()
          t4.update()
          t4.write("GAME OVER!", font=('Arial', 20))
        t3.clear()
        t3.update()
        #updates the lives everytime collision occurs with harm
        t3.write("Lives: " + str(amongus["lives"]), font=('Arial', 12))
        redballcollided = True
#calls main() to run the program
main()

