import os 
from Bio import SeqIO
from Bio.SeqUtils.ProtParam import ProteinAnalysis
import pandas as pd 

# Paths
# I UPDATED THIS LINE TO MATCH YOUR FOLDER "Result"
input_file = "../Data/wheat_SOD_candidates.fasta"
output_csv = "../Result/SOD_physicochemical_properties.csv"

# Check if output directory exists to be safe
output_dir = os.path.dirname(output_csv)
if not os.path.exists(output_dir):
    # This will create the folder if it's missing
    os.makedirs(output_dir)

data_list = []

print("--- Calculating Protein Properties ---")

try:
    # Read the file containing the 17 SOD genes
    for record in SeqIO.parse(input_file, "fasta"):
        seq_str = str(record.seq)
        
        # Clean sequence (remove stops)
        if "*" in seq_str:
            seq_str = seq_str.replace("*", "")
        
        # Analyze
        analysed_seq = ProteinAnalysis(seq_str)
        
        # Calculate math
        mol_weight = analysed_seq.molecular_weight()
        isoelectric_point = analysed_seq.isoelectric_point()
        
        # Add to list
        data_list.append({
            "Gene_ID": record.id,
            "Amino_Acid_Length": len(seq_str),
            "Molecular_Weight_Da": round(mol_weight, 2),
            "Isoelectric_Point_pI": round(isoelectric_point, 2)
        })

    # Save to Excel-compatible CSV
    df = pd.DataFrame(data_list)
    df.to_csv(output_csv, index=False)

    print(f"Analysis complete for {len(data_list)} genes.")
    print(f"Results saved to: {output_csv}")

except FileNotFoundError:
    print("ERROR: Could not find the input file.")
    print(f"Checked path: {input_file}")
    print("Please check that 'wheat_SOD_candidates.fasta' is inside your Data folder.")