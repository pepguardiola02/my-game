import turtle
import time
import random

delay = 0.1

orm = turtle.Screen()
orm.title("Snake spel av Amar")
orm.bgcolor("green")
orm.setup(width=600, height=600)
orm.tracer(0) 


huvud = turtle.Turtle()
huvud.speed(0)
huvud.shape("square")
huvud.color("black")
huvud.penup()
huvud.goto(0,0)
huvud.direction = "stop"

mat = turtle.Turtle()
mat.speed(0)
mat.shape("circle")
mat.color("red")
mat.penup()
mat.goto(0,100)

segments = []

def go_up():
    if huvud.direction != "down":
        huvud.direction = "up"

def go_down():
    if huvud.direction != "up":
        huvud.direction = "down"

def go_left():
    if huvud.direction != "right":
        huvud.direction = "left"

def go_right():
    if huvud.direction != "left":
        huvud.direction = "right"

def move():
    if huvud.direction == "up":
        y = huvud.ycor()
        huvud.sety(y + 20)

    if huvud.direction == "down":
        y = huvud.ycor()
        huvud.sety(y - 20)

    if huvud.direction == "left":
        x = huvud.xcor()
        huvud.setx(x - 20)

    if huvud.direction == "right":
        x = huvud.xcor()
        huvud.setx(x + 20)


orm.listen()
orm.onkeypress(go_up, "i")
orm.onkeypress(go_down, "k")
orm.onkeypress(go_left, "j")
orm.onkeypress(go_right, "l")

while True:
    orm.update()

    if huvud.distance(mat) < 20:
       
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        mat.goto(x,y)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("circle")
        new_segment.color("black")
        new_segment.penup()
        segments.append(new_segment)

   
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:
        x = huvud.xcor()
        y = huvud.ycor()
        segments[0].goto(x,y)

    move()    

    time.sleep(delay)

orm.mainloop()