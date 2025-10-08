# src/operators.py
import random
import copy # Make sure to add this import at the top

# ... (imports from before remain the same) ...
from src.core import FormulaTree, Node
from src.fitness import calculate_fitness
from src.tree_generator import create_random_tree
from src.utils import load_data

# ... (tournament_selection function remains the same) ...
def tournament_selection(population: list, fitnesses: list, k: int = 3):
    tournament_indices = random.sample(range(len(population)), k)
    best_index_in_tournament = min(tournament_indices, key=lambda index: fitnesses[index])
    return population[best_index_in_tournament]

# NEW CODE STARTS HERE ▼▼▼

def _get_all_nodes(current_node: Node):
    """A recursive helper to get a flat list of all nodes in a tree."""
    nodes = [current_node]
    for child in current_node.children:
        nodes.extend(_get_all_nodes(child))
    return nodes

def crossover(parent1: FormulaTree, parent2: FormulaTree):
    """
    Performs crossover between two parent trees to produce two children.

    Args:
        parent1: The first parent FormulaTree.
        parent2: The second parent FormulaTree.

    Returns:
        A tuple containing two new child FormulaTree objects.
    """
    # Use deepcopy to ensure original parents are not modified
    child1 = copy.deepcopy(parent1)
    child2 = copy.deepcopy(parent2)

    # Get a list of all nodes from each child
    nodes1 = _get_all_nodes(child1.root)
    nodes2 = _get_all_nodes(child2.root)

    # Select a random node from each tree to be the crossover point
    crossover_point1 = random.choice(nodes1)
    crossover_point2 = random.choice(nodes2)

    # Swap the values and children of the selected nodes
    crossover_point1.value, crossover_point2.value = crossover_point2.value, crossover_point1.value
    crossover_point1.children, crossover_point2.children = crossover_point2.children, crossover_point1.children
    
    return child1, child2


# --- Update the test code at the bottom of the file ---
if __name__ == "__main__":
    # ... (Verification for Task 2 remains the same) ...
    print("\n" + "-"*20 + "\n") # Separator
    
    print("--- Day 4, Task 3 Verification ---")
    
    # 1. Create two distinct parents to see the crossover clearly
    p1_root = Node('+', children=[Node('x'), Node(10)])
    parent1 = FormulaTree(p1_root)
    
    p2_root = Node('*', children=[Node(5.5), Node(-2.0)])
    parent2 = FormulaTree(p2_root)

    print(f"Parent 1: {parent1}")
    print(f"Parent 2: {parent2}")

    # 2. Perform crossover
    child1, child2 = crossover(parent1, parent2)
    
    print("\n--- After Crossover ---")
    print(f"Child 1: {child1}")
    print(f"Child 2: {child2}")
    print("\nNote: Your child formulas will be different due to random crossover points.")