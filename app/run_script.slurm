#!/bin/bash
#SBATCH --nodes=1
#SBATCH --gpus-per-node=2
#SBATCH --cpus-per-gpu=16
#SBATCH --mem=64G
#SBATCH --constraint="v100"
#SBATCH --time=24:00:00
#SBATCH --partition=batch
#SBATCH --output=log-%x-%j.out
#SBATCH --error=log-%x-%j.out

module purge
module load gcc
source ~/miniconda3/etc/profile.d/conda.sh
conda activate /home/xux/miniconda3/envs/clean

python CLEAN_inference.py --inference_fasta_folder data  --inference_fasta new.fasta --gpu_id 0 --inference_fasta_end 10000000 --toks_per_batch 2048  --esm_batches_per_clean_inference 300