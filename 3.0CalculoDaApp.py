
#CALCULADORA DE PINTURA#

#Bem, agora pegando todos os dados do usario
# vamos fazer todos os calculos que faltam definir
# a litragem de tinta necessaria para fazer a nossa calculadora de pintura

#CALCULADORA DE PINTURA#

#1- REMOVER A EXPRESSAO DO PRINT E COLOCA-LA DENTRO DE UMA VARIAVEL
# VARIAVEL CHAMADA DE AREA PAREDE:

#ANTES
#print("A area das paredes é: ",
      #(2 * (largura + profundidade) * altura))

#DEPOIS

#area_paredes: float = 2 * (largura + profundidade) * altura

#print("A area das paredes é ")



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

# (area_paredes + area_teto) / 10 > 10 E O RENDIMENTO DA TINTA
#DIVIDO pelo RENDIMENTO estimado da tinta.
#Nesse caso vamos calcular que o rendimento da tinta e de 1 litro para cada 10m2


#ESTILO SKANE_CASE
#NOTE QUE, no PYTHON a convencao e voce nomear a variavel pelo
#estilo SKAKE_CASE
#que e separar as palavras por um UNDERSCORE

#BOAS PRATICAS DE PROGRAMACAO
# uma linha nao deveria passar de 80 caracteres
# mantem seu codigo mais legivel e mais bonito