from turtle import *
import random

# Set up tracy

# image showing
screen = Screen()
screen.setup(1200, 800)
penup()

# Set the background image
screen.bgpic(r"DarkStore.gif")
bgcolor("Black")
shape("turtle")
pensize(4)
goto(-730, 400)
color("white")
text = "You go shopping in hopes of finding something good for \n dinner tonight you enter the store its dark but it has the open sign you enter the store and you see shopping carts \n on the floor and it was abandoned you check the store logo and its the one you always \n go to the one that was always there you decide to stay and look around maybe \n theres customer service you are confused, just \n yersterday the store was lively and bright now its a shell of what it used to be."
write(text, move=False, align="left", font=("Arial", 16, "normal"))
()
goto(-730, 300)
color("white")
text = "What do you do?"
write(text, move=False, align="left", font=("Arial", 16, "normal"))

goto ( 730, 350)
text = "Leave the store"
write(text, move=False, align="left", font=("Arial", 16, "normal"))
goto(730, 250)
text = "Stay and explore"
write(text, move=False, align="left", font=("Arial", 16, "normal"))
hideturtle()

goto(btn1_x, btn1_y)
write("Leave the store", font=("Arial", 14, "bold"))

goto(btn2_x, btn2_y)
write("Stay and explore", font=("Arial", 14, "bold"))

done()
# speed("fastest")
# screen.bgpic(r"BLOODYFLOOR.gif")
