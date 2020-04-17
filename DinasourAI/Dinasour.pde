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
  private PImage pos1, pos2, pos3;
  public float DNA;
  public float fitness;
  public boolean isHit;

  // Object Constuctor
  public Dinasour(float groundZero, float DNA) {
    this.groundZero = groundZero;
    this.img = loadImage("T-Rex\\Trex_3.png");
    this.size = new PVector(img.width * 0.75, img.height * 0.75);
    this.location = new PVector(width / 10, groundZero - size.y);
    this.velocity = new PVector(speedFlow, 0);
    this.acceleration = new PVector(0, 0);
    this.gravity = new Gravity();
    this.frameIndex = 0;
    this.DNA = DNA;
    this.isHit = false;

    this.pos1 = loadImage("T-Rex\\Trex_1.png");
    this.pos2 = loadImage("T-Rex\\Trex_2.png");
    this.pos3 = loadImage("T-Rex\\Trex_3.png");
  }

  // Encapsulates all methods
  public void run(ArrayList<Obstacle> obstacles) {

    if (mustHop(obstacles))  // Hop if in sight
      hop();

    this.score(obstacles);  // Calculate fitness
    this.applyForce(gravity.getForce());
    this.move();
    this.display();
  }

  // Decides for the dinasour whether to jump or not
  private boolean mustHop(ArrayList<Obstacle> obstacles) {
    for (Obstacle obstacle : obstacles)
      if (abs(obstacle.getLocation().x - this.location.x) < DNA)
        return true;
    return false;
  }

  // Checks if obstacle has passed or not
  public void score(ArrayList<Obstacle> obstacles) {
    for (Obstacle obstacle : obstacles)
      if (this.location.x > obstacle.getLocation().x + obstacle.getSize().x)
        fitness++;
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
    if (!isHit) {  // If object has not crashed yet
      if (location.y + size.y < groundZero)
        img = pos3;
      else if (frameIndex >= 0 && frameIndex < 5)
        img = pos2;
      else if (frameIndex >= 5 && frameIndex < 10)
        img = pos1;    

      img.resize((int)size.x, (int)size.y);

      frameIndex++;
      if (frameIndex == 10)
        frameIndex = 0;

      image(img, location.x, location.y + 5);
    }
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
