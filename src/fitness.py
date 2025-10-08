# src/fitness.py

# We need to import the tools we built in other files.
from src.core import Node, FormulaTree
from src.utils import load_data

def calculate_fitness(tree: FormulaTree, data_points: list):
    """
    Calculates the fitness of a formula tree using Mean Squared Error (MSE).
    A lower score indicates a better fit (less error).

    Args:
        tree: The FormulaTree object to evaluate.
        data_points: A list of (x, y) tuples from our dataset.

    Returns:
        The MSE value as a float.
    """
    total_squared_error = 0.0

    for x, y_actual in data_points:
        # Get the formula's prediction for the current x value
        y_predicted = tree.evaluate(x_value=x)
        
        # Calculate the squared error for this point
        error = y_predicted - y_actual
        squared_error = error ** 2
        
        # Add it to the total
        total_squared_error += squared_error

    # Calculate the mean by dividing by the number of data points
    mean_squared_error = total_squared_error / len(data_points)
    
    return mean_squared_error

# --- Test code to make sure it works ---
if __name__ == "__main__":
    print("--- Day 3, Task 2 Verification ---")
    
    # 1. Load the data
    pendulum_data = load_data('data/pendulum.csv')

    # 2. Create a couple of simple, "test" formulas to score
    # Formula 1: A deliberately bad guess, y = x + 1
    node_x1 = Node('x')
    node_one = Node(1.0)
    node_add = Node('+', children=[node_x1, node_one])
    bad_formula = FormulaTree(root=node_add)

    # Formula 2: A slightly better guess, y = 2 * x
    node_x2 = Node('x')
    node_two = Node(2.0)
    node_mult = Node('*', children=[node_x2, node_two])
    better_formula = FormulaTree(root=node_mult)
    
    # 3. Calculate and print the fitness for each
    fitness1 = calculate_fitness(bad_formula, pendulum_data)
    fitness2 = calculate_fitness(better_formula, pendulum_data)

    print(f"Testing formula: {bad_formula}")
    print(f"Fitness (MSE): {fitness1:.4f}") # Using .4f to format to 4 decimal places
    
    print(f"\nTesting formula: {better_formula}")
    print(f"Fitness (MSE): {fitness2:.4f}")
    
    if fitness2 < fitness1:
        print("\nSuccess! The 'better' formula correctly received a lower error score.")
    else:
        print("\nSomething might be wrong. The fitness scores don't seem right.")