comando = input("biscoito ou bolacha? ")

match comando:
    case "biscoito":
      print("definitivamente você é carioca.")
    case "bolacha":
      print("paulista identificado!")
    
    case ValueError:
      print("por favor, resposta simples, biscoito ou bolacha.")
