class Obstacle {

  // Object fields
  protected PVector location;
  protected PVector size;
  protected float speedFlow;
  protected PImage img;

  public Obstacle(float groundZero, float speedFlow) { }

  // Encapsulates all methods
  protected void run() {
    this.move();
    this.display();
  }

  // Moves the dirt
  protected void move() {
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
    return (din_location.y + din_size.y - 25 >= location.y && (din_location.x + din_size.x >= location.x && din_location.x <= location.x + size.x)) ? true : false;
  }

  // Getter: Location
  public PVector getLocation() {
    return this.location;
  }
}
