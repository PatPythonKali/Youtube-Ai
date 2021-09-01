from tkinter import *

window = Tk()
window.title("Youtube AI")
window.geometry("1280x760")
window.resizable(False, False)

frame = Frame(window, bd=5)
frame.pack()

Button1 = Button(frame, text="submit")
Button1.pack()


window.mainloop()