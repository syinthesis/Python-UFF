lanche = ('Hamburguer','Suco','Pizza','Pudim','Agua','Batata-Frita')
for comida in lanche: 
  print(f"eu vou comer {comida} ")

for cont in range(0,len(lanche)):
  print(f"eu vou comer {lanche[cont]} na posicao {cont}")

print(sorted(lanche))

a = (2,6,4,3)
b = (5,8,1,7,1)
c = a + b
print(a+b)
print(b+a)
print(sorted(a+b))
print(c.count(1))




 