import turtle

beeper=turtle.Turtle()
beeper.shape("turtle")
beeper.speed(0.5)
def p():
    for i in list(range(4)):
        beeper.forward(100)
        beeper.right(90)
def draw_art():
 window=turtle.Screen()
 window.bgcolor("red")
 for i in list(range(40)):
     p()
     beeper.right(10)

 window.exitonclick()

draw_art()
