from turtle import Screen
from snake import Snake
from food import Food
from score_board import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.listen()
screen.tracer(0)  # Turning off the screen. The tracer when on(1) shows animation on  screen

snake = Snake()
food = Food()
score_board = ScoreBoard()

# cause the snake to move
is_game_on = True
while is_game_on:
    screen.update()  # there is no animation for the update() function to trigger yet and: screen.tracer(0)
    time.sleep(0.1)  # to cause a delay of 0.1 seconds

    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:  # distance b/w them is measured from the center of snake and that of food
        food.refresh_food_location()
        snake.extend()
        score_board.score_update()

    # detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score_board.reset()
        snake.reset()

    # #detect collision with tail
    for segment in snake.segments[1:]:
        # since the first segment is the snake head
        if snake.head.distance(segment) < 10:
            score_board.reset()
            snake.reset()

    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

screen.exitonclick()