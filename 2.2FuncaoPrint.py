
#FUNCAO PRINT


largura:float = float(input('Qual a largura do comodo?'))
profundidade:float = float(input('Qual a profundidade do comodo?'))
altura:float = 2.9


print("A area das paredes é: ",
       (2 * (largura + profundidade) * altura))


#FUNCAO PRINT
#A funcao PRINT ela aceita mais de uma coisa que vai imprimir na tela, ou seja, mais de um argumento

# Essa expressao e um argumento matematico >

# ANTES
#print(2 * (largura + profundidade) * altura)

# vamos recortar e colocar entre parentese:

#OBS: ENTAO antes da equacao nos vamos colocar uma VIRGULA
#VIRGULA: para indicar que queremos separar essa expressao matematica de outra coisa

# DEPOIS
#print("A area das paredes é: ",
     #  (2 * (largura + profundidade) * altura))