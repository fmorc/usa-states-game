from turtle import Turtle, Screen
import pandas

TOTAL_STATES = 50

screen = Screen()
screen.title("U.S. States Game")

turtle = Turtle()
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
turtle.penup()
screen.tracer(0)

data = pandas.read_csv("50_states.csv")
title = "Guess the state"
all_states = data["state"].to_list()
guessed_states = []

while len(guessed_states) < TOTAL_STATES:
    answer_state = screen.textinput(title=title, prompt="What's another state's name?").title()
    state = data[data.state == answer_state]
    if answer_state == "Exit":
        # export_states = []
        # for state in all_states:
        #     if state not in guessed_states:
        #         export_states.append(state)
        missing_states = [state for state in all_states if state not in guessed_states]
        pandas.DataFrame(missing_states).to_csv('missing_states.csv')
        break
    if not state.empty and answer_state not in guessed_states:
        new_turtle = Turtle()
        new_turtle.penup()
        new_turtle.hideturtle()
        new_turtle.setpos(x=state.x.item(), y=state.y.item())
        new_turtle.write(answer_state)
        guessed_states.append(answer_state)
        title = f"{len(guessed_states)}/{TOTAL_STATES} States Correct"
        screen.update()



