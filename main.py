import tkinter as tk 
from tkinter import ttk
#Tkinter: biblioteca padrão pra criar janelas gráficas no Python.
#Ttk: uma versão visual moderna dos widgets do tkinter (botões, labels, etc.)
import random
import string 

#Cria a Janela
janela = tk.Tk()

janela.title("Gerador de senhas")
janela.geometry("400x300")
janela.resizable(True,True)
#Configurações visuais

#Campo de exibição do resultado
resultado = tk.StringVar()

#Título da sessão
ttk.Label(janela, text="Tamanho da senha: ").pack(pady=5)

#Campo de escolha de tamanho
spin_tamanho = ttk.Spinbox(janela,from_=4, to=64,width=5)
spin_tamanho.set(12) #Valor padrão
spin_tamanho.pack()

#Variáveis de controle (armazenam se o checkbox foi marcado ou não)
var_maiusculas = tk.BooleanVar(value=True)
var_minusculas = tk.BooleanVar(value=True)
var_numeros = tk.BooleanVar(value=True)
var_simbolos = tk.BooleanVar(value=False)

#Checkboxes
ttk.Checkbutton(janela,text="Letras MAIÚSCULAS", variable=var_maiusculas).pack(anchor="w", padx=20)
ttk.Checkbutton(janela,text="Letras minúsculas", variable=var_minusculas).pack(anchor="w", padx=20)
ttk.Checkbutton(janela,text="NÚMEROS", variable=var_numeros).pack(anchor="w", padx=20)
ttk.Checkbutton(janela,text="SÍMBOLOS (ex: @#$%)", variable=var_simbolos).pack(anchor="w", padx=20)


#Função que gera a senha
def gerar_senha():
    try:
        tamanho = int(spin_tamanho.get())
    except ValueError:
        resultado.set("Tamanho Inválido")
        return
    usar_maiusculas = var_maiusculas.get()
    usar_minusculas = var_minusculas.get()
    usar_numeros = var_numeros.get()
    usar_simbolos = var_simbolos.get()
    caracteres = ''
    if usar_maiusculas:
        caracteres+= string.ascii_uppercase
    if usar_minusculas:
        caracteres+= string.ascii_lowercase
    if usar_numeros:
        caracteres+= string.digits
    if usar_simbolos:
        caracteres+= string.punctuation
    if not caracteres:
        resultado.set("Erro: selecione pelo menos um tipo")
        return
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    resultado.set(senha)
def copiar_senha():
    janela.clipboard_clear()
    janela.clipboard_append(resultado.get())
#Botão de gerar senha    
ttk.Button(janela, text="Gerar Senha", command=gerar_senha).pack(pady=10)

#Campo de exibição da senha gerada
ttk.Entry(janela, textvariable=resultado, width=30).pack()

#Botão de copiar senha
ttk.Button(janela, text="Copiar", command=copiar_senha).pack(pady=5)

#Inicia o loop da interface
janela.mainloop()