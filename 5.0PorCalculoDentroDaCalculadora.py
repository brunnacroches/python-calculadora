# 1.0 COLOCAR OS CALCULOS DENTRO DA CALCULADORA

# 2.0  ESCREVER O NOSSO PRIMEIRO METODO PYTHON


#class Calculadora:
   # area_paredes: float
   # area_teto: float

# def calcular_area_paredes(self, largura, profundidade, altura):
  #  self.area_paredes = 2 * ( largura + profundidade) * altura



#colocar o calculo da  area_paredes" dentro classe calculadora (pasta calculadora)
#UM METODO: nada mais e do que uma funcao que percente a uma Classe

# o self e um parametro obrigatorio de qualquer metodo de uma classe E ATRAVES DO SELF, que nos teremos acesso as informacoes dentro de uma classe, como no caso area_paredes
#SELF : obrigatorio de todo metodo, de toda a classe

# em seguida iremos declarar todos os metodos que ira exigir: a largura, profundidade, altura
#que sao os dados necessario para calcular a area das paredes

#AGORA QUE ESTAMOS NO MEDOTO A PRIMEIRA COISA QUE NOS VAMOS FAZER E
# REFERENCIAR AS AREAS DAS PAREDES >> self.area_paredes

#INDICANDO QUE NOS ESTAMOS NOS REFERINDO A ATRIBUTOS AREA_CLASSE E NAO A VARIAVEL NOVA NO METODO

#DENTRO DO ATRIBUTO NOS VAMOS COLOCAR:  ( largura + profundidade) * altura < o valor calculado dentro da classe

#POR FIM, nos vamos colocar a palavra "RETURN"pra dizer que :
        # quem for que quem executar essa funcao recebera como valor a area das paredes que acabou de ser calculada

#ELE FUNCIONA EXATAMENTE COMO ANTES, SO QUE AGORA CONECTADO AO OBJETO