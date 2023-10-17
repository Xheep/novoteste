from tkinter import*
import tkinter as tk
from tkinter import messagebox

janela = Tk()
cor_cinza = '#707070'
branco = '#ffffff'
janela['bg'] = cor_cinza
janela.title('teste')
janela.geometry('500x300+550+150')
janela.resizable(height=False, width=False)

def mensagem():
    nome = str(caixa.get())
    resultado['text'] = f'O teu nome é {nome}'

lb = tk.Label(janela, text='Escreva o teu nome:', font=('Arial', 12, 'bold'), bg=cor_cinza, fg=branco)
lb.grid(row=0, column=0)
caixa = tk.Entry(janela, font=('Arial', 12, 'bold'))
caixa.grid(row=1, column=0)
botao = tk.Button(janela, font=('Arial', 12, 'bold'), text='Executar', height=2, width=10)
botao.place(row=2, column=0)
resultado = tk.Label(janela, font=('Arial', 12), bg=cor_cinza, fg=branco)
resultado.grid(row=3, column=0)


janela.mainloop()