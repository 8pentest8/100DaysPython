# import random
# import turtle
# from turtle import Turtle, Screen
# from random import choice


#############################18 days
# tim = Turtle()
# tim.shape("turtle")
# turtle.colormode(255)
#
#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     color = (r, g, b)
#     return color
#
# tim.speed("fastest")
#
# def draw_spirograph(size_of_gap):
#     for _ in range(360 // size_of_gap):
#         tim.color(random_color())
#         tim.circle(100)
#         tim.setheading(tim.heading() + size_of_gap)
# draw_spirograph(5)



# def moving_square():
#     tim.forward(200)
#     tim.right(90)
#
#
# for square in range(4):
#     moving_square()
# n = 0
# while n < 30:
#     tim.pendown()
#     tim.forward(10)
#     tim.up()
#     tim.forward(10)
#     n += 1

# for number in range(10):

# num = 0
#
# list_color = ["royal blue", "dark olive green", "aquamarine", "seashell", "gold", "blue violet", "dark red"]
# def draw_shape(num_sides):
#     for _ in range(num_sides):
#         angle = 360 / num_sides
#         tim.forward(100)
#         tim.right(angle)
#
#
# for _n in range(7):
#     num = 3
#     draw_shape(num + _n)
#     tim.pencolor(list_color[_n - 1])
# list_color = ["royal blue", "dark olive green", "aquamarine", "seashell", "gold", "blue violet", "dark red"]
# side = ["right", "left"]
# direction = [0, 90, 180, 270]
# tim.pensize(20)
# tim.speed("fastest")
# for _ in range(200):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(direction))

##########################19 days
#
# tim = Turtle()
# screen = Screen()
#
#
# def move_forwards():
#     tim.forward(10)
#
#
# def move_back():
#     tim.backward(10)
#
#
# def counter_clockwise():
#     new_heading = tim.heading() + 10
#     tim.setheading(new_heading)
#
# def clockwise():
#     new_heading = tim.heading() - 10
#     tim.setheading(new_heading)
#
#
# def clear_drawlind():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
#
# screen.listen()
# screen.onkey(fun=move_forwards, key="w")
# screen.onkey(fun=move_back, key="s")
# screen.onkey(fun=counter_clockwise, key="a")
# screen.onkey(fun=clockwise, key="d")
# screen.onkey(fun=clear_drawlind, key="e")
#
# screen.exitonclick()
###############################Day 20 Snake

###############################Day 24

# with open("test.txt") as file:
#     contents = file.read()
#     print(contents)
#
# with open("new_file.txt", mode="a") as file:
#     file.write("abracadabra")

###############################Day 25

# with open("weather_data.csv") as f:
#     data = f.readlines()
#     print(data)
# import csv
# with open("weather_data.csv") as f:
#     data = csv.reader(f)
#     temperatures = []
#     for row in data:
#         temperatures.append(row[1])
# temperatures.remove("temp")
# print(temperatures)
# import pandas

# data = pandas.read_csv("weather_data.csv")
# data_dic = data.to_dict()
# print(data_dic)
#
# data_list = data["temp"].to_list()
# data_ = sum(data_list)
#
# print(data["temp"].max())
#
# print(data.condition)
# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# grey = len(data[data["Primary Fur Color"] == "Gray"])
# red = len(data[data["Primary Fur Color"] == "Cinnamon"])
# black = len(data[data["Primary Fur Color"] == "Black"])
# data_dic = {
#     "Fur Color": ["Gray", "Cinnamon", "Black"],
#     "Count": [grey, red, black]
# }
# to_csv = pandas.DataFrame(data_dic)
# to_csv.to_csv("squirrel_count.csv")


###############################Day 26


# numbers = [1, 2, 3]
# new_number = [n + 1 for n in numbers]
# print(new_number)

# name = "Igor"
# new_list = [letter for letter in name]
#
# print(new_list)
# new_list = [n * 2 for n in range(1, 5)]
# print(new_list)

# letters = ["a", "s", "d", "a", "s"]
#
# new_list_ = [letter for letter in letters if letter == "a"]
# print(new_list_)

# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
#
# new_list = [name.upper() for name in names if len(name) > 5]
# print(new_list)
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# import random
# students_score = {student: random.randint(1, 100) for student in names}
#
# passed_students = {student: score for (student, score) in students_score.items() if score > 59}


# import pandas
# student_dict = {
#     "student": ["Alex", "Beth", "Caroline"],
#     "score": [56, 76, 99]
# }
# student_data_frame = pandas.DataFrame(student_dict)


###############################Day 27

from tkinter import *

#Creating a new window and configurations
window = Tk()
window.title("Widget Examples")
window.minsize(width=500, height=500)

#Labels
label = Label(text="This is old text")
label.config(text="This is new text")
label.pack()

#Buttons
def action():
    print("Do something")

#calls action() when pressed
button = Button(text="Click Me", command=action)
button.pack()

#Entries
entry = Entry(width=30)
#Add some text to begin with
entry.insert(END, string="Some text to begin with.")
#Gets text in entry
print(entry.get())
entry.pack()

#Text
text = Text(height=5, width=30)
#Puts cursor in textbox.
text.focus()
#Adds some text to begin with.
text.insert(END, "Example of multi-line text entry.")
#Get's current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()

#Spinbox
def spinbox_used():
    #gets the current value in spinbox.
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

#Scale
#Called with current scale value.
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

#Checkbutton
def checkbutton_used():
    #Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())
#variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

#Radiobutton
def radio_used():
    print(radio_state.get())
#Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


#Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()
window.mainloop()



# from tkinter import *
#
#
# def button_clicked():
#     print("I got clicked")
#     new_text = input.get()
#     my_label.config(text=new_text)
#
#
# window = Tk()
# window.title("My First GUI Program")
# window.minsize(width=500, height=300)
# window.config(padx=100, pady=200)
#
# #Label
# my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
# my_label.config(text="New Text")
# my_label.grid(column=0, row=0)
# my_label.config(padx=50, pady=50)
#
# #Button
# button = Button(text="Click Me", command=button_clicked)
# button.grid(column=1, row=1)
#
# new_button = Button(text="New Button")
# new_button.grid(column=2, row=0)
#
# #Entry
# input = Entry(width=10)
# print(input.get())
# input.grid(column=3, row=2)
#
#

# window.mainloop()
# def add(*args):
#     args = sum(args)
#     return args
#
# def calculate(**kwargs):
#     print(kwargs)
#     # for key, value in kwargs.items():
#     #     print(key)
#     #     print(value)
#
# calculate(add=3, multiply=5)































