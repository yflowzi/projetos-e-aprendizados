# def object_car(carro):
#   print(carro)


# object_car("cor: vermelho")
# object_car("placa: 509E3")
# object_car("modelo: corsa classic")


#criei uma função objeto carro com 3 argumentos
def meu_carro (placa, cor, modelo):
  print("modelo:",modelo,"cor:", cor,"placa", placa)

#chamei essa função duas vezes
meu_carro("509e35","red", "monza 1989")
meu_carro("88888", "blue", "opala")

#ao executar o codigo ira aparecer a placa a cor e o modelo do carro.


#se o numero de argumentos forem desconhecidos add * no argumento exemplo:

def my_function(*kids):
  for kid in kids:
    print(kid)

my_function("jacob","maria","john","ana","arthur")





