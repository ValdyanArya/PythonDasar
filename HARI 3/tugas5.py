import turtle

# Membuat objek turtle
balon = turtle.Turtle()
balon.speed(1)  # Mengatur kecepatan menggambar (1 = lambat, 10 = cepat)

# Menggambar badan balon (warna merah)
balon.color('red')
balon.begin_fill()
balon.circle(100)  
balon.end_fill()

balon.penup()
balon.goto(0, -100)  
balon.pendown()
balon.color('black')
balon.pensize(5)
balon.setheading(90)  
balon.forward(100)  

turtle.done()

turtle.mainloop()
