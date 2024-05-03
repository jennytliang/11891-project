#!/bin/bash
#

step=$1
outfile=docker_tmp.txt

for file in *step_"$step".eval_harness_gens;
do
    if [ -f $file ]; then
        if ! [ -f $file.individual_results.json ]; then
            echo $file
            docker run -v $(pwd)/$file:/app/generations_py.json:ro -it evaluation-harness-local-updated python3 main.py \
            --model test_docker \
            --tasks humanevalplus \
            --load_generations_path /app/generations_py.json \
            --allow_code_execution  \
            --n_samples 1 > $outfile

            awk 'p>2; /}/{++p}' $outfile | sed '$d' > $file.individual_results.json
            echo $file >> step_"$step"_pass_at_one.txt
            grep -w 'pass@1' $outfile >> step_"$step"_pass_at_one.txt
        else
            echo "$file.individual_results.json already exists; skipping"
        fi
    fi
done
