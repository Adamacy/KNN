from tkinter import *
from tkinter.ttk import *
import tkinter.messagebox as msg
from main import generate_dataset, count_elements, sort_distance
import matplotlib.pyplot as plt
from matplotlib.backend_bases import MouseButton
import math

def KNN(x_b: float, y_b: float, n: int) -> float:
    """Classifies to which group point should be added"""
    
    
    #Calculating distance to each point
    data = []
    for group in dataset:
        for i in range(len(group["X"])):
            x_a = group["X"][i]
            y_a = group["Y"][i]
            distance = round(math.sqrt(((x_b - x_a)**2) + ((y_b - y_a)**2)), 2)
            data.append({"group": group["group"], "distance": distance})
    data.sort(key = sort_distance)
    highest = count_elements(data[:n])
    for i in dataset:
        if i["group"] == highest:
            i["X"].append(x_b)
            i["Y"].append(y_b)
            refresh()
        

def on_click(event):
    if event.button is MouseButton.LEFT:
        x = round(event.xdata, 2); y = round(event.ydata, 2)
        KNN(x, y, n = neighbours_num.get())

def generate():
    global dataset
    if group_nums.get() < 2:
        msg.showinfo("Error", "Number of groups can't be smaller than 2")
    else:
        dataset = generate_dataset(group_nums.get(), points_num.get())
        for group in dataset:
            plt.scatter(group["X"], group["Y"])
        plt.connect("button_press_event", on_click)
        plt.show()
        

def refresh():
    plt.cla()
    for group in dataset:
        plt.scatter(group["X"], group["Y"])
    plt.show()




root = Tk()
root.geometry("300x500")
root.title("KNN - Adam Jakubiak")


#Variables
group_nums = IntVar()
points_num = IntVar()
group_nums.set(2)
points_num.set(10)
neighbours_num = IntVar()
neighbours_num.set(5)

#Widgets
Label(root, text="Number of groups").grid(row = 0, column = 1, padx=100)
Entry(root, textvariable=group_nums).grid(row = 1, column = 1)
Label(root, text="Number of point in group").grid(row = 2, column = 1)
Entry(root, textvariable=points_num).grid(row = 3, column = 1)
Label(root, text="Number of neighbours").grid(row = 4, column = 1)
Entry(root, textvariable=neighbours_num).grid(row = 5, column = 1)
Button(root, command=generate, text="Generate").grid(row = 6, column = 1)


root.mainloop()