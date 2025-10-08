# src/utils.py
import csv

def load_data(filepath: str):
    """
    Loads a two-column CSV file into a list of tuples.
    
    Args:
        filepath: The path to the CSV file.
        
    Returns:
        A list of (x, y) tuples, where x and y are floats.
    """
    data_points = []
    with open(filepath, 'r') as f:
        reader = csv.reader(f)
        header = next(reader)  # Skip the header row
        for row in reader:
            # Convert string values from the file into floating-point numbers
            x_val = float(row[0])
            y_val = float(row[1])
            data_points.append((x_val, y_val))
    return data_points

# --- Test code to make sure it works ---
if __name__ == "__main__":
    print("--- Day 3, Task 1 Verification ---")
    
    # The path is relative to the root `evosolve` folder
    dataset_path = 'data/pendulum.csv'
    
    try:
        pendulum_data = load_data(dataset_path)
        print(f"Successfully loaded {len(pendulum_data)} data points.")
        print("First 3 data points:", pendulum_data[:3])
    except FileNotFoundError:
        print(f"Error: The file was not found at '{dataset_path}'")
        print("Please make sure you are running this script from the root 'evosolve' directory.")