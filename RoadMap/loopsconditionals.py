#python utiliza dois comandos de loop, for e while
# x = 4
# for numero in x:
#     print(numero)
#--------------------------------

entry= int(input("deseja rodar qual parte do codigo? [1,2,3,4?] "))
lista = ["banana","maçã"]
lista.append("abacate")
lista.append("kiwi")
x = 7
#tem como romper um loop de for:
if entry==1:
    for y in lista:
        print(y)
    if y=="abacate":
      pass

    else:
      print("essa é a lista de compras")
      #Nota: O bloco NÃO será executado se o loop for interrompido por uma instrução.elsebreak

      #vou criar o loop quando for 3 irei quebrar, no terminal nao ira ser execultado o bloco:else
if entry==2:
      for numero in range(x):
         print(numero)
         if numero==4:
            break
         else:
            (":D")
            #o bloco else não roda quando o laço de repetição quebra no meio.
         



#Com o loop while podemos executar um conjunto de instruções, desde que uma condição seja verdadeira.
if entry==3:
    i = 1
    while i < 6:
        print(i)
    i += 1

if entry==4:
    #Loops aninhados imprima adjetivos
    adj = ["big", "small", "widht"]
    itens = ["poppa", "city", "guy"]
    for x in adj:
        for y in itens:
            print(x,y)

        #um for precisa de conteudo, se caso nao tiver adicione um pass que não vai dar problema no cmd.
for x in [1,2,3,4,5]:
    pass