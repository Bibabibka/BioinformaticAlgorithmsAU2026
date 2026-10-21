import random
def random_motifs(dna: list[str],k: int,rng: random.Random) -> list[str]:
    l = []
    for i in dna:
        s = rng.randint(0,len(i)-k)
        l.append(i[s:s+k])
    return l
def profile_randomly_generated_kmer(text: str,k: int,profile: dict[str, list[float]],rng: random.Random) -> str:
    n = len(text)
    km =[]
    pr = []
    for i in range(n-k+1):
        m = text[i:i+k]
        km.append(m)
        v = 1
        for i, n in enumerate(m):
            v = v*profile[n][i]
        pr.append(v)
    res = rng.choices(km,weights=pr, k=1)[0]
    return res
