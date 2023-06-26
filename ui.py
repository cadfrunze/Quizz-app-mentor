from tkinter import *
from quiz_brain import QuizBrain
from tkinter import messagebox
import sys

THEME_COLOR = "#375362"


class InterfataQuizz:
    def __init__(self, quizzer: QuizBrain):
        self.scorul_interfata: int = 0
        self.len_lista: int = 0
        self.cancel_after = None
        self.quiz = quizzer
        self.ecran = Tk()
        image_true = PhotoImage(file='./images/true.png')
        image_false = PhotoImage(file='./images/false.png')
        self.ecran.title('Quizz game!')
        self.ecran.resizable(False, False)
        self.ecran.config(pady=20, padx=20, bg=THEME_COLOR)
        self.scorul = Label(text=f'Scorul: {self.quiz.score}', fg='white', bg=THEME_COLOR)
        self.scorul.grid(column=1, row=0)
        self.canvas = Canvas(width=300, height=250, bg='white')
        self.textul = self.canvas.create_text(150, 125, width=280, text='', font=('Arial', 20, 'italic'))
        self.canvas.grid(column=0, row=1, pady=50, columnspan=2)
        self.button_true = Button(image=image_true, highlightthickness=0)
        self.button_true.grid(column=0, row=2, pady=20, padx=20)
        self.button_false = Button(image=image_false, highlightthickness=0)
        self.button_false.grid(column=1, row=2, pady=20, padx=20)
        self.generate_question()
        self.ecran.mainloop()

    def generate_question(self):
        self.check_len()
        self.button_true.config(command=self.true_button)
        self.button_false.config(command=self.false_button)
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.textul, text=q_text)

    def change_background(self, check: bool, count: int):
        self.button_true.config(command=self.button_pass)
        self.button_false.config(command=self.button_pass)
        self.ecran.config(bg=THEME_COLOR)
        if check is True:
            self.ecran.config(bg='blue')
        elif check is False:
            self.ecran.config(bg='red')
        if count == 0:
            self.ecran.after_cancel(self.cancel_after)
            self.ecran.config(bg=THEME_COLOR)
            self.button_true.config(command=self.true_button)
            self.button_false.config(command=self.false_button)

        else:
            self.cancel_after = self.ecran.after(500, self.change_background, check, count - 1)

    def true_button(self):
        self.quiz.check_answer(user_answer='true')
        self.scorul.config(text=f'Scorul: {self.quiz.score}')
        if self.quiz.score > self.scorul_interfata:
            self.ecran.after(200, self.change_background, True, 1)
        else:
            self.ecran.after(200, self.change_background, False, 1)
        self.scorul_interfata = self.quiz.score
        self.len_lista += 1
        self.generate_question()

    def false_button(self):
        self.quiz.check_answer(user_answer='false')
        self.scorul.config(text=f'Scorul: {self.quiz.score}')
        if self.quiz.score > self.scorul_interfata:
            self.ecran.after(200, self.change_background, True, 1)
        else:
            self.ecran.after(200, self.change_background, False, 1)
        self.scorul_interfata = self.quiz.score
        self.len_lista += 1
        self.generate_question()

    def button_pass(self):
        pass

    def check_len(self):
        try:
            self.quiz.question_list[self.len_lista]
        except IndexError:
            messagebox.showinfo(title='Done!', message='Jocul s-a incheciat')
            sys.exit()
