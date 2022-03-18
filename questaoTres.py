mercadoria = int(input("Qual o valor da mercadoria?"))
percentual = int(input("Qual valor do desconto, em percentual?"))
desconto = (mercadoria*percentual)/100
valorFinal = (mercadoria-desconto)
print("O valor do desconto é de", desconto, "reais")
print("O valor da mercadoria com o desconto é", valorFinal, "reais")