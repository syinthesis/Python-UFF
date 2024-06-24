lanche = ['Hamburguer','Suco','Pizza','Pudim','Agua','Batata-Frita']
print(lanche)
lanche.append('Sushi') # >> Adiciona um valor na lista
print(lanche)
lanche[4] = 'Refrigerante'
print(lanche)
lanche.insert(0,'Picole') # >> Adiciona um valor na posiçao desejada da lista
print(lanche)
del lanche[0]  # >> Para deletar uma variavel , lanche.pop(), lanche.remove()
            
print(lanche)
print(sorted(lanche))

valores = list(range(4,11))
print(valores)

