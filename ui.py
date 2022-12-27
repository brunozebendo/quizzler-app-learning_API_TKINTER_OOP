"""nessa parte do código, nessa pasta, foi criada a função para o user interface (ui), ou seja,
a parte que o usuário vai usar, para isso foi importada a biblioteca tkinter, que trabalha com imagens,
e o quiz brain onde foram criadas as funções. Primeiro é criada uma variável constante para a cor
de fundo, então é criada uma classe, atentar para o Pasqual Case, colocar cada inicial em maiúscula,
depois é usado o método init e o sel para partes que poderão ser usadas em outras parte do código, aqui está se usando
os conceitos de OOP. Acho que é o parâmetro como argumento.
 Na class QuizInterface o resto do código é a criação do layout."""

from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
"""Aqui foi passada uma solução que eu ainda não tinha visto, a classe quiz_brain, que é a clase onde estão
as funções de verificar se ainda há questões, de definir a próxima questão e de verificar se a questão
 está correta, foi passada como um argumento para a função iniciar, dentro da classe QuizInterface, para isso
 foi usada a sintaxe quiz_brain: QuizBrain que quer dizer que quiz brain é um parâmetro do tipo Quiz Brain, por
 isso, no começo do código foi importada a classe QuizBrain, depois o self.quiz recebe o quiz brain como
 método. Logo, mais abaixo no código ele é passado como self.quiz.still_has_questions():, ou seja, virou uma parâmetro.
  Esse procedimento visa facilitar a reutilização do argumento no código, e minimizar erros. Lembro aqui que a
  função do __init__ é começar um construtor, como se fosse um manual de instruções que determina as características
  da classe e o self é uma palavra reservada que depois quando chamada junto com os métodos, vai criando o objeto
 """

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,#aqui a largura foi determinada como 280, um pouco menor que a tela, para que o texto caiba
            text="Some Question Text",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()
"""a função abaixo traz uma nova questão até atingir o limite de dez, para isso, primeiro, a configuração do
background é colocada fora do if, assim, ela não dependerá das demais condições e manterá o fundo branco,
depois, é verificada se há mais questões através de uma função criada em outra parte do código que verifica
se o número da questão é maior do que a o comprimento da questão na lista. Se houver mais questões, ele
chama os métodos das questões, se não, ele desabilita os butões"""
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
           self.score_label.config(text=f"Score: {self.quiz.score}")#aqui o score é atualizado
           q_text = self.quiz.next_question()
           self.canvas.itemconfig(self.question_text, text=q_text)
        else:
           self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
           self.true_button.config(state="disabled")
           self.false_button.config(state="disabled")
"""as funções abaixo são para os botões de true e false quando forem pressionados. Reparar como aqui a OOP foi
aplicada, e são chamados métodos de funções criadas em outras pastas do código"""
    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)
"""aqui o código muda a cor do fundo chamando o método do config, e no final usa a função after com 1000 milisegundos,
para chamar a nova questão. Foi necessário criar a linha self.canvas.config(bg="white") no get_nest_question
para que não ficasse a cor do bg aqui selecionada"""
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)








