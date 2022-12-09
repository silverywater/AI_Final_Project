from readCSV import readCSV
import Map
import Agent
from tkinter import *
from tkinter import ttk
import tkinter as tk

input_array = [[0, 0], [0, 0], 0, 0]
def submit_handler(widget, start, goal, pathing, climbing):
    s = start.get().split(",")
    input_array[0] = s
    s2 = goal.get().split(",")
    input_array[1] = s2
    input_array[2] = pathing.get()
    input_array[3] = climbing.get()
    print(str(input_array))
def main():
    trailMap = readCSV('TrailMap.csv')
    elevationMap = readCSV('ElevationMap.csv')

    map = Map.Map(elevationMap, trailMap)
    map.printTrailMap()
    map.printElevationMap()
    map.printQTable()
    map.printPolicy()


    agent = Agent.Agent(map)
    agent.setTransitionModel('On', 'Low')

    i = 0
    while not agent.goalReached():

        location1 = agent.location

        location2 = agent.findNextLocation(location1)
        agent.takeMove(location2)

        location3 = agent.findNextLocation(location2)
        print(location1, location2, location3)
        agent.updateQTable(location1,location2, location3)

        map.printQTable()
        i += 1

def inputInterface():
    root = Tk()
    windowWidth = root.winfo_reqwidth()
    windowHeight = root.winfo_reqheight()
    positionRight = int(root.winfo_screenwidth() / 2 - windowWidth / 2)
    positionDown = int(root.winfo_screenheight() / 2 - windowHeight / 2)
    root.geometry("+{}+{}".format(positionRight, positionDown))
    start_label = ttk.Label(root)
    start_entry = ttk.Entry(root)
    goal_label = ttk.Label(root)
    goal_entry = ttk.Entry(root)
    path_label = ttk.Label(root)
    path_frame = ttk.Frame(root)
    control = IntVar()
    control.set(1)
    control2 = IntVar()
    control2.set(1)
    path_radio_1 = ttk.Radiobutton(path_frame, value=1, variable=control)
    path_radio_2 = ttk.Radiobutton(path_frame, value=2, variable=control)
    path_radio_3 = ttk.Radiobutton(path_frame, value=3, variable=control)
    climb_label = ttk.Label(root)
    climb_frame = ttk.Frame(root)
    climb_radio_1 = ttk.Radiobutton(climb_frame, value=1, variable=control2)
    climb_radio_2 = ttk.Radiobutton(climb_frame, value=2, variable=control2)
    climb_radio_3 = ttk.Radiobutton(climb_frame, value=3, variable=control2)
    submit_button = ttk.Button(root, command=lambda: submit_handler(submit_button,start_entry,goal_entry, control, control2))
    start_label["text"] = "Starting grid value (X and Y)"
    goal_label["text"] = "Ending grid value (X and Y)"
    path_label["text"] = "Degree of off-roading"
    climb_label["text"] = "How much can you climb"
    submit_button["text"] = "Submit Entries"
    path_radio_1["text"] = "Trail only"
    path_radio_2["text"] = "No restrictions"
    path_radio_3["text"] = "Hybrid"
    climb_radio_1["text"] = "Low"
    climb_radio_2["text"] = "Medium"
    climb_radio_3["text"] = "High"
    start_label.grid(row=0, column=0)
    start_entry.grid(row=0, column=1)
    goal_label.grid(row=1, column=0)
    goal_entry.grid(row=1, column=1)
    path_label.grid(row=2, column=0)
    path_frame.grid(row=2, column=1)
    path_radio_1.grid(row=0, column=0)
    path_radio_2.grid(row=0, column=1)
    path_radio_3.grid(row=0, column=2)
    climb_label.grid(row=3, column=0)
    climb_frame.grid(row=3, column=1)
    climb_radio_1.grid(row=0, column=0)
    climb_radio_2.grid(row=0, column=1)
    climb_radio_3.grid(row=0, column=2)
    submit_button.grid(row=4, column=1)
    root.mainloop()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #main()
    inputInterface()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
