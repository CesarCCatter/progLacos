'''
12) Desenvolver um programa que peça ao usuário para digitar diversos números reais, e ao final, exibir o maior e o
menor número que foram digitados, além da média entre TODOS os números digitados pelo usuário. A inserção
de números deve parar quando o usuário digitar o número -1, e este número -1 não deve ser considerado nem
como maior, nem como menor, e nem na contagem da média.
'''




num1 = float(input("Digite um número: "))

while (num1 != -1):
    num1 = int(input("Digite um número: "))

maior = num1
menor = num1
