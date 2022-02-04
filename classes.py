import random
import copy
from contants import (
    GENE_MAX,
    GENE_MUTATION
)

class Genom:
    genes = []

    def __rand(self, n):
        return random.randint(0, n)

    def __init__(self):
        self.genes = [
            self.__rand(1) for idx in range(GENE_MAX)
        ]
    
    def get_score(self):
        return sum(self.genes)
    
    def mutation(self):
        for idx, gene in enumerate(self.genes):
            if self.__rand(GENE_MUTATION) == 0:
                self.genes[idx] = (gene + 1) % 2

    def crossover(self, genom):
        progeny = copy.deepcopy(self)
        if len(progeny.genes) != len(genom.genes):
            raise Exception()
        
        for idx, _ in enumerate(progeny.genes):
            if self.__rand(1) == 0:
                continue
            progeny.genes[idx] = genom.genes[idx]
        
        return progeny
