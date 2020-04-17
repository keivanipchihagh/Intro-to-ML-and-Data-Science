class Population {

  private ArrayList<Dinasour> dinasours;
  private int hitCount;
  private float maxFitness;
  public int generation;

  public Population(int populationCount, float groundZero) {
    this.dinasours = new ArrayList<Dinasour>();
    hitCount = 0;
    maxFitness = 0;
    generation = 0;

    for (int i = 0; i < populationCount; i++)
      dinasours.add(new Dinasour(groundZero, random(width)));
  }

  public void run(ArrayList<Obstacle> obstacles) {
    for (Dinasour dinasour : dinasours)
      dinasour.run(obstacles);

    // Check for collision & Remove the wasted dinasours
    for (Obstacle obstacle : obstacles)
      for (Dinasour dinasour : dinasours)
        if (obstacle.isCollision(dinasour.getLocation(), dinasour.getSize()) && !dinasour.isHit) {
          dinasour.isHit = true;
          hitCount++;
        }

    // If the entire generation fails, Set  max fitness
    if (hitCount == dinasours.size()) {      
      for (Dinasour dinasour : dinasours)
        if (dinasour.fitness >= maxFitness)
          maxFitness = dinasour.fitness;
      generate();  // Generate a new generation
      hitCount = 0;  // Reset hit count
    }
  }

  // Accept Reject Algorithm
  Dinasour acceptReject(float maxFitness) { 
    int safe = 0;  // In we couldn't find the appropriate parent, then giveup (Throw error)
    while (safe < 1000) {

      Dinasour partner = dinasours.get((int)random(dinasours.size()));  // Choose a random Rocket
      float prob = random(maxFitness);

      if (prob < partner.fitness)
        return partner;

      safe++;
    }
    return null;
  }

  // selection
  void generate() {
    ArrayList<Dinasour> new_dinasours = new ArrayList<Dinasour>();

    for (int i = 0; i < dinasours.size(); i++) {

      // Choose two fittest parents' DNAs
      float parent1_DNA = acceptReject(maxFitness).DNA;
      float parent2_DNA = acceptReject(maxFitness).DNA;

      float child_DNA = (parent1_DNA + parent2_DNA) / 3;  // Inherit genes
      child_DNA += random(20) - 10;  // Mutation

      new_dinasours.add(new Dinasour(groundZero, child_DNA));
    }
    dinasours = new_dinasours;  // Replace the old generation with the new one
    generation++;
  }
}
