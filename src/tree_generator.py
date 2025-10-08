# src/tree_generator.py
import random
from src.core import Node, FormulaTree

# Define the building blocks for our formulas
OPERATORS = ['+', '-', '*', '/']
TERMINALS = ['x']

def create_random_tree(max_depth: int, current_depth: int = 0):
    """
    Recursively creates a random formula tree.

    Args:
        max_depth: The maximum allowed depth of the tree.
        current_depth: The current depth in the recursion (used internally).

    Returns:
        A FormulaTree object.
    """
    # Base Case: If we're at the max depth, we MUST choose a terminal node.
    # Or, we can randomly choose a terminal even if we're not at max depth.
    if current_depth == max_depth or random.random() < 0.3: # 30% chance to be a terminal
        # Choose a terminal (either 'x' or a random constant)
        if random.random() < 0.5:
            value = 'x'
        else:
            value = round(random.uniform(-10, 10), 2) # Random float between -10 and 10
        
        leaf_node = Node(value=value)
        return FormulaTree(root=leaf_node)

    # Recursive Step: Choose an operator and create children recursively.
    op_value = random.choice(OPERATORS)
    
    left_child_tree = create_random_tree(max_depth, current_depth + 1)
    right_child_tree = create_random_tree(max_depth, current_depth + 1)
    
    op_node = Node(value=op_value, children=[left_child_tree.root, right_child_tree.root])
    
    return FormulaTree(root=op_node)


# --- Test code to make sure it works ---
if __name__ == "__main__":
    print("--- Day 4, Task 1 Verification ---")
    print("Generating 3 random formula trees...")

    for i in range(3):
        random_formula = create_random_tree(max_depth=3)
        print(f"  Tree {i+1}: {random_formula}")