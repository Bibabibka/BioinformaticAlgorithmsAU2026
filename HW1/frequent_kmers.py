from neighbors import neighbors


def reverse_complement(pattern: str) -> str:
    s = list(pattern)
    s = s[::-1]
    compl = {"A": "T", "T": "A", "G": "C", "C": "G"}
    s = [compl[i] for i in s]
    return "".join(s)


def frequent_words_with_mismatches_and_reverse_complements(
    text: str, k: int, d: int
) -> list[str]:
    fr = {}
    n = len(text)
    for i in range(n - k + 1):
        word = text[i : i + k]
        for neighbor in neighbors(word, d):
            fr[neighbor] = fr.get(neighbor, 0) + 1
    res = {}
    for word in fr:
        rc_p = reverse_complement(word)
        res[word] = fr[word] + fr.get(rc_p, 0)
    max_res = max(res.values())
    return [word for word, count in res.items() if count == max_res]
