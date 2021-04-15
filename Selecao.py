def elitismo(population):
    aux = {'index': 0, 'fitness': 0.0}
    for i in range(len(population)):
        if population[i].fitness > aux['fitness']:
            aux['index']   = i
            aux['fitness'] = population[i].fitness
    return population[aux['index']]

def somatorio_fitness(population, index):  
    soma_dos_fitness = 0
    for i in range(index):
        soma_dos_fitness += population[i].fitness
    return soma_dos_fitness

def substitui_elitismo(population, selecionado):
    aux = {'index': 0, 'fitness': 1.0}
    for i in range(len(population)):
        if population[i].fitness < aux['fitness']:
            aux['index']   = i
            aux['fitness'] = population[i].fitness
    population.pop(aux['index'])
    population.append(selecionado)
    return population

def roleta(population, soma_dos_fitness_total, choosen_number):
    for index in range(len(population)):
        soma_dos_fitness_parcial = somatorio_fitness(population, index + 1)
        if soma_dos_fitness_parcial >= choosen_number:
            return population[index]