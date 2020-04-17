class Bird extends Obstacle {

  // Object fields
  private int frameIndex;
  private PImage pos1, pos2;

  // Object Constructor (Used in Setup function)
  public Bird(float groundZero, float speedFlow) {
    super(groundZero, speedFlow);

    this.speedFlow = speedFlow;
    pos1 = loadImage("Bird\\bird_1.png");
    pos2 = loadImage("Bird\\bird_2.png");
    
    switch((int)random(2)) {
    case 0: 
      this.img = pos1;
      break;
    case 1: 
      this.img = pos1;
      break;
    }
    
    float sizeDimention = random(0.2, 0.5);
    this.size = new PVector(img.width * sizeDimention, img.height * sizeDimention);
    this.location = new PVector(width + size.x, groundZero - size.y - random(5, 40));
    this.frameIndex = 0;
  }

  // Displays the object
  public void display() {

    if (frameIndex >= 0 && frameIndex < 5)
      img = pos2;
    else if (frameIndex >= 5 && frameIndex < 10)
      img = pos1;

    frameIndex++; //<>//
    if (frameIndex == 10)
      frameIndex = 0;

    img.resize((int)size.x, (int)size.y);
    image(img, location.x, location.y + 5);
  }
}
