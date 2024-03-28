#!/bin/bash
#SBATCH --job-name=run_outputs
#SBATCH --output=debug-run_outputs.out
#SBATCH --error=debug-run_outputs.err
#SBATCH --time=5:00:00

cd /home/jtliang/interactive-constrained-decoding/11891-project
module load cuda-12.1
python3 3_run_outputs.py