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
reps = 0
checks = ""
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    # enable the start button
    start_button.config(state="normal")
    # stop the countdown
    window.after_cancel(timer)
    # rest the reps
    global reps
    reps = 0
    # reset the checks
    global checks
    checks = ""
    check_mark.config(text=checks)
    # reset the tile and time
    title_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    # disable the start button
    start_button.config(state="disabled")

    global checks
    global reps
    reps += 1
    work_sec = int(WORK_MIN * 60)
    short_break_sec = int(SHORT_BREAK_MIN * 60)
    long_break_sec = int(LONG_BREAK_MIN * 60)
    if reps < 9:
        if reps == 8:
            # add a check
            checks += "✔"
            check_mark.config(text=checks)
            # change the title and countdown the break
            title_label.config(text="Break", fg=RED)
            count_down(long_break_sec)
        elif reps % 2 == 1:
            title_label.config(text="Work", fg=GREEN)
            count_down(work_sec)
        else:
            # add a check
            checks += "✔"
            check_mark.config(text=checks)
            # change the title and countdown the break
            title_label.config(text="Break", fg=PINK)
            count_down(short_break_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = count // 60
    count_sec = count % 60
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec:02}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    elif count == 0:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)


# title of timer
title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 48))
title_label.grid(column=2, row=1)

# pic of tomato
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
# make the countdown time a variable to be accessed elsewhere
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 34, "bold"))
canvas.grid(column=2, row=2)

# start button
start_button = Button(text="Start", font=(FONT_NAME, 16), bg=YELLOW, highlightthickness=0, command=start_timer)
start_button.grid(column=1, row=3)

# reset button
reset_button = Button(text="Reset", font=(FONT_NAME, 16), bg=YELLOW, highlightthickness=0, command=reset_timer)
reset_button.grid(column=3, row=3)

# check mark
check_mark = Label(fg=GREEN, bg=YELLOW)
check_mark.grid(column=2, row=4)

# keep the window
window.mainloop()