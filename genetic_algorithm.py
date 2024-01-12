import random

class Chromosome:
    def __init__(self, gene=None):
        self.gene = gene if gene is not None else self.initializeChromosome()

    def initializeChromosome(self):
        return ''.join(random.choice('01') for _ in range(len(target_chromosome)))

class ChromosomePopulation:
    def __init__(self, population_size):
        self.population_size = population_size
        self.chromosomes = []
        self.initializePopulation()

    def initializePopulation(self):
        for _ in range(self.population_size):
            chromosome = Chromosome()
            self.chromosomes.append(chromosome)

    def fitness(self, chromosome):
        # A simple fitness function, comparing the number of matching bits
        return sum(c1 == c2 for c1, c2 in zip(chromosome.gene, target_chromosome))

    def selectParents(self):
        # Select two parents based on their fitness
        parents = random.sample(self.chromosomes, 2)
        parents.sort(key=lambda x: self.fitness(x), reverse=True)
        return parents

    def crossover(self):
        # Select the two most suitable parents
        parents = self.selectParents()
        parent1, parent2 = parents[0], parents[1]

        # One-point crossover
        crossover_point = random.randint(1, len(target_chromosome) - 1)
        child_gene = parent1.gene[:crossover_point] + parent2.gene[crossover_point:]
        child = Chromosome(child_gene)
        return child

    def mutate(self, chromosome):
        # Flip a random bit
        mutation_point = random.randint(0, len(target_chromosome) - 1)
        mutated_gene = list(chromosome.gene)
        mutated_gene[mutation_point] = '1' if chromosome.gene[mutation_point] == '0' else '0'
        return Chromosome(''.join(mutated_gene))

def genetic_algorithm(target_chromosome, population_size):
    # Create the initial population
    chromosomePopulation = ChromosomePopulation(population_size)

    # Maximum number of generations
    max_generations = 1000

    for generation in range(max_generations):
        # Perform crossover and mutate until success
        child = chromosomePopulation.crossover()
        mutated_child = chromosomePopulation.mutate(child)

        # Check if the mutated child matches the target chromosome
        if mutated_child.gene == target_chromosome:
            print(f"Success! Target chromosome achieved in generation {generation + 1}")
            return mutated_child

        # Replace the least fit chromosomes with the mutated child
        least_fit_indices = sorted(range(len(chromosomePopulation.chromosomes)), key=lambda x: chromosomePopulation.fitness(chromosomePopulation.chromosomes[x]))[:2]
        for index in least_fit_indices:
            chromosomePopulation.chromosomes[index] = mutated_child

        # Print the current population for inspection
        print(f"Generation {generation + 1} - Chromosomes:")
        for i, chromosome in enumerate(chromosomePopulation.chromosomes):
            print(f"Chromosome {i + 1}: {chromosome.gene} (Fitness: {chromosomePopulation.fitness(chromosome)})")

    print("Failed to achieve the target chromosome within the specified generations.")
    return None

# Target chromosome to match
target_chromosome = "100110101110111110111010"

# Set the population size and run the genetic algorithm
result = genetic_algorithm(target_chromosome, population_size=100)

# Print the final result for inspection
if result:
    print(f"Final Chromosome: {result.gene}")
