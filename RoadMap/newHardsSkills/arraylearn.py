'''
O que é um Array?

Um array é uma variável especial, que pode conter mais de um valor de cada vez.

Se você tiver uma lista de itens (uma lista de nomes de carros, por exemplo), armazenando o Carros em variáveis individuais podem ser assim:
'''


#array ou em português: matrizes

cars = ["fiat","wolksvagen","ferrari"]
cars.append("honda")
print(cars)

x =cars[1]
print(x)

change_array = input("DO YOU WANT RUN THE NEXT CODE? YES[y] NO[n] send in lowercase: ")

if change_array =="y":
    cars[1] = "Land rover"
print(cars)

# utilizando o len da para descobrir quando itens exitem em uma array.
print(len(cars))

'''
Method 	Description
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the first item with the specified value
reverse()	Reverses the order of the list
'''