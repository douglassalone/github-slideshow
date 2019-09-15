import turtle
wn = turtle.Screen()
wn.bgcolor("black")
tess = turtle.Turtle()
tess.shape("turtle")
tess.color("blue")

tess.penup()
size = 20
for i in range(100):
    tess.stamp()
    size = size + 2
    tess.forward(size)
    tess.right(50)

wn.mainloop()