from random import randint
tentativas = 0 
print("Sou seu computador...")
print("Acabei de pensar em um numero entre 0 e 10.")
print("Sera que vc consegue adivinhar ?")
p = int(input("Qual é o seu palpite: "))

computador = randint(0,10)
while p < computador:
  print("Mais...Tenta mais uma vez")
  p = int(input("Qual é o seu palpite: "))
  tentativas += 1

while p > computador: 
  print("Menos...Tente mais uma vez")
  p = int(input("Qual é o seu palpite: "))
  tentativas += 1
if p == computador:
  tentativas += 1 
  print(f"Acertou com {tentativas} tentativas. Parabens!")
