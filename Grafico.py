import matplotlib.pyplot as pyplot

def gerar_grafico(population):
    eixo_x = []
    eixo_y = []
    i = 0
    for individuo in population:
        eixo_y.append(individuo.fitness)
        eixo_x.append(i)
        i = i + 1
    pyplot.title("Evolução do fitness x gerações")
    pyplot.xlabel("Gerações")
    pyplot.ylabel("Melhor Fitness")

    pyplot.plot(eixo_x, eixo_y)
    pyplot.show()