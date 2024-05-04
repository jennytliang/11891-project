#!/bin/bash
#SBATCH --job-name=deepseek-baseline # Job name
#SBATCH --gres=gpu:A6000:1               # Request GPU resources
#SBATCH --time=2:00:00             # Time limit hrs:min:sec

eval "$(conda shell.zsh hook)"
conda activate code_gen

# Run your Python script
datadir=../data_v2/
models=("deepseek-ai/deepseek-coder-1.3b-instruct" "deepseek-ai/deepseek-coder-6.7b-instruct")
temperatures=("0.0" "0.5" "1.0" "2.0" "3.0")
for model in "${models[@]}"
do
    for temperature in "${temperatures[@]}"
    do
        python3 baseline_no_interaction.py --data-dir=$datadir --model-name=$model --temperature=$temperature
        python3 convert_gen_dict_to_eval_harness.py --data-dir=$datadir --model-name=$model --temperature=$temperature --key-in-dict=generation_step_0 
        python3 evaluate_gens.py --data-dir=$datadir --model-name=$model --temperature=$temperature --key-in-dict=generation_step_0 
    done
done