#!/bin/bash

source ~/miniconda3/etc/profile.d/conda.sh
conda activate /home/xux/miniconda3/envs/clean

fasta_path=$1
fasta_dir=$(dirname "$fasta_path")
fasta_name=$(basename "$fasta_path")

python CLEAN_inference.py --inference_fasta_folder "$fasta_dir"  --inference_fasta "$fasta_name" --gpu_id 0 --inference_fasta_end 10000000 --toks_per_batch 2048  --esm_batches_per_clean_inference 300