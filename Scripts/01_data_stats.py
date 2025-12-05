import os

# Define the file path
input_file = "../Data/wheat_proteins.fasta"

def count_sequences(file_path):
    """
    Reads a FASTA file and counts the total number of protein sequences.
    """
    if not os.path.exists(file_path):
        print(f"Error: File not found at {file_path}")
        return

    count = 0
    with open(file_path, 'r') as file:
        for line in file:
            # In FASTA files, every header starts with '>'
            if line.startswith('>'):
                count += 1
    
    return count

# Run the function
print("--- Wheat Genome Analysis Started ---")
print(f"Reading file: {input_file}")

total_proteins = count_sequences(input_file)

if total_proteins:
    print(f"Success! Total protein sequences found: {total_proteins}")
else:
    print("Could not count sequences. Please check your file.")

print("--- Analysis Complete ---")