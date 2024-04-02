#!/bin/bash
#SBATCH --job-name=8_yes_oracle_no_tests_run
#SBATCH --output=debug-yes_oracle_no_tests_run_8.out
#SBATCH --error=debug-yes_oracle_no_tests_run_8.err
#SBATCH --time=15:00:00
#SBATCH --gres=gpu:A6000:1
#SBATCH --mem=40G

cd /home/jtliang/interactive-constrained-decoding/11891-project
module load cuda-12.1
export CUDA_VISIBLE_DEVICES=0
INPUT_FOLDER=/home/jtliang/interactive-constrained-decoding/11891-project/data/CodeLlama-7b-Python-hf/code
OUTPUT_FOLDER=/home/jtliang/interactive-constrained-decoding/11891-project/experiments/out/CodeLlama-7b-Python-hf/yes_oracle_no_tests/round1
TEMPERATURE=2.0

# python3 ./experiments/2_yes_oracle_no_tests.py run -f $INPUT_FOLDER $OUTPUT_FOLDER -i 0 20 -t $TEMPERATURE
# python3 ./experiments/2_yes_oracle_no_tests.py run -f $INPUT_FOLDER $OUTPUT_FOLDER -i 20 41 -t $TEMPERATURE
# python3 ./experiments/2_yes_oracle_no_tests.py run -f $INPUT_FOLDER $OUTPUT_FOLDER -i 41 61 -t $TEMPERATURE
# python3 ./experiments/2_yes_oracle_no_tests.py run -f $INPUT_FOLDER $OUTPUT_FOLDER -i 61 82 -t $TEMPERATURE
# python3 ./experiments/2_yes_oracle_no_tests.py run -f $INPUT_FOLDER $OUTPUT_FOLDER -i 82 102 -t $TEMPERATURE
# python3 ./experiments/2_yes_oracle_no_tests.py run -f $INPUT_FOLDER $OUTPUT_FOLDER -i 102 123 -t $TEMPERATURE
# python3 ./experiments/2_yes_oracle_no_tests.py run -f $INPUT_FOLDER $OUTPUT_FOLDER -i 123 143 -t $TEMPERATURE
# python3 ./experiments/2_yes_oracle_no_tests.py run -f $INPUT_FOLDER $OUTPUT_FOLDER -i 143 164 -t $TEMPERATURE