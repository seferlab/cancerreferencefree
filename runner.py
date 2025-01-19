import blitzgsea as blitz
import pandas as pd

# read signature as pandas dataframe
signature = pd.read_csv("ageing_muscle_gtex.tsv")

# list available gene set libraries in Enrichr
blitz.enrichr.print_libraries()

# use enrichr submodule to retrieve gene set library
library = blitz.enrichr.get_library("KEGG_2021_Human")

# run enrichment analysis
if __name__ == "__main__":  # make sure process is main, when run in a script it can cause errors otherwise
  result = blitz.gsea(signature, library)

import matplotlib
from matplotlib import pyplot as plt

from upsetplot import generate_counts, plot

example = generate_counts()
print(example)

plot(example, sort_by="cardinality")
plt.suptitle("Ordered by cardinality")
plt.show()

from venny4py.venny4py import *

#dict of sets
sets = {
    'Set1': set(list("Harry Potter")),
    'Set2': set(list("Hermione Granger")),
    'Set3': set(list("Ron Weasley")),
    'Set4': set(list("Severus Snape"))
}

venny4py(sets=sets, size=6, dpi=600, out='Example_output', ext='png')


from gseapy import Biomart
bm = Biomart()
# note the dataset and attribute names are different
m2h = bm.query(dataset='mmusculus_gene_ensembl',
               attributes=['ensembl_gene_id','external_gene_name',
                           'hsapiens_homolog_ensembl_gene',
                           'hsapiens_homolog_associated_gene_name'])

h2m = bm.query(dataset='hsapiens_gene_ensembl',
               attributes=['ensembl_gene_id','external_gene_name',
                           'mmusculus_homolog_ensembl_gene',
                           'mmusculus_homolog_associated_gene_name'])
