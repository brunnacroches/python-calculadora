from calculadora import Calculadora
from comodo import Comodo

calc = Calculadora()

comodo = Comodo(
    input('Qual a largura do cômodo?'),
    input('Qual a profundidade do cômodo?')
)

print(
    "A area das paredes é: ",
      calc.calcular_area_paredes(
          comodo
      )
)


print(
    'A area do teto e:',
    calc.calcular_area_teto(
        comodo)
)

print(
    'A litragem de tinta necessaria é: ',
    calc.calcular_litragem_necessaria()
)
