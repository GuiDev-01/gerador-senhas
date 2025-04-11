
import random 
#Biblioteca que serve para aleatorizar elementos

import string 
#Coleção de caracteres (números, letras maiúsculas e minúsculas e símbolos)

def gerar_senha(tamanho = 12, usar_maiusculas=True, usar_minusculas=True, usar_numeros=True, usar_simbolos=True):
#Utilizado para criar uma função personalizada, utilizando os parâmetros que eu defini. 
    caracteres = ''
    if usar_maiusculas:
        caracteres+= string.ascii_uppercase
    if usar_minusculas:
        caracteres+= string.ascii_lowercase
    if usar_numeros:
        caracteres += string.digits
    if usar_simbolos:
        caracteres += string.punctuation
    if not caracteres:
        return 'Erro: Nenhum tipo de caractere foi selecionado.'
    
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha
#Devolve o resultado da função.

entrada = input('Quantos caracteres você quer na senha? Enter para usar o valor padrão de 12 caracteres. ')
if entrada.isdigit():
    tamanho = int(entrada)
    senha = gerar_senha(tamanho)
    print('Senha Gerada:',senha)
elif entrada =="":
    tamanho = 12 
    senha = gerar_senha()
    print('Senha padrão (12 caracteres): ',senha)
else:
    print('Por favor, digite apenas números! Ou deixe em branco.')
    exit()
def deseja_incluir(msg):
    resp = input(msg + 's/n: ').lower()
    return resp == 's'
usar_maiusculas = deseja_incluir("Incluir letras MAIÚSCULAS?")
usar_minusculas = deseja_incluir("Incluir letras minúsculas?")
usar_numeros = deseja_incluir("Incluir NÚMEROS?")
usar_simbolos = deseja_incluir("Incluir Símbolos (ex: #@$%)?")

senha = gerar_senha(tamanho,usar_maiusculas,usar_minusculas,usar_numeros,usar_simbolos)
if senha.startswith('Erro'):
    print(senha)
else:
    print("Senha gerada: ",senha)