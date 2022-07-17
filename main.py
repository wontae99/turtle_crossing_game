import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

scoreboard = Scoreboard()
car_manager = CarManager()
player = Player()


screen.listen()
screen.onkeypress(player.go_forward, "Up")
screen.onkeypress(player.go_right, "Right")
screen.onkeypress(player.go_left, "Left")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    car_manager.car_generator()
    car_manager.move_cars()
    for car in car_manager.all_cars:
        if player.distance(car.position()) < 20:
            scoreboard.game_over()
            game_is_on = False
    if player.ycor() > 280:
        player.reset_position()
        car_manager.car_generator()
        scoreboard.get_score()
        scoreboard.print_score()
        car_manager.level_up()

screen.exitonclick()
