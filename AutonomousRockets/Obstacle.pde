// Keivan Ipchi Hagh

// Obstacle class, pretty straight forward
class Obstacle {

  PVector location;
  float w, h;

  Obstacle(PVector location, float w, float h) {
    this.location = location.get();
    this.w = w;
    this.h = h;
  }

  void display() {
    stroke(0);
    fill(175);
    strokeWeight(2);
    rectMode(CORNER);
    rect(location.x, location.y, w, h);
  }

  boolean contains(PVector agent) {
    if (agent.x > location.x && agent.x < location.x + w && agent.y > location.y && agent.y < location.y + h)
      return true;
    else
      return false;
  }
}
