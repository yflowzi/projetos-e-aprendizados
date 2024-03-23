
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


    
    

    
for i in range(len(list2)):
    print(list2[i])


    # para utilizar  a função len se deve primeiro criar uma variavel ou lista tupla  enfim


# a unica forma de contar quantos itens ou str tem nessa lista (variavel tupla ou outro troço) é, criando outra variavel que nem a seguir:
for i in list3:
    lentest = len(list3)
    print(i)

 
