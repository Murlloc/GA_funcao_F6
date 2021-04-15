import random
import individuos

def crossover(mother, father):
    ponto_de_corte = random.randint(0,43)
    mother_head,mother_tail = mother.cromossoma[:ponto_de_corte], mother.cromossoma[ponto_de_corte:]
    father_head,father_tail = father.cromossoma[:ponto_de_corte], father.cromossoma[ponto_de_corte:]
    filho1 = individuos.Individual((mother_head + father_tail), mother.geracao)
    filho2 = individuos.Individual((father_head + mother_tail), mother.geracao)
    filho1 = filho1.define_x_and_y(filho1)
    filho2 = filho2.define_x_and_y(filho2)
    return [filho1, filho2]

def mutacao(f, TAXA_MUTACAO):
    aux = list(f.cromossoma)
    for index in range(len(aux)):
        taxa_mutacao_aleatoria = round(random.uniform(0.000, 1.000), 3)
        if taxa_mutacao_aleatoria < TAXA_MUTACAO:
            if (aux[index] == '0'):
                aux[index] = '1'
            else:
                aux[index] = '0'
    f.cromossoma = ''.join(aux)
    return f
