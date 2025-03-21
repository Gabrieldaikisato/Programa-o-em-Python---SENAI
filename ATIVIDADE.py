import statistics

def calcular_moda(notas):
    return statistics.mode(notas)

def calcular_media(notas):
    return statistics.mean(notas)

def desvio_padrao(notas):
    return statistics.stdev(notas)

def maior_nota(notas):
    return max(notas)

def menor_nota(notas):
    return min(notas)

def exibir(notas):
    print (f'Moda das notas:{calcular_moda(notas)}')
    print (f'Média das notas:{calcular_media(notas):.2f}')
    print (f'Desvio de padrão:{desvio_padrao(notas):.2f}')
    print (f'Maior nota:{maior_nota(notas)}')
    print (f'Menor nota:{menor_nota(notas)}')

quantidade_notas = int(input('Quantas notas você deseja inserir? '))
notas = []

for i in range(quantidade_notas):
    nota = float(input('Digite a nota do aluno:'))
    notas.append(nota)

exibir(notas)

print('press esc para sair')