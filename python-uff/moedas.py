import modulomoedas

n = int(input("Digite o preco: R$ "))

print(f"O dobro de {n} é {modulomoedas.dobro(n)}")
print(f"A metade de {n} é {modulomoedas.metade(n)}")
print(f"Aumentando 50%, temos {modulomoedas.aumentar(n)}")
print(f"Diminuindo 50%, temos {modulomoedas.diminuir(n)}")
