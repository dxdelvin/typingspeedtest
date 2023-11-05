from tkinter import *
import ctypes
import random


ctypes.windll.shcore.SetProcessDpiAwareness(1)
window = Tk()
window.title("Typing Speed Checker")
window.geometry("480x420")
window.config()
window.resizable('False','False')

window.option_add('*Font', "Poppins")
window.option_add('*Button.Font', "Poppins")
window.option_add('*Foreground', 'black')


def start_game():
    text_list = ["Apple is the brave thing i have ever shown",
                "Why i am the one who is going to eat the peanut butter",
                "Eat Well so you can be angry and frustrated from your life"]

    text = random.choice(text_list).lower()

    split_point = 0
    # My Text Label
    global text_label
    text_label = Label(window, text=text[0:split_point], fg="grey", font=("Poppins", 24))
    text_label.place(relx=.5, rely=.45, anchor="e")

    global write_label
    write_label = Label(window, text=text[split_point:], font=("Poppins", 24))
    write_label.place(relx=.5, rely=.45, anchor="w")

    # My Time Label
    global time_label
    time_label = Label(window, text=f"7 Seconds Left", fg="grey", font=("Poppins", 16))
    time_label.place(relx=.5, rely=.3, anchor="center")

    # My Current Letter Label
    global letter_label
    letter_label = Label(window, text=text[split_point], fg="grey", font=("Poppins", 16))
    letter_label.place(relx=.5, rely=.6, anchor="center")

    global current_time
    global stillWriting
    current_time = 0
    stillWriting = True

    window.bind('<Key>', keyPress)

    window.after(1000, add_secound)
    window.after(10000, stop_secound)

def add_secound():
    global current_time
    current_time += 1
    time_label.configure(text=f"{10-current_time} Seconds")

    if stillWriting:
        window.after(1000, add_secound)

def stop_secound():
    global stillWriting
    stillWriting = False

def keyPress(e):
    if e.char.lower() == write_label.cget('text')[0].lower():
        write_label.config(text=write_label.cget('text')[1:])
        text_label.config(text=text_label.cget('text') + e.char.lower())
        letter_label.config(text=text_label.cget('text')[0])

start_game()



window.mainloop()


