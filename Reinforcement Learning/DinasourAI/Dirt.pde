class Dirt {

  // Object fields
  private float speedFlow;
  private PVector location;
  private float groundZero;
  private PVector size;

  // Object Constructor
  public Dirt(float speedFlow, float groundZero) {
    this.speedFlow = speedFlow;
    this.groundZero = groundZero;
    size = new PVector(random(1, 10), random(1, 2));
    this.location = new PVector(width, random(groundZero + size.x, groundZero + 100));
  }

  // Encapsulates all methods
  private void run() {
    this.move();
    this.display();
  }

  // Moves the dirt
  private void move() {
    this.location.x += (-speedFlow);
  }

  // Indicates whether dirt is in the page coordinates or not
  private boolean inPage() {
    return (this.location.x < 0) ? false : true;
  }

  // Displays the object
  public void display() {
    stroke(0);
    strokeWeight(size.y);
    line(location.x, location.y, location.x + size.x, location.y);
  }
}
