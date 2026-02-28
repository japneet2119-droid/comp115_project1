import turtle
drawing_screen = turtle.Screen()
drawing_screen.bgcolor("skyblue")

alex = turtle.Turtle()
alex.speed(0)
alex.hideturtle()



alex.penup()
alex.goto(-390, -110)
alex.color("green")
alex.begin_fill()
for _ in range(2):
    alex.forward(790)
    alex.right(90)
    alex.forward(290)
    alex.right(80)
alex.end_fill()   



alex.goto(200, 130)
alex.color("yellow")
alex.begin_fill()
alex.circle(50)
alex.end_fill()



def cloud_drawing(x, y):
    alex.penup()
    alex.goto(x, y)
    alex.pendown()
    for _ in range(5):
        alex.circle(20)
        alex.penup()
        alex.forward(20)
        alex.pendown()

    for _ in range(5):
            alex.begin_fill()
            alex.circle(20)
            alex.end_fill()
            alex.penup()
            alex.forward(20)
            alex.pendown()


cloud_drawing(-200, 180)
cloud_drawing(50, 200)  

def bird_drawing(x, y):
    alex.penup()
    alex.color("black")
    alex.goto(x, y)
    alex.pendown()

    alex.setheading(45)
    alex.forward(15)
    alex.backward(15)

    alex.setheading(135)
    alex.forward(15)


bird_drawing(-100, 120)
bird_drawing(0, 140)
bird_drawing(100, 120)
bird_drawing(50, 120)

radius = 100
increase = 10
alex.pensize(increase)

colors = ['purple', 'darkblue', 'lightblue', 'green', 'yellow', 'orange', 'red']
alex.up()
alex.speed(6)
for color in colors:
    alex.color(color)

    alex.backward(radius) 
    alex.left(90)
    alex.down()
    alex.circle(-radius, 180)
    alex.left(90)
    alex.up()
    alex.backward(radius)

    radius += increase
alex.shape('blank')

drawing_screen.mainloop()