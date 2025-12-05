from Bio import SeqIO
import os

# Paths
input_file = "../data/wheat_proteins.fasta"
output_file = "../data/wheat_SOD_candidates.fasta"

print("--- Searching for SOD Genes ---")

found_genes = []

# Logic: Read the huge file and look for keyword "Superoxide dismutase"
try:
    with open(output_file, "w") as f_out:
        for record in SeqIO.parse(input_file, "fasta"):
            # Check if the description contains our target keyword (case insensitive)
            if "superoxide dismutase" in record.description.lower():
                SeqIO.write(record, f_out, "fasta")
                found_genes.append(record.id)

    print(f"Search complete.")
    print(f"Total SOD candidates found: {len(found_genes)}")
    print(f"Saved to: {output_file}")
    print("-----------------------------")

    # Print the first few IDs to verify
    if len(found_genes) > 0:
        print("Preview of Gene IDs found:")
        for gene in found_genes[:5]:
            print(f"- {gene}")

except FileNotFoundError:
    print(f"ERROR: Could not find the input file at: {input_file}")
    print("Make sure the data folder exists and contains wheat_proteins.fasta")