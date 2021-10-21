#BOAS PRATICAS DE PROGRAMACAO
# uma linha nao deveria passar de 80 caracteres
# mantem seu codigo mais legivel e mais bonito


largura:float = float(input('Qual a largura do cômodo?'))
profundidade:float = float(input('Qual a profundidade do comodo?'))
altura:float = 2.9

area_paredes: float = 2 * (largura + profundidade) * altura

print("A area das paredes é: ", area_paredes )

area_teto: float = largura * profundidade

print(
    'A area do teto e:',
    area_teto
)

print(
    'A litragem de tinta necessaria é',
    (area_paredes + area_teto) / 10
)