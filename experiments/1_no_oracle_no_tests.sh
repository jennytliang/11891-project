#!/bin/bash
#SBATCH --job-name=4_no_oracle_no_tests
#SBATCH --output=debug-no_oracle_no_tests_4.out
#SBATCH --error=debug-no_oracle_no_tests_4.err
#SBATCH --time=5:00:00
#SBATCH --mem-per-cpu=64G

INPUT_FOLDER=/home/jtliang/interactive-constrained-decoding/11891-project/experiments/out/CodeLlama-7b-Python-hf/yes_oracle_no_tests/round1
OUTPUT_FOLDER=/home/jtliang/interactive-constrained-decoding/11891-project/experiments/out/CodeLlama-7b-Python-hf/yes_oracle_no_tests/round1/tests

cd /home/jtliang/interactive-constrained-decoding/11891-project
module load cuda-12.1
python3 ./experiments/1_no_oracle_no_tests.py test -f $INPUT_FOLDER $OUTPUT_FOLDER -t 3.0