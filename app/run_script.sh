#!/bin/bash

source ~/miniconda3/etc/profile.d/conda.sh
conda activate /home/xux/miniconda3/envs/clean

query_path=$1
fasta_dir=$(dirname "$query_path")
fasta_path=$(basename "$query_path")

NR_DB_PATH=/home/xux/Desktop/IEnzyme/EnzymeMine/CLEAN/app/data/blastdb/nr_db

# Install blastp
# sudo apt install ncbi-blast+

# Download nr dataset
# wget -P $NR_DB_PATH ftp://ftp.ncbi.nlm.nih.gov/blast/db/FASTA/nr.gz
# gunzip $NR_DB_PATH/nr.gz

# Build blastp ncbi nr database
# makeblastdb -in nr.fa  -dbtype prot -out nr_db -title "NCBI NR Protein Database"

# Run blastp
blastp -query $query_path -db nr_db -out blastp_results.tsv -outfmt "6 qseqid sseqid pident evalue bitscore stitle" -evalue 1e-5 -max_target_seqs 100

# Get seq ids
awk '{print $2}' blastp_results.tsv | sort | uniq > matched_sids.txt

# Extract sequences
blastdbcmd -db my_custom_db -entry_batch matched_sids.txt -out matched_sequences.fasta -outfmt %f

# Run clean
python CLEAN_inference.py --inference_fasta "$fasta_path" --gpu_id 0