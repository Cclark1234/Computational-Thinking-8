import turtle
t = turtle.Turtle()

# setup
t.speed(10)
turtle.Screen().bgcolor("light blue")


# stripes

# move to stripe 1
t.goto(-250, -100)
h = 50
# stripe 1
t.color("red")
t.begin_fill()
t.forward(500)
t.left(90)
t.forward(h)
t.left(90)
t.forward(500)
t.left(90)
t.forward(h)
t.left(90)
t.end_fill()


# move to stripe 2
t.goto(-250, -50)

# stripe 2
t.color("white")
t.begin_fill()
t.forward(500)
t.left(90)
t.forward(h)
t.left(90)
t.forward(500)
t.left(90)
t.forward(h)
t.left(90)
t.end_fill()

# move to stripe 3
t.goto(-250, 0)

# stripe 3
t.color("red")
t.begin_fill()
t.forward(500)
t.left(90)
t.forward(h)
t.left(90)
t.forward(500)
t.left(90)
t.forward(h)
t.left(90)
t.end_fill()

# move to stripe 4
t.goto(-250, 50)

# stripe 4
t.color("white")
t.begin_fill()
t.forward(500)
t.left(90)
t.forward(h)
t.left(90)
t.forward(500)
t.left(90)
t.forward(h)
t.left(90)
t.end_fill()

# move to stripe 5
t.goto(-250, 100)

# stripe 5
t.color("red")
t.begin_fill()
t.forward(500)
t.left(90)
t.forward(h)
t.left(90)
t.forward(500)
t.left(90)
t.forward(h)
t.left(90)
t.end_fill()

# move to stripe 6
t.goto(-250, -150)
h = 50
# stripe 1
t.color("white")
t.begin_fill()
t.forward(500)
t.left(90)
t.forward(h)
t.left(90)
t.forward(500)
t.left(90)
t.forward(h)
t.left(90)
t.end_fill()

# move to stripe 7
t.goto(-250, -200)
h = 50
# stripe 1
t.color("white")
t.begin_fill()
t.forward(500)
t.left(90)
t.forward(h)
t.left(90)
t.forward(500)
t.left(90)
t.forward(h)
t.left(90)
t.end_fill()

# move to stripe 8
t.goto(-250, -250)
h = 50
# stripe 1
t.color("white")
t.begin_fill()
t.forward(500)
t.left(90)
t.forward(h)
t.left(90)
t.forward(500)
t.left(90)
t.forward(h)
t.left(90)
t.end_fill()

# move to stripe 9
t.goto(-250, -300)
h = 50
# stripe 1
t.color("red")
t.begin_fill()
t.forward(500)
t.left(90)
t.forward(h)
t.left(90)
t.forward(500)
t.left(90)
t.forward(h)
t.left(90)
t.end_fill()

# move to stripe 10
t.goto(-250, -350)
h = 50
# stripe 1
t.color("white")
t.begin_fill()
t.forward(500)
t.left(90)
t.forward(h)
t.left(90)
t.forward(500)
t.left(90)
t.forward(h)
t.left(90)
t.end_fill()

# move to stripe 11
t.goto(-250, 150)
h = 50
# stripe 1
t.color("red")
t.begin_fill()
t.forward(500)
t.left(90)
t.forward(h)
t.left(90)
t.forward(500)
t.left(90)
t.forward(h)
t.left(90)
t.end_fill()

# move to stripe 12
t.goto(-250, 200)
h = 50
# stripe 1
t.color("white")
t.begin_fill()
t.forward(500)
t.left(90)
t.forward(h)
t.left(90)
t.forward(500)
t.left(90)
t.forward(h)
t.left(90)
t.end_fill()

# move to stripe 13
t.goto(-250, 250)
h = 50
# stripe 1
t.color("red")
t.begin_fill()
t.forward(500)
t.left(90)
t.forward(h)
t.left(90)
t.forward(500)
t.left(90)
t.forward(h)
t.left(90)
t.end_fill()

# blue square
t.goto(-250, 250)
t.color("blue")
t.begin_fill()
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.end_fill()

turtle.exitonclick()
