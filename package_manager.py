import random

EMOJI = {"empty":"⬜",
         "package":"📦",
         "charger":"🔌",
         "dock":"📮"}

# 🔌 📦 󠀠󠀠󠀠⬜ 📮

class Environment:
    def __init__(self, grid_size=10):
        self.grid_size = grid_size
        self.grid = [[random.choice(["empty", "package"]) 
                      for _ in range(grid_size)] for _ in range(grid_size)]
        
        self.grid[0][0] = "charger"
        self.grid[-1][-1] = "dock"

        self.robot_position = (random.randint(0, grid_size-1), random.randint(0, grid_size-1))
        self.robot_battery = "hög"
        self.robot_has_package = False

        self.nr_of_package = sum([1 for row in self.grid for item in row if item == "package"])
        

    def get_percept(self):
        x, y = self.robot_position
        return {
            "current_cell": self.grid[x][y],
            "battery": self.robot_battery,
            "has_package": self.robot_has_package,
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

    # def print_grid(self):
    #     for row in self.grid:
    #         for col in row:
    #             print(f"{col:<9}", end="")
    #         print()

    def print_grid(self):
        for row in self.grid:
            for col in row:
                print(EMOJI[col], end="")
            print()

    def __str__(self):
        self.print_grid()
        return f"Robotens position: {self.robot_position}, Batteri: {self.robot_battery}, Har paket: {self.robot_has_package}"
    


# Reflexagent
class ReflexAgent:
    def decide_action(self, percept):
        if percept['battery'] == "låg":
            if percept['current_cell'] == "charger":
                return "charge"
            
            return random.choice(["up", "left"])


        elif percept['has_package'] == True:
            if percept['current_cell'] == "dock":
                return "deliver"
            
            return random.choice(["down", "right"])


        elif percept['current_cell'] in ["empty", "charger", "dock"]:
            return random.choice(["up", "down", "left", "right"])


        elif percept['current_cell'] == "package":            
            return "pick up"
        
print("START")
environment = Environment()
print(environment)
agent = ReflexAgent()
print("*"*20)
step = 1
while True:
    input("Run 50") 
    for i in range(50):
        percept = environment.get_percept()
        action = agent.decide_action(percept)
        environment.perform_action(action)
    step+=50
    print(f"Efter {step} steg: ")
    print(environment)
