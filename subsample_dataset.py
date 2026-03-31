import pandas as pd
import random
from Bio import SeqIO

N = 30

meta = pd.read_csv("metadata.tsv", sep="\t")
meta = meta[
    meta["date"].str.match(r"\d{4}-\d{2}-\d{2}", na=False) &
    meta["region"].notna() &
    meta["country"].notna()
]
#filtered_meta.groupby("country").sample(n=2, random_state=42)
sampled_ids = random.sample(list(meta["accession"]), N)

# metadata
meta[meta["accession"].isin(sampled_ids)] \
    .to_csv("subsample_metadata.tsv", sep="\t", index=False)

# fasta
records = SeqIO.parse("sequences.fasta", "fasta")

with open("subsample.fasta", "w") as out:
    SeqIO.write(
        (r for r in records if r.id in sampled_ids),
        out,
        "fasta"
    )
