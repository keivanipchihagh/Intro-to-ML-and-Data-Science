// Variables
public int cols = 32;
public int rows = 32;
public Cell[][] grid;
public boolean noSolution = false;
public ArrayList<Cell> openSet;
public ArrayList<Cell> closedSet;
public ArrayList<Cell> path;

// Objects
public Cell start, end;

// Funtion: Setup
void setup() {

  // Initialize Window
  size(800, 800);
  background(255);
  smooth();

  // Initialize Array Lists & Matrix
  grid = new Cell[cols][rows];
  openSet = new ArrayList<Cell>();
  closedSet = new ArrayList<Cell>();  

  for (int i = 0; i < cols; i++)
    for (int j = 0; j < rows; j++)
      grid[i][j] = new Cell(i, j);

  for (int i = 0; i < cols; i++)
    for (int j = 0; j < rows; j++)
      grid[i][j].addNeighbors(grid);


  // Set Start & Ending Points
  start = grid[0][0];
  end = grid[cols - 1][rows - 1];

  // Start & Ending Points Cannot Be Walls
  start.wall = false;
  end.wall = false;

  // Add Starting Point To OpenSet
  openSet.add(start);
}

// Function: Draw
void draw() {

  Cell current = null;

  // If Cells Are Still In Our Check List
  if (openSet.size() > 0) {

    // Find The Cell In OpenSet With The Smallest F() 
    int index = 0;
    for (int i = 0; i < openSet.size(); i++)
      if (openSet.get(i).f < openSet.get(index).f)
        index = i;

    // Rename Selected Cell
    current = openSet.get(index);

    // Check If We Have Reached Destination
    if (current == end) {      
      println("Done.");      
      noLoop();
    }

    // Move Element From OpenSet To ClosedSet
    openSet.remove(current);
    closedSet.add(current);

    // For Each Neighbor
    for (int i = 0; i < current.neighbors.size(); i++) {

      Cell neighbor = current.neighbors.get(i);  // Get Neighbor

      // If It Has Not Been Checked Before
      if (!checkExists(neighbor, closedSet) && !neighbor.wall) {
        int tempG = current.g + 1;  // Incement Is 1, Because Matrix Is Flat Graph
                
        if (checkExists(neighbor, openSet)) {  // If Selected Cell Is In OpenSet
          if (tempG < neighbor.g)
            neighbor.g = tempG;
        } else {  // Otherwise
          neighbor.g = tempG;
          openSet.add(neighbor);
        }

        neighbor.h = heuristic(neighbor, end);  // Calculate H() 
        neighbor.f = neighbor.g + neighbor.h;   // Calculate F()
        neighbor.previous = current;  // Back-Trace
      }
    }
  } else {  // If OpenSet Is Empty
    println("No Solution.");
    noSolution = true;
    noLoop();
  }
  
  // ----------- Display ------------ //
  
  for (int i = 0; i < cols; i++)
    for (int j = 0; j < rows; j++)
      grid[i][j].display(color(255, 255, 255));

  for (int i = 0; i < closedSet.size(); i++)
    closedSet.get(i).display(color(255, 0, 0));

  for (int i = 0; i < openSet.size(); i++)
    openSet.get(i).display(color(0, 255, 0));

  // Find The Path
  Cell temp = current;
  path = new ArrayList<Cell>();
  while (!noSolution && temp.previous != null) {
    path.add(temp.previous);
    temp = temp.previous;
  }  

  for (int i = 0; i < path.size(); i++)
    path.get(i).display(color(0, 0, 255));
}

// Funtion: Check Whether The Object Exists In The Given List
public boolean checkExists(Cell neighbor, ArrayList<Cell> list) {
  for (int i = 0; i < list.size(); i++)
    if (list.get(i) == neighbor)
      return true;
  return false;
}

// Function: Return Taxi Path To The Destination
public int heuristic(Cell a, Cell b) {
  return (int)Math.abs(a.i - b.i) + Math.abs(a.j - b.j);
}

class Cell {

  // Variables
  public int f, g, h;
  public int i, j;
  public ArrayList<Cell> neighbors;
  public Cell previous;
  public boolean wall = false;   

  // Constructor
  public Cell(int i, int j) {
    neighbors = new ArrayList<Cell>();
    this.i = i;
    this.j = j;

    if (random(1) < 0.3)
      this.wall = true;
  }

  // Function: Display Cell
  public void display(color col) {    
    if (this.wall)
      fill(0);
    else
      fill(col);

    stroke(0);
    rect(this.i * (width / cols), this.j * (height / rows), (width / cols), (height / rows));
  }

  // Function: Add Near Neighbors To The List For Path Check
  public void addNeighbors(Cell[][] grid) {
    if (i < cols - 1)
      this.neighbors.add(grid[i + 1][j]);
    if (i > 0)
      this.neighbors.add(grid[i - 1][j]);
    if (j < rows - 1)
      this.neighbors.add(grid[i][j + 1]);
    if (j > 0)
      this.neighbors.add(grid[i][j - 1]);
  }
}
