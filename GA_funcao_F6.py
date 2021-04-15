import random
import individuos
import Operacoes
import Selecao
import Grafico

TAMANHO_POPULACAO   = 100
NUMERO_DE_GERACOES  = 400
TAXA_MUTACAO        = 0.008
TAXA_CROSSOVER      = 0.65

def main():
    global TAMANHO_POPULACAO, NUMERO_DE_GERACOES, TOTAL_DE_INDIVIDUOS
    global TAXA_CROSSOVER, TAXA_MUTACAO

    found      = False
    generation = 0
    best = individuos.Individual(individuos.Individual.create_gnome(), 0)
    melhores = []
    population = create_initial_population()
    count = 1
    while (not found):
        aux = {'index': 0, 'fitness': 0.0}
        for index in range(len(population)):
            if population[index].fitness > aux['fitness']:
                aux['index']   = index
                aux['fitness'] = population[index].fitness
            if population[index].fitness > best.fitness:
                best = population[index]
            if population[index].fitness >= 1.0:
                found = True
                print("Temos o vencedor na geração: " + str(population[index].geracao))
                Grafico.gerar_grafico(melhores)
            elif count >= NUMERO_DE_GERACOES:
                found = True

        melhores.append(population[aux['index']])
        if found == True:
            Grafico.gerar_grafico(melhores)

        print("Geração atual: " + str(count) + " | " + "O melhor até agora: " + str(best.geracao) + "°: " 
                + str(best.fitness) + " | " + "Valor do cromossomo: " + best.cromossoma)

        soma_dos_fitness_total   = Selecao.somatorio_fitness(population, len(population))
        selecionado_por_elitismo = Selecao.elitismo(population)
        selecionados_por_roleta  = []
        for _ in range(TAMANHO_POPULACAO):
            choosen_number = random.uniform(0.0, soma_dos_fitness_total)
            selecionados_por_roleta.append(Selecao.roleta(population, soma_dos_fitness_total, choosen_number))
        maes, pais = selecionados_por_roleta[:int(len(selecionados_por_roleta)/2)], selecionados_por_roleta[int(len(selecionados_por_roleta)/2):]
        
        '''
        Realiza o cruzamento, começando com o Crossover
        '''
        filhos = []
        for index in range(len(maes)):
            comparador_da_taxa = round(random.uniform(0.0, 1.0), 2)
            if (comparador_da_taxa >= TAXA_CROSSOVER):
                #Realiza o cruzamento
                aux = Operacoes.crossover(maes[index], pais[index])
                filhos.extend([Operacoes.mutacao(aux[0], TAXA_MUTACAO), Operacoes.mutacao(aux[1], TAXA_MUTACAO)])
            else:
                filhos.append(maes[index])
                filhos.append(pais[index])

        population = Selecao.substitui_elitismo(filhos, selecionado_por_elitismo)
        count = count + 1

def create_initial_population():
    population = []
    for _ in range(TAMANHO_POPULACAO):
        gnome  = individuos.Individual.create_gnome()
        aux = individuos.Individual(gnome, 0)
        aux = aux.define_x_and_y(aux)
        population.append(aux)
    return population

if __name__ == '__main__':
    main()