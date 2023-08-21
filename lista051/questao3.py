'''
3) Desenvolver um programa que apresente os quadrados dos números inteiros de 15 a 200.
'''
import math

cont = 15



while (cont <= 200):
    qua = math.pow(cont,2)
    print(f"Quadrado do número {cont}: {qua:.0f}")
    cont = cont + 1