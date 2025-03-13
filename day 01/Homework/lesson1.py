from turtle import *

#we want to paint a house


width(6)
color("green")
begin_fill()
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

end_fill()


forward(75)
color("blue")
begin_fill()
left(90)
forward(115)
right(90)
forward(50)
right(90)
forward(115)
end_fill()

color("red")
left(89)

penup()
goto(200, 200)
pendown()
begin_fill()

left(130)
forward(150)

left(98)
forward(163)
end_fill()

penup()
goto(65,100)
pendown()
begin_fill()

color("yellow")
begin_fill()
right(51)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()

penup()
goto(182,100)
pendown()
begin_fill()

color("yellow")
begin_fill()
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()

exitonclick()