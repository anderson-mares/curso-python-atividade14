# importar biblioteca
from math import sqrt

# equação do 1º grau
primeiro_grau = lambda a, b: -b/a

# equação do 2º grau
def segundo_grau(a, b, c):
    delta = b**2 - 4*a*c
    if delta < 0:
        x1 = (-b)+sqrt(delta)/(2*a)
        x2 = (-b)-sqrt(delta)/(2*a)
        yield f'Valor de x1": {x1}.'
        yield f'Valor de x2:" {x2}.'
    elif delta == 0:
        x = -b/(2*a)
        yield x    
    else:
        yield f"Não existem raízes reais para a equação"