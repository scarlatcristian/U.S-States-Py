import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. State Game")
img = "usa_states_map.gif"
screen.addshape(img)

turtle.shape(img)

data = pandas.read_csv("usa_50_states.csv").to_dict()

guessed_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?")

    for state in data["state"]:
        if data["state"][state].lower().replace(" ", "") == answer_state.lower().replace(" ", ""):
            guessed_states.append(answer_state)
            state_turtle = turtle.Turtle()
            state_turtle.hideturtle()
            state_turtle.penup()
            state_turtle.goto(
                x=data["x"][state], y=data["y"][state])
            state_turtle.write(
                f"{data['state'][state]}", align="center", font="Ariel")

# Get the states coors
# def get_mouse_click_coors(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coors)


turtle.mainloop()
