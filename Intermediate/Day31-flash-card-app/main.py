from tkinter import *
import pandas as pd
from random import choice

BACKGROUND_COLOR = "#B1DDC6"


# ---------------------------- LOAD WORDS ------------------------------- #
try:
    # if there's saved progress, load the progress file
    progress_data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    word_list = original_data.to_dict(orient="records")
else:
    word_list = progress_data.to_dict(orient="records")


# ---------------------------- CREATE NEW FLASH CARDS ------------------------------- #
def new_card():
    global new_word, flip_timer
    window.after_cancel(flip_timer)
    new_word = choice(word_list)
    canvas.itemconfig(canvas_img, image=front_img)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=f"{new_word['French']}", fill="black")

    flip_timer = window.after(3000, flip_card)


# ---------------------------- FLIP CARDS ------------------------------- #
def flip_card():
    canvas.itemconfig(canvas_img, image=back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=f"{new_word['English']}", fill="white")


# ---------------------------- SAVE PROGRESS ------------------------------- #
def update_progress():
    # save the progress
    word_list.remove(new_word)
    new_progress = pd.DataFrame(word_list)
    new_progress.to_csv("data/words_to_learn.csv", index=False)
    # create a new card
    new_card()


# ---------------------------- UI SETUP ------------------------------- #
# set the window
window = Tk()
window.config(bg=BACKGROUND_COLOR, padx=30, pady=30)
window.title("Flash Cards")
flip_timer = window.after(3000, flip_card)

# set the card
# set the background
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
canvas_img = canvas.create_image(400, 263, image=front_img)
# set the words
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
canvas.grid(column=1, row=1, columnspan=2)

# set the wrong button
wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=new_card)
wrong_button.grid(column=1, row=2)

# set the right button
right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=update_progress)
right_button.grid(column=2, row=2)

new_card()

# keep the window
window.mainloop()

