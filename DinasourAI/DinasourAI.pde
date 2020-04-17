// Global variables
private float groundZero;
private float speedFlow;
private ArrayList<Dirt> dirts;
private Dinasour dinasour;

void setup() {
  // Initialize windows Interface
  smooth();
  size(900, 360);
  background(255);

  // Initialize environmental variables
  groundZero = 240.0;
  speedFlow = 7.0;
  dirts = new ArrayList<Dirt>();
  dinasour = new Dinasour(groundZero, speedFlow);
}

void draw() {
  // Reset background on draw
  background(255);
  
  dinasour.run();
  drawGroundZero(groundZero);


  // Dirty part
  if (random(1) < 0.07)
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
