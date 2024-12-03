import random

# Definiera miljön
class Environment:
    def __init__(self):
        # Två rum: A och B
        self.rooms = {"A": random.choice(["rent", "smutsigt"]),
                      "B": random.choice(["rent", "smutsigt"]),
                      "C": random.choice(["rent", "smutsigt"])}
        self.agent_location = random.choice(['A', 'B', 'C'])

    def get_percept(self):
        return self.rooms[self.agent_location]

    def perform_action(self, action):
        if action == "clean":
            self.rooms[self.agent_location] = "rent"
        elif action == "right":
            self.agent_location = "C" if self.agent_location == "B" else "B"

        elif action == "left":
            self.agent_location = "A" if self.agent_location == "B" else "B"

    def __str__(self):
        return f"Rum: {self.rooms}, Agentens plats: {self.agent_location}"

# Reflexagent
class ReflexAgent:
    def decide_action(self, percept):
        if percept == "smutsigt":
            return "clean"
        else:
            if environment.agent_location == "A":
                return "right"
            
            elif environment.agent_location == "B":
                return random.choice(['right', 'left'])
            
            return "left"

# Huvudprogram
environment = Environment()
agent = ReflexAgent()

print("Starttillstånd:")
print(environment)

for step in range(10):
    print(f"\nSteg {step + 1}:")
    percept = environment.get_percept()
    print(f"Percept: {percept}")
    action = agent.decide_action(percept)
    print(f"Handling: {action}")
    environment.perform_action(action)
    print(environment)
