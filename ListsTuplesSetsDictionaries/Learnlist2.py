entry = int(input("qual codigo? [1,2,3?]"))
if entry==1:
    list1 = [
        " "
        "apple",
        "banana",
        "cherry",
        "orange",
        "kiwi",
        "melon",
        "carrot",
        "beans",
        "rice",
    ]
    list2 = ["apple", "banana", "cherry"]
    list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

    

        
    print(list1)
        
    # remove
    # pop
    # del
    # clear
    list1.remove("banana")  # segundo
    list1.pop(0)  # primeiro
    list1.pop()  # ultimo
    list1.pop()  # penultimo

if entry==2:
        
        

        
    for i in range(len(list2)):
        print(list2[i])


        # para utilizar  a função len se deve primeiro criar uma variavel ou lista tupla  enfim


    # a unica forma de contar quantos itens ou str tem nessa lista (variavel tupla ou outro troço) é, criando outra variavel que nem a seguir:
    for i in list3:
        lentest = len(list3)
        print(i)

if entry==3:
    #o sort é o comando que ordena as listas bagunçadas exemplo:
    list4 = [7878687,567555,24456,975332,0,9,5,7]
    list4.sort()
    print(list4)
    #a função sort tambem Classifica lista alfanumericamente:
    list5 = ["orange", "mango", "kiwi", "pineapple", "banana", "watermellon", "apple"]
    list5.sort()
    print(list5)
    entry2 = input("gostaria de executar a lista em ordem descrescente? Sim[s] Não[n]")
    if entry2 =="s":
        list4.sort(reverse=True)
        list5.sort(reverse=True)
        print(list4,list5)
