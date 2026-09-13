import math
import sys, os
sys.path.insert(0, os.environ.get('PKG_DIR', ''))
from dsqi.features import seq_features
from dsqi.validate import boot_ci, spearman_ci

def test_entropy_bounds():
    assert seq_features('ACGT')['entropy'] <= 2 + 1e-9
    assert seq_features('AAAA')['entropy'] == 0

def test_gc_range():
    assert 0 <= seq_features('ACGTACGT')['gc_content'] <= 1
    assert seq_features('GGCC')['gc_content'] == 1

def test_homopolymer():
    assert seq_features('ACGTAAAAACGT')['homopolymer_max'] == 5
    assert seq_features('ACGT')['homopolymer_max'] == 1

def test_u3():
    f = seq_features('ACGTAC')
    assert 0 < f['uniq3_ratio'] <= 1

def test_boot_ci_contains_mean():
    lo, hi = boot_ci(list(range(100)), seed=1)
    assert lo < 49.5 < hi

def test_spearman_ci_orders():
    x = list(range(50)); y = [v * 2 for v in x]
    r, p, lo, hi = spearman_ci(x, y)
    assert r > 0.99 and lo <= r <= hi
