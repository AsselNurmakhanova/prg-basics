import turtle
import figures   

window = turtle.Screen()
window.bgcolor("lightgreen")

pen = turtle.Turtle()
pen.speed(5)

pen.penup()
pen.goto(-150, 120)
pen.pendown()
figures.draw_square(pen, 80)

pen.penup()
pen.goto(100, 120)
pen.pendown()
figures.draw_square(pen, 120)

pen.penup()
pen.goto(-150, -20)
pen.pendown()
figures.draw_triangle(pen, 100)

pen.penup()
pen.goto(100, -20)
pen.pendown()
figures.draw_triangle(pen, 140)

pen.penup()
pen.goto(-150, -180)
pen.pendown()
figures.draw_rectangle(pen, 120, 60)

pen.penup()
pen.goto(100, -180)
pen.pendown()
figures.draw_rectangle(pen, 160, 40)

pen.hideturtle()
window.mainloop()
