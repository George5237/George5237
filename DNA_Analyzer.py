def is_valid_dna_sequence(sequence):
    valid_nucleotides = set('ATGC')
    return all(nucleotide in valid_nucleotides for nucleotide in sequence)

def analyze_dna_sequence(dna_sequence):
    """
    Analyzes a DNA sequence and calculates GC content and nucleotide counts.

    Parameters:
    - dna_sequence (str): The input DNA sequence.

    Returns:
    - gc_content (float): The GC content of the DNA sequence.
    - nucleotide_counts (dict): A dictionary containing counts for each nucleotide.
    """
    # Convert the DNA sequence to uppercase to handle lowercase input
    dna_sequence = dna_sequence.upper()

    # Calculate GC content
    gc_count = dna_sequence.count('G') + dna_sequence.count('C')
    total_nucleotides = len(dna_sequence)
    gc_content = (gc_count / total_nucleotides) * 100

    # Count occurrences of each nucleotide
    nucleotide_counts = {
        'A': dna_sequence.count('A'),
        'T': dna_sequence.count('T'),
        'G': dna_sequence.count('G'),
        'C': dna_sequence.count('C')
    }

    return gc_content, nucleotide_counts

def main():
    print("Enter your DNA sequence, one line at a time. Type 'done' on a new line when finished:")
    
    user_input_sequence = ""
    while True:
        line = input()
        if line.lower() == "done":
            break
        user_input_sequence += line.upper()

    # Validate the input sequence
    if not is_valid_dna_sequence(user_input_sequence):
        print("Invalid DNA sequence. Please enter a sequence containing only A, T, G, and C.")
        return

    # Analyze the DNA sequence
    gc_content, nucleotide_counts = analyze_dna_sequence(user_input_sequence)

    # Display results
    print("\nAnalysis Results:")
    print(f"GC Content: {gc_content:.2f}%")
    print("Nucleotide Counts:")
    for nucleotide, count in nucleotide_counts.items():
        print(f"{nucleotide}: {count}")

if __name__ == "__main__":
    # Execute the program if it is run as the main script
    main()
