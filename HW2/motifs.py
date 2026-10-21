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
def gibbs_sampler(dna: list[str],k: int,n_iterations: int,rng: random.Random) -> list[str]:
    t = len(dna)
    ba = "ACGT"

    def score(ms):
        return sum(len(ms) - max(col.count(b) for b in ba)for col in zip(*ms))
    motifs = [s[(p := rng.randrange(len(s) - k + 1)):p + k] for s in dna]
    best_m = motifs[:]
    best_sc = score(motifs)

    for _ in range(n_iterations):
        i = rng.randrange(t)
        rest = motifs[:i] + motifs[i + 1:]
        pr = [{b: (col.count(b) + 1) / (t - 1 + 4) for b in ba} for col in zip(*rest)]
        km = [dna[i][j:j + k] for j in range(len(dna[i]) - k + 1)]
        weights = []
        for i in km:
            p = 1.0
            for pos, b in enumerate(i):
                p *= pr[pos][b]
            weights.append(p)

        motifs[i] = rng.choices(km, weights=weights)[0]

        if (s := score(motifs)) < best_sc:
            best_m = motifs[:]
            best_sc = s

    return best_m