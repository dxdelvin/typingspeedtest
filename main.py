from tkinter import *


window = Tk()
window.title("Typing Speed Checker")
window.geometry("480x420")
window.config()
window.resizable('False','False')

def display():
    computer.delete('1.0','end')
    computer.config(text=user_text.get('1.0', 'end-1c'))
    window.after(1000, display)

computer = Text(height=2, width=20, padx=10, pady=10)
computer.place(relx= 0.5, rely=0.4, anchor="center")

user_text = Text(height=2, width=20, padx=10, pady=10)
user_text.place(relx= 0.5, rely=0.5, anchor="center")

display()

high_score = Label(text="Your High Score: " , font=('Poppins', 12)).place(relx= 0.5, rely=0.8, anchor="center")
high_score = Label(text="0 WPM" , font=('Poppins', 12)).place(relx= 0.5, rely=0.87, anchor="center")











window.mainloop()