import turtle

turtle.title("Turtle Drawing")
circle = turtle.Turtle()
circle.shape("turtle")
circle.pensize(20)
circle.pencolor("cyan")

circle.dot(80)
circle.penup()
circle.goto(0, -200)
circle.pendown()
circle.circle(200)
turtle.exitonclick()