# INTERVALOS DE PRIMOS

'''
Os números primos têm diversas aplicações, principalmente na criptografia utilizada pelos aplicativos de seu banco e nos sites
de compra que nos trazem tanta comodidade.
Um número natural é considerado primo quando possui somente dois divisores, o número um e ele próprio. O número zero e o número um não são primos
e o número dois é o único primo par.
Seu objetivo é criar um programa que receba como entrada dois números naturais, INÍCIO e FIM, e exibe os números primos que existem no intervalo
fechado [INÍCIO...FIM]. Ao final, o programa também deve exibir a quantidade de primos encontrados no intervalo.

*** Entrada ***

Dois números naturais, INÍCIO e FIM, respectivamente, um por linha. Adote (INÍCIO <= FIM <= 5000).

*** Saída ***

Os números primos presentes no intervalo fechado [INÍCIO...FIM] e a quantidade de números primos do intervalo.

'''

# RESOLUÇÃO:

inicio = int(input())
fim = int(input())
quantidade_primos = 0

def eh_primo(num):
  if num < 2:
    return False
  elif num == 2:
    print(num)
    return True
  else:
    for i in range(2, num):
      if num % i == 0:
        return False
    print(num)
    return True

if (inicio <= fim <= 5000):
  for i in range(inicio, fim + 1):
    if eh_primo(i):
      quantidade_primos += 1
  
  print(f'primos: {quantidade_primos}')
