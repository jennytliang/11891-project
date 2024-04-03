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
# PREDS_FOLDER=/home/jtliang/interactive-constrained-decoding/11891-project/experiments/out/CodeLlama-13b-Python-hf/yes_oracle_no_tests/round2
PREDS_FOLDER=/home/jtliang/interactive-constrained-decoding/11891-project/data/CodeLlama-13b-Python-hf/code
OUTPUT_FILE=/home/jtliang/interactive-constrained-decoding/11891-project/analysis/out/CodeLlama-13b-Python-hf/codebert/temperature-4.0_round-0.json
TEMPERATURE=4.0

python3 ./analysis/codebert_score.py -f $PREDS_FOLDER -t $TEMPERATURE -o $OUTPUT_FILE