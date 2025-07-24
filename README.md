# CLEAN: Enzyme Function Prediction using Contrastive Learning

## Install
```shell
mamba create -n clean python==3.10.4 -y
mamba activate clean

cd app
pip install -r requirements.txt
pip install torch==1.11.0+cu113 torchvision==0.12.0+cu113 torchaudio==0.11.0 --extra-index-url https://download.pytorch.org/whl/cu113
pip install pysam easydict loguru biopython

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
cd app
python CLEAN_inference.py --inference_fasta new.fasta --gpu_id 0 
```


## Script run 
```shell
cd app
sbatch run_script.slurm $fasta_path 
```