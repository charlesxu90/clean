# CLEAN: Enzyme Function Prediction using Contrastive Learning

## Install
```shell
mamba create -n clean python==3.10.4 -y
mamba activate clean

cd app
pip install -r requirements.txt
pip install torch==1.11.0+cu113 torchvision==0.12.0+cu113 torchaudio==0.11.0 --extra-index-url https://download.pytorch.org/whl/cu113
pip install pysam easydict loguru

python build.py install
git clone https://github.com/facebookresearch/esm.git
mkdir data/esm_data
```
## Download weights
```shell
wget -o pretrained.zip https://drive.usercontent.google.com/download\?id\=1kwYd4VtzYuMvJMWXy6Vks91DSUAOcKpZ\&export\=download\&authuser\=0\&confirm\=t\&uuid\=c00d4dea-49d5-4146-a9e1-feaa2190e284\&at\=AN8xHoryCgnWepVrRlVfochDAbN6%3A1753263349783
unzip pretrained.zip
mv pretrained data/pretrained 
```

## Test run
```shell
# test inference with esm embeddings saved
python CLEAN_infer_fasta.py --fasta_data price

python CLEAN_inference.py --inference_fasta_folder data  --inference_fasta new.fasta --gpu_id 0 --inference_fasta_start 0 --inference_fasta_end 250 --toks_per_batch 2048  --esm_batches_per_clean_inference 300
```

