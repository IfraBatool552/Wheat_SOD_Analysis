import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# --- Configuration: File Paths ---
input_file = "../Data/gene_expression_data.csv"
output_img = "../Result/Figure_4_Expression_Heatmap.png"

print("--- Generating Expression Heatmap ---")

# 1. Load the Data
# We use 'index_col=0' to tell Python that the first column (Gene_ID) contains the names, not the numbers.
try:
    df = pd.read_csv(input_file, index_col=0)
    print("Data Loaded Successfully.")
    print("Preview of data:")
    print(df.head()) # Shows the first 5 rows to verify
except FileNotFoundError:
    print(f"Error: Could not find {input_file}. Did you name the CSV file correctly?")
    exit()

# 2. Create the Heatmap
plt.figure(figsize=(8, 10)) # Set the image size (Width=8, Height=10)

# sns.heatmap parameters explained:
# data=df : The data to plot
# cmap='RdYlBu_r' : Color Map (Red-Yellow-Blue reversed). Red = High Expression, Blue = Low.
# annot=True : Writes the actual number inside the box.
# fmt=".1f" : Formats numbers to 1 decimal place.
sns.heatmap(df, cmap='RdYlBu_r', annot=True, fmt=".1f", linewidths=.5)

# 3. Add Titles and Labels
plt.title('In-Silico Expression Profile of TaSOD Genes\n(FPKM Values)', fontsize=14, fontweight='bold')
plt.xlabel('Stress Condition', fontsize=12)
plt.ylabel('Gene ID', fontsize=12)

# 4. Save the Image
plt.tight_layout() # Adjusts margins so the text doesn't get cut off
plt.savefig(output_img, dpi=300) # dpi=300 is "Publication Quality" resolution

print(f"Success! Heatmap saved to: {output_img}")
print("--- Analysis Complete ---")