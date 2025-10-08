# src/core.py

# ... (Node class remains the same) ...
class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children is not None else []
    def __repr__(self):
        return f"Node({self.value})"


class FormulaTree:
    def __init__(self, root: Node):
        self.root = root

    def __str__(self):
        return self._build_string_recursive(self.root)

    def _build_string_recursive(self, current_node: Node):
        if not current_node.children:
            return str(current_node.value)
        child_strings = [self._build_string_recursive(child) for child in current_node.children]
        return f"({child_strings[0]} {current_node.value} {child_strings[1]})"

    # NEW CODE STARTS HERE ▼▼▼

    def evaluate(self, x_value: float):
        """
        Calculates the result of the formula for a given value of x.
        """
        return self._evaluate_recursive(self.root, x_value)

    def _evaluate_recursive(self, current_node: Node, x_value: float):
        """
        Recursively traverses the tree to calculate the result.
        """
        # Base Case 1: If the node is the variable 'x', return the input value.
        if current_node.value == 'x':
            return x_value
        
        # Base Case 2: If the node has no children and is not 'x', it must be a constant.
        if not current_node.children:
            return float(current_node.value)

        # Recursive Step: The node is an operator.
        # First, calculate the results of its children.
        child_results = [self._evaluate_recursive(child, x_value) for child in current_node.children]

        # Now, perform the operation based on the node's value.
        if current_node.value == '+':
            return child_results[0] + child_results[1]
        elif current_node.value == '-':
            return child_results[0] - child_results[1]
        elif current_node.value == '*':
            return child_results[0] * child_results[1]
        elif current_node.value == '/':
            # Add a check to prevent division by zero
            return child_results[0] / child_results[1] if child_results[1] != 0 else float('inf')


# --- Update the test code at the bottom of the file ---
if __name__ == "__main__":
    # Let's test with a more complex formula: (x * 2) + 5
    node_x = Node('x')
    node_two = Node(2.0)
    node_five = Node(5.0)
    
    node_mult = Node('*', children=[node_x, node_two])
    node_add = Node('+', children=[node_mult, node_five])
    
    formula = FormulaTree(root=node_add)

    # --- Verification for today's task ---
    print("--- Day 2, Task 3 Verification ---")
    print(f"The formula is: {formula}")
    
    # Test the evaluation
    x_input = 10.0
    result = formula.evaluate(x_value=x_input)
    print(f"Result when x = {x_input}: {result}") # Expected: (10 * 2) + 5 = 25

    x_input_2 = -3.0
    result_2 = formula.evaluate(x_value=x_input_2)
    print(f"Result when x = {x_input_2}: {result_2}") # Expected: (-3 * 2) + 5 = -1