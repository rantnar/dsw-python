import re

def knuth_morris_pratt(text, pattern):
    pattern_length = len(pattern)
    text_length = len(text)

    lps = [0]*pattern_length
    j = 0

    compute_lps_array(pattern, pattern_length, lps)

    i = 0
    while i < text_length:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == pattern_length:
            return i-j
            j = lps[j-1]

        elif i < text_length and pattern[j] != text[i]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1

    return -1

def compute_lps_array(pattern, pattern_length, lps):
    length = 0
    lps[0]
    i = 1

    while i < pattern_length:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length-1]
            else:
                lps[i] = 0
                i += 1

def boyer_moore(text, pattern):
    m = len(pattern)
    n = len(text)

    badChar = badCharHeuristic(pattern, m)

    s = 0
    while(s <= n-m):
        j = m-1

        while j>=0 and pattern[j] == text[s+j]:
            j -= 1

        if j < 0:
            return s
        else:
            s += max(1, j-badChar[ord(text[s+j])])

    return -1

def badCharHeuristic(string, size):
    NO_OF_CHARS = 256

    badChar = [-1]*NO_OF_CHARS

    for i in range(size):
        badChar[ord(string[i])] = i;

    return badChar


def regex_search(text, pattern):
    return re.findall(pattern, text)