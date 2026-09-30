def check_if_anagrams(str1, str2, *, ignore_case=False):
    if len(str1) != len(str2):
        return False
    
    if ignore_case:
        str1, str2 = str1.lower(), str2.lower()

    d = {}
    for idx in range(len(str1)):
        c1, c2 = str1[idx], str2[idx]
        d[c1] = d.get(c1, 0) + 1
        d[c2] = d.get(c2, 0) - 1

    return all(val == 0 for val in d.values())