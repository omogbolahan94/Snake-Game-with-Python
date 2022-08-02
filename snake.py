from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]  # the default size of a turtle is 20x20
MOVE_DISTANCE = 20
UP = 90
RIGHT = 0
LEFT = 180
DOWN = 270


class Snake:
    def __init__(self):
        """
        once the instance of a class is created, the commands
        inside this special function is executed
        """
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """
        create the initial length of the snake in a
        specific starting position and execute it one time in the
        __init__ method
        ;return:
        """
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        """
        adds a new turtle to the self.segment when ever the snake eats a food
        :return:
        """
        new_turtle = Turtle(shape="square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(position)
        self.segments.append(new_turtle)

    def extend(self):
        """
        add a new segment to the list of segment when
        snake eats a food. this new segment will take the
        position of the last segment in the list of segment
        :return:
        """
        self.add_segment(self.segments[-1].position())  # obtain the position of the last element

    def move(self):
        """
        the last segment will obtain the position of the second to the last segment
        and the second to the last will move to the next on and so on until
        the second moves to the position of the first one(the head) before the
        After the loop, move the head to the MOVE_DISTANCE
        :return:
        """
        start_range = len(self.segments) - 1
        end = 0
        step = -1
        for num_of_seg in range(start_range, end, step):
            new_x = self.segments[num_of_seg - 1].xcor()  # get x coordinates of the 2nd to the last segment
            new_y = self.segments[num_of_seg - 1].ycor()  # get y coordinates of the 2nd to the last segment
            self.segments[num_of_seg].goto(new_x, new_y)  # move the 3rd segment to position of the second segment
        self.head.forward(MOVE_DISTANCE)  # move all 3 forward before the update gets triggered

    def reset(self):
        """
        delete all the segment in the list and create a new list of segment
        starting with 3 segment and reset the head
        :return:
        """
        for segment in self.segments:
            segment.goto(1000, 1000)  # before clearing, take each segment to a location off the screen
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)  # starting position of the turtle

