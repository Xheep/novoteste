from tkinter import*
import tkinter as tk
from tkinter import messagebox

janela = Tk()
cinza = '#707070'
branco = '#ffffff'
janela['bg'] = cinza
janela.title('Minha primeira tela')
janela.geometry('500x400+550+150')

def erro():
    tk.messagebox.showerror(title='Error', message='Falha no cadastro.')

entrada1 = tk.Label(janela, text='Digite seu nome', font=('Arial', 14, 'bold'), bg=cinza, fg=branco)
entrada1.pack(pady=20)
caixa1 = tk.Entry(janela, font=('Arial', 12))
caixa1.pack(ipadx=100, ipady=5)
entrada2 = tk.Label(janela, text='Digite sua idade', font=('Arial', 14, 'bold'), bg=cinza, fg=branco)
entrada2.pack(pady=20)
caixa2 = tk.Entry(janela, font=('Arial', 12))
caixa2.pack(ipadx=100, ipady=5)
botao1 = tk.Button(janela,text='Salva', font=('Arial', 14, 'bold'), height=1, width=10, command=erro)
botao1.pack(pady=10)

janela.mainloop()
