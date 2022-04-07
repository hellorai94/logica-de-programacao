idade = int(input("Qual a sua idade, em dias?"))
anos = idade//365
meses = idade%365//30
dias = idade%365%30

print("Você tem", anos, "anos,", meses, "mes(es) e", dias, "dia(s) de idade")
