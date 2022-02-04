# number of genomes to generate
GENERATE_GENOMS = 250

# genoms to leave for the next generation
ELITE_GENOMS = int(GENERATE_GENOMS * 0.2)
PROGENY_GENOMS = int(GENERATE_GENOMS * 0.4)
NORMAL_GENOMS = GENERATE_GENOMS - (ELITE_GENOMS + PROGENY_GENOMS)

# maximum number of genes
GENE_MAX = 100

# probability of mutation(1/n)
GENE_MUTATION = 100

# probability of crossover(1/n)
GENOM_CROSSOVER = 100

# number of generations to try
GENOM_GENERATION = 100
