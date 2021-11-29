from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
QUESTION_FONT = ("Arial", 20, "italic")


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        # create the window
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        # scoreboard
        self.scoreboard = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.scoreboard.grid(column=2, row=1, padx=20, pady=20)

        # canvas with question
        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            fill=THEME_COLOR,
            text="Sample question",
            font=QUESTION_FONT
        )
        self.canvas.grid(column=1, row=2, columnspan=2, pady=20)

        # True and False button
        true_img = PhotoImage(file="images/true.png")
        false_img = PhotoImage(file="images/false.png")

        self.true_button = Button(image=true_img, highlightthickness=0, command=self.check_answer_true)
        self.true_button.grid(column=1, row=3, pady=20)

        self.false_button = Button(image=false_img, highlightthickness=0, command=self.check_answer_false)
        self.false_button.grid(column=2, row=3, pady=20)

        # start the quiz
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            # show the quiz question
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            # end of quiz
            self.canvas.itemconfig(self.question_text, text="The end of the quiz.")
            self.true_button.config(state="disable")
            self.false_button.config(state="disable")

    def check_answer_true(self):
        is_correct = self.quiz.check_answer("true")
        self.answer_feedback(is_correct)

    def check_answer_false(self):
        is_correct = self.quiz.check_answer("false")
        self.answer_feedback(is_correct)

    def answer_feedback(self, is_correct):
        if is_correct:
            self.canvas.config(bg="green")
            self.scoreboard.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)


