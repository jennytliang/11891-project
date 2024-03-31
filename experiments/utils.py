import logging
from difflib import SequenceMatcher

def get_logger(args, name, output=True):
    logger = logging.getLogger(name)
    if type(args) == str:
        logger.setLevel(eval("logging." + args))
    else:
        logger.setLevel(eval("logging." + args.verbose))
    if output:
        fmt = "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
        datefmt = '%Y-%m-%d %H:%M:%S'
        formatter = logging.Formatter(fmt, datefmt)
        ch = logging.StreamHandler()
        ch.setFormatter(formatter)
        logger.addHandler(ch)
    return logger

def get_constraints(s1_tokens, s2_tokens):
    s = SequenceMatcher(None, s1_tokens, s2_tokens)
    diffs = []
    for tag, i1, i2, j1, j2 in s.get_opcodes():
        if tag != "equal":
            diffs.append((tag, i1, i2, j1, j2))

    return diffs

def get_second_quote_end_index(code):
    quote = "\"\"\"" if "\"\"\"" in code else "'''"
    first_quotes_index = code.index(quote)
    
    return code.index(quote, first_quotes_index + 1) + len(quote) # Return the location of the second quote

def clean_tokens(tokens):
    return [t.strip("▁") for t in tokens if t != "<0x0A>" and t != "<0x09>"]

def get_constraint_text(constraint, generated_solution_tokens, reference_solution_tokens):
    tag, i1, i2, j1, j2 = constraint

    # Only consider first 10 tokens for constraints
    i2 = i2 if abs(i2 - i1) < 10 else i1 + 10
    j2 = j2 if abs(j2 - j1) < 10 else j1 + 10

    clean_generated_solution_tokens = clean_tokens(generated_solution_tokens[i1:i2])
    clean_reference_solution_tokens = clean_tokens(reference_solution_tokens[j1:j2])

    # Return empty string if there are no constraint tokens to enforce
    inclusion_constraint_text = ""
    exclusion_constraint_text = ""

    if tag == "insert":
        if len(clean_reference_solution_tokens) > 0:
            inclusion_constraint_text = "\tInclude these tokens in the code: " + " ".join(clean_reference_solution_tokens) + "\n"
        return inclusion_constraint_text
    elif tag == "delete":
        if len(clean_generated_solution_tokens) > 0:
            exclusion_constraint_text = "\tDo not include these tokens in the code: " + " ".join(clean_generated_solution_tokens)+ "\n"
        return exclusion_constraint_text
    elif tag == "replace":
        # Deduplicate the tokens
        deduplicated_generated_solution_tokens = [t for t in clean_generated_solution_tokens if t not in clean_reference_solution_tokens]

        if len(clean_reference_solution_tokens) > 0:
            inclusion_constraint_text = "\tInclude these tokens in the code: " + " ".join(clean_reference_solution_tokens) + "\n"
        if len(deduplicated_generated_solution_tokens) > 0:
            exclusion_constraint_text = "\tDo not include these tokens in the code: " + " ".join(deduplicated_generated_solution_tokens)+ "\n"

        return inclusion_constraint_text + exclusion_constraint_text

    return None # Not a valid tag, return None