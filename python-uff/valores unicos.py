lista = []
cont = 0
op = "s"
while op == "s":
  while len(lista) <= 4:
    lista.insert(cont,int(input("Digite um numero: ")))
    print("Valor adicionado com sucesso! ")
    cont = cont + 1
    op = str(input("Deseja continuar ? (s/n): "))
print(lista)
