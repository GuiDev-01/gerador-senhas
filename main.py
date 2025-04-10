import random 
#Biblioteca que serve para aleatorizar dados (caracteres)
import string 
#Coleção de caracteres (números, letras maiúsculas e minúsculas e pontuações)

def gerar_senha(tamanho = 12 ):
#Utilizado para criar uma função personalizada

    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha
#Devolve o resultado da função para quem chamou ela.

entrada = input('Quantos caracteres você quer na senha? ')
if entrada.isdigit():
    tamanho = int(entrada)
    senha = gerar_senha(tamanho)
    print('Senha Gerada:',senha)
elif entrada =="":
    senha = gerar_senha()
    print('Senha padrão (12 caracteres): ',senha)
else:
    print('Por favor, digite apenas números!')