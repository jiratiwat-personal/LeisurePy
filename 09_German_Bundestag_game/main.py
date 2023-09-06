from turtle import Turtle, Screen, Shape, textinput
import turtle
from tkinter import PhotoImage
import pandas

screen = Screen()
smaller = PhotoImage(file="Germany_location_map.gif").subsample(5, 5)
screen.addshape("smaller", Shape("image", smaller))
t = Turtle("smaller")
t.penup()
t.stamp()
t.hideturtle()
data = pandas.read_csv("list_of_states_of_germany_-57j.csv")["State"]
mapData = pandas.read_csv("germany_state_map.csv")

stateList = data.to_list()
cityCount = 0
done = False
cityDict = {}
def write_dict():
    global cityDict
    cityTable = pandas.DataFrame(cityDict)
    # cityTable.to_csv("germany_state_map.csv")
    print("write csv file")


def print_answer(x, y, cityName, color="black"):
    t.setpos(x, y)
    t.color(color)
    t.write(cityName)
    cityDict[cityName] = (x, y)


def get_mouse_click_coor(x, y):
    global cityCount
    print(x, y, stateList[cityCount])
    global done
    if done:
        return
    if cityCount == len(stateList)-1:
        write_dict()
        done = True
    print_answer(x, y, stateList[cityCount])
    cityCount += 1
    if done:
        return
    print(stateList[cityCount])




# print(stateList[cityCount])
# turtle.onscreenclick(get_mouse_click_coor)

numQuiz = len(mapData.columns)-1
numCorrect = 0
done = False
while not done:
    if numQuiz == numCorrect:
        done = True
        break
    cityName = textinput(f"Quiz {numCorrect}/{numQuiz}", "Name the state of Germany:")
    if cityName in mapData:
        x = int(mapData[cityName][0])
        y = int(mapData[cityName][1])
        print_answer(x, y, cityName)
        del mapData[cityName]
        numCorrect += 1
    elif cityName is None:
        break
# turtle.mainloop()
skip = True
if not done:
    for cityName in mapData:
        if skip:
            skip = False
            continue
        x = int(mapData[cityName][0])
        y = int(mapData[cityName][1])
        print_answer(x, y, cityName, "red")

screen.exitonclick()

