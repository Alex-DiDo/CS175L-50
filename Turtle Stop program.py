'''
#CS175L-50
#Name:Alexander DiDomenico
#Turtle Stop program
'''
#Import Turtle
import turtle
bob = turtle.Turtle()
bob.color("white")
#Give Turtle a position on grid
bob.penup()
bob.setposition(-55,-100)
bob.pendown()
turtle.hideturtle()
#Give Turtle a color
turtle.bgcolor("red")
bob.color("white")
#Turtle writes the word "Stop"
style = ('Arial', 69, 'bold')
turtle.write('STOP', font=style, align='center')
bob.pencolor("white")
#Create the shape
for i in range(8):
    bob.forward(100)
    bob.left(45)
turtle.done()
