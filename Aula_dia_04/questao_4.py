from tkinter import*
import tkinter as tk
from tkinter import messagebox

janela = Tk()
cor_cinza = '#707070'
branco = '#ffffff'
janela['bg'] = cor_cinza
janela.title('janela1')
janela.geometry('500x400+550+150')

def janela2():
    root = Tk()
    root['bg']= cor_cinza
    root.title('janela2')
    root.geometry('500x400+550+150')
    root.mainloop()


botao1 = tk.Button(janela, font=('Arial', 12, 'bold'), text='Abrir janela dois.', command=janela2)
botao1.pack(padx=160, pady=160)


janela.mainloop()