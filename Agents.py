import random  
from game import Agent
from game import Directions
class DumbAgent(Agent):
 def getAction(self, state):
    print("Location: ", state.getPacmanPosition())
    print("Actions available: ", state.getLegalPacmanActions())
    if Directions.EAST in state.getLegalPacmanActions():
            print("Going East.")
            return Directions.EAST
    else:
             print("Stopping.")
    return Directions.STOP
class RandomAgent(Agent):  
    def getAction(self, state):  
        # Get the current position of Pacman  
        print("Location: ", state.getPacmanPosition())  
        
        # Get the legal actions available to Pacman  
        legalActions = state.getLegalPacmanActions()  
        print("Actions available: ", legalActions)  
        
        # If there are no legal actions, return STOP  
        if not legalActions:  
            print("No legal actions available. Stopping.")  
            return Directions.STOP  
        
        # Choose a random action from the available legal actions  
        action = random.choice(legalActions)  
        print(f"Chosen action: {action}")  
        
        return action
class BetterRandomAgent(Agent):  
    def getAction(self, state):  
        print("Location: ", state.getPacmanPosition())  # Optional: for debugging  
        legalActions = state.getLegalPacmanActions()  
        print("Actions available: ", legalActions)  # Optional: for debugging  

        # Filter out the STOP action  
        legalActions = [action for action in legalActions if action != Directions.STOP]  

        if not legalActions:  
            print("No legal actions available. Defaulting to a random action.")  # Optional: for debugging  
            return Directions.STOP  # Handle the situation where no legal actions are available  

        # Choose a random action from the filtered legal actions  
        action = random.choice(legalActions)  
        print(f"Chosen action: {action}")  # Optional: for debugging  
        return action  
class ReflexAgent(Agent):  
    def getAction(self, state):  
        legalActions = state.getLegalPacmanActions()  

        # Filter out the STOP action  
        legalActions = [action for action in legalActions if action != Directions.STOP]  

        # Check for actions that lead to food  
        food = state.getFood()  # Get the food grid  
        pacmanPosition = state.getPacmanPosition()  # Get Pacman's current position  

        # Check which legal actions lead to eating food  
        possibleFoodActions = []  
        for action in legalActions:  
            # Find the new position after taking the action  
            newPosition = state.generateSuccessor(0, action).getPacmanPosition()  
            if food[newPosition[0]][newPosition[1]]:  # Check if there's food at the new position  
                possibleFoodActions.append(action)  

        # Choose the action that leads to food if possible  
        if possibleFoodActions:  
            return random.choice(possibleFoodActions)  

        # Otherwise, choose randomly from the remaining legal actions  
        if legalActions:  
            return random.choice(legalActions)  
        
        return Directions.STOP  # If there are no legal actions left  