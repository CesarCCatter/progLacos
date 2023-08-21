'''
9) Elaborar um programa que apresente no final a soma dos valores pares existentes na faixa de 0 até 500. Utilize
um laço que efetue a variação de 2 em 2.
'''

cont = 0
acum = 0

while (cont <= 500):
    print(f"O valor {cont}é par")
    acum = acum + cont
    cont = cont +2
