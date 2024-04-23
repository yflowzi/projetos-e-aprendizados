
entry = int(input("qual codigo? [1,2?] "))
objetos = ["macaco","margarida","maçaneta","mar","bancada","berinjela"]
newlist = []

if entry==1:
    
    for x in objetos:
        if "m" in x:
            newlist.append(x)
    print(newlist)
    #é assim que puxa um objeto especifico sem a Compreensão de Listas, com laço de repetição.
    #a compreensão de lista demanda de linha de codigo menor para fazer a mesma coisa exemplo:
if entry==2:

    fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

    newlist = [x for x in fruits if "b" in x]
    print(newlist)

