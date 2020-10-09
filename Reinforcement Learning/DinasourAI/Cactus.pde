class Cactus extends Obstacle {

  // Object Constructor (Used in Setup function)
  public Cactus(float groundZero, float speedFlow) {
    super(groundZero, speedFlow);

    this.speedFlow = speedFlow;
    switch((int)random(4)) {
    case 0: 
      img = loadImage("Cactus\\cactus_1.png");
      break;
    case 1: 
      img = loadImage("Cactus\\cactus_2.png"); 
      break;
    case 2: 
      img = loadImage("Cactus\\cactus_3.png"); 
      break;
    case 3: 
      img = loadImage("Cactus\\cactus_4.png"); 
      break;
    case 4:
      img = loadImage("Cactus\\cactus_5.png"); 
      break;
    }
    float sizeDimention = random(0.3, 0.65);
    this.size = new PVector(img.width * sizeDimention, img.height * sizeDimention);
    this.location = new PVector(width + size.x, groundZero - size.y);
  }
}
