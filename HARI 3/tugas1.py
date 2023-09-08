import turtle

def draw_rectangle(width, height):
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)

def draw_triangle(side_length):
    for _ in range(3):
        turtle.forward(side_length)
        turtle.left(120)

def draw_trapezium(base1, base2, height):
    angle = 45  # Sudut untuk trapesium
    turtle.forward(base1)
    turtle.left(angle)
    turtle.forward(height)
    turtle.left(180 - angle)
    turtle.forward(base2)
    turtle.left(angle)
    turtle.forward(height)

def draw_parallelogram(base, height):
    turtle.forward(base)
    turtle.left(45)
    turtle.forward(height)
    turtle.left(135)
    turtle.forward(base)
    turtle.left(45)
    turtle.forward(height)

def draw_rhombus(side_length):
    for _ in range(4):
        turtle.forward(side_length)
        turtle.left(45)

turtle.speed(1)

# Menggambar Persegi Panjang
turtle.color("red")
draw_rectangle(100, 50)

# Menggambar Segitiga
turtle.color("blue")
turtle.penup()
turtle.goto(-100, 0)
turtle.pendown()
draw_triangle(100)

# Menggambar Trapesium
turtle.color("green")
turtle.penup()
turtle.goto(-150, -100)
turtle.pendown()
draw_trapezium(100, 60, 50)

# Menggambar Jajar Genjang
turtle.color("purple")
turtle.penup()
turtle.goto(50, 0)
turtle.pendown()
draw_parallelogram(80, 50)

# Menggambar Belah Ketupat
turtle.color("orange")
turtle.penup()
turtle.goto(-50, -100)
turtle.pendown()
draw_rhombus(70)

turtle.hideturtle()
turtle.done()