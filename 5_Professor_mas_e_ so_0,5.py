# PROFESSOR, MAS É SÓ 0,5

'''
Você, um estudante exemplar, conquista notas elevadas e por isso não se preocupa com a média final nas disciplinas, pois sabe que será aprovado sem
precisar de prova substitutiva. No entanto, alguns de seus colegas estão apreensivos, pois estavam acostumados a estudar “em cima da hora” e demoraram
para perceber que essa “tática” não funciona mais. Por isso, querem saber se com a nota que possuem serão aprovados ou se há a possibilidade de
aprovação com a prova substitutiva.
Dessa forma, você resolve criar um programa para ajudar seus colegas. Seu programa receberá como entrada dois números reais, o primeiro representando a
nota de trabalho e o segundo a nota da prova regular. Considerando que cada uma das duas notas representa 50% da média final, seu programa exibirá uma
mensagem indicando a situação do aluno que poderá ser uma das três:
a) Aprovado:  se a média final for maior ou igual a seis;
b) Talvez com a prova substitutiva: se existir alguma nota possível na prova substitutiva que permita que a média final fique maior ou igual a seis.
Lembrando que, assim como a nota de trabalho e da prova regular, a nota máxima na prova substitutiva é dez e que ela pode substituir apenas a nota da
prova regular, não a de trabalho;
c) Reprovado: se a média final for menor do que seis e não existir possibilidade de recuperação, mesmo com a nota máxima na prova substitutiva.
Obs.: O nome do problema é uma referência a clássica frase proferida no final do semestre pelos alunos que não estudaram adequadamente.

*** Entrada ***

Dois números reais que podem variar de 0.00 a 10.00, um por linha, que representam a nota de trabalhos e a nota da prova regular, respectivamente.

*** Saída ***

Uma frase indicando a situação do aluno a quem pertencem as notas de entrada. A situação pode ser ‘aprovado’, ‘reprovado’ ou ‘talvez com a sub’, sem
os apóstrofos e completamente em minúsculo.

'''

# RESOLUÇÃO: 

trabalho = float(input())
prova = float(input())

media = (trabalho + prova) / 2

if media >= 6.0:
    print('aprovado')
else:
    media = (trabalho + 10) / 2
    if media >= 6.0:
        print('talvez com a sub')
    else:
        print('reprovado')
