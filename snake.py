from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVING_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in STARTING_POSITION:
            self.add_segment(i)

    def add_segment(self, i):
        tim = Turtle(shape='square')
        tim.color('white')
        tim.penup()
        tim.setpos(i)
        self.segments.append(tim)

    def extend_snake(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for new_segment in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[new_segment - 1].xcor()
            new_y = self.segments[new_segment - 1].ycor()
            self.segments[new_segment].goto(new_x, new_y)
        self.head.forward(MOVING_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)
