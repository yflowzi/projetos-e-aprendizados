#Porque raios eu uso lambda?
'''
O poder do lambda é melhor mostrado quando você os usa como um anônimo. função dentro de outra função.

Digamos que você tem uma definição de função que leva um argumento, e esse argumento será multiplicado com um número desconhecido:
'''


def minha_funcao(n):
  return lambda a : a * n

dobro = minha_funcao(5)

print(dobro(4))


def dobro():
  numero = int(input("Digite um numero que eu dobro haha: "))
  x =  lambda x : x*2

  print(f"o dobro de {numero} é: {x(numero)}")

meu_objeto= dobro()

