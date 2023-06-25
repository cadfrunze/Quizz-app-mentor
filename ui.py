from tkinter import *

THEME_COLOR = "#375362"


class InterfataQuizz:
    def __init__(self):
        self.scor: int = 0
        self.ecran = Tk()
        image_true = PhotoImage(file='./images/true.png')
        image_false = PhotoImage(file='./images/false.png')
        self.ecran.title('Quizz game!')
        self.ecran.resizable(False, False)
        self.ecran.config(pady=20, padx=20, bg=THEME_COLOR)
        self.scorul = Label(text=f'Scorul: {self.scor}', fg='white', bg=THEME_COLOR)
        self.scorul.grid(column=1, row=0)
        self.canvas = Canvas(width=300, height=250, bg='white')
        self.canvas.create_text(150, 125, text='', font=('Arial', 20, 'italic'))
        self.canvas.grid(column=0, row=1, pady=50, columnspan=2)
        self.button_true = Button(image=image_true, highlightthickness=0)
        self.button_true.grid(column=0, row=2, pady=20, padx=20)
        self.button_false = Button(image=image_false, highlightthickness=0)
        self.button_false.grid(column=1, row=2, pady=20, padx=20)
        self.ecran.mainloop()
