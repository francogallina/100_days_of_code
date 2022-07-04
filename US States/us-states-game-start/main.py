import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. State Game")

# Establecer la imagen principal
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Creation and configuration of the turtle
turtle_text = turtle.Turtle()
turtle_text.penup()
turtle_text.hideturtle()

# # Obtener las coordenadas del click del mouse
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)

data_csv = pandas.read_csv("50_states.csv")
state = data_csv["state"].to_list()
list_coor_x = data_csv["x"].to_list()
list_coor_y = data_csv["y"].to_list()

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name").title()
    # if answer_state in state:
    #     coor_x = list_coor_x[state.index(answer_state)]
    #     coor_y = list_coor_y[state.index(answer_state)]
    #     turtle_text.goto(coor_x, coor_y)
    #     turtle_text.write(answer_state)

    if answer_state == "Exit":
        missing_states = [x for x in state if x not in guessed_states]

        # missing_states = []
        # for x in state:
        #     if x not in guessed_states:
        #         missing_states.append(x)

        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in state:
        guessed_states.append(answer_state)
        state_data = data_csv[data_csv.state == answer_state]
        turtle_text.goto(int(state_data.x), int(state_data.y))
        turtle_text.write(state_data.state.item())















