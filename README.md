# genetic_algorithm_sample
genetic algorithm sample by python3.

# usage
execute the following command.
```bash
$ python3 run.py
```

The following result will be output.
```
1 generasions score:
        high: 64
        median: 50
        low: 38

2 generasions score:
        high: 63
        median: 51
        low: 38

...

100 generasions score:
        high: 90
        median: 82
        low: 70

last generasions score:
        high: 90
        median: 83
        low: 70
```

# config
want to change the setting, edit [constants.py](https://github.com/mochi256/genetic_algorithm_sample/blob/main/constants.py)

### GENERATE_GENOMS
- the number of individuals produced in one generation.

### ELITE_GENOMS
- a high-scoring individual that will be left to the next generation.

### PROGENY_GENOMS
- leave intermingled individuals for the next generation.

### NORMAL_GENOMS
- leave the arbitrarily extracted genome to the next generation.

### GENE_MAX
- the number of genes by genom.

### GENE_MUTATION
- probability of mutation(1/N).

### GENOM_CROSSOVER
- probability of crossover(1/N).

### GENOM_GENERATION
- number of generations to try.