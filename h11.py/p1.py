import turtle

screen = turtle.Screen()
screen.bgcolor("purple")
screen.setup(300, 400)

square = turtle.Turtle()
num_sides = 4
side_length = 65
angle = 360 / num_sides

for i in range(num_sides):
    square.forward(side_length)
    square.right(angle)

turtle.done()