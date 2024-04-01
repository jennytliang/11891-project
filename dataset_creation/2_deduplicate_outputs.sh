#!/bin/bash
#SBATCH --job-name=deduplicate_outputs
#SBATCH --output=debug-deduplicate_outputs.out
#SBATCH --error=debug-deduplicate_outputs.err
#SBATCH --time=5:00:00

cd /home/jtliang/interactive-constrained-decoding/11891-project
module load cuda-12.1
python3 ./dataset_creation/2_deduplicate_outputs.py 