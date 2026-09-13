import math
from collections import Counter

def seq_features(s):
    c = Counter(s); n = len(s)
    gc = (c.get('G', 0) + c.get('C', 0)) / n
    hp = cur = 1
    for i in range(1, n):
        cur = cur + 1 if s[i] == s[i - 1] else 1
        hp = max(hp, cur)
    ent = -sum((v / n) * math.log2(v / n) for v in c.values())
    k = 3
    ks = {s[i:i + k] for i in range(n - k + 1)}
    u3 = len(ks) / max(1, n - k + 1)
    return dict(length=n, gc_content=gc, homopolymer_max=hp,
                entropy=ent, uniq3_ratio=u3, repeat_ratio=1 - u3)
