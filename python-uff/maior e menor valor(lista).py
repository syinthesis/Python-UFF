lista = []
cont = 0
pos = 0
while cont <= 4:
  lista.insert(cont,int(input(f"Digite um valor para posicao {pos}: ")))
  pos = pos + 1
  cont=cont + 1
print('-=' * 60)
print(f'Voce digitou os valores {lista}')
maior = max(lista)
menor = min(lista)
print(f"O maior valor digitado foi {maior} nas posicoes ", end='')
for i,v in enumerate(lista):
  if v == maior:
    print(f"{i}...", end='')
print()
print(f"O menor valor digitado foi {menor} nas posicoes ", end='')
for i,v in enumerate(lista):
  if v == menor:
    print(f"{i}...", end='')
print()