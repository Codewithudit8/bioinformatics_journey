"""
Rosalind Problem: Mortal Fibonacci Rabbits (FIBD)
Strategy: Dynamic Programming (Age-tracking Array)
Time Complexity: O(n * m)
Space Complexity: O(m)
"""

def solve_mortal_fibonacci(n, m):
    """
    Simulates the population of mortal Fibonacci rabbits.
    :param n: Total number of months to simulate.
    :param m: Lifespan of a rabbit in months.
    :return: Total number of rabbit pairs remaining after n months.
    """
    
    # --- 1. Defensive Guards (Edge Cases) ---
    if n <= 0 or m <= 0:
        return 0
    if n > 100 or m > 20:
        print("Warning: Input exceeds typical Rosalind constraints. Proceeding anyway...")

    # --- 2. Initialization (Month 1) ---
    # ages[0] = newborns, ages[1] = 1-month-old, ..., ages[m-1] = oldest
    ages = [0] * m
    ages[0] = 1 
    
    # --- 3. Simulation Loop (Month 2 to n) ---
    for month in range(2, n + 1):
        next_ages = [0] * m
        
        # Rule A: Reproduction (All adults create 1 newborn pair)
        next_ages[0] = sum(ages[1:])
        
        # Rule B & C: Aging and Death 
        # Shift everyone by 1 month. The oldest (ages[m-1]) naturally drop off.
        for i in range(m - 1):
            next_ages[i + 1] = ages[i]
            
        # Update state for the next month
        ages = next_ages
        
    # --- 4. Final Extraction ---
    return sum(ages)


def main():
    """
    Handles File Input/Output and executes the algorithm.
    """
    input_file = "rosalind_fibd (2).txt"
    output_file = "output.txt"
    
    # Read the dataset securely
    try:
        with open(input_file, "r") as file:
            data = file.readline().strip().split()
            n = int(data[0])
            m = int(data[1])
            print(f"Dataset Loaded Successfully: Simulating {n} months with lifespan of {m} months...")
            
    except FileNotFoundError:
        print(f"Error: Dataset '{input_file}' nahi mila. Kripya file check karein.")
        return
    except ValueError:
        print("Error: File ka format galat hai. Integers expected the.")
        return

    # Calculate the answer
    result = solve_mortal_fibonacci(n, m)
    
    # Print to console for confirmation
    print(f"Calculation Complete!\nTotal pairs of rabbits after {n} months: {result}")

    # Save to output file for easy copy-pasting to Rosalind
    try:
        with open(output_file, "w") as out_file:
            out_file.write(str(result))
        print(f"Answer successfully saved to '{output_file}'. Ab aap submit kar sakte hain!")
    except Exception as e:
        print(f"Error saving file: {e}")


# The Gatekeeper: Ensures the script runs only when executed directly
if __name__ == "__main__":
    main()