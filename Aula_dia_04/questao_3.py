from tkinter import*
import tkinter as tk
from tkinter import messagebox

janela = Tk()
cor_cinza = '#707070'
branco = '#ffffff'
janela['bg'] = cor_cinza
janela.title('teste')
janela.geometry('500x400+550+150')

imagem = PhotoImage(file='bd.png')
mostrar = Label(janela, image=imagem)
mostrar.pack(padx=10, pady=10)

janela.mainloop()