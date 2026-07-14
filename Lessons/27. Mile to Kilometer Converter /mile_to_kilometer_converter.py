import tkinter

window = tkinter.Tk()
window.title("Mile to Kilometer Converter")
window.minsize(width=400, height=150)
window.config(padx=20, pady=20)

is_equal_to = tkinter.Label(text="is equal to", font=("Arial", 16))
is_equal_to.grid(column=0, row=1)

miles_text = tkinter.Label(text="Miles", font=("Arial", 16))
miles_text.grid(column=2, row=0)

kilometers_text = tkinter.Label(text="Kilometers", font=("Arial", 16))
kilometers_text.grid(column=2, row=1)

change_text = tkinter.Label(text="0", font=("Arial", 16))
change_text.grid(column=1, row=1)

def change_text_funktion():
    change_text.config(text=float(input_field.get()) * 1.60934)

my_button = tkinter.Button(text="Calculate", command=change_text_funktion, font=("Arial", 16))
my_button.grid(column=1, row=2)

input_field = tkinter.Entry(width=10, font=("Arial", 16))
input_field.grid(column=1, row=0)

window.mainloop()
