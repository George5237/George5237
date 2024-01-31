def calculate_molarity(moles_of_solute, liters_of_solution):
    """
    Calculates the molarity of a solution.

    Parameters:
    - moles_of_solute (float): The moles of solute.
    - liters_of_solution (float): The liters of solution.

    Returns:
    - molarity (float): The molarity of the solution.
    """
    try:
        molarity = moles_of_solute / liters_of_solution
        return molarity
    except ZeroDivisionError:
        return "Error: Division by zero. Please provide a non-zero value for liters of solution."

def main():
    try:
        # Input moles of solute
        moles_of_solute = float(input("Enter moles of solute: "))

        # Input liters of solution
        liters_of_solution = float(input("Enter liters of solution: "))

        # Calculate molarity
        result = calculate_molarity(moles_of_solute, liters_of_solution)

        # Display the result
        print("\nMolarity Result:")
        print(result)
    except ValueError:
        print("Error: Invalid input. Please enter valid numerical values.")

if __name__ == "__main__":
    # Execute the program if it is run as the main script
    main()
