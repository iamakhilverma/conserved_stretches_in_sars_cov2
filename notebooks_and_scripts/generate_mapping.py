#!python3

"""
Author: "Akhil Kumar"
Email: "akhil.kumar@alumni.iitd.ac.in"

This script maps each NT's post-alignment position in
the genome to its position in the reference genome before
alignment using an input file prepost_sars_cov2_ref_seq.fasta
which has both pre- and post-alignment versions of reference
genome.
"""


import itertools
import pandas as pd


seqArray = []

with open("../seq_data_files/prepost_sars_cov2_ref_seq.fasta") as infile:
    for line1, line2 in itertools.zip_longest(*[infile] * 2):
        seqArray.append(line2.replace("\n", "").upper())

seqArray = [i for i in seqArray[-1]] # list(seqArray[-1])

df_mapping = pd.DataFrame(seqArray, columns=["aligned_seq"])
df_mapping["aligned_number"] = df_mapping.apply(lambda x: x.index + 1)


for row in df_mapping.itertuples():
    if row.aligned_seq == "-":
        if row.Index == 0:
            count = [0]
        else:
            count.append(count[-1])
    else:
        if row.Index == 0:
            count = [1]
        else:
            count.append(count[-1] + 1)

df_mapping["pre_aligned_number"] = count
df_mapping["pre_aligned_number"] = df_mapping.apply(
    lambda x: "Ins: "
    + str(x["pre_aligned_number"])
    + ", pa: "
    + str(x["aligned_number"])
    if x["aligned_seq"] == "-"
    else x["pre_aligned_number"],
    axis=1,
)

df_mapping.to_excel("../other_data_files/mapping.xlsx", index=False)
