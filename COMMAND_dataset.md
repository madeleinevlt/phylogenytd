# Command Line to prepare dataset

Dataset path : https://nextstrain.org/pathogens/files

Example with yellow fever :

```
wget https://data.nextstrain.org/files/workflows/yellow-fever/sequences.fasta.zst
wget https://data.nextstrain.org/files/workflows/yellow-fever/metadata.tsv.zst
```

To unzip : 
```
zstd -d sequences.fasta.zst
zstd -d metadata.tsv.zst
```

To create subsample :
```
python3 subsample_dataset.py
```
