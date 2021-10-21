# E COMO COLOCAR DADOS DO USUARIO EM :
# LINHAS DE COMANDO?

# RESPOSTA : A GENTE USA O COMANDO input()


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


# FLOAT PQ USAR?
# O input quando a gente salva ele salva como uma 'string' e no Ptyhon nao e permitido fazer um calculo com uma palavra
# Para resolver esse problema nos temos que infomar para o Python que o valor desse INPUT vai ter que virar um numero
# E para isso nos usaremos a funcao FLOAT


# FLOAT : converte um valor de uma variavel em um numero do tpo real, ou seja, um numero real que tem casas decimais
# E usaremos um recurso do Python chamado 'TypeHint' para dizer que essa VARIAVEL do TIPO LARGURA e do tipo FLOAT


# ASSIM, toda a funcionalidade que vai guaurdar essa variavel largura, esta guardando uma variavel do tipo Float
# Faremos isso com a profundidad e com a altura.

# O QUE E TYPEHINT?
# e o nome da variavel + : float = 'lagura: float =
# nas entrelinhas eu estou dando uma dica de qual e o tipo daquela variavel ali, dizendo que largura deve esperar o float
# TYPEHINT ele e pra facilitar a lebilidade do codigo


#OBS: apareceu "Not allowed to run in parallel. Would you like to stop the running one?
# PARA CORRIGIR O ERRO VA EM 'run'> 'Edit Confugurations' >toque em > ' allow parallel run ' <
