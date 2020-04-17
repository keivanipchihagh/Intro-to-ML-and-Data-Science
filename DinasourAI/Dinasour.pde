class Dinasour {

  // Object fields
  private float groundZero;
  private PVector size;
  private PVector location;
  private PVector velocity;
  private PVector acceleration;
  private Gravity gravity;
  private int frameIndex;
  private PImage img;

  // Object Constuctor
  public Dinasour(float groundZero) {
    this.groundZero = groundZero;
    this.img = loadImage("T-Rex\\Trex_1.png");
    this.size = new PVector(img.width * 0.75, img.height * 0.75);
    this.location = new PVector(width / 10, groundZero - size.y);
    this.velocity = new PVector(speedFlow, 0);
    this.acceleration = new PVector(0, 0);
    this.gravity = new Gravity();
    this.frameIndex = 0;
    this.img = null;
  }

  // Encapsulates all methods
  public void run() {
    this.applyForce(gravity.getForce());
    this.move();
    this.display();
  }

  // Makes the dinasour jump
  public void hop() {
    if (location.y + size.y == groundZero)
      acceleration.y = -35;
  }

  // Apply force method
  private void applyForce(PVector force) {
    this.acceleration.add(force);
  }

  // Moves the object across the sketch
  public void move() {    
    velocity.add(acceleration);
    velocity.mult(0.9);

    location.add(velocity);
    if (location.y + size.y > groundZero)
      location.y = groundZero - size.y;

    acceleration.mult(0);
  }

  // Displays the object
  public void display() {

    if (location.y + size.y < groundZero)
      img = loadImage("T-Rex\\Trex_3.png");
    else if (frameIndex >= 0 && frameIndex < 5)
      img = loadImage("T-Rex\\Trex_2.png");
    else if (frameIndex >= 5 && frameIndex < 10)
      img = loadImage("T-Rex\\Trex_1.png");

    img.resize((int)size.x, (int)size.y);

    frameIndex++;
    if (frameIndex == 10)
      frameIndex = 0;

    image(img, location.x, location.y + 5);
  }
  
  // Getter: Velocity
  public PVector getVelocity() {
    return this.velocity;
  }
  
  // Getter: Location
  public PVector getLocation() {
    return this.location;
  }
  
  // Getter: Size
  public PVector getSize() {
    return this.size;
  }
}
