class Gravity {
  
  private PVector coefficient;
  
  public Gravity() {
    this.coefficient = new PVector(0, 1);
  }
  
  public PVector getForce() {
   return coefficient; 
  }
}
