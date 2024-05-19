import numpy
import numpy as np

y = 600

equations = np.arange(start=5, stop=-11, step=-4)
num_weigths = len(equations)
solutions_per_population = 8

population_size = (solutions_per_population, num_weigths)
new_population = np.random.uniform(-4.0, 4.0, population_size)
precision = 0.1
max_generation = 1000
num_parents = 4


def cai_pop_fitness(equation_inputs, pop, y):
    fitness = numpy.sum(pop * equation_inputs, axis=1)
    for i in range(len(fitness)):
        fitness[i] = y - fitness[i]
    fitness = numpy.abs(fitness)
    return fitness


fitness = cai_pop_fitness(equations, new_population, y)

print(fitness)


def select_mating_pool(pop, fitness, num_parents):
    parents = np.empty((num_parents, pop.shape[1]))
    for parent_num in range(num_parents):
        min_fitness_index = numpy.where(fitness == np.min(fitness))
        min_fitness_index = min_fitness_index[0][0]
        parents[parent_num, :] = pop[min_fitness_index, :]
        fitness[min_fitness_index] = float('inf')  # representação do infinito
        return parents


def crossover(parents, offspring_size):
    offspring = np.empty(offspring_size)
    crossover_points = np.uint8(offspring_size[1] / 2)  # pega o ponto central
    for k in range(offspring_size[0]):
        parent1_index = k % parents.shape[0]
        parent2_index = (k + 1) % parents.shape[0]
        offspring[k, 0:crossover_points] = parents[parent1_index, 0:crossover_points]
        offspring[k, crossover_points:] = parents[parent1_index, crossover_points:]
    return offspring


def mutatation(offpring_crossover):
    for index in range(offpring_crossover.shape[0]):
        random_value = np.random.uniform(-1.0, 1.0, 1)
        offpring_crossover[index, 4] = offpring_crossover[index, 4] + random_value
    return offpring_crossover


for generation in range(max_generation):
    print(f'Generation {generation} : ')
    fitness = cai_pop_fitness(equations, new_population, y)
    best_match_index = np.where(fitness == np.min(fitness))

    if fitness[best_match_index] <= precision:
        break
    print(f'Fitness valor \n\n: {fitness}')
    parents = select_mating_pool(new_population, fitness, num_parents)
    print(f'Pais seleceionados \n\n: {parents}')
    # continuar depois

fitness = cai_pop_fitness((equations, new_population, y))
# continuar depois