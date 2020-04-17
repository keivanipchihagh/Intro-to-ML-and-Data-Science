class Obstacle {

  // Object fields
  private PVector location;
  private PVector size;
  private float groundZero;
  private float speedFlow;
  private PImage img;

  // Object Constructor (Used in Setup function)
  public Obstacle(float groundZero, float speedFlow) {
    this.groundZero = groundZero;
    this.speedFlow = speedFlow;    
    switch((int)random(4)) {
    case 0: 
      img = loadImage("Obstacle\\obstacle_1.png"); 
      break;
    case 1: 
      img = loadImage("Obstacle\\obstacle_2.png"); 
      break;
    case 2: 
      img = loadImage("Obstacle\\obstacle_3.png"); 
      break;
    case 3: 
      img = loadImage("Obstacle\\obstacle_4.png"); 
      break;
    case 4: 
      img = loadImage("Obstacle\\obstacle_5.png"); 
      break;
    }
    this.size = new PVector(img.width * 0.75, img.height * 0.75);
    this.location = new PVector(width + size.x, groundZero - size.y);
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
  public boolean inPage() {
    return (this.location.x + size.x < 0) ? false : true;
  }

  // Displays the object
  public void display() {
    img.resize((int)size.x, (int)size.y);
    image(img, location.x, location.y + 5);
  }

  // Checks whether player haa crashed or not
  public boolean isCollision(PVector din_location, PVector din_size) {
    if (din_location.y + din_size.y >= location.y + size.y && (din_location.x + din_size.x >= location.x && ))
      return true;
    else
      return false;
  }

  // Getter: Location
  public PVector getLocation() {
    return this.location;
  }
}
