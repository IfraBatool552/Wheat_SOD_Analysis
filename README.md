# Genome-Wide Identification and In-Silico Expression Analysis of the Superoxide Dismutase (SOD) Gene Family in Wheat (*Triticum aestivum*)

## 📌 Project Overview
**Objective:** To identify, categorize, and analyze the *Superoxide Dismutase* (SOD) gene family in the hexaploid wheat genome (*Triticum aestivum*) and predict their responsiveness to abiotic stress (Drought and Heat).

**Scientific Context:**
Wheat is a major global crop, but its yield is severely threatened by abiotic stress. The SOD gene family is the first line of antioxidant defense against Reactive Oxygen Species (ROS). This study utilizes computational biology (In-Silico) methods to "mine" the wheat genome for these defense genes.

**Author:** [Ifra Batool]
**Tools Used:** Python (Biopython, Pandas, Matplotlib, Seaborn), MEGA11, HMMER, WoLF PSORT.

---

## 🔬 Methodology & Workflow

### 1. Data Mining (Hidden Markov Models)
*   **Source:** IWGSC RefSeq v1.1 (Ensembl Plants).
*   **Method:** Utilized HMM profiles (PF00080, PF00081) to screen the complete wheat proteome (133,346 sequences).
*   **Result:** Identified **17 high-confidence TaSOD genes**.

### 2. Physicochemical Characterization
*   **Analysis:** Calculated Molecular Weight (MW) and Isoelectric Point (pI) using Python scripts.
*   **Localization:** Predicted subcellular localization (Chloroplast, Mitochondria) using WoLF PSORT II.

### 3. Phylogeny & Evolutionary Analysis
*   **Alignment:** Multiple Sequence Alignment (MSA) performed using MUSCLE.
*   **Tree Construction:** Neighbor-Joining (NJ) phylogenetic tree built in MEGA11 (1000 bootstrap replications).
*   **Insight:** The tree revealed distinct clusters, suggesting evolutionary conservation with rice and Arabidopsis models.

### 4. Chromosomal Mapping
*   **Distribution:** Mapped genes to physical chromosomal locations using Python.
*   **Finding:** Genes are distributed across A, B, and D sub-genomes, with a notable cluster on **Chromosome 7D**.

### 5. Digital Expression Profiling (Heatmap)
*   **Data Source:** Public RNA-Seq transcriptomic data (FPKM values).
*   **Visualization:** Generated a Heatmap to analyze differential expression under Control, Drought, and Heat stress.

---

## 📊 Key Results

### Figure 1: Phylogenetic Relationship
*(Please see `Result/Figure_1_Phylogenetic_Tree.png` in the repository)*
The analysis grouped the 17 TaSOD genes into three distinct sub-families, consistent with their metal co-factors (Cu/Zn, Fe, Mn).

### Figure 2: Chromosomal Distribution
*(Please see `Result/Figure_3_Chromosomal_Distribution.png`)*
*   **TaSOD genes are present on all three sub-genomes (A, B, D).**
*   **Chromosome 7D** hosts the highest density of SOD genes, indicating a potential evolutionary "hotspot" for stress adaptation.

### Figure 3: Expression Profiling (Heatmap)
*(Please see `Result/Figure_4_Expression_Heatmap.png`)*
The digital expression analysis identified specific stress-responsive candidates:
*   **Drought Responders:** *TaSOD3* and *TaSOD12* showed significant upregulation (>3-fold) under drought conditions.
*   **Heat Responders:** *TaSOD8* and *TaSOD15* were highly induced by heat stress.

---

## 📝 Conclusion
This in-silico study successfully identified **17 TaSOD genes** in the wheat genome. The expression profiling suggests that **TaSOD3** and **TaSOD8** are the most promising candidates for genetic engineering to enhance drought and heat tolerance, respectively. This computational analysis lays the groundwork for future wet-lab validation (qRT-PCR).

---

## 💻 How to Run the Code
1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/Wheat_SOD_Analysis.git
    ```
2.  **Install dependencies:**
    ```bash
    pip install biopython pandas matplotlib seaborn
    ```
3.  **Run the analysis scripts in order:**
    ```bash
    cd Scripts
    python 01_data_stats.py
    python 02_find_sod_genes.py
    python 03_calc_properties.py
    python 04_chromosomal_map.py
    python 05_expression_heatmap.py
    ```

---

