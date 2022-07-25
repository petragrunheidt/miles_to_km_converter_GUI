from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(100, 100)
window.maxsize(300, 200)
window.config(padx=50, pady=50)

# Labels

miles_label = Label(text="miles", font=("Arial", 12, "italic"))
miles_label.config(text="miles")
miles_label.grid(column=2, row=0)
miles_label.config(padx=5, pady=10)

km_label = Label(text="km", font=("Arial", 12, "italic"))
km_label.config(text="km")
km_label.grid(column=2, row=1)
km_label.config(padx=5, pady=10)

equal_label = Label(text="is equal to", font=("Arial", 12, "italic"))
equal_label.config(text="is equal to")
equal_label.grid(column=0, row=1)
equal_label.config(padx=5, pady=10)

answer_label = Label(text="result", font=("Arial", 12, "italic"))
answer_label.config(text="result")
answer_label.grid(column=1, row=1)
answer_label.config(padx=5, pady=10)

miles_input = Entry(width=10)
print(miles_input.get())
miles_input.grid(column=1, row=0)

def miles_to_km():
    answer_label["text"] = str(round(float(miles_input.get()) * 1.60934, 2))




button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)
miles_label.config(padx=5, pady=10)

window.mainloop()
