
def Levenshtein(a, b, i, j):
    if (i == 0 or j == 0):
        return max(i, j)