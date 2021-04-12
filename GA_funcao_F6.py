import random
import individuos

TAMANHO_POPULACAO   = 100
NUMERO_DE_GERACOES  = 40
TOTAL_DE_INDIVIDUOS = 4000

def main():
    global TAMANHO_POPULACAO, NUMERO_DE_GERACOES, TOTAL_DE_INDIVIDUOS

    found      = False
    generation = 0
  
    population = create_initial_population()

    while not found:
        soma_dos_fitness_total   = somatorio_fitness(population, len(population))
        selecionado_por_elitismo = elitismo(population)
        selecionados_por_roleta  = []
        for _ in range(TAMANHO_POPULACAO):
            choosen_number = random.uniform(0.0, soma_dos_fitness_total)
            selecionados_por_roleta.append(roleta(population, soma_dos_fitness_total, choosen_number))
        maes, pais = selecionados_por_roleta[:int(len(selecionados_por_roleta)/2)], selecionados_por_roleta[int(len(selecionados_por_roleta)/2):]
        
        '''
        Realiza o cruzamento, começando com o Crossover
        '''
        filhos = []
        for index in range(len(maes)):
            comparador_da_taxa = round(random.uniform(0.0, 1.0), 2)
            if (comparador_da_taxa >= 0.65):
                #Realiza o cruzamento
                aux = crossover(maes[index], pais[index])
                filhos.append(aux[0])
                filhos.append(aux[1])
            else:
                filhos.append(maes[index])
                filhos.append(pais[index])

        #Fazer a mutação
        found = True

def roleta(population, soma_dos_fitness_total, choosen_number):
    for index in range(len(population)):
        soma_dos_fitness_parcial = somatorio_fitness(population, index + 1)
        if soma_dos_fitness_parcial >= choosen_number:
            return population[index]
    

def elitismo(population):
    aux = {'index': 0, 'fitness': 0.0}
    for i in range(len(population)):
        if population[i].fitness > aux['fitness']:
            aux['index']   = i
            aux['fitness'] = population[i].fitness
    return population[aux['index']]

def create_initial_population():
    population = []
    for _ in range(TAMANHO_POPULACAO):
        gnome  = individuos.Individual.create_gnome()
        population.append(individuos.Individual(gnome))
    return population

def somatorio_fitness(population, index):  
    soma_dos_fitness = 0
    for i in range(index):
        soma_dos_fitness += population[i].fitness
    return soma_dos_fitness

def crossover(mother, father):
    ponto_de_corte = random.randint(1,43)
    mother_head,mother_tail = mother.cromossoma[:ponto_de_corte], mother.cromossoma[ponto_de_corte:]
    father_head,father_tail = father.cromossoma[:ponto_de_corte], father.cromossoma[ponto_de_corte:]
    filho1 =individuos.Individual(mother_head + father_tail)
    filho2 =individuos.Individual(father_head + mother_tail)
    return [filho1, filho2]

if __name__ == '__main__':
    main()