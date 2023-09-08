import turtle

def fibonacci_tree(turtle, branch_len, angle, level):
    if level > 0:
        turtle.forward(branch_len)
        turtle.right(angle)
        fibonacci_tree(turtle, branch_len - 15, angle, level - 1)
        turtle.left(2 * angle)
        fibonacci_tree(turtle, branch_len - 15, angle, level - 1)
        turtle.right(angle)
        turtle.backward(branch_len)

def main():
    turtle.speed(0)
    turtle.bgcolor("white")
    turtle.color("green")
    turtle.penup()
    turtle.left(90)
    turtle.backward(200)
    turtle.pendown()

    branch_length = 100  
    angle = 30  
    levels = 6  

    fibonacci_tree(turtle, branch_length, angle, levels)

    turtle.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()



