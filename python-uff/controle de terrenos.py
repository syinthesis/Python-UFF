def area(larg,comp):
  a = larg * comp
  print(f"A area de um terreno de {larg}x{comp} é {a}m²")

print("Controle de terreno")
print("="*13)
l = float(input("Largura(m): "))
c = float(input("Comprimento(m): "))
area(l,c)


