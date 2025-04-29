import turtle
win = turtle.Screen()
bob = turtle.Turtle()

# characteristics
win.bgcolor("lightblue")
bob.shape("turtle")
bob.color("purple")

# movements
bob.penup()
bob.pendown()
for i in [0,1,2,3]:
    bob.forward(50)
    bob.left(90)

bob.penup()
bob.forward(50)
bob.pendown()

for i in [0,1,2]:
    bob.forward(50)
    bob.left(120)

win.mainloop() 
 