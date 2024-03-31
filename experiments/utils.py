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
    return [t.strip("▁") for t in tokens if t != "<0x0A>"]

def get_constraint_text(constraint, generated_solution_tokens, reference_solution_tokens):
    tag, i1, i2, j1, j2 = constraint

    # Only consider first 10 tokens for constraints
    i2 = i2 if abs(i2 - i1) < 10 else i1 + 10
    j2 = j2 if abs(j2 - j1) < 10 else j1 + 10

    clean_generated_solution_tokens = clean_tokens(generated_solution_tokens)[i1:i2]
    clean_reference_solution_tokens = clean_tokens(reference_solution_tokens)[j1:j2]

    # Deduplicate the tokens
    new_generated_solution_tokens = [t for t in clean_generated_solution_tokens if t not in clean_reference_solution_tokens]
    new_reference_solution_tokens = [t for t in clean_reference_solution_tokens if t not in clean_generated_solution_tokens]

    if tag == "insert":
        return "\tInclude these tokens in the code: " + " ".join(new_generated_solution_tokens) + "\n"
    elif tag == "delete":
        return "\tDo not include these tokens in the code: " + " ".join(new_reference_solution_tokens)+ "\n"
    elif tag == "replace":
        return "\tInclude these tokens in the code: " + " ".join(new_generated_solution_tokens) + "\n" + "\tDo not include these tokens in the code: " + " ".join(new_reference_solution_tokens)+ "\n"

    return None