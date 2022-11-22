import tkinter
from tkinter import *

# create program window
window = Tk()
window.title("Watermark Generator")
window.minsize(width=500, height=300)

#label that instructs user how to use program
instruction_label = Label(text="Click 'Browse' to find an image to add a watermark to",
                          font=("Arial", 12, "bold")
                          )
instruction_label.pack(side="left")




mainloop()