import os
from Bio import SeqIO

# Replace with your actual total number of taxa
TOTAL_TAXA = 250

base_dirs = ["hit_4", "hit_10", "hit_50", "hit_100"]

for base in base_dirs:
    occupancies = []

    for file in os.listdir(base):
        if file.endswith((".fa", ".fasta", ".fas", ".aln")):
            taxa = set()
            try:
                for record in SeqIO.parse(os.path.join(base, file), "fasta"):
                    taxa.add(record.id.split("|")[0])  # Adjust based on your FASTA headers
                occupancy = len(taxa) / TOTAL_TAXA
                occupancies.append(occupancy)
            except Exception as e:
                print(f"Error reading {file}: {e}")

    print(f"\n📁 {base}")
    print(f"  Total clusters: {len(occupancies)}")

    if occupancies:
        mean_occupancy = sum(occupancies) / len(occupancies)
        over_10 = sum(o >= 0.10 for o in occupancies)
        over_50 = sum(o >= 0.50 for o in occupancies)
        over_75 = sum(o >= 0.75 for o in occupancies)

        print(f"  Mean occupancy per cluster: {mean_occupancy * 100:.2f}%")
        print(f"  Clusters with ≥10% of taxa: {over_10}")
        print(f"  Clusters with ≥50% of taxa: {over_50}")
        print(f"  Clusters with ≥75% of taxa: {over_75}")
    else:
        print("  No valid clusters found.")
