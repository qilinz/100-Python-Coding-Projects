from tkinter import *

# window setup
window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

# content setup
# mile input
entry = Entry(width=5)
entry.focus()
entry.grid(column=2, row=1)

# miles
label_mile = Label(text="Miles")
label_mile.grid(column=3, row=1)

# km
label_km = Label(text="Kms")
label_km.grid(column=3, row=2)

# equal
label_equal = Label(text="is equal to")
label_equal.grid(column=1, row=2)

# output
label_output = Label(text="0")
label_output.grid(column=2, row=2)


# button
def button_click():
    mile = int(entry.get())
    km = round(mile * 1.609, 1)
    label_output.config(text=km)


button = Button(text="Calculate",command=button_click)
button.grid(column=2, row=3)

# keep the window
window.mainloop()