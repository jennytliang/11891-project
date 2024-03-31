#!/bin/bash
#SBATCH --job-name=no_oracle_no_tests
#SBATCH --output=debug-no_oracle_no_tests.out
#SBATCH --error=debug-no_oracle_no_tests.err
#SBATCH --time=5:00:00

cd /home/jtliang/interactive-constrained-decoding/11891-project
module load cuda-12.1
python3 ./experiments/1_no_oracle_no_tests.py