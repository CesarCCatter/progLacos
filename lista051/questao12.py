'''
12) Desenvolver um programa que peça ao usuário para digitar diversos números reais, e ao final, exibir o maior e o
menor número que foram digitados, além da média entre TODOS os números digitados pelo usuário. A inserção
de números deve parar quando o usuário digitar o número -1, e este número -1 não deve ser considerado nem
como maior, nem como menor, e nem na contagem da média.
'''

num = float(input("Digite um valor real (-1 encerra o programa): "))

mai = num
men = num
med = num
tot_resp = 0
soma = 0
while (num != -1):
    soma = soma + num
    tot_resp = tot_resp + 1


    if (mai < num):
        mai = num

    if (men > num):
        men = num

    num = float(input("Digite outro valor real (-1 encerra o programa): "))

if (mai == -1):
    print(f"Maluco")
else:
    print(f"Maior valor inserido: {mai}")
    print(f"Menor valor inserido: {men}")
    print(f"Média dos valores inseridos: {soma / tot_resp}")

