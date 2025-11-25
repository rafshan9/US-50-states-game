import turtle 
import pandas

data = pandas.read_csv("50_states.csv")

screen = turtle.Screen()
screen.title("US state game")
image = "blank_states_img.gif"


turtle.addshape(image)
turtle.shape(image)

all_states = data.state.to_list()
guessed_states = []


while len(guessed_states) < 50:
    answer_state = screen.textinput(title = "Guess the sate", prompt =" What's another state's name?").title() 

    if answer_state == "Exit":
    

        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break




    if answer_state in data.state.values:
        #specific row of data for this state
        guessed_states.append(answer_state)
        

        #create a turtle to write the name
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]

        #put the answer to proper coordinates
        t.goto(int(state_data.x), int(state_data.y))

        #write the state name
        t.write(state_data.state.item())
        

turtle.mainloop()
