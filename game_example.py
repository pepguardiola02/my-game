import turtle
import time
import random


delay = 0.1




orm = turtle.Turtle()

orm = turtle.Screen()
orm.title("snake spel av amar")
orm.bgcolor("green")
orm.setup(width=600, height=600)
orm.tracer(0)



head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)


segments = []


def go_up():
    head.direction = "up"

def go_down():
    head.direction = "down"

def go_right():
    head.direction = "right"

def go_left():
    head.direction = "left"  

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

    if head.direction == "left":   
        x = head.xcor()
        head.setx(x - 20)
        

orm.listen()
orm.onkeypress(go_up, "w")
orm.onkeypress(go_down, "s")
orm.onkeypress(go_right, "d")
orm.onkeypress(go_left, "a")



while True:
    orm.update()

    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)
        

    new_segment = turtle.Turtle()
    new_segment.speed(0)
    new_segment.shape("square")
    new_segment.color("black")
    new_segment.penup()
    segments.append(new_segment)


for index in range(len(segments)-1, 0, -1):
    x = segments[index-1].xcor()
    y = segments[index-1].ycor()
    segments[index].goto(x, y)

if len(segments) > 0:
    x = head.xcor()
    y = head.ycor()
    segments[0].goto(x, y)
move()

time.sleep(delay)

orm.mainloop()