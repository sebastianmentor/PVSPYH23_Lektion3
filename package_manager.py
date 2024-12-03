import random

class Environment:
    def __init__(self, grid_size=5):
        self.grid_size = grid_size
        self.grid = [[random.choice(["empty", "package", "dock", "charger"]) 
                      for _ in range(grid_size)] for _ in range(grid_size)]
        self.robot_position = (random.randint(0, grid_size-1), random.randint(0, grid_size-1))
        self.robot_battery = "hög"
        self.robot_has_package = False

    def get_percept(self):
        x, y = self.robot_position
        return {
            "current_cell": self.grid[x][y],
            "battery": self.robot_battery,
            "has_package": self.robot_has_package
        }

    def perform_action(self, action):
        x, y = self.robot_position
        
        if action == "pick up":
            if self.grid[x][y] == "package":
                self.grid[x][y] = "empty"
                self.robot_has_package = True
        elif action == "deliver":
            if self.grid[x][y] == "dock" and self.robot_has_package:
                self.robot_has_package = False
        elif action == "charge":
            if self.grid[x][y] == "charger":
                self.robot_battery = "hög"
        elif action in ["up", "down", "left", "right"]:
            if action == "up" and x > 0:
                self.robot_position = (x-1, y)
            elif action == "down" and x < self.grid_size-1:
                self.robot_position = (x+1, y)
            elif action == "left" and y > 0:
                self.robot_position = (x, y-1)
            elif action == "right" and y < self.grid_size-1:
                self.robot_position = (x, y+1)
        
        # Batteriet förbrukas
        if random.random() < 0.2:  # 20% chans att batteriet går från "hög" till "låg"
            self.robot_battery = "låg"

    def __str__(self):
        grid_view = ""
        for i, row in enumerate(self.grid):
            grid_view += " ".join(row) + "\n"
        return f"Rutnät:\n{grid_view}Robotens position: {self.robot_position}, Batteri: {self.robot_battery}, Har paket: {self.robot_has_package}"
