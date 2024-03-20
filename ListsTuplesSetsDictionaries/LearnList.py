
# Há quatro tipos de dados de coleção na linguagem de programação Python:

# Lista é uma coleção que é ordenada e mutável. Permite membros duplicados.
# Tupla é uma coleção ordenada e imutável. Permite membros duplicados.
# Set é uma coleção que não está ordenada, imutável* e não indexado. Sem membros duplicados.
# Dicionário é uma coleção que é ordenada** e mutável. Sem membros duplicados.

# As listas são um dos 4 tipos de dados internos em Python usados para armazenar coleções de Os outros 3 são Tuple, Set e Dicionário, todos com qualidades e usos diferentes.

# Os itens de lista são ordenados, alteráveis e permitem valores duplicados.

# Os itens de lista são indexados, o primeiro item tem índice , o segundo item tem índice etc.[0][1]

# uma lista pode conter bool int str diferentes tipos de dados:
list1 = ["abc", 34, True, 40, "male"]

# listas ordenadas o item que estiver não irá mudar imutável, exemplo, o abacate [2] não muda de posição.
listas = ("banana", "maçã", "abacate", "kiwi")
for item in listas:
    print("Lista de frutas para comprar na feira:", item)
print("O total de frutas é:", len(listas))
print("------------------------------------------------------")

# na perspectiva do python uma lista são definidas com o tipo de dado "list"
print("Exemplo, qual é o tipo de dados de uma lista?")
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

print("------------------------------------------------------")

print("para acessar um item da lista específico:")

minha_playlist = ["metallica", "black sabbath", "marylin mason", "motorhead"]
print(minha_playlist[2])

print("------------------------------------------------------")


thislist = ["apple", "banana", "cherry"]
print(thislist)
print("indentação negativa significa começar do fim, exemplo:")
print(thislist[-1])

print("------------------------------------------------------")

print("é possivel manipular qual tipo de item que irá ser o primeiro:")

print("exercicio, Retorne o terceiro, quarto e o quinto item:")
essalista = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

print(essalista[2:5])

print(essalista[:4])
print("O exemplo acima só irá contar os itens da lista até o quarto item.")


print(f"Este exemplo abaixo retorna os itens de ""cherry"" para o final:")

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])
print("------------------------------------------------------")
# print("Alterando o valor dos itens, exemplo abaixo:")
listdfruits = ["apple", "banana", "cherry"]
listdfruits[1] = "blackmelon"

print(listdfruits)
# utilizando o insert() é possivel adicionar um item na lista sem necessariamente substituilo por outro
list2 = ["apple", "banana", "cherry", "orange", "kiwi", "melon"]
list2.insert(0, "rapadura")

print(list2)
