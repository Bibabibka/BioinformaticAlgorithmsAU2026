def reverse_complement(pattern: str) -> str:
    s = list(pattern)
    s = s[::-1]
    compl = {"A": "T", "T": "A", "G": "C", "C": "G"}
    s = [compl[i] for i in s]
    return "".join(s)