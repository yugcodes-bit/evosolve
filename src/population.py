# src/population.py
from src.core import Node, FormulaTree

class Population:
    """
    Manages a collection of FormulaTree individuals.
    """
    def __init__(self, size: int):
        """
        Initializes a population of a given size.

        Args:
            size: The number of individuals in the population.
        """
        self.size = size
        self.individuals = []
        self._create_initial_population()

    def _create_initial_population(self):
        # TODO: This is a temporary placeholder!
        # Later, this will generate random, unique trees.
        # For now, we'll create identical simple trees to test the structure.
        
        # A simple placeholder formula: y = x + 1
        node_x = Node('x')
        node_one = Node(1.0)
        node_add = Node('+', children=[node_x, node_one])
        placeholder_tree = FormulaTree(root=node_add)
        
        for _ in range(self.size):
            # In a real scenario, we'd create a deep copy of the tree
            self.individuals.append(placeholder_tree)

# --- Test code to make sure it works ---
if __name__ == "__main__":
    print("--- Day 3, Task 3 Verification ---")
    
    population_size = 10
    population = Population(size=population_size)

    print(f"Population created with {len(population.individuals)} individuals.")
    print(f"The first individual is: {population.individuals[0]}")
    print(f"The last individual is: {population.individuals[-1]}")