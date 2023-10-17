from tkinter import*
import tkinter as tk
from tkinter import messagebox

janela = Tk()
cor_cinza = '#707070'
branco = '#ffffff'
janela['bg'] = cor_cinza
janela.title('teste')
janela.geometry('500x400+550+150')

def informativo():
    tk.messagebox.showinfo(title='info', message='informação')

def erro():
    tk.messagebox.showerror(title='Error', message='algum erro encontrado')

def aviso():
    tk.messagebox.showwarning(title='Aviso', message='OPA!!!')

def pergunta():
    tk.messagebox.askquestion(title='Pergunta', message='Ser ou não ser?')

def sim_nao():
    tk.messagebox.askyesnocancel(title='Sim ou não', message='Sim ou não?')

botao1 = tk.Button(janela,text='informativo', font=('Arial', 12, 'bold'), height=2, width=100, command=informativo)
botao1.pack(padx=10)
botao2 = tk.Button(janela,text='Erro', font=('Arial', 12, 'bold'), height=2, width=100, command=erro)
botao2.pack(padx=10)
botao3 = tk.Button(janela,text='Aviso', font=('Arial', 12, 'bold'), height=2, width=100, command=aviso)
botao3.pack(padx=10)
botao4 = tk.Button(janela,text='Pergunta', font=('Arial', 12, 'bold'), height=2, width=100, command=pergunta)
botao4.pack(padx=10)
botao4 = tk.Button(janela,text='Sim e não', font=('Arial', 12, 'bold'), height=2, width=100, command=sim_nao)
botao4.pack(padx=10)

janela.mainloop()