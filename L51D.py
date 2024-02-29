#Emme and Mandy

import turtle
riley = turtle.Turtle()
riley.width(5)
riley.speed(0)

def draw_star(color):
    for side in range(5):
        riley.color(color)
        riley.forward(100)
        riley.right(144)

mood= input("What is your mood?")
if mood == "Happy":
    draw_star("pink")
elif mood == "Sad":
    draw_star("blue")
elif mood == "Sleepy":
    draw_star("green")
elif mood == "Angry":
    draw_star("red")


        
