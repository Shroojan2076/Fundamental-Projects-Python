import turtle
import random

position = [25, -25, 125, -125, 75, -75]
color = ['red', 'blue', 'green', 'yellow', 'pink', 'black']
screen_width = 1000
screen_height = 600
start_line = int(-(screen_width / 2 - 10))
end_line = int((screen_width / 2 - 10))
all_turtles = []
race_on = False

scr = turtle.Screen()
scr.setup(height= screen_height, width= screen_width)
scr.title('Turtle Race Game.')
announcer = turtle.Turtle()
announcer.hideturtle()

user_bet = scr.textinput(title='Welcome to the Turtle race!', prompt= 'Which turtle will you bet on?')

if user_bet == None:
    scr.bye()
    exit()

user_bet = user_bet.lower()

if user_bet == '':
    scr.bye()
    exit()

elif user_bet not in color:
    announcer.clear()
    announcer.goto(0, 0) 
    announcer.write('Colour not available.', align='center', font=('Arial', 18, 'bold'))

else:
    for turtle_no in range(6):
        new_turtle = turtle.Turtle(shape='turtle')
        new_turtle.penup()
        new_turtle.goto(x = start_line, y = position[turtle_no])
        new_turtle.color(color[turtle_no])
        all_turtles.append(new_turtle)

    race_on = True

    while race_on:
        for tur in all_turtles:
            turtle_speed = random.randint(10,50)
            tur.forward(turtle_speed)
            if tur.xcor() >= end_line:
                race_on = False
                if tur.pencolor() == user_bet:
                    announcer.clear()
                    announcer.goto(0, 0)
                    announcer.write(f'You won the bet!\nYour {tur.pencolor()} turtle won!', align='center', font=('Arial', 18, 'bold'))   
                    break
                else:
                    announcer.clear()
                    announcer.goto(0, 0)
                    announcer.write(f'You lost the bet.\nThe winning turtle is {tur.pencolor()}!', align='center', font=('Arial', 18, 'bold'))   
                    break

scr.exitonclick()

