# CARRINHO DE COMPRAS

'''
Você está criando um site para uma loja virtual e precisa guardar os itens que os usuários adicionam em seu carrinho. Cada item é representado
no sistema por um código numérico, isto é, um número inteiro que é capaz de identificá-lo unicamente. Como solução inicial, você decidiu guardar
os itens adicionados ao carrinho em uma lista, e para testar o seu programa, implementou alguns comandos básicos para simular uma interação do
usuário com o sistema:

- adicionar: inclui o código de um novo produto à lista;
- remover: remove o código de um produto da lista;
- exibir: exibe os itens da lista em ordem crescente;
- encerrar: exibe os itens da lista, assim como no comando exibir, em ordem crescente, e encerra o programa.

A primeira linha poderá conter uma lista de inteiros separado por espaços, representando produtos que já estavam no carrinho, por exemplo,
de uma sessão anterior que o usuário iniciou mas não finalizou a compra. Você deve receber essa lista e inicializar o carrinho de compras
já com os códigos dessa lista, que devem ser números inteiros.
Caso não haja nenhum produto salvo de uma sessão anterior, essa primeira linha será uma linha em branco, sem nenhum texto ou caractere.

*** Entrada ***

- A primeira linha poderá conter números inteiros separados por espaço ou ser uma linha em branco;
- Cada linha seguinte conterá um dos comandos listados acima e, para os comandos "adicionar" e "remover", conterá também o código
de um produto separado por um espaço;
- A entrada termina sempre com o comando "encerrar".

*** Saída ***

A saída deve conter:
- A exibição dos códigos na lista, separados por espaço, de acordo com a execução dos comandos "exibir" e "encerrar";
- A mensagem "código <código> não encontrado", quando o comando remover é executado com um código que não esteja presente na lista.
Substitua <código> pelo número do código em questão.

Obs.: Lembre-se de não exibir texto no input.

'''

# RESOLUÇÃO:

carrinho_de_compras = input().split()

if (carrinho_de_compras != []):

  for i in range(len(carrinho_de_compras)):
    carrinho_de_compras[i] = int(carrinho_de_compras[i])

def adicionar(lista, item):
  lista.append(item)

def remover(lista, item):
  if (item in lista):
    lista.remove(item)
  else:
    print(f'código {item} não encontrado')

def exibir(lista):
  lista.sort()

  for i in range(len(lista)):
    if (i < len(lista) - 1):
      print(lista[i], end=' ')
    else:
      print(lista[i])

comando = input().split()

while comando[0] != 'encerrar':
  if (comando[0] == 'adicionar'):
    adicionar(carrinho_de_compras, int(comando[1]))
  elif (comando[0] == 'remover'):
    remover(carrinho_de_compras, int(comando[1]))
  else:
    exibir(carrinho_de_compras)

  comando = input().split()

exibir(carrinho_de_compras)
