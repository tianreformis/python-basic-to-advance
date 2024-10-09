import turtle

# Setting up the turtle
screen = turtle.Screen()
screen.title("Garuda")
t = turtle.Turtle()

# Garuda wings (simplified)
t.penup()
t.goto(-100, 0)
t.pendown()
t.circle(100, 180)
t.left(90)
t.forward(200)

t.penup()
t.goto(100, 0)
t.pendown()
t.circle(100, -180)
t.right(90)
t.forward(200)

# Garuda body (simplified)
t.penup()
t.goto(-50, -50)
t.pendown()
t.circle(50)

# Garuda head (simplified)
t.penup()
t.goto(-10, 20)
t.pendown()
t.circle(10)

# End drawing
t.hideturtle()
turtle.done()
