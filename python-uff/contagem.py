from time import sleep

def contador(inicio,fim,passos):
  for k in range(inicio,fim,passos):
    print(k,end = " ")






print("-="*20)
print("Contagem de 1 ate 10 de 1 em 1")
for i in range(1,11,1):
  print(i, end =" ")
print("FIM!!")
print("-="*20)
print("Contagem de 10 ate 0 de 2 em 2")
for j in range(10,-1,-2):
  print(j,end=" ")
print("FIM!!")
print("-="*20)
print("Agora é a sua vez de personalizar a contagem!")
inicial = int(input("Inicio: "))
final = int(input("Fim: "))
passadas = int(input("Passos: "))
contador(inicial,final,passadas)
