### naive_search ###
# Complexity:
# - Best case: O(n) (when the pattern is not present in the text)
# - Average case: O(n * m) (when the pattern is present in the text and is different from the text)
# - Worst case: O(n * m) (when the pattern is present in the text and is equal to the text)


def naive_search(text, pattern):
    n = len(text)  # O(1)
    m = len(pattern)  # O(1)
    result = []

    for i in range(n - m + 1):  # O(n)
        match = True  # O(1)
        for j in range(m):  # O(m)
            if text[i + j] != pattern[j]:  # O(1)
                match = False  # O(1)
                break
        if match:
            result.append(i)  # O(1)

    return result  # O(n * m) en el peor de los casos


### Algoritmo de Knuth-Morris-Pratt (KMP) ###
# Complexity:
# - Best case: O(n) (when the pattern is not present in the text)
# - Average case: O(n) (when the pattern is present in the text and is different from the text)
# - Worst case: O(n + m) (when the pattern is present in the text and is equal to the text)


def compute_lps(pattern):
    lps = [0] * len(pattern)  # O(1)
    length = 0  # O(1)
    i = 1  # O(1)

    while i < len(pattern):  # O(m)
        if pattern[i] == pattern[length]:  # O(1)
            length += 1  # O(1)
            lps[i] = length  # O(1)
            i += 1  # O(1)
        else:
            if length != 0:  # O(1)
                length = lps[length - 1]  # O(1)
            else:
                lps[i] = 0  # O(1)
                i += 1  # O(1)
    return lps  # O(m)


def kmp_search(text, pattern):
    lps = compute_lps(pattern)  # O(m)
    result = []  # O(1)
    i = j = 0

    while i < len(text):  # O(n)
        if pattern[j] == text[i]:  # O(1)
            i += 1  # O(1)
            j += 1  # O(1)
        if j == len(pattern):  # O(1)
            result.append(i - j)  # O(1)
            j = lps[j - 1]  # O(1)
        elif i < len(text) and pattern[j] != text[i]:  # O(1)
            if j != 0:  # O(1)
                j = lps[j - 1]  # O(1)
            else:
                i += 1  # O(1)

    return result  # O(n + m) en el peor de los casos


### Algoritmo de Boyer-Moore ###
# Complexity:
# - Best case: O(n) (when the pattern is not present in the text)
# - Average case: O(n) (when the pattern is present in the text and is different from the text)
# - Worst case: O(n*m) (when the pattern is present in the text and is equal to the text)


def bad_char_heuristic(pattern):  # O(m)
    bad_char = [-1] * 256  # O(1)
    for i in range(len(pattern)):  # O(m)
        bad_char[ord(pattern[i])] = i  # O(1)
    return bad_char  # O(1)


def boyer_moore_search(text, pattern):  # O(n + m)
    m = len(pattern)  # O(1)
    n = len(text)  # O(1)
    bad_char = bad_char_heuristic(pattern)  # O(m)
    result = []  # O(1)

    s = 0
    while s <= n - m:  # O(n)
        j = m - 1  # O(1)
        while j >= 0 and pattern[j] == text[s + j]:  # O(1)
            j -= 1  # O(1)
        if j < 0:
            result.append(s)  # O(1)
            s += m - bad_char[ord(text[s + m])] if s + m < n else 1  # O(1)
        else:
            s += max(1, j - bad_char[ord(text[s + j])])  # O(1)
    return result


### Rabin-Karp Algorithm ###
# Complexity:
# - Best case: O(n) (when the pattern is not present in the text)
# - Average case: O(n) (when the pattern is present in the text and is different from the text)
# - Worst case: O(n*m) (when the pattern is present in the text and is equal to the text)


def rabin_karp(text, pattern, d=256, q=101):
    n = len(text)  # O(1)
    m = len(pattern)  # O(1)
    h = pow(d, m - 1) % q  # O(1)
    p = 0  # O(1) hash pattern
    t = 0  # O(1) hash texto
    result = []  # O(1)

    for i in range(m):  # O(m)
        p = (d * p + ord(pattern[i])) % q  # O(1)
        t = (d * t + ord(text[i])) % q  # O(1)

    for s in range(n - m + 1):  # O(n)
        if p == t:
            if text[s : s + m] == pattern:  # O(1)
                result.append(s)  # O(1)
        if s < n - m:  # O(1)
            t = (d * (t - ord(text[s]) * h) + ord(text[s + m])) % q  # O(1)
            if t < 0:  # O(1)
                t += q  # O(1)
    return result
