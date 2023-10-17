from tkinter import*
import tkinter as tk
from tkinter import messagebox

janela = Tk()
cor_cinza = '#707070'
branco = '#ffffff'
janela['bg'] = cor_cinza
janela.title('teste')
janela.geometry('500x400+550+150')

def mensagemTexto():
    mensagem['text'] = 'Parabéns!!'

botao1 = tk.Button(janela, text='Clique aqui!', font=('Arial', 12), height=2, width=10, command=mensagemTexto)
botao1.pack(padx=150, pady=10)

mensagem = Label(janela, font=('Arial', 12, 'bold'), bg = cor_cinza, fg = branco)
mensagem.pack(padx=150, pady=10)



janela.mainloop()