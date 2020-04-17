class Dinasour {

  // Object fields
  private float groundZero;
  private float speedFlow;
  private PVector size;
  private PVector location;
  private PVector velocity;
  private PVector acceleration;
  private Gravity gravity;

  // Object Constuctor
  public Dinasour(float groundZero, float speedFlow) {
    this.groundZero = groundZero;
    this.speedFlow = speedFlow;
    this.size = new PVector(30, 60);
    this.location = new PVector(width / 10, groundZero - size.y);
    this.velocity = new PVector(0, 0);
    this.acceleration = new PVector(0, 0);
    this.gravity = new Gravity();
  }

  // Encapsulates the methods
  public void run() {
    this.applyForce(gravity.getForce());
    this.move();
    this.display();
  }

  // Makes the dinasour jump
  public void hop() {
    if (location.y + size.y == groundZero)
      acceleration.y = -60;
  }

  // Apply force method
  private void applyForce(PVector force) {
    this.acceleration.add(force);
  }

  // Moves the object across the sketch
  public void move() {    
    velocity.add(acceleration);
    velocity.mult(0.87);

    location.add(velocity);
    if (location.y + size.y > groundZero)
      location.y = groundZero - size.y;

    acceleration.mult(0);
  }

  // Displays the object
  public void display() {
    noStroke();
    fill(0);
    rect(location.x, location.y, size.x, size.y, 5);
  }
}
