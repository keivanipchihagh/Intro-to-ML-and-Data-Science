// Keivan Ipchi Hagh //<>//
// NOC - Chapter 9 - Generic Algorithms

// Population class, describes a collection of agents and methods to manipulate their data structures
class Population {

  // A floating point which describes the mutation rate of each DNA
  float mutationRate;

  // Array of rockets
  Rocket[] population;

  // Current number of generations
  int generations;  

  // Maximum fitness (Best score)
  float maxFitness;

  // Life time describes the number of genes each DNA contains
  int lifetime;

  // Target location
  Obstacle target;

  // Mating pool of rockets
  ArrayList<Rocket> matingPool;

  // #1 Population Constructor
  Population(float mutationRate, int populationCount, int lifetime, Obstacle target) {

    // Initialize fields
    generations = 0;
    this.mutationRate = mutationRate;
    this.lifetime = lifetime;
    this.target = target;
    matingPool = new ArrayList<Rocket>();

    population = new Rocket[populationCount];

    // Initialize rockets
    for (int i = 0; i < population.length; i++)
      population[i] = new Rocket(new PVector(width / 2, height + 20), new DNA(lifetime));

    // Calculate maxumim fitness (Obviously fitnesses are all '0' at this point, but anyway)
    maxFitness = getMaxFitness();
  }

  // Get number of generations
  int getGenerations() {
    return generations;
  }

  // Live, wraps all the methods we want to call
  void live (ArrayList<Obstacle> obstacles) {
    // Run every rocket
    for (int i = 0; i < population.length; i++) {
      population[i].run(obstacles);
    }
  }

  // selection
  void generate() {

    float maxFitness = getMaxFitness();

    Rocket[] newPopulation = new Rocket[population.length];
    for (int i = 0; i < population.length; i++) {

      // Choose two fittest parents' DNAs
      DNA parent1_DNA = acceptReject(maxFitness).dna;
      DNA parent2_DNA = acceptReject(maxFitness).dna;

      DNA child_DNA = parent1_DNA.crossover(parent2_DNA);  // Inherit genes
      child_DNA.mutate(mutationRate);  // Mutate genes

      newPopulation[i] = new Rocket(new PVector(width / 2, height + 20), child_DNA);
    }
    population = newPopulation;  // Replace the old generation with the new one
    generations++;
  }

  // Accept Reject algorithm for calculating weighted probability
  Rocket acceptReject(float maxFitness) {        
    int safe = 0;  // In we couldn't find the appropriate parent, then giveup (Throw error)
    while (safe < 1000) {

      Rocket partner = population[(int)random(population.length)];  // Choose a random Rocket
      float prob = random(maxFitness);

      if (prob < partner.getFitness())
        return partner;

      safe++;
    }
    return null;
  }

  // Calculate fitness for each rocket object
  void calculateFitness() {
    for (int i = 0; i < population.length; i++) {
      population[i].calculateFitness(target);
    }
  }    

  // Get maximum fitnesss
  float getMaxFitness() {
    float record = 0;
    for (int i = 0; i < population.length; i++) {
      if (population[i].getFitness() > record) {
        record = population[i].getFitness();
      }
    }
    return record;
  }
}
