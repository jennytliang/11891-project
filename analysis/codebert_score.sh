#!/bin/bash
#SBATCH --job-name=0_codebert_score
#SBATCH --output=debug-codebert_score_0.out
#SBATCH --error=debug-codebert_score_0.err
#SBATCH --time=15:00:00
#SBATCH --gres=gpu:A6000:1
#SBATCH --mem=40G

cd /home/jtliang/interactive-constrained-decoding/11891-project
module load cuda-12.1
export CUDA_VISIBLE_DEVICES=0
PREDS_FOLDER=/home/jtliang/interactive-constrained-decoding/11891-project/data/CodeLlama-13b-Python-hf/code
TEMPERATURE=0.5

python3 ./analysis/codebert_score.py -f $PREDS_FOLDER -t $TEMPERATURE