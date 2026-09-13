import numpy as np

def spearman_ci(x, y, alpha=0.05):
    from scipy import stats as st
    r, p = st.spearmanr(x, y)
    z = np.arctanh(r); se = 1 / np.sqrt(len(x) - 3)
    za = st.norm.ppf(1 - alpha / 2)
    return float(r), float(p), float(np.tanh(z - za * se)), float(np.tanh(z + za * se))

def boot_ci(v, B=500, seed=42):
    rng = np.random.default_rng(seed)
    idx = rng.integers(0, len(v), (B, len(v)))
    means = np.asarray(v)[idx].mean(axis=1)
    return np.percentile(means, [2.5, 97.5])
