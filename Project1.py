import turtle
drawing_screen = turtle.Screen()
drawing_screen.bgcolor("skyblue")

alex = turtle.Turtle()
alex.speed(0)
alex.hideturtle()

def mountain_drawing(x, y, color, size):
    alex.color(color)
    alex.begin_fill()
    alex.goto(x, y)
    alex.pendown()
    alex.goto(x + size, y + size)
    alex.goto(x + size, y)
    alex.goto(x, y)
    alex.penup()
    alex.end_fill()

mountain_drawing(-300, -100, 130, "gray")
mountain_drawing(-120, -90, 150, "lightgray")
mountain_drawing(90, -90, 150, "darkgray" )

alex.color("yellow")
alex.goto(200, 100)
alex.circle(50)
alex.begin_fill()
alex.end_fill()


def snow_covering(x, y, size):
    alex.color("white")
    alex.goto(x + size * 0.5, y + size * 0.5 )
    alex.pendown()
    alex.begin_fill()
    alex.goto(x + size, y + size)
    alex.goto(x + size * 1.2, y + size * 0.5)
    alex.goto(x + size * 0.5, y + size * 0.5 )
    alex.end_fill()
    alex.pendown()

snow_covering(-300, -100, 130)
snow_covering(-120, -90, 150)
snow_covering(90, -190, 50)    

alex.penup()
alex.goto(-350, -200)
alex.color("darkgreen")
alex.begin_fill()
for _ in range(2):
    alex.forward(500)
    alex.right(100)
    alex.forward(200)
    alex.right(70)
alex.end_fill()   



drawing_screen.mainloop()

