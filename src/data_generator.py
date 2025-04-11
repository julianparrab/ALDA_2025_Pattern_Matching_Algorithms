import numpy as np
import string
from src import constants


def generate_random_text_and_pattern(text_length, pattern_probability):
    pattern_length = np.random.randint(
        constants.MIN_LENGTH_PATTERN, constants.MAX_LENGTH_PATTERN
    )  # Asegurarse de que el patrón no sea más largo que el texto
    # Generate random pattern
    pattern = "".join(np.random.choice(list(string.ascii_uppercase), size=pattern_length))

    # Generate random text with the pattern inserted
    text = []
    i = 0
    while i < text_length:
        if np.random.random() < pattern_probability and i + pattern_length <= text_length:
            variation = list(pattern)
            idx_to_change = np.random.choice(pattern_length, size=np.random.randint(1, pattern_length), replace=False)
            for idx in idx_to_change:
                variation[idx] = np.random.choice(list(string.ascii_uppercase))
            text.append("".join(variation))
            i += pattern_length
        else:
            text.append(np.random.choice(list(string.ascii_uppercase)))
            i += 1

    return "".join(text)[:text_length], pattern
