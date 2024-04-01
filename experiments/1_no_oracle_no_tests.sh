#!/bin/bash
#SBATCH --job-name=no_oracle_no_tests
#SBATCH --output=debug-no_oracle_no_tests.out
#SBATCH --error=debug-no_oracle_no_tests.err
#SBATCH --time=5:00:00

INPUT_FOLDER=/home/jtliang/interactive-constrained-decoding/11891-project/data/CodeLlama-13b-Python-hf/code
OUTPUT_FOLDER=/home/jtliang/interactive-constrained-decoding/11891-project/experiments/out/CodeLlama-13b-Python-hf/no_oracle_no_tests

cd /home/jtliang/interactive-constrained-decoding/11891-project
module load cuda-12.1
python3 ./experiments/1_no_oracle_no_tests.py run -f $INPUT_FOLDER $OUTPUT_FOLDER -t 4.0