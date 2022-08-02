from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)  # resize the turtle to half of its original size
        self.color("green")
        self.speed(10)
        self.refresh_food_location()

    def refresh_food_location(self):
        """
        This will reset the location of food on the screen
        :return:
        """
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
