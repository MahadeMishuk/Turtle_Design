import turtle
colors = ['pink','purple','skyblue','cyan','orange','yellow']


t = turtle.Turtle()
turtle.bgcolor("black")
t.speed(1000)

for x in range(400):
    t.pencolor(colors[x%6])
    t.width(x//100+1)
    t.shape("turtle")
    t.forward(x)
    t.left(59)
