import random
import copy
from classes import Genom
from constants import (
    GENERATE_GENOMS,
    GENOM_GENERATION,
    ELITE_GENOMS,
    PROGENY_GENOMS,
    NORMAL_GENOMS
)

if __name__=='__main__':
    # generate genoms
    current_genoms = [Genom() for idx in range(GENERATE_GENOMS)]

    # function to be executed when sorting genomes.
    extact_genom_score = lambda g: g.get_score()

    for loop in range(GENOM_GENERATION):
        next_genoms = []

        # sort the genome by score.
        current_genoms = sorted(current_genoms, key=extact_genom_score, reverse=True)
        # show score
        print("{0} generasion score:".format(loop + 1))
        print("\thigh: {0}".format(current_genoms[0].get_score()))
        print("\tmedian: {0}".format(
            current_genoms[int(GENERATE_GENOMS / 2)].get_score()
        ))
        print("\tlow: {0}".format(
            current_genoms[GENERATE_GENOMS - 1].get_score()
        ))
        print("")

        # extracting superior genomes
        elites = [
            current_genoms[idx] for idx in range(ELITE_GENOMS)
        ]

        # genomes create offspring from each other.
        progenies = []
        for idx in range(PROGENY_GENOMS):
            g1 = random.randint(0, GENERATE_GENOMS - 1)
            g2 = random.randint(0, GENERATE_GENOMS - 1)
            progenies.append(
                current_genoms[g1].crossover(current_genoms[g2])
            )
        
        # leave any genome to the next generation
        normals = []
        for idx in range(NORMAL_GENOMS):
            pickup_genom_idx = random.randint(0, (GENERATE_GENOMS - (idx + 1)))
            normals.append(
                current_genoms.pop(pickup_genom_idx)
            )
        
        # generating the next generation of genomes
        next_genoms.extend(elites)
        next_genoms.extend(progenies)
        next_genoms.extend(normals)

        if len(next_genoms) != GENERATE_GENOMS:
            raise Exception()
        
        # mutate in all genomes with arbitrary probability
        for genom in next_genoms:
            genom.mutation()
        
        # update "current_genoms" and execute the next generation process.
        current_genoms = copy.deepcopy(next_genoms)
        del next_genoms
    
    # show the last score
    current_genoms = sorted(current_genoms, key=extact_genom_score, reverse=True)
    print("last generasion score: {0}".format(current_genoms[0].get_score()))
    print("\thigh: {0}".format(current_genoms[0].get_score()))
    print("\tmedian: {0}".format(
        current_genoms[int(GENERATE_GENOMS / 2)].get_score()
    ))
    print("\tlow: {0}".format(
        current_genoms[GENERATE_GENOMS - 1].get_score()
    ))
    print("")
