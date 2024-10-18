import turtle
turtle.Screen().bgcolor("cyan")
turtle.Screen().setup(500,600)
t= turtle.Turtle()
t.shape("classic")
sides=int(input("Enter desired number of sides : "))
angle=360/sides
len=int(input("Enter length you want :"))
for i in range(sides):
    t.forward(len)
    t.right(angle)

turtle.done()