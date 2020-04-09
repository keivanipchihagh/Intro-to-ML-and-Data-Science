int lifetime;  // How long should each generation live

Population population;  // Population

int lifeCounter;          // Timer for cycle of generation

Obstacle target;        // Target position

ArrayList<Obstacle> obstacles;  // An array list to keep track of all the obstacles!

void setup() {
  size(640, 360);
  // The number of cycles we will allow a generation to live
  lifetime = height;

  // Initialize variables
  lifeCounter = 0;

  target = new Obstacle(new PVector(width / 2 - 12, 24), 24, 24);


  // Create a population with a mutation rate, and population max
  float mutationRate = 0.01;
  population = new Population(mutationRate, 100, lifetime, target);

  // Create the obstacle course  
  obstacles = new ArrayList<Obstacle>();
  obstacles.add(new Obstacle(new PVector(width / 2 - 100, height / 2), 200, 10));
}

void draw() {
  background(255);

  // Draw the start and target positions
  fill(0);

  // If the generation hasn't ended yet
  if (lifeCounter < lifetime) {
    population.live(obstacles);
    lifeCounter++;
    // Otherwise a new generation
  } else {
    lifeCounter = 0;

    population.calculateFitness();
    population.generate();
  }

  // Draw the obstacles
  for (Obstacle obs : obstacles) {
    obs.display();
  }
  
  target.display();

  // Display some info
  fill(0);
  text("Generation #: " + population.getGenerations(), 10, 18);
  text("Cycles left: " + (lifetime-lifeCounter), 10, 36);
}

// Move the target if the mouse is pressed
// System will adapt to new target
void mousePressed() {
  target.location.x = mouseX;
  target.location.y = mouseY;
}
