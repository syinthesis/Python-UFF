#validaçao de dados

s = str(input("Digite seu sexo(M/F): "))
while s != "m" and s != "M" and s != "f" and s != "F":
  s = str(input("Dados invalidos , tente novamente: "))
if s == "m" or s == "M":
  print("Voce é do sexo masculino")
elif s == "f" or s == "F":
  print("Voce é do sexo feminino")
