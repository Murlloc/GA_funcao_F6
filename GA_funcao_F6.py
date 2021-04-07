import random
import indiviuos

TAMANHO_POPULACAO   = 100
NUMERO_DE_GERACOES  = 40
TOTAL_DE_INDIVIDUOS = 4000

def main():
    global TAMANHO_POPULACAO, NUMERO_DE_GERACOES, TOTAL_DE_INDIVIDUOS

    found = False
    generation = 0
    population = []
  
    # Criando a população inicial aleatória
    for _ in range(TAMANHO_POPULACAO):
        gnome = indiviuos.Individual.create_gnome()
        population.append(indiviuos.Individual(gnome))
    pass

if __name__ == '__main__':
    main()