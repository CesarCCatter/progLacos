'''
11) Elaborar um programa que apresente o valor de uma potência de uma base qualquer (Variável b) elevada a um
expoente qualquer (Variável e), ou seja, de be
. (Sem usar Math.pow();)
'''

b = int(input("Informe um número para ser a base: "))
e = int(input("Informe um número para ser o expoente: "))

cont = 1
acum = 1
while (cont <= e):
    acum = acum * b
    cont = cont + 1
print(f"{b:.0f} elevado a {e:.0f} é: {acum:.0f}")
