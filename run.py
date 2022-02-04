import random
import copy
from classes import Genom
from contants import (
    GENERATE_GENOMS,
    GENOM_GENERATION,
    ELITE_GENOMS,
    PROGENY_GENOMS,
    NORMAL_GENOMS
)

if __name__=='__main__':
    current_genoms = [Genom() for idx in range(GENERATE_GENOMS)]
    extact_genom_score = lambda g: g.get_score()

    for loop in range(GENOM_GENERATION):
        next_genoms = []
        current_genoms = sorted(current_genoms, key=extact_genom_score, reverse=True)
        print("{0} generasion score:".format(loop + 1))
        print("\thigh: {0}".format(current_genoms[0].get_score()))
        print("\tmedian: {0}".format(
            current_genoms[int(GENERATE_GENOMS / 2)].get_score()
        ))
        print("\tlow: {0}".format(
            current_genoms[GENERATE_GENOMS - 1].get_score()
        ))
        print("")

        elites = [
            current_genoms[idx] for idx in range(ELITE_GENOMS)
        ]

        progenies = []
        for idx in range(PROGENY_GENOMS):
            g1 = random.randint(0, GENERATE_GENOMS - 1)
            g2 = random.randint(0, GENERATE_GENOMS - 1)
            progenies.append(
                current_genoms[g1].crossover(current_genoms[g2])
            )
        
        normals = []
        for idx in range(NORMAL_GENOMS):
            pickup_genom_idx = random.randint(0, (GENERATE_GENOMS - (idx + 1)))
            normals.append(
                current_genoms.pop(pickup_genom_idx)
            )
        
        next_genoms.extend(elites)
        next_genoms.extend(progenies)
        next_genoms.extend(normals)
        if len(next_genoms) != GENERATE_GENOMS:
            raise Exception()
        
        for genom in next_genoms:
            genom.mutation()
        
        current_genoms = copy.deepcopy(next_genoms)
        del next_genoms
    
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
