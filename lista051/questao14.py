'''
14) Desenvolver um programa que calcule o fatorial do número 5, ou seja, 5!. Desta forma, temos que 5! = 5 . 4 . 3 .
2 . 1 ou 5! = 1 . 2 . 3 . 4 . 5, equivalente a 120.
'''

cont = 1
acum = 1
while ( cont <= 5 ):
    print(acum)
    acum = cont * acum
    cont = cont + 1
print(acum)
