# CORRA FORREST

'''
Forrest é um garoto que adora correr, e como está acostumado em correr diariamente, ele sempre procura fazer o menor tempo possível,
porém não é muito organizado e anota os tempos de suas corridas em papéis que são jogados em sua gaveta sem nenhum tipo de ordenação.
Como Forrest está muito ocupado ultimamente, planejando como cumprir uma promessa a um amigo que adorava restaurantes e camarão,
pediu a você que crie um programa que receba como entrada os tempos das corridas que estão nos papéis e calcule a média aritmética
dos tempos gastos para completar o seu percurso de corrida diário.
Ao final, seu programa deve também exibir todos os tempos que ficaram abaixo dessa média, na mesma ordem em que foram recebidos na entrada.

*** Entrada ***

- Diversos valores inteiros, um por linha, que representam os tempos gastos em cada corrida (em segundos);
- A entrada é finalizada com a inserção de um valor negativo, que não deve ser contabilizado.

*** Saída ***

- Na primeira linha a palavra 'MEDIA', sem apóstrofos, sem acentuação e completamente em maiúsculo, seguida por dois pontos (':'),
um caractere de espaço e um valor real com duas casas decimais, indicando a média dos tempos dados na entrada, em segundos;
- Nas linhas seguintes, os tempos que ficaram abaixo dessa média, em segundos, um por linha e na mesma ordem em que foram dados na entrada.

'''

# RESOLUÇÃO:

tempos = []
tempo = int(input())

def calcula_media():
  media = sum(tempos) / len(tempos)
  return media

def exibe_media(media):
  print(f'MEDIA: {media:.2f}')

def exibe_tempos_abaixo_da_media(media):
  if(tempo < media):
    print(tempo)

def adiciona_tempo_na_lista():
  tempos.append(tempo)

while (tempo >= 0):
  adiciona_tempo_na_lista()
  tempo = int(input())

exibe_media(calcula_media())

for tempo in tempos:
  if ( tempo >= 0 ):
    exibe_tempos_abaixo_da_media(calcula_media())
