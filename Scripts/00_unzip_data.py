import gzip
import shutil
import os

# Define file paths
# This looks for the file in the Data folder one level up
compressed_file = "../Data/Triticum_aestivum.IWGSC.pep.all.fa.gz"
output_file = "../Data/wheat_proteins.fasta"

print("Starting extraction...")

# Check if the file exists first
if os.path.exists(compressed_file):
    with gzip.open(compressed_file, 'rb') as f_in:
        with open(output_file, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
    print("Success! File extracted to 'Data/wheat_proteins.fasta'")
else:
    print(f"Error: Could not find file at {compressed_file}")
    