from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
timer = None
reps = 0
check = ""
# ---------------------------- TIMER RESET ------------------------------- # 
def timer_reset():
    global timer, reps, check
    window.after_cancel(timer)
    reps = 0
    check = ""
    button1.config(state="normal")
    label1.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    button1.config(state="disabled")
    work_sec = WORK_MIN * 1
    short_break_sec = SHORT_BREAK_MIN * 1
    long_break_sec = LONG_BREAK_MIN * 1

    if reps % 8 == 0:
        label1.config(text="Break", fg=RED)
        sec = long_break_sec
    else:
        if reps % 2 != 0:
            label1.config(text="Work", fg="green")
            sec = work_sec
        else:
            label1.config(text="Break", fg=PINK)
            sec = short_break_sec

    count_down(sec)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global check, timer
    count_min = count // 60
    count_sec = count % 60

    if count_min == 0 and count_sec == 10:
        change_canvas_timer_text_fill(10)

    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_sec == 0:
        count_sec = "00"
    if count_min < 10:
        count_min = f"0{count_min}"

    count_format = f"{count_min}:{count_sec}"
    canvas.itemconfig(timer_text, text=count_format)
    if count > 0:
        timer = window.after(1000, count_down, count - 1)

    else:
        if reps % 2 != 0:
            check = check + "✔"
            label2.config(text=check)

        start_timer()

        if reps > 8:
            window.after_cancel(timer)
            label1.config(text="Done:) ", fg="purple")
            check = check + "✔"
            label2.config(text=check)
            canvas.itemconfig(timer_text, text="00:00")
            button1['state'] = DISABLED




def change_canvas_timer_text_fill(count):
    canvas.itemconfig(timer_text, fill="yellow")
    if count > 0:
        window.after(1000, change_canvas_timer_text_fill, count - 1)
    else:
        canvas.itemconfig(timer_text, fill="white")

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

label1 = Label(text="Timer", font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW)
label1.grid(column=1, row=0)
label2 = Label(text="", font=(FONT_NAME, 45, "bold"), fg=GREEN, bg=YELLOW)
label2.grid(column=1, row=3)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

button1 = Button(text="Start", font=("Arial", 20, "bold"), command=start_timer, highlightthickness=0)
button1.grid(column=0, row=2)
button2 = Button(text="Reset", font=("Arial", 20, "bold"), command=timer_reset, highlightthickness=0)
button2.grid(column=2, row=2)

window.mainloop()
