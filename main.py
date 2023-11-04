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

    if answer_state == 'exit' or answer_state == None:
        missing_states = []
        for state in data["state"]:
            if data["state"][state] not in guessed_states:
                missing_states.append(data["state"][state])
        new_data = pandas.DataFrame(
            missing_states).to_csv("states_to_learn.csv")
        break

    for state in data["state"]:
        if data["state"][state] == answer_state.title():
            guessed_states.append(answer_state.title())
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
