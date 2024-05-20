def mydic1():
    global dicionario
    dicionario = {
        "marca": "Chevrolet",
        "modelo": "Monza",
        "ano": 1989,
    }

mydic1()
    # dicionario armazena informações em duplas chave : valor e não aceita valores duplicados uma coleção ordenada e mutavel
def mydic2():
    global dicionario2
    dicionario2 = {"marca": "motorola",
                "modelo": "g42", 
                "ano": "2022 6 28"}

    print("Exercicio imprimir a marca, modelo e ano de lançamento.")
    print(dicionario2["ano"])
    print( dicionario2["marca"])
    print( dicionario2 ["modelo"])

mydic2()

def mydic3():
    #descubra quantos itens tem no dicionario com a função len
    print(len(dicionario))

    print(len(dicionario2))

    #nome da chave 
    y = dicionario2.keys()

    print(y)

   

mydic3()
#Get the value of the "model" key:
x = dicionario.get("marca")
#Add a new item to the original dictionary, and see that the keys list gets updated as well:
dicionario["color"]="red"
print(dicionario)
print(x)

