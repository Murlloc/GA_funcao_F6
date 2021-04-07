import random
import math

MAX = 100
MIN = -100

class Individual(object):
    def __init__(self, cromossoma):
        self.cromossoma = cromossoma 
        self.fitness = self.cal_fitness()
  
    @classmethod
    def create_gnome(self):
        
        return self.rand_key(self, 44)
  
    def rand_key(self, p):
    
        binary = ""
    
        for i in range(p):
            temp = str(random.randint(0, 1))
            binary += temp

        return(binary)
  
    def cal_fitness(self):

        global MIN, MAX

        #Primeiro dividimos o cromossoma em 2
        x,y = self.cromossoma[:len(self.cromossoma)/2], self.cromossoma[len(self.cromossoma)/2:]
        base_dez_x = int(x, 2)
        base_dez_y = int(y, 2)
        real_x = (base_dez_x * ((MAX-MIN) / (2**22 - 1))) + MIN
        real_y = (base_dez_y * ((MAX-MIN) / (2**22 - 1))) + MIN

        fSix_result = aply_fSix(x,y)

        #Avalio o quão proximo ela está do meu otimo

    def aply_fSix(self, x, y):
        return (0.5 - (((math.sin(math.sqrt(x**2 + y**2)))**2 - 0.5) / (1.0 + 0.001 * (x**2 + y**2))**2))