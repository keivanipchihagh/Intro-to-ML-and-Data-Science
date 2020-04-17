class Gravity {
  
  private PVector coefficient;
  
  public Gravity() {
    this.coefficient = new PVector(0, 2.5);
  }
  
  public PVector getForce() {
   return coefficient; 
  }
}
