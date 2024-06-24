g = str(input("Informe seu genero(M/F): "))
while g != "M" and g != "m" and g != "F" and g != "f":
  g = str(input("Dados invalidos. Por Favor, informe seu genero(M/F): "))
if g == "M" or g == "m":
  print("vc é do genero masculino")
elif g =="F" or g == "f":
  print("vc é do genero feminino")