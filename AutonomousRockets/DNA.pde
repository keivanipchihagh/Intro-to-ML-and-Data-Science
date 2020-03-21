// Keivan Ipchi Hagh
// NOC - Chapter 9 - Generic Algorithms

// DNA contains array of vectors that lead to the desired target - Genotype
class DNA {

  // Array of vectors
  PVector[] genes;
  
  // Maximum strength of the vector force
  float maxForce;

  // #1 DNA Constructor
  DNA (int lifetime) {
    
    // Initialize fields
    genes = new PVector[lifetime];
    maxForce = 0.1;
    
    // Initialize gene vectors
    for (int i = 0; i < genes.length; i++) {
      genes[i] = PVector.random2D();
      genes[i].mult(random(0, maxForce));
    }
  }  

  // #2 DNA Constructor - Based on existing genes
  DNA (PVector[] genes) {
    this.genes = genes;
  }

  // Crossover, creates a new genes array using the two parents
  DNA crossover(DNA partner) {

    int midPoint = (int)random(genes.length);  // Random location in genes array
    DNA child = new DNA(genes.length);  // Create child DNA

    // Inherit from patner and self
    for (int i = 0; i < genes.length; i++)
      if (i < midPoint)
        child.genes[i] = this.genes[i];
      else
        child.genes[i] = partner.genes[i];
        
    return child;
  }
  
  // Mutate genes based on the given probability
  void mutate(float mutationRate) {
    for (int i = 0; i < genes.length; i++)
      if (random(1) < mutationRate) {
        this.genes[i] = PVector.random2D();
        this.genes[i].mult(random(0, maxForce));
      }
  }
}
