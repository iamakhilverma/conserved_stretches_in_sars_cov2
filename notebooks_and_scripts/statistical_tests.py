#!python3

from scipy import stats
import numpy as np

# obs = np.array([[1, 10], [75009, 34991]])
# print(obs.size)

# print(stats.chi2_contingency(obs, correction=False))
# print(stats.chi2_contingency(obs, correction=True))


# # res = stats.barnard_exact([[1, 10], [7501, 3499]], alternative="two-sided", pooled=False)
# # print(res)


# res = stats.fisher_exact([[1, 10], [7545185, 3454815]], alternative="two-sided")
# print(res)

# Values obtained from notebook_02.ipynb
av_zap_motifs_count_seed_A = {
    "mean_zap_motifs": 3.6163,
    "iterations_with_zap_motifs_lt1": 2101,
    "median_zap_motifs": 3.0,
    "stretches_with_zap_motifs_geq1": 75271,
    "stretches_with_zap_motifs_eq0": 34729,
    "mean_gc_content": 38.0304128440367,
    "median_gc_content": 37.99694189602447,
    "stretches_with_gc_geq_ref": 51118,
    "stretches_with_gc_lt_ref": 58882,
    "stretches_with_cpgs_geq_ref": 43676,
    "stretches_with_cpgs_lt_ref": 66324,
}

av_zap_motifs_count_seed_B = {
    "mean_zap_motifs": 3.61815,
    "iterations_with_zap_motifs_lt1": 2096,
    "median_zap_motifs": 3.0,
    "stretches_with_zap_motifs_geq1": 75472,
    "stretches_with_zap_motifs_eq0": 34528,
    "mean_gc_content": 38.01757262996942,
    "median_gc_content": 37.99694189602447,
    "stretches_with_gc_geq_ref": 50798,
    "stretches_with_gc_lt_ref": 59202,
    "stretches_with_cpgs_geq_ref": 43602,
    "stretches_with_cpgs_lt_ref": 66398,
}

av_zap_motifs_count_seed_C = {
    "mean_zap_motifs": 3.6047333333333333,
    "iterations_with_zap_motifs_lt1": 2126,
    "median_zap_motifs": 3.0,
    "stretches_with_zap_motifs_geq1": 74568,
    "stretches_with_zap_motifs_eq0": 35432,
    "mean_gc_content": 38.013037716615706,
    "median_gc_content": 37.99694189602447,
    "stretches_with_gc_geq_ref": 50705,
    "stretches_with_gc_lt_ref": 59295,
    "stretches_with_cpgs_geq_ref": 43528,
    "stretches_with_cpgs_lt_ref": 66472,
}


obs_tuple_dict_randomized = {
    "zap_motifs": ("stretches_with_zap_motifs_geq1", "stretches_with_zap_motifs_eq0"),
    "gc_content": ("stretches_with_gc_geq_ref", "stretches_with_gc_lt_ref"),
    "cpg_o_by_e": ("stretches_with_cpgs_geq_ref", "stretches_with_cpgs_lt_ref"),
}

obs_tuple_dict_cs = {
    "zap_motifs": [1, 10],
    "gc_content": [6, 5],
    "cpg_o_by_e": [6, 5],
}

with open("../other_data_files/statistical_tests_results.txt", "w") as f:
    for rand_, c in zip(
        [
            av_zap_motifs_count_seed_A,
            av_zap_motifs_count_seed_B,
            av_zap_motifs_count_seed_C,
        ],
        ["A", "B", "C"],
    ):
        for (k, (obs1a, obs2a)), (_, (obs1b, obs2b)) in zip(
            obs_tuple_dict_randomized.items(), obs_tuple_dict_cs.items()
        ):
            f.write(f"For Seed {c}, {k=}, [{obs1b=}, {obs2b=}], and {rand_=}:\n\n")
            obs = np.array([[obs1b, obs2b], [rand_[obs1a], rand_[obs2a],],])

            f.write(f"\t- {stats.chi2_contingency(obs, correction=False)=}\n")
            f.write(f"\t- {stats.chi2_contingency(obs, correction=True)=}\n")

            res_fisher = stats.fisher_exact(
                [[obs1b, obs2b], [rand_[obs1a], rand_[obs2a],],],
                alternative="two-sided",
            )
            f.write(f"\t- stats.fisher_exact(two-sided): {res_fisher=}\n")

            # res_barnard = stats.barnard_exact(
            #     [[obs1b, obs2b], [rand_[obs1a], rand_[obs2a],],],
            #     alternative="two-sided",
            #     pooled=False,
            # )
            # f.write(
            #     f"\t- stats.barnard_exact(pooled=False, two-sided): {res_barnard=}\n"
            # )

            f.write("\n\n")
