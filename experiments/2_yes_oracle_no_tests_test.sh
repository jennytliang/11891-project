#!/bin/bash
#SBATCH --job-name=yes_oracle_no_tests_test
#SBATCH --output=debug-yes_oracle_no_tests_test.out
#SBATCH --error=debug-yes_oracle_no_tests_test.err
#SBATCH --time=15:00:00

cd /home/jtliang/interactive-constrained-decoding/11891-project
module load cuda-12.1
export CUDA_VISIBLE_DEVICES=0
INPUT_FOLDER=/home/jtliang/interactive-constrained-decoding/11891-project/experiments/out/CodeLlama-7b-Python-hf/yes_oracle_no_tests/round1
OUTPUT_FOLDER=/home/jtliang/interactive-constrained-decoding/11891-project/experiments/out/CodeLlama-7b-Python-hf/yes_oracle_no_tests/round1

python3 ./experiments/2_yes_oracle_no_tests.py test -f $INPUT_FOLDER $OUTPUT_FOLDER -i 0 164