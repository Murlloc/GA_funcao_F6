import random
import math

MAX          = 100
MIN          = -100

class Individual(object):
    def __init__(self, cromossoma, geracao):
        self.cromossoma = cromossoma 
        self.fitness = self.cal_fitness()
        self.geracao = self.count_de_geracoes(geracao)
        self.x = 0.0
        self.y = 0.0

    @classmethod
    def create_gnome(self):
        
        return self.rand_key(self, 44)
  
    def rand_key(self, p):
        binary = ""
        for i in range(p):
            temp = str(random.randint(0, 1))
            binary += temp
        return(binary)
  
    def count_de_geracoes(self, count):
        return count + 1

    def define_x_and_y(self, f):
        #Primeiro dividimos o cromossoma em 2
        x,y = f.cromossoma[:22], f.cromossoma[22:]
        base_dez_x = int(x, 2)
        base_dez_y = int(y, 2)
        real_x = (base_dez_x * ((MAX-MIN) / (2**22 - 1))) + MIN
        real_y = (base_dez_y * ((MAX-MIN) / (2**22 - 1))) + MIN
        f.x = real_x
        f.y = real_y
        return f

    def cal_fitness(self):
        global MIN, MAX
        #Primeiro dividimos o cromossoma em 2
        x,y = self.cromossoma[:22], self.cromossoma[22:]
        base_dez_x = int(x, 2)
        base_dez_y = int(y, 2)
        real_x = (base_dez_x * ((MAX-MIN) / (2**22 - 1))) + MIN
        real_y = (base_dez_y * ((MAX-MIN) / (2**22 - 1))) + MIN
        #Calcula o valor da função F6, que será usado para o fitness
        fSix_result = self.aply_fSix(real_x, real_y)

        return fSix_result

    def aply_fSix(self, x, y):
        return (0.5 - (((math.sin(math.sqrt(x**2 + y**2)))**2 - 0.5) / (1.0 + 0.001 * (x**2 + y**2))**2))