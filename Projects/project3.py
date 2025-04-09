import turtle

t = turtle.Turtle()

t.color("cyan")
turtle.Screen().bgcolor("black")

# three colors
colors = ["cyan","darkblue","lightblue"]
for i in range(1000):
    t.color(colors[i % 3] )
# turtle goes forward 100 degrees
    t.forward(100)
    t.left(1200 + 1)
# speed is at 100000000000000000000000
    t.speed(1000000000000000000000000)

    turtle.exitonclick