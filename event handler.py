from tkinter import *

window = Tk()
window.title("Event Handler")
window.geometry("100x100")

def handle_keypress(event):
    """print the character associated to the key pressed"""
    print(event.char)

window.bind("<Key>",handle_keypress)

def hand_click(event):
    print("\nThe button was clicked!")

button = Button(text="Click me!")
button.pack()

button.bind("<Button-1>", hand_click)

window.mainloop()