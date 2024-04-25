#!/bin/bash
#SBATCH --job-name=13b-0.5 # Job name
#SBATCH --gres=gpu:A6000:1               # Request GPU resources
#SBATCH --time=2:00:00             # Time limit hrs:min:sec

eval "$(conda shell.zsh hook)"
conda activate code_gen

# Run your Python script
model="codellama/CodeLlama-13b-Python-hf"
interaction_step=2
temperature=0.5
python3 experiment_with_constraints.py --data-dir=/data/user_data/nishant2/code_gen_project/ --model-name=$model --temperature=$temperature --interaction-step=$interaction_step
python3 convert_gen_dict_to_eval_harness.py --data-dir=/data/user_data/nishant2/code_gen_project/ --model-name=$model --temperature=$temperature --key-in-dict=generation_step_$interaction_step --interaction-step=$interaction_step --phase=exp
python3 evaluate_gens.py --data-dir=/data/user_data/nishant2/code_gen_project/ --model-name=$model --temperature=$temperature --key-in-dict=generation_step_$interaction_step --interaction-step=$interaction_step --phase=exp
