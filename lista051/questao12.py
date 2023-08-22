'''
12) Desenvolver um programa que peça ao usuário para digitar diversos números reais, e ao final, exibir o maior e o
menor número que foram digitados, além da média entre TODOS os números digitados pelo usuário. A inserção
de números deve parar quando o usuário digitar o número -1, e este número -1 não deve ser considerado nem
como maior, nem como menor, e nem na contagem da média.
'''


num1 = float(input("Digite um valor real:\n"))
div = 0

if num1 != -1:
    med = num1
    mai = num1
    men = num1

    while num1 != -1:
        num1 = float(input("Digite um valor real:\n"))
        if num1 != -1:
            med = med + num1
        if num1 != -1:
            div = div + 1
        if mai < num1 and num1 != -1:
            maior = num1
        if men > num1 and num1 != -1:
            menor = num1

    print(f"O maior número é {maior} e o menor é {menor} e a média é de {med / div:.2f}")
 