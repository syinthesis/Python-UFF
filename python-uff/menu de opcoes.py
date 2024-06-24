a = int(input("primeiro numero: "))
b = int(input("segundo numero: "))
print("[ 1 ] somar")
print("[ 2 ] multiplicar")
print("[ 3 ] maior")
print("[ 4 ] novos numeros") 
print("[ 5 ] sair do programa")
o = int(input("Qual a sua opçao: "))
if o == 1:
  print(f"A soma é igual a {a+b}")
elif o == 2:
  print(f"o produto é igual a {a*b}")
elif o == 3:
  if a > b:
    print(f"{a} é maior ")
  elif b > a:
    print(f"{b} é maior ")
  elif a == b:
    print("sao iguais !!")
elif o == 4:
  a = int(input("primeiro numero: "))
  b = int(input("segundo numero: "))
elif o == 5:
  print("programa finalizado...")