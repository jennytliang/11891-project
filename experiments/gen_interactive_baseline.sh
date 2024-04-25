#!/bin/bash
interaction_step=1
models=("codellama/CodeLlama-7b-Python-hf" "codellama/CodeLlama-13b-Python-hf" "deepseek-ai/deepseek-coder-1.3b-instruct" "deepseek-ai/deepseek-coder-6.7b-instruct")
for model in "${models[@]}"
do
    python3 baseline_with_interaction.py --data-dir=/data/user_data/nishant2/code_gen_project/ --model-name=$model --temperature=0.0 --interaction-step=$interaction_step
    python3 baseline_with_interaction.py --data-dir=/data/user_data/nishant2/code_gen_project/ --model-name=$model --temperature=0.5 --interaction-step=$interaction_step
    python3 baseline_with_interaction.py --data-dir=/data/user_data/nishant2/code_gen_project/ --model-name=$model --temperature=1.0 --interaction-step=$interaction_step
    python3 baseline_with_interaction.py --data-dir=/data/user_data/nishant2/code_gen_project/ --model-name=$model --temperature=2.0 --interaction-step=$interaction_step
    python3 baseline_with_interaction.py --data-dir=/data/user_data/nishant2/code_gen_project/ --model-name=$model --temperature=3.0 --interaction-step=$interaction_step
    python3 convert_gen_dict_to_eval_harness.py --data-dir=/data/user_data/nishant2/code_gen_project/ --model-name=$model --temperature=0.0 --key-in-dict=generation_step_$interaction_step --interaction-step=$interaction_step
    python3 convert_gen_dict_to_eval_harness.py --data-dir=/data/user_data/nishant2/code_gen_project/ --model-name=$model --temperature=0.5 --key-in-dict=generation_step_$interaction_step --interaction-step=$interaction_step
    python3 convert_gen_dict_to_eval_harness.py --data-dir=/data/user_data/nishant2/code_gen_project/ --model-name=$model --temperature=1.0 --key-in-dict=generation_step_$interaction_step --interaction-step=$interaction_step
    python3 convert_gen_dict_to_eval_harness.py --data-dir=/data/user_data/nishant2/code_gen_project/ --model-name=$model --temperature=2.0 --key-in-dict=generation_step_$interaction_step --interaction-step=$interaction_step
    python3 convert_gen_dict_to_eval_harness.py --data-dir=/data/user_data/nishant2/code_gen_project/ --model-name=$model --temperature=3.0 --key-in-dict=generation_step_$interaction_step --interaction-step=$interaction_step
    #python3 evaluate_gens.py --data-dir=/data/user_data/nishant2/code_gen_project/ --model-name=$model --temperature=0.0 --key-in-dict=generation_step_0
    #python3 evaluate_gens.py --data-dir=/data/user_data/nishant2/code_gen_project/ --model-name=$model --temperature=0.5 --key-in-dict=generation_step_0
    #python3 evaluate_gens.py --data-dir=/data/user_data/nishant2/code_gen_project/ --model-name=$model --temperature=1.0 --key-in-dict=generation_step_0
    #python3 evaluate_gens.py --data-dir=/data/user_data/nishant2/code_gen_project/ --model-name=$model --temperature=2.0 --key-in-dict=generation_step_0
    #python3 evaluate_gens.py --data-dir=/data/user_data/nishant2/code_gen_project/ --model-name=$model --temperature=3.0 --key-in-dict=generation_step_0
done