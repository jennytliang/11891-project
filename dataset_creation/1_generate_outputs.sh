#!/bin/bash
#SBATCH --job-name=generate_outputs
#SBATCH --output=debug-generate_outputs.out
#SBATCH --error=debug-generate_outputs.err
#SBATCH --time=5:00:00
#SBATCH --gpus=8

cd /home/jtliang/interactive-constrained-decoding/11891-project
module load cuda-12.1
export CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7
python3 1_generate_outputs.py 
