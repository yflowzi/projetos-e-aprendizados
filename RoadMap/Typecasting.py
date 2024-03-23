try:
    x= int(input("adicione um numero x: "))

    y = int(input(" adicione um numero y: "))
    if x==y:
        print("numeros iguais")

    else:
        print("numeros diferentes")
except ValueError:
    print("erro, por favor insira um numero inteiro.")