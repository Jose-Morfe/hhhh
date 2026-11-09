from turtle import *
#star imports everything


shape("turtle")
pensize(3)

#square
for i in range (4):
    forward(150)
    left(90)
#Title area
penup()
goto(-250, 320)
pendown()
write("Welcome to Tracy's Book Shelf!", font=("Courirer", 24, "bold"))

penup()
goto(-100, -250)
pendown()
right(90)
circle(100, 180) # radius, degrees
penup()
left(100)
forward(100)
pendown()

#keeps window open
done()