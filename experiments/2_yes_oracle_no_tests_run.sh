#!/bin/bash
#SBATCH --job-name=yes_oracle_no_tests_run_8
#SBATCH --output=debug-yes_oracle_no_tests_run_8.out
#SBATCH --error=debug-yes_oracle_no_tests_run_8.err
#SBATCH --time=15:00:00
#SBATCH --gres=gpu:A6000:1
#SBATCH --mem=40G

cd /home/jtliang/interactive-constrained-decoding/11891-project
module load cuda-12.1
export CUDA_VISIBLE_DEVICES=0
INPUT_FOLDER=/home/jtliang/interactive-constrained-decoding/11891-project/experiments/out/CodeLlama-7b-Python-hf/yes_oracle_no_tests/round1
OUTPUT_FOLDER=/home/jtliang/interactive-constrained-decoding/11891-project/experiments/out/CodeLlama-7b-Python-hf/yes_oracle_no_tests/round2

# python3 ./experiments/2_yes_oracle_no_tests.py run -f $INPUT_FOLDER $OUTPUT_FOLDER -i 0 20
# python3 ./experiments/2_yes_oracle_no_tests.py run -f $INPUT_FOLDER $OUTPUT_FOLDER -i 20 41
# python3 ./experiments/2_yes_oracle_no_tests.py run -f $INPUT_FOLDER $OUTPUT_FOLDER -i 41 61
# python3 ./experiments/2_yes_oracle_no_tests.py run -f $INPUT_FOLDER $OUTPUT_FOLDER -i 61 82
# python3 ./experiments/2_yes_oracle_no_tests.py run -f $INPUT_FOLDER $OUTPUT_FOLDER -i 82 102
# python3 ./experiments/2_yes_oracle_no_tests.py run -f $INPUT_FOLDER $OUTPUT_FOLDER -i 102 123
# python3 ./experiments/2_yes_oracle_no_tests.py run -f $INPUT_FOLDER $OUTPUT_FOLDER -i 123 143
python3 ./experiments/2_yes_oracle_no_tests.py run -f $INPUT_FOLDER $OUTPUT_FOLDER -i 143 164