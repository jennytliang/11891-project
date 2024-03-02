#!/bin/bash
#SBATCH --job-name=debug-humaneval
#SBATCH --output=debug-humaneval.out
#SBATCH --error=debug-humaneval.err
#SBATCH --time=1:00:00
#SBATCH --gpus=2

cd /home/jtliang/interactive-constrained-decoding/11891-project
module load cuda-12.1
export CUDA_VISIBLE_DEVICES=0,1
python3 get_outputs.py 
