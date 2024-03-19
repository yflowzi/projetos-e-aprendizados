# # def object_car(carro):
# #   print(carro)


# # object_car("cor: vermelho")
# # object_car("placa: 509E3")
# # object_car("modelo: corsa classic")


# #criei uma função objeto carro com 3 argumentos
# def meu_carro (placa, cor, modelo):
#   print("modelo:",modelo,"cor:", cor,"placa", placa)

# #chamei essa função duas vezes
# meu_carro("509e35","red", "monza 1989")
# meu_carro("88888", "blue", "opala")

# #ao executar o codigo ira aparecer a placa a cor e o modelo do carro.


# #se o numero de argumentos forem desconhecidos add * no argumento exemplo:

# def my_function(*kids):
#   for kid in kids:
#     print(kid)

# my_function("jacob","maria","john","ana","arthur")

# # a ordem do argumento nao importa. basta usar a sintaxe key = valor exemplo a seguir 

# def my_function(brinquedo1, brinquedo3, brinquedo2):
#   print("O brinquedo favorito do Arthur é um(a):" + brinquedo3 )

# my_function(brinquedo1="urso de pelucia", brinquedo2="boneca de pano", brinquedo3="estilingue")

# se por acaso um parametro padrão for add, se caso se chama um argumento vazio o parametro padrão preenche.
def my_function(country = "Brasil"):
  print("país: "+country )

my_function()
my_function(country="Canada")


def my_function(cars):
  for car in cars:
    print(car)

car_names = ["sedan", "monza", "corsa"]

my_function(car_names)

def y(x):
    return x/10

print(y(100))
print(y(50))
