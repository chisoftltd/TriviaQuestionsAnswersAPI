from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class UserInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Trivia Questions and Answers")
        self.window.config(padx=50, pady=50, bg=THEME_COLOR)

        self.score_label = Label(
            text="Score: 0",
            font=("Arial", 12, "bold"),
            fg="white",
            bg=THEME_COLOR
        )
        self.score_label.config(padx=20, pady=20)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(
            width=500,
            height=614,
            bg="white"
        )
        self.question_text = self.canvas.create_text(
            250,
            307,
            text="Question goes HERE",
            width=400,
            font=("Arial", 20, "italic"),
            fill=THEME_COLOR
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=30)

        self.true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=self.true_img, highlightthickness=0, command=self.true_reply)
        self.true_button.grid(row=2, column=1)
        self.false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.false_img, highlightthickness=0, command=self.wrong_reply)
        self.false_button.grid(row=2, column=0)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.config(bg="orange")
            self.canvas.itemconfig(self.question_text, text="You have reach the end of quiz, Thank you!")
            self.true_button.config(state="disable")
            self.false_button.config(state="disable")

    def true_reply(self):
        self.check_answer(self.quiz.check_answer("True"))

    def wrong_reply(self):
        self.check_answer(self.quiz.check_answer("False"))

    def check_answer(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)



