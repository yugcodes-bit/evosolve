# src/core.py

class Node:
    """
    The basic building block of our formula tree.
    Each Node can be an operator (+, *, etc.), a variable (x), or a constant (5.0).
    """
    def __init__(self, value, children=None):
        """
        Initializes a new Node.
        
        Args:
            value: The value of the node. Can be an operator like '+',
                   a variable like 'x', or a number like 3.14.
            children: A list of child Nodes. For operators, this will contain
                      the operands. For variables and constants, it's usually None.
        """
        self.value = value
        self.children = children if children is not None else []

    def __repr__(self):
        """
        Provides a developer-friendly string representation of the Node.
        This is super helpful for debugging!
        """
        return f"Node({self.value})"

# --- Test code to make sure it works ---
if __name__ == "__main__":
    # Let's create a few nodes to represent the formula: 5 + x
    # This formula has three parts: the number 5, the variable 'x', and the '+' operator.

    print("Creating individual nodes...")
    
    # Node for the constant number 5
    node_five = Node(5.0)
    
    # Node for the variable 'x'
    node_x = Node('x')
    
    # Node for the '+' operator. Its children are the two nodes it operates on.
    node_add = Node('+', children=[node_five, node_x])

    print(f"Created a constant node: {node_five}")
    print(f"Created a variable node: {node_x}")
    print(f"Created an operator node: {node_add}")
    print(f"The children of the addition node are: {node_add.children}")