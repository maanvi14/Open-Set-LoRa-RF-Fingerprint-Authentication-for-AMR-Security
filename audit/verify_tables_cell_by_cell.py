"""
Cell-by-cell verification of all LaTeX tables against source CSVs.
"""
import re, math
import pandas as pd
import numpy as np

def clean_num(s):
    s = s.strip()
    s = re.sub(r'\\textbf\{([^}]+)\}', r'\1', s)
    s = re.sub(r'\\textit\{([^}]+)\}', r'\1', s)
    s = re.sub(r'\\%', '', s)
    s = re.sub(r'\$', '', s)
    s = s.replace('\\', '').replace('+', '').strip()
    if s in ['NaN', 'nan', 'NA', '--']:
        return np.nan
    try:
        return float(s)
    except:
        return s

def verify_all_tables():
    results = {}
    
    # 1. Burst table
    tex = open('paper/tables/tab_burst_aggregation.tex').read()
    csv = pd.read_csv('results/tables/burst_aggregation_summary.csv')
    lines = [l for l in tex.splitlines() if '&' in l and not l.strip().startswith('%') and 'textbf' not in l and 'toprule' not in l and 'midrule' not in l and 'bottomrule' not in l]
    burst_errors = 0
    total_cells = 0
    for idx, row in csv.iterrows():
        parts = [p.strip() for p in lines[idx].split('&')]
        total_cells += 6
        l_tex = int(re.search(r'^\d+', parts[0]).group(0))
        if l_tex != row['burst_length']: burst_errors += 1
        fa = clean_num(parts[1])
        if not math.isclose(fa, row['FAR_A']*100, abs_tol=0.015): burst_errors += 1
        fb = clean_num(parts[2])
        if not math.isclose(fb, row['FAR_B']*100, abs_tol=0.015): burst_errors += 1
        fr = clean_num(parts[3])
        if not math.isclose(fr, row['FRR']*100, abs_tol=0.015): burst_errors += 1
        df = clean_num(parts[4])
        if not math.isclose(df, row['DeltaFAR']*100, abs_tol=0.015): burst_errors += 1
        au = clean_num(parts[5])
        if not math.isclose(au, row['AUROC'], abs_tol=0.0005): burst_errors += 1
    results['tab_burst_aggregation.tex'] = {'errors': burst_errors, 'cells': total_cells}

    # Helper for tables that directly mirror CSVs line-by-line
    def check_mirror(tex_name, csv_path, skip_header_condition):
        tex = open(tex_name).read()
        csv = pd.read_csv(csv_path)
        lines = [l for l in tex.splitlines() if '&' in l and not l.strip().startswith('%') and not skip_header_condition(l) and 'toprule' not in l and 'midrule' not in l and 'bottomrule' not in l]
        errs = 0
        cells = 0
        for idx, row in csv.iterrows():
            parts = [p.strip() for p in lines[idx].split('&')]
            cells += len(parts)
            for c_idx, col in enumerate(csv.columns):
                val_tex = clean_num(parts[c_idx])
                val_csv = row[col]
                if pd.isna(val_tex) and pd.isna(val_csv):
                    continue
                if isinstance(val_csv, (int, float)):
                    if not math.isclose(float(val_tex), float(val_csv), abs_tol=1e-4):
                        errs += 1
                elif str(val_tex) != str(val_csv):
                    errs += 1
        return {'errors': errs, 'cells': cells}

    results['tab_episode_summary.tex'] = check_mirror(
        'paper/tables/tab_episode_summary.tex',
        'results/tables/episode_summary.csv',
        lambda l: 'macro_F1' in l or 'AUROC_B' in l
    )

    results['tab_lopo_bias.tex'] = check_mirror(
        'paper/tables/tab_lopo_bias.tex',
        'results/tables/lopo_bias.csv',
        lambda l: 'abs_error' in l or 'estimator' in l
    )

    results['tab_neighbour_analysis.tex'] = check_mirror(
        'paper/tables/tab_neighbour_analysis.tex',
        'results/tables/neighbour_analysis.csv',
        lambda l: 'device_level_rho' in l or 'nearest_dist' in l
    )

    results['tab_stats_summary.tex'] = check_mirror(
        'paper/tables/tab_stats_summary.tex',
        'results/tables/stats_summary.csv',
        lambda l: 'ci_type' in l or 'p_value' in l
    )

    results['tab_sweep_results.tex'] = check_mirror(
        'paper/tables/tab_sweep_results.tex',
        'results/sweep/sweep_results.csv',
        lambda l: 'tau_matched_frr' in l or 'FRR_matched' in l
    )

    results['tab_threshold_tradeoff.tex'] = check_mirror(
        'paper/tables/tab_threshold_tradeoff.tex',
        'results/tables/threshold_tradeoff.csv',
        lambda l: 'tau_youden' in l or 'FAR_true_youden' in l
    )

    print("=" * 65)
    print(f"{'LaTeX Table':<30} | {'Cells':<6} | {'Mismatches':<10} | {'Status'}")
    print("=" * 65)
    for name, r in results.items():
        status = "PASS (100% cell match)" if r['errors'] == 0 else f"FAIL ({r['errors']} errs)"
        print(f"{name:<30} | {r['cells']:<6} | {r['errors']:<10} | {status}")
    print("=" * 65)

if __name__ == '__main__':
    verify_all_tables()
