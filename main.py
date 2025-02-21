from itertools import count
from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    win.after_cancel(timer)
    timer_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    ticks.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    temp = "✔" * (reps//2)
    ticks.config(text=temp)

    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        timer_label.config(text="Break" , fg=RED)
    elif reps % 2 == 1:
        count_down(WORK_MIN * 60)
        timer_label.config(text="Work" , fg=GREEN)
    else:
        count_down(SHORT_BREAK_MIN * 60)
        timer_label.config(text="Break" , fg=PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    min = math.floor(count/60)
    sec = count%60
    if sec < 10:
        sec = "0" + str(sec)
    if min < 10:
        min = "0" + str(min)

    canvas.itemconfig(timer_text , text=f"{min}:{sec}")

    if count > 0:
        global  timer
        timer = win.after(1000, count_down, count-1)
    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
win = Tk()
win.title("Pamadoro")
win.config(background=YELLOW , padx=100 , pady=50)

timer_label = Label(text="Timer", font=(FONT_NAME, 45), fg=GREEN, bg=YELLOW)
timer_label.grid(row=0, column=1)

canvas = Canvas(width=202 , height=224, background=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(102, 112, image=tomato_img)
timer_text = canvas.create_text(102,132,text="00:00",font=(FONT_NAME,28,"bold"), fill="White")
canvas.grid(row=1, column=1)


start_button = Button(text="start", bg="White", fg="Black", bd=0, padx=5, pady=2, highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="reset", bg="White", fg="Black", bd=0, padx=5, pady=2, highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

ticks = Label(text="" ,font=(FONT_NAME, 15), fg=GREEN, bg=YELLOW)
ticks.grid(row=3, column=1)




win.mainloop()