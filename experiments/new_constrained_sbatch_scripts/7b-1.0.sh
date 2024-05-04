#!/bin/bash
#SBATCH --job-name=7b-1.0 # Job name
#SBATCH --gres=gpu:A6000:1               # Request GPU resources
#SBATCH --time=2:00:00             # Time limit hrs:min:sec

eval "$(conda shell.zsh hook)"
conda activate code_gen

# Run your Python script
model="codellama/CodeLlama-7b-Python-hf"
interaction_step=1
temperature=1.0
datadir=../data_v2/
upweight=1.05
downweight=0.95

python3 experiment_with_constraints.py --data-dir=$datadir --model-name=$model --temperature=$temperature --interaction-step=$interaction_step --constraints-mode=constraints_"$upweight"_"$downweight" --upweight-factor=$upweight --downweight-factor=$downweight
python3 convert_gen_dict_to_eval_harness.py --data-dir=$datadir --model-name=$model --temperature=$temperature --key-in-dict=generation_step_$interaction_step --interaction-step=$interaction_step --phase=exp_finalreport
python3 evaluate_gens.py --data-dir=$datadir --model-name=$model --temperature=$temperature --key-in-dict=generation_step_$interaction_step --interaction-step=$interaction_step --phase=exp_finalreport

