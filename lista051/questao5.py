'''
5) Desenvolver um programa que apresente os resultados de uma tabela de um número qualquer. Ela deve ser
impressa no seguinte formato:
Considerando como exemplo o fornecimento do número 2
2 . 1 = 2
2 . 2 = 4
2 . 3 = 6
2 . 4 = 8
2 . 5 = 10
(...)
2 . 10 = 20
'''

cont = 2
fat = 1

while (fat <= 100 ):
    print(f"2 . {fat} = {fat * cont}")
    fat = fat + 1
