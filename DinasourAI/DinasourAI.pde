float groundZero;

void setup() {
  // Initialize windows Interface
  smooth();
  size(900, 360);
  background(255);

  // Initialize variables
  groundZero = 240;
}

void draw() {
  drawGroundZero(groundZero);
}

// A Ground Zero from the sketch 
void drawGroundZero(float groundZero) {
  stroke(0);
  strokeWeight(2);
  line(0, groundZero, width, groundZero);
}
