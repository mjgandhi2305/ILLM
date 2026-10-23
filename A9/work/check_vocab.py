
import sys, pyonmttok
path, nrows = sys.argv[1], int(sys.argv[2])
toks = open(path, encoding="utf-8").read().split("\n")[:-1]
sp = ["<unk>", "<blank>", "<s>", "</s>"]
v = pyonmttok.build_vocab_from_tokens(toks, maximum_size=0, special_tokens=sp)
bad = [t for i, t in enumerate(toks) if v[t] != i + len(sp)]
print("   OpenNMT vocab size", len(v), "| matrix rows", nrows, "| misaligned tokens", len(bad))
sys.exit(0 if (len(v) == nrows and not bad) else 1)
