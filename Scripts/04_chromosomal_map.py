import pandas as pd
import matplotlib.pyplot as plt
from Bio import SeqIO
import re

# --- Setup Paths ---
input_file = "../Data/wheat_SOD_candidates.fasta"
output_chart = "../Result/Figure_3_Chromosomal_Distribution.png"
output_table = "../Result/SOD_Gene_Renaming.csv"

print("--- Starting Chromosomal Mapping ---")

gene_data = []

# --- Step 1: Parse the IDs ---
# Wheat IDs usually look like: TraesCS1A02G... 
# The "1A" part is the chromosome.
for record in SeqIO.parse(input_file, "fasta"):
    gene_id = record.id
    
    # We look for the pattern "CS" followed by a digit and a letter (e.g., CS1A)
    # This uses Regular Expressions (Regex) to be accurate
    match = re.search(r"CS(\d[ABD])", gene_id)
    
    if match:
        chromosome = match.group(1) # Extracts '1A', '5D', etc.
    else:
        chromosome = "Unknown"

    gene_data.append({"Gene_ID": gene_id, "Chromosome": chromosome})

# --- Step 2: Create a Table ---
df = pd.DataFrame(gene_data)

# Sort the data so TaSOD1 is on Chromosome 1, not Chromosome 7
df = df.sort_values(by=['Chromosome', 'Gene_ID'])

# Create new names: TaSOD1, TaSOD2, TaSOD3...
df['New_Name'] = [f"TaSOD{i+1}" for i in range(len(df))]

print(f"Successfully mapped {len(df)} genes.")
print(df.head()) # Show first few rows

# Save the table
df.to_csv(output_table, index=False)
print(f"Renaming table saved to: {output_table}")

# --- Step 3: Draw the Chart ---
# Count how many genes are on each chromosome
counts = df['Chromosome'].value_counts().sort_index()

# Plotting
plt.figure(figsize=(10, 6))
counts.plot(kind='bar', color='#2E8B57', edgecolor='black') # SeaGreen color

plt.title('Chromosomal Distribution of TaSOD Genes', fontsize=14, fontweight='bold')
plt.xlabel('Chromosome', fontsize=12)
plt.ylabel('Number of Genes', fontsize=12)
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Save the image
plt.savefig(output_chart, dpi=300)
print(f"Chart saved to: {output_chart}")
print("--- Day 4 Analysis Complete ---")