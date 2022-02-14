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
reps = 1
cycle = 0
my_timer = None

# ---------------------------- TIMER RESET ------------------------------- #

def reset():
    global reps
    global cycle
    reps = 1
    cycle = 0
    timer_label.config(text="Timer", fg=GREEN)  # resets timer label to Timer
    check_label.config(text="") #clears all checkmarks
    window.after_cancel(my_timer) #cancels the window.after function that is running the timer
    canvas.itemconfig(timer_text, text="00:00") #sets time back to 00:00

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    global cycle
    print(reps)
    if reps%2 != 0: #25 min timer
        timer_label.config(text="Work", fg=GREEN)
        countdown(WORK_MIN*60)
    elif reps == 8:
        timer_label.config(fg=RED, text="Break")
        countdown(LONG_BREAK_MIN*60)

    elif reps > 8:
        reps =1
    elif reps%2 == 0:
        timer_label.config(fg=PINK, text="Break")
        countdown(SHORT_BREAK_MIN*60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    global reps
    global cycle
    mins = math.floor(count/60)

    seconds = count%60

    pad_mins = str(mins).zfill(2)
    pad_seconds = str(seconds).zfill(2)

    canvas.itemconfig(timer_text, text=f"{pad_mins}:{pad_seconds}")
    if count > 0:
        global my_timer
        # print(count)
        my_timer = window.after(1000, countdown, count - 1) #after 1000 milliseconds, countdown will be called with count -1 as an arg
    else:
        reps += 1
        if reps%2 == 0:
            add_check(int(reps/2))
        start_timer() #restarts timer

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=100, bg=YELLOW)

check = "✔"

#window.after(1000, yeet, "bingbong") #bingbong will be passed into yeet as thing

tomato_img = PhotoImage(file="tomato.png") #converts the image we want to utilize into a format usable by canvas, format is photoimage

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0) #bg = background color, highlightthickness = border thickness
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME,35,'bold'))
canvas.grid(column=1, row=1)

timer_label = Label(text="Timer", fg = GREEN, bg=YELLOW, font=(FONT_NAME,35,'bold'))
timer_label.grid(column=1, row=0)

start_button = Button(text="Start", command = start_timer)
start_button.grid(column=0, row =2)

reset_button = Button(text="Reset", command = reset)
reset_button.grid(column=2, row =2)

def add_check(cycle):
    check_text = ""
    for x in range(cycle):
        check_text += "✔"
    check_label.config(text=check_text)

check_label = Label(text="", fg = GREEN, bg=YELLOW)
check_label.grid(column=1, row =3)

window.mainloop()

