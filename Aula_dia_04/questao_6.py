from tkinter import*
import tkinter as tk
from tkinter import messagebox

janela = Tk()
cinza = '#707070'
branco = '#ffffff'
janela['bg'] = cinza
janela.title('Minha primeira tela')
janela.geometry('900x300+550+150')

botao1 = tk.Button(janela,text='Pack(Fill X)', font=('Arial', 12,), height=2, width=10)
botao1.pack(fill='x')
botao1 = tk.Button(janela,text='Pack(Fill X - BOTTOM)', font=('Arial', 12), height=2, width=10)
botao1.pack(fill='x', side = 'bottom')
botao1 = tk.Button(janela,text='Pack(Fill y - LEFT)', font=('Arial', 12), height=1, width=20)
botao1.pack(fill='y', side = 'left')
botao1 = tk.Button(janela,text='Pack(Fill y - RIGHT)', font=('Arial', 12), height=1, width=20)
botao1.pack(fill='y', side = 'right')

janela.mainloop()