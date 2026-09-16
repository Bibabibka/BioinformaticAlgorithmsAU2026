def hamming_distance(first: str, second: str) -> int:
    return sum(f != s for f, s in zip(first, second))


def neighbors(pattern: str, d: int) -> set[str]:
    res = {pattern}
    alph = ["A", "C", "G", "T"]

    for _ in range(d):
        new_n = set()
        for seq in res:
            chars = list(seq)
            for i, orig_char in enumerate(chars):
                for char in alph:
                    if char != orig_char:
                        chars[i] = char
                        new_n.add("".join(chars))
                chars[i] = orig_char
        res.update(new_n)

    return res