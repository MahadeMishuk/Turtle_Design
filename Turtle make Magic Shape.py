import turtle

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(200)
        some_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("black")
    #turtle Brad
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("gold")
    brad.speed(100)
    brad.pensize(1) #lineWidth
    for i in range(1,47):
        draw_square(brad)
        brad.right(50)

    window.exitonclick()

draw_art()

