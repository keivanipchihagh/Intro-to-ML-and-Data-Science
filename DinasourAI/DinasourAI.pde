// Global variables
private float groundZero;
private float speedFlow;
private ArrayList<Dirt> dirts;
private ArrayList<Obstacle> obstacles;
private Dinasour dinasour;

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
  dinasour = new Dinasour(groundZero);
  
  obstacles.add(new Obstacle(groundZero, speedFlow)); 
}

void draw() {
  // Reset background on draw
  background(255);

  dinasour.run();
  drawGroundZero(groundZero);

  // Obstacles
  if (random(1) < 0.03 && (width - obstacles.get(obstacles.size() - 1).getLocation().x > 150))
    obstacles.add(new Obstacle(groundZero, speedFlow)); 
  for (int i = obstacles.size() - 1; i >= 0; i--) {
    obstacles.get(i).run();
    if (!obstacles.get(i).inPage())
      obstacles.remove(i);
    if (obstacles.get(i).isCollision(dinasour.getLocation(), dinasour.getSize()))
      noLoop();
  }

  // Dirts
  if (random(1) < 0.08)
    dirts.add(new Dirt(speedFlow, groundZero));
  for (int i = dirts.size() - 1; i >= 0; i--) {
    dirts.get(i).run();
    if (!dirts.get(i).inPage())
      dirts.remove(i);
  }
}

// A Ground Zero from the sketch
void drawGroundZero(float groundZero) {
  stroke(0);
  strokeWeight(2);
  line(0, groundZero, width, groundZero);
}

// Manual hop function
void keyPressed() {
  if (key == ' ')
    dinasour.hop();
}
