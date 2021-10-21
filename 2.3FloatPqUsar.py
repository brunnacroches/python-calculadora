# FLOAT PQ USAR?

largura:float = float(input('Qual a largura do comodo?'))
profundidade:float = float(input('Qual a profundidade do comodo?'))
altura:float = 2.9


print("A area das paredes é: ",
       (2 * (largura + profundidade) * altura))

# FLOAT PQ USAR?
# O input quando a gente salva ele salva como uma 'string' e no Ptyhon nao e permitido fazer um calculo com uma palavra
# Para resolver esse problema nos temos que infomar para o Python que o valor desse INPUT vai ter que virar um numero
# E para isso nos usaremos a funcao FLOAT


# FLOAT : converte um valor de uma variavel em um numero do tpo real, ou seja, um numero real que tem casas decimais
# E usaremos um recurso do Python chamado 'TypeHint' para dizer que essa VARIAVEL do TIPO LARGURA e do tipo FLOAT


# ASSIM, toda a funcionalidade que vai guaurdar essa variavel largura, esta guardando uma variavel do tipo Float
# Faremos isso com a profundidad e com a altura.