class Dirt {

  // Object fields
  private float speedFlow;
  private PVector location;
  private float len;
  private float thickness;

  // Object Constructor
  public Dirt(float speedFlow, float groundZero) {
    this.speedFlow = speedFlow;
    this.location = new PVector(width, random(groundZero + 5, groundZero + 100));
    this.len = random(1, 10);
    this.thickness = random(1, 2);
  }

  // Encapsulates the methods
  public void run() {
    this.move();
    this.display();
  }

  // Moves the dirt
  private void move() {
    this.location.x += (-speedFlow);
  }

  // Displays the object
  private void display() {
    stroke(0);
    strokeWeight(thickness);
    line(location.x, location.y, location.x + len, location.y);
  }

  // Indicates whether dirt is in the page coordinates or not
  public boolean inPage() {
    return (this.location.x < 0) ? false : true;
  }
}
