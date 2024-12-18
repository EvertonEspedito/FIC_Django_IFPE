#POO em PY
class Pessoa:  
    def __init__ (self, nome, idade, altura):  
        self.nome = nome  
        self.idade = idade
        self.altura = altura

    def saudacao(self):  
        return f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos."  

    def envelhecer(self, anos):  
        self.idade += anos  

    def minhaAltura(self):
        return f"Tenho {self.altura} de altura"    

# Criando objetos da classe Pessoa  
pessoa1 = Pessoa("Alice", 30, 1.55)  
pessoa2 = Pessoa("Bob", 25, 1.90)  

# Chamando métodos nos objetos  
print(pessoa1.saudacao()) # Saída: Olá, meu nome é Alice e eu tenho 30 anos.  
print(pessoa1.minhaAltura()) # Saída: Tenho 1.55

print(pessoa2.saudacao()) # Saída: Olá, meu nome é Bob e eu tenho 25 anos.  

pessoa1.envelhecer(5) 
print(pessoa1.saudacao()) # Saída: Olá, meu nome é Alice e eu tenho 35 anos.
if pessoa1.idade >= 30:
    pessoa1.altura += 0.01
    print(f'Agora {pessoa1.minhaAltura()}') 