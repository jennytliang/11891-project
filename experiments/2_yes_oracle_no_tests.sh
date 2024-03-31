#!/bin/bash
#SBATCH --job-name=yes_oracle_no_tests_test
#SBATCH --output=debug-yes_oracle_no_tests_test.out
#SBATCH --error=debug-yes_oracle_no_tests_test.err
#SBATCH --time=15:00:00
#SBATCH --gres=gpu:A6000:1
#SBATCH --mem=40G

cd /home/jtliang/interactive-constrained-decoding/11891-project
module load cuda-12.1
export CUDA_VISIBLE_DEVICES=0
python3 ./experiments/2_yes_oracle_no_tests.py run -f /home/jtliang/interactive-constrained-decoding/11891-project/data/CodeLlama-7b-Python-hf/code /home/jtliang/interactive-constrained-decoding/11891-project/experiments/out/CodeLlama-7b-Python-hf/yes_oracle_no_tests/round1 -i 0 20
# python3 ./experiments/2_yes_oracle_no_tests.py run -f /home/jtliang/interactive-constrained-decoding/11891-project/data/CodeLlama-7b-Python-hf/code /home/jtliang/interactive-constrained-decoding/11891-project/experiments/out/CodeLlama-7b-Python-hf/yes_oracle_no_tests/round1 -i 20 41
# python3 ./experiments/2_yes_oracle_no_tests.py run -f /home/jtliang/interactive-constrained-decoding/11891-project/data/CodeLlama-7b-Python-hf/code /home/jtliang/interactive-constrained-decoding/11891-project/experiments/out/CodeLlama-7b-Python-hf/yes_oracle_no_tests/round1 -i 41 61
# python3 ./experiments/2_yes_oracle_no_tests.py run -f /home/jtliang/interactive-constrained-decoding/11891-project/data/CodeLlama-7b-Python-hf/code /home/jtliang/interactive-constrained-decoding/11891-project/experiments/out/CodeLlama-7b-Python-hf/yes_oracle_no_tests/round1 -i 61 82
# python3 ./experiments/2_yes_oracle_no_tests.py run -f /home/jtliang/interactive-constrained-decoding/11891-project/data/CodeLlama-7b-Python-hf/code /home/jtliang/interactive-constrained-decoding/11891-project/experiments/out/CodeLlama-7b-Python-hf/yes_oracle_no_tests/round1 -i 82 102
# python3 ./experiments/2_yes_oracle_no_tests.py run -f /home/jtliang/interactive-constrained-decoding/11891-project/data/CodeLlama-7b-Python-hf/code /home/jtliang/interactive-constrained-decoding/11891-project/experiments/out/CodeLlama-7b-Python-hf/yes_oracle_no_tests/round1 -i 102 123
# python3 ./experiments/2_yes_oracle_no_tests.py run -f /home/jtliang/interactive-constrained-decoding/11891-project/data/CodeLlama-7b-Python-hf/code /home/jtliang/interactive-constrained-decoding/11891-project/experiments/out/CodeLlama-7b-Python-hf/yes_oracle_no_tests/round1 -i 123 143
# python3 ./experiments/2_yes_oracle_no_tests.py run -f /home/jtliang/interactive-constrained-decoding/11891-project/data/CodeLlama-7b-Python-hf/code /home/jtliang/interactive-constrained-decoding/11891-project/experiments/out/CodeLlama-7b-Python-hf/yes_oracle_no_tests/round1 -i 143 164