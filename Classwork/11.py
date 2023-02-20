
def Levenshtein(a, b, i, j):
    if (i == 0 or j == 0):
        return max(i, j)
    elif (a[i - 1] == b[j - 1]):
        return Levenshtein(a, b, i - 1, j - 1)
    else:
        return 1 + min(Levenshtein(a, b, i - 1, j), Levenshtein(a, b, i, j - 1), Levenshtein(a, b, i - 1, j - 1))