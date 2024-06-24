import datetime
ano_atual = datetime.date.today().year

def Votacao(nascimento):
  idade = ano_atual - nascimento
  if idade >= 18:
    print(f"Com {idade} anos, VOTO OBRIGATORIO!")
  elif idade == 17 or idade == 16:
    print(f"Com {idade} anos , VOTO OPCIONAL")  
  elif idade < 16:
    print(f"Com {idade} anos, NAO PRECISA VOTAR")

ano = int(input("Em que ano vc nasceu? "))
Votacao(ano)
