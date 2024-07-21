# Curtesy to Rayan Ali
import random
"""
Objective of this GA is 
fitness = my name "jiratiwat sinchai"
populate = empirical
targret type = string
"""
SIZE_POP = 500
MUT_RATE = 0.01
TARGET = "jiratiwat sinchai"
GENES = ' abcdefghijklmnopqrstuvwxyz'
INDEX_FITNESS = 1
INDEX_CHROMOSOME = 0

def init_pop(N_TARGET):
    """
    create initial population based TARGET size
    :param N_TARGET:
    :return: population (list of chromosomes)
    """
    pop = []
    for _ in range(SIZE_POP):
        chromosome = [random.choice(GENES) for _ in range(N_TARGET)]
        pop.append(chromosome)
    return pop

def fitness_cal(TARGET, chromo_from_pop):
    """
    Calculate fitness value by comparing lexicographically chromosome with the target. The more fitness value the less
    fit it is.
    :param TARGET:
    :param chromo_from_pop:
    :return:
    """
    diff = sum(tar_char != chromo_char for tar_char, chromo_char in zip(TARGET, chromo_from_pop))
    return [chromo_from_pop, diff]

def selection(pop, TARGET):
    """
    Return elites which represents the best first 20 percent of the population.
    :param pop:
    :param TARGET:
    :return:
    """
    sorted_chromo_pop = sorted(pop, key=lambda x: x[INDEX_FITNESS])
    return sorted_chromo_pop[:int(0.2 * SIZE_POP)]

def crossover(selected_chromo, CHROMO_LEN, pop):
    offspring_cross = []
    for _ in range(SIZE_POP):
        p1 = random.choice(selected_chromo)[0]
        p2 = random.choice(selected_chromo)[0]
        crossover_point = random.randint(1, CHROMO_LEN-1)
        child = p1[:crossover_point] + p2[crossover_point:]
        offspring_cross.append(child)
    return offspring_cross

def mutate(offspring, MUT_RATE):
    mutants = []
    for chromosome in offspring:
        mutant = [
            random.choice(GENES) if random.random() < MUT_RATE else gene
            for gene in chromosome
        ]
        mutants.append(mutant)
    return mutants

def replace(new_gen, pop):
    for p in range(len(pop)):
        if pop[p][INDEX_FITNESS] > new_gen[p][INDEX_FITNESS]:
            pop[p][INDEX_CHROMOSOME] = new_gen[p][INDEX_CHROMOSOME]
            pop[p][INDEX_FITNESS] = new_gen[p][INDEX_FITNESS]
    return pop

# 1) initialize population
first_pop = init_pop(len(TARGET))
found = False
pop = []
gen = 1

# 2) Assign tuples of [chromosome string, fitness] into pop list
for p in range(len(first_pop)):
    pop.append(fitness_cal(TARGET, first_pop[p]))

# 3) If found then stop
while not found:

    # 3.1) Select elites from pop (accounted for 50% of the pop)
    selected = selection(pop, TARGET)

    # 3.2) mate parents to make new generation
    pop = sorted(pop, key=lambda x: x[1])
    crossovered = crossover(selected, len(TARGET), pop)

    # 3.3) mutating the crossovered chromosome children to diversify the new generation (search algorithm)
    # new mutant does not have fitness value yet.
    mutants = mutate(crossovered, MUT_RATE)
    new_gen = [fitness_cal(TARGET, mutant) for mutant in mutants]

    # 3.4) replacement of bad population with new generation
    # we sort here first to compare the least fit population with the most fit new_gen

    pop = replace(new_gen, pop)

    if (pop[0][1] == 0):
        print('Target found')
        print('String: ' + str(pop[0][0]) + ' Generation: ' + str(gen) + ' Fitness: ' + str(
            pop[0][1]))
        break
    print('String: ' + str(pop[0][0]) + ' Generation: ' + str(gen) + ' Fitness: ' + str(
        pop[0][1]))
    gen += 1
