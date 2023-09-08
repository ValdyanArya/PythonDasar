import turtle
from PIL import Image, ImageDraw

def save_as_jpg(canvas, filename):
    canvas.postscript(file=filename + ".eps")
    img = Image.open(filename + ".eps")
    img.save(filename + ".jpg", "JPEG")

def drawRectangle(ttl, x, y, width, height):
    ttl.up()
    ttl.goto(x, y)
    ttl.setheading(0)
    ttl.down()
    for i in range(2):
        ttl.forward(width)
        ttl.right(90)
        ttl.forward(height)
        ttl.right(90)
    ttl.up()

def drawTriangle(ttl, x1, y1, x2, y2, x3, y3):
    ttl.penup()
    ttl.goto(x1, y1)
    ttl.pendown()
    ttl.goto(x2, y2)
    ttl.goto(x3, y3)
    ttl.goto(x1, y1)
    ttl.penup()

def fillTriangle(ttl, x1, y1, x2, y2, x3, y3, color):
    ttl.fillcolor(color)
    ttl.begin_fill()
    drawTriangle(ttl, x1, y1, x2, y2, x3, y3)
    ttl.end_fill()

turtle.setup(1500, 100, 0, 0)
myBlue = "#003882"
myYellow = "#FCD647"
myRed = "#D12421"
myGreen = "#007336"
myWhite = "#FFFFFF"

Joe = turtle.Turtle()
Joe.screen.colormode(255)

drawRectangle(Joe, 0, 300, 600, 300)
Joe.goto(0, 0)
fillTriangle(Joe, 0, 0, 0, 300, 200, 300, myBlue)
fillTriangle(Joe, 0, 0, 200, 300, 200, 0, myYellow)
fillTriangle(Joe, 0, 0, -200, 0, 0, -300, myRed)
fillTriangle(Joe, 0, 0, 0, -300, 200, -300, myWhite)
fillTriangle(Joe, 0, 0, -200, 0, -200, 300, myGreen)
Joe.hideturtle()
tc = Joe.getcanvas()
save_as_jpg(tc, "SeychellesFlag")
turtle.done()