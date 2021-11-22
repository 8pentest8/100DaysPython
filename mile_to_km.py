from tkinter import *
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=40)


def calculate():
    miles = float(entry.get())
    km = miles * 1.60934
    label_3.config(text=km)


button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)

entry = Entry(width=10)
entry.grid(column=1, row=0)
entry.insert(END, string="0.0")

label_1 = Label(text="Miles")
label_1.grid(column=2, row=0)

label_2 = Label(text="is equal to")
label_2.grid(column=0, row=1)

label_3 = Label(text="0.0")
label_3.grid(column=1, row=1)

label_4 = Label(text="Km")
label_4.grid(column=2, row=1)

window.mainloop()
