import turtle
import pandas

screen = turtle.Screen()
screen.title("US States game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
states_to_learn = []
guessed_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 states guessed correctly",
                                    prompt="What's another state's name?")
    if answer_state == "Exit":
        for state in all_states:
            if state not in guessed_states:
                states_to_learn.append(state)
        print(states_to_learn)
        states_to_review_file = pandas.DataFrame(states_to_learn)
        states_to_review_file.to_csv("states_to_review.csv")
        exit(0)
    elif answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(float(state_data.x), float(state_data.y))
        t.write(state_data.state.item())

screen.exitonclick()
