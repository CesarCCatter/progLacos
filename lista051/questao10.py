'''
10) Desenvolver um programa que apresente as potências de 3 variando de 0 a 15. Deve ser considerado que
qualquer número elevado a zero é 1, e elevado a 1 é ele próprio. A apresentação deve observar a seguinte
exibição na tela:
3 elevado à 0 = 1
3 elevado à 1 = 3
3 elevado à 2 = 9
(...)
3 elevado à 15 = 14348907
OBS: Tente fazer em uma classe utilizando Math.pow() e em outra classe sem utilizar Math.pow()
'''
import math

contp = 0

while (contp <= 15):
    cont = math.pow(3,contp)
    print(f"O resultado de 3 elevado a {contp} é : {cont:.0f}")
    contp = contp + 1

