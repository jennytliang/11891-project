#!/bin/bash
#SBATCH --job-name=get_constraints
#SBATCH --output=debug-get_constraints.out
#SBATCH --error=debug-get_constraints.err
#SBATCH --time=5:00:00

cd /home/jtliang/interactive-constrained-decoding/11891-project
module load cuda-12.1
python3 4_get_constraints.py