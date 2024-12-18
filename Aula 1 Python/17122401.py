#Variaveis
nome = "Everton"
idade = 21
altura = 1.64

#concatenar
print(f"Olá {nome}, tudo bem?\nvocê tem {idade} anos!\ne tambem {altura}mt de altura!")

#IF ELSE
if altura >= 1.70:
    print("Você é um Gostoso!")
else:
    print("Você ainda é um Gostoso!")

#FOR
palavra = "Everton"
for letras in palavra:
    print(letras)

#WHILE
num = 0
while  num < 10:
    print(num)
    num += 1
if num == 10:
    print("Você chegou ao final!")
else:
    print("Você ainda não chegou ao final!")

#Leitura de arquivo
with open('arquivo.txt', 'r') as arquivo:
    conteudo = arquivo.read()
print(conteudo)  
      
#Função
def soma(a, b):
    return a + b
print(soma(5, 5))
