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
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label_timer.config(text="Get Sh*t Done!", fg=GREEN)
    label_check.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 == 1:
        count_down(work_sec)
        label_timer.config(text="Get Sh!t Done💖", fg=GREEN)
    elif reps % 8 == 0:
        count_down(long_break_sec)
        label_timer.config(text="Break🍽️", fg=RED)
    else:
        count_down(short_break_sec)
        label_timer.config(text="Break☕", fg=PINK)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f"0{count_sec}"


    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        window.attributes('-topmost', True)
        window.attributes('-topmost', False)
        start_timer()
        marks = ""
        for _ in range(math.floor(reps/2)):
            marks += "✔"
        label_check.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=100, pady=50, bg=YELLOW)
window.title("Goal Timer")
app_width = 600
app_height = 450

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2)

window.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

label_timer = Label(text="Get Sh*t Done!", fg=GREEN, font=(FONT_NAME, 20, "bold"), bg=YELLOW)
label_timer.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(102,112, image=tomato_img)
timer_text = canvas.create_text(112, 135, text="00:00", fill="white", font=(FONT_NAME, 32, "bold"))
canvas.grid(row=1, column=1)


button_start = Button(text="Start", command=start_timer, font=(FONT_NAME, 16, "bold"), fg=GREEN, bg=YELLOW, highlightthickness=0)
button_start.grid(row=2, column=0)

button_reset = Button(text="Reset", command=reset_timer, font=(FONT_NAME, 16,"bold"), fg=GREEN, bg=YELLOW, highlightthickness=0)
button_reset.grid(row=2, column=2)

label_check = Label(fg=GREEN, font=(FONT_NAME, 24, "bold"), bg=YELLOW)
label_check.grid(row=3, column=1)

window.mainloop()
