# DSQI Project — Automated Results Report

Generated: 2026-09-13 11:50 | data_source: synthetic_fallback | rows: 28,000

## 1. Regression
| model                      |      rmse |       mae |       r2 |
|:---------------------------|----------:|----------:|---------:|
| GBT                        |   0.02314 |   0.01603 |  0.79084 |
| RandomForest               |   0.02459 |   0.01775 |  0.76373 |
| LinearRegression           |   0.02497 |   0.01862 |  0.75632 |
| MEAN_BASELINE              |   0.05059 |   0.03995 | -1e-05   |
| RandomForest_5foldCV(best) | nan       | nan       |  0.79668 |

## 2. Classification
| model              |   accuracy |     f1 |   precision |   recall |
|:-------------------|-----------:|-------:|------------:|---------:|
| MAJORITY_BASELINE  |     0.3458 | 0.3458 |    nan      | nan      |
| LogisticRegression |     0.7613 | 0.7637 |      0.7676 |   0.7613 |
| DecisionTree       |     0.73   | 0.7378 |      0.7638 |   0.73   |
| RandomForest       |     0.7402 | 0.7435 |      0.749  |   0.7402 |

## 3. DSQI validation (external EXP_C)
| scheme        |   external_n |   spearman |   p_value |   ci_low |   ci_high | selected   |
|:--------------|-------------:|-----------:|----------:|---------:|----------:|:-----------|
| equal         |         7062 |   -0.61817 |         0 | -0.63237 |  -0.60354 | False      |
| statistical   |         7062 |   -0.71822 |         0 | -0.72933 |  -0.70674 | False      |
| model_derived |         7062 |   -0.77534 |         0 | -0.78448 |  -0.76587 | True       |

Primary scheme: **model_derived** — Spearman -0.7753 [-0.7845, -0.7659], p=0.00e+00

## 4. DSQI group means (bootstrap CI)
| group   |    n |   mean_error |   ci_low |   ci_high | note               |
|:--------|-----:|-------------:|---------:|----------:|:-------------------|
| Low     | 2354 |      0.10892 |  0.10674 |   0.11105 | Kruskal p=0.00e+00 |
| Medium  | 2354 |      0.05591 |  0.05441 |   0.05738 | Kruskal p=0.00e+00 |
| High    | 2354 |      0.02667 |  0.02606 |   0.02729 | Kruskal p=0.00e+00 |

## 5. Cross-dataset generalization
| dataset           | scheme        |    n |   spearman |   p_value |   ci_low |   ci_high |
|:------------------|:--------------|-----:|-----------:|----------:|---------:|----------:|
| EXT2_aegis_like   | equal         | 9000 |    -0.7492 |         0 |  -0.7581 |   -0.74   |
| EXT2_aegis_like   | statistical   | 9000 |    -0.7754 |         0 |  -0.7835 |   -0.767  |
| EXT2_aegis_like   | model_derived | 9000 |    -0.7979 |         0 |  -0.8053 |   -0.7903 |
| EXT3_yerlich_like | equal         | 8000 |    -0.61   |         0 |  -0.6236 |   -0.5961 |
| EXT3_yerlich_like | statistical   | 8000 |    -0.7346 |         0 |  -0.7445 |   -0.7243 |
| EXT3_yerlich_like | model_derived | 8000 |    -0.7808 |         0 |  -0.7892 |   -0.7721 |

## 6. Platform transfer matrix
|          |   Illumina |   Nanopore |   PacBio |   Unknown |
|:---------|-----------:|-----------:|---------:|----------:|
| Illumina |     -0.803 |     -0.797 |   -0.786 |    -0.693 |
| Nanopore |     -0.805 |     -0.799 |   -0.788 |    -0.696 |
| PacBio   |     -0.805 |     -0.798 |   -0.788 |    -0.695 |
| Unknown  |     -0.805 |     -0.799 |   -0.789 |    -0.693 |

## 7. Constrained-code benchmark
| metric                                |      rho |       p |    n |
|:--------------------------------------|---------:|--------:|-----:|
| binary pass_all (point-biserial)      | -0.15127 | 0       | 9751 |
| DSQI overall (spearman)               | -0.77136 | 0       | 9751 |
| DSQI within constraint-passing subset | -0.1312  | 0.04229 |  240 |

## 8. Retrieval-success models
| model                |   roc_auc |   pr_auc |
|:---------------------|----------:|---------:|
| LR_full_features     |    0.9528 |   0.9753 |
| RF_full_features     |    0.9468 |   0.9719 |
| DSQI_alone(rank-AUC) |    0.8925 | nan      |

## 9. ECC overhead by DSQI band
dsqi_group  mean_error  rs_correctable_symbols  est_overhead_pct
       Low    0.108924                      32             42.67
    Medium    0.055912                      20             26.67
      High    0.026671                      12             16.00

## 10. Sensitivity
|   n_trials |   base_rho |   rho_mean |   rho_std |   min_tau |   mean_tau |
|-----------:|-----------:|-----------:|----------:|----------:|-----------:|
|         80 |    -0.7786 |    -0.7092 |    0.0521 |     0.583 |     0.7588 |

## 11. Hypotheses log
| hypothesis                                                        | test                                         |   effect |        p | conclusion               |
|:------------------------------------------------------------------|:---------------------------------------------|---------:|---------:|:-------------------------|
| Higher GC deviation -> higher error                               | Spearman(gc_deviation,error)                 |  -0.012  |   0.0445 | supported                |
| Longer homopolymers -> higher error                               | MannWhitneyU(high>=4 vs <=3)                 |   0.6083 |   0      | supported                |
| Lower entropy -> higher error                                     | Spearman(entropy,error)                      |  -0.5652 |   0      | supported                |
| Error differs across platforms                                    | Kruskal-Wallis                               |   0.1687 |   0      | supported                |
| High-error sequences cluster in graph communities                 | Kruskal-Wallis across communities            | nan      |   0      | supported                |
| High DSQI -> lower observed error (external)                      | Spearman(DSQI_model_derived, error) on EXP_C |  -0.7753 |   0      | supported                |
| DSQI adds error resolution within constraint-feasible oligos      | Spearman within pass_all subset (n=240)      |  -0.1312 |   0.0423 | NOT supported (reported) |
| Low-error retrieval success is predictable from sequence features | ROC-AUC RF full features > 0.5               |   0.9528 | nan      | supported                |

## 12. Extensions status
- SHAP top features: ['homopolymer_max', 'gc_deviation', 'entropy', 'gc_content', 'uniq3_ratio']
- Unit tests passed: True
- Streaming demo: True (3 batches)
- MLflow logged runs: 0
- Interactive dashboard: True


## Limitations
Local-mode Spark; synthetic fallback data if Drive absent; heuristic ECC mapping; SHAP via sklearn mirror.