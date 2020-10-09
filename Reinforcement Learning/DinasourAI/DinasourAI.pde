// Global variables
private float groundZero;
private float speedFlow;
private ArrayList<Dirt> dirts;
private ArrayList<Obstacle> obstacles;
private Population population;
private Dinasour dinasour;
private float cactusChance, birdChance;

void setup() {
  // Initialize windows Interface
  smooth();
  size(900, 360);
  background(255);

  // Initialize environmental variables
  groundZero = 270.0;
  speedFlow = 5.0;
  dirts = new ArrayList<Dirt>();
  obstacles = new ArrayList<Obstacle>();
  population = new Population(50, groundZero);  // Create a population
  this.cactusChance = 0.03;
  this.birdChance = 0.01;

  obstacles.add(new Cactus(groundZero, speedFlow));  // A cactus at the beginning
}

void draw() {  
  background(255);              // Reset background on draw
  info();                       // Display game information
  drawGroundZero(groundZero);   // Draw Ground Zero

  population.run(obstacles);

  // Add cactuses
  if (random(1) < cactusChance && obstacles.size() != -1 && width - obstacles.get(obstacles.size() - 1).getLocation().x > 150)
    obstacles.add(new Cactus(groundZero, speedFlow));

  // Add birds
  if (random(1) < birdChance && obstacles.size() != -1 && width - obstacles.get(obstacles.size() - 1).getLocation().x > 150)
    obstacles.add(new Bird(groundZero, speedFlow));

  // Run obstacles
  for (int i = obstacles.size() - 1; i >= 0; i--) {
    obstacles.get(i).run();  // Run move(), display()

    // Remove if out of sight
    if (!obstacles.get(i).inPage())
      obstacles.remove(i);
  }

  // Add dirts
  if (random(1) < 0.08)
    dirts.add(new Dirt(speedFlow, groundZero));

  // Run dirts
  for (int i = dirts.size() - 1; i >= 0; i--) {
    dirts.get(i).run();  // Run move(), display()        
    if (!dirts.get(i).inPage())  // Remove if out of sight
      dirts.remove(i);
  }
  
  // Let's make it more challenging over time
  speedFlow += 0.002;
  cactusChance += 0.00003;
  birdChance += 0.00001;
}

// A Ground Zero from the sketch
void drawGroundZero(float groundZero) {
  stroke(0);
  strokeWeight(2);
  line(0, groundZero, width, groundZero);
}

// Manual hop function
void keyPressed() {
  if (keyCode == UP)
    dinasour.hop();
}

public void info() {
  fill(0);
  text("Developed by: Keivan Ipchi Hagh", width - 190, 20);
  text("Generation: " + population.generation, 10, 20);
}
