print("Array de inteiros vazio:", numeros)
print("Array de objetos vazio:", objetos)
print("-" * 60)

import random

# =============================================
# 1. Criar um array vazio de inteiros e de objetos
# =============================================

# Array de inteiros
numeros = []

# Classe de exemplo (para array de objetos)
class Foo:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

    def __repr__(self):
        return f"Foo(nome={self.nome}, valor={self.valor})"

# Array de objetos
objetos = []

print("Array de inteiros vazio:", numeros)
print("Array de objetos vazio:", objetos)
print("-" * 60)

numeros = [1, 2, 3, 4, 5]
objetos = [Foo("A", 10), Foo("B", 20), Foo("C", 30)]

print("Array de inteiros preenchido:", numeros)
print("Array de objetos preenchido:", objetos)
print("-" * 60)

print("Tamanho do array de inteiros:", len(numeros))
print("Tamanho do array de objetos:", len(objetos))
print("-" * 60)

numeros.append(6)
print("Após adicionar 6 ao final:", numeros)

ultimo = numeros.pop()
print(f"Removido o último elemento ({ultimo}):", numeros)
print("-" * 60)

numeros.insert(0, 100)
print("Após adicionar 100 no início:", numeros)