def translate_dna_to_amino_acids(dna_sequence):
    """
    Translates a DNA sequence into amino acids.

    Parameters:
    - dna_sequence (str): The input DNA sequence.

    Returns:
    - amino_acids (str): The translated amino acid sequence.
    """
    # Define the genetic code (RNA codons to amino acids)
    genetic_code = {
        'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
        'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
        'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M',
        'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
        'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
        'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
        'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
        'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
        'UAU': 'Y', 'UAC': 'Y', 'UAA': 'STOP', 'UAG': 'STOP',
        'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
        'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
        'UGU': 'C', 'UGC': 'C', 'UGA': 'STOP', 'UGG': 'W',
        'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
        'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
        'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G',
    }

    # Ensure the DNA sequence length is divisible by 3
    if len(dna_sequence) % 3 != 0:
        return "Insufficient nucleotides for a full codon."

    amino_acids = ""
    for i in range(0, len(dna_sequence), 3):
        codon = dna_sequence[i:i+3]
        amino_acid = genetic_code.get(codon, 'X')  # 'X' for unknown codons
        if amino_acid == 'STOP':
            break  # Stop translation if a stop codon is encountered
        amino_acids += amino_acid

    return amino_acids

def main():
    # Input DNA sequence
    user_input_sequence = input("Enter a DNA sequence: ")

    # Translate the DNA sequence to amino acids
    result = translate_dna_to_amino_acids(user_input_sequence.upper())

    # Display the result
    print("\nTranslation Result:")
    print(result)

if __name__ == "__main__":
    # Execute the program if it is run as the main script
    main()
