import turtle
wn = turtle.Screen()
bob = turtle.Turtle()

bob.penup()
bob.pendown()
for i in [0,1,2,3]:
    bob.forward(50)
    bob.left(90)
for i in [0,1,2]:
    bob.forward(50)
    bob.left(120)
 wn.mainloop()