import random


def random_motifs(dna: list[str], k: int, rng: random.Random) -> list[str]:
    l = []
    for s in dna:
        p = rng.randint(0, len(s) - k)
        l.append(s[p:p + k])
    return l


def profile_randomly_generated_kmer(text: str, k: int, profile: dict[str, list[float]], rng: random.Random) -> str:
    km = []
    pr = []
    for i in range(len(text) - k + 1):
        m = text[i:i + k]
        km.append(m)
        v = 1.0
        for pos, b in enumerate(m):
            v *= profile[b][pos]
        pr.append(v)
    return rng.choices(km, weights=pr, k=1)[0]


def score(ms: list[str]) -> int:
    return sum(len(ms) - max(col.count(b) for b in "ACGT") for col in zip(*ms))


def gibbs_sampler(dna: list[str], k: int, n_iterations: int, rng: random.Random) -> list[str]:
    t = len(dna)
    motifs = random_motifs(dna, k, rng)
    best_m = motifs[:]
    best_sc = score(motifs)

    for _ in range(n_iterations):
        i = rng.randrange(t)
        rest = motifs[:i] + motifs[i + 1:]
        pr = {b: [(col.count(b) + 1) / (t - 1 + 4) for col in zip(*rest)] for b in "ACGT"}
        motifs[i] = profile_randomly_generated_kmer(dna[i], k, pr, rng)

        if (s := score(motifs)) < best_sc:
            best_m = motifs[:]
            best_sc = s

    return best_m


def repeated_gibbs_sampler(dna: list[str], k: int, n_iterations: int, n_restarts: int, seed: int) -> tuple[list[str], list[int]]:
    rng = random.Random(seed)
    gl_mo = None
    gl_sc = float('inf')
    all_sc = []

    for _ in range(n_restarts):
        cur_m = gibbs_sampler(dna, k, n_iterations, rng)
        cur_sc = score(cur_m)
        all_sc.append(cur_sc)

        if cur_sc < gl_sc:
            gl_sc = cur_sc
            gl_mo = list(cur_m)

    return gl_mo, all_sc


k = 8
n_iterations = 200
n_restarts = 30
seed = 42
dna = """CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA
GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG
TAGTACCGAGACCGAAAGAAGTATACAGGCGT
TAGATCAAGTTTCAGGTGCACGTCGGTGAACC
AATCCACCAGCTCCACGTGCAATGTTGGCCTA""".split()

motifs, scores = repeated_gibbs_sampler(dna, k, n_iterations, n_restarts, seed)
print("\n".join(motifs))
print(f"\nBest score: {min(scores)}")
print(f"Scores: {scores}")

motifs2, scores2 = repeated_gibbs_sampler(dna, k, n_iterations, n_restarts, seed)
if motifs == motifs2 and scores == scores2:
    print("Все хорошо")