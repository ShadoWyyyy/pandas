import pandas as pd
import numpy as np

df = pd.read_csv('/Users/chengjintao/Downloads/novel/indel.annovar.hg38_multianno.txt', delimiter = "\t")

for i in df.columns:
    if "ExAC" in i:
        for j in df.index:
            if df.at[j,i] == '.':
                df.at[j,i] = df.at[j,i].replace('.', '0')
        df = df.astype({i: float}, errors='raise')

import collections
print(df.dtypes)

exon = df[df['Func.ensGene'].str.contains('exonic') & df['Func.refGene'].str.contains('exonic') & df['Func.knownGene'].str.contains('exonic')]
clean_exon = exon[~exon['Func.ensGene'].str.contains('RNA') & ~exon['Func.refGene'].str.contains('RNA')& ~exon['Func.knownGene'].str.contains('RNA')]
clean_exon = clean_exon[~clean_exon['ExonicFunc.refGene'].str.contains('unknown') & ~clean_exon['ExonicFunc.refGene'].str.contains('\.')]
low_AF = clean_exon[(clean_exon['ExAC_ALL'] < 0.001) & (clean_exon['ExAC_EAS'] < 0.001)]
AF = clean_exon[(clean_exon['ExAC_ALL'] < 0.01) & (clean_exon['ExAC_EAS'] < 0.01)]
pathogenic_possible = AF[~AF['CLNSIG'].str.contains('enign')]
unknown = pathogenic_possible[pathogenic_possible['CLNALLELEID'] == '.']

df1 = pd.read_csv('/Users/chengjintao/Downloads/novel/snp.annovar.hg38_multianno.txt', delimiter = "\t")
for i in df1.columns:
    if "ExAC" in i:
        for j in df1.index:
            if df1.at[j,i] == '.':
                df1.at[j,i] = df1.at[j,i].replace('.', '0')
        df1 = df1.astype({i: float}, errors='raise')
    elif "EAS.sites" in i:
        for j in df1.index:
            if df1.at[j,i] == '.':
                df1.at[j,i] = df1.at[j,i].replace('.', '0')
        df1 = df1.astype({i: float}, errors='raise')
    elif "dbscSNV" in i:
        for j in df1.index:
            if df1.at[j,i] == '.':
                df1.at[j,i] = df1.at[j,i].replace('.', '0')
        df1 = df1.astype({i: float}, errors='raise')
    elif "gnomAD" in i:
        for j in df1.index:
            if df1.at[j,i] == '.':
                df1.at[j,i] = df1.at[j,i].replace('.', '0')
        df1 = df1.astype({i: float}, errors='raise')

for i in df1.columns:
    if "esp" in i:
        for j in df1.index:
            if df1.at[j,i] == '.':
                df1.at[j,i] = df1.at[j,i].replace('.', '0')
        df1 = df1.astype({i: float}, errors='raise')

exon1 = df1[df1['Func.ensGene'].str.contains('exonic') & df1['Func.refGene'].str.contains('exonic') & df1['Func.knownGene'].str.contains('exonic')]
clean_exon1 = exon1[~exon1['Func.ensGene'].str.contains('RNA') & ~exon1['Func.refGene'].str.contains('RNA')& ~exon1['Func.knownGene'].str.contains('RNA')]
clean_exon1 = clean_exon1[~(clean_exon1['ExonicFunc.ensGene'] == 'synonymous SNV') & ~(clean_exon1['ExonicFunc.refGene'] == 'synonymous SNV') & ~(clean_exon1['ExonicFunc.knownGene'] == 'synonymous SNV')]
clean_exon1 = clean_exon1[~(clean_exon1['ExonicFunc.ensGene'] == 'unknown') & ~(clean_exon1['ExonicFunc.refGene'] == 'unknown') & ~(clean_exon1['ExonicFunc.knownGene'] == 'unknown')]
clean_exon1 = clean_exon1[~(clean_exon1['ExonicFunc.ensGene'] == '\.') & ~(clean_exon1['ExonicFunc.refGene'] == '\.') & ~(clean_exon1['ExonicFunc.knownGene'] == '\.')]

low_AF = clean_exon1[(clean_exon1['EAS.sites.2015_08'] < 0.001) & (clean_exon1['gnomAD_exome_ALL'] < 0.001) & (clean_exon1['gnomAD_exome_EAS'] < 0.001) & (clean_exon1['esp6500siv2_all'] < 0.001) & (clean_exon1['ExAC_ALL'] < 0.001) & (clean_exon1['ExAC_EAS'] < 0.001)]
AF = clean_exon1[(clean_exon1['EAS.sites.2015_08'] < 0.01) & (clean_exon1['gnomAD_exome_ALL'] < 0.01) & (clean_exon1['gnomAD_exome_EAS'] < 0.01) & (clean_exon1['esp6500siv2_all'] < 0.01) & (clean_exon1['ExAC_ALL'] < 0.01) & (clean_exon1['ExAC_EAS'] < 0.01)]

pathogenic_possible1 = AF[~AF['CLNSIG'].str.contains('enign')]
effect = pathogenic_possible1[~(pathogenic_possible1['ExonicFunc.ensGene'] == 'synonymous SNV') & ~(pathogenic_possible1['ExonicFunc.refGene'] == 'synonymous SNV') & ~(pathogenic_possible1['ExonicFunc.knownGene'] == 'synonymous SNV')]

effect.to_csv("/Users/chengjintao/Downloads/snp_filtered_0810.tsv", sep="\t", index=False)

pathogenic_possible.to_csv("/Users/chengjintao/Downloads/indel_filtered_0810.tsv", sep="\t", index=False)

###################################################################################################################################

df = pd.read_csv('/Users/chengjintao/Downloads/novel/snp_0810.txt', delimiter = "\t")
recessive = df[(df['Daughter'].str.startswith('1/1') | df['Daughter'].str.startswith('1|1')) & (df['Dad'].str.startswith('1/1') | df['Dad'].str.startswith('1|1'))]
recessive1 = recessive[(~recessive['Mom'].str.startswith('1/1')) & (~recessive['Mom'].str.startswith('1|1'))]
recessive2 = recessive1[(~recessive1['Grandma'].str.startswith('1/1')) & (~recessive1['Grandma'].str.startswith('1|1'))]
recessive3 = recessive2[(~recessive1['Grandpa'].str.startswith('1/1')) & (~recessive2['Grandpa'].str.startswith('1|1'))]

recessive3.to_csv("/Users/chengjintao/Downloads/snp_recessive.txt", sep="\t", index=False)

het = df[(df['Daughter'].str.startswith('1/2') | df['Daughter'].str.startswith('1|2'))]

de_novo = df[(df['Daughter'].str.startswith('0/1') | df['Daughter'].str.startswith('0|1')) & (df['Dad'].str.startswith('0/1') | df['Dad'].str.startswith('0|1'))]
de_novo1 = de_novo[(de_novo['Mom'].str.startswith('0/0') | de_novo['Mom'].str.startswith('0|0'))]
de_novo2 = de_novo1[(~de_novo1['Grandma'].str.startswith('1/1')) & (~de_novo1['Grandma'].str.startswith('1|1'))]
de_novo3 = de_novo2[(~de_novo2['Grandpa'].str.startswith('1/1')) & (~de_novo2['Grandpa'].str.startswith('1|1'))]
de_novo4 = de_novo3[(de_novo3['Grandma'].str.startswith('0/0') | de_novo3['Grandma'].str.startswith('0|0'))]
de_novo5 = de_novo4[(de_novo4['Grandpa'].str.startswith('0/0') | de_novo4['Grandpa'].str.startswith('0|0'))]

cli_type = set(de_novo3['CLNSIG'])
dominant = de_novo3[de_novo3['CLNSIG'] == "Pathogenic"]

de_novo5.to_csv("/Users/chengjintao/Downloads/novel/de_novo.txt", sep="\t", index=False)
dominant.to_csv("/Users/chengjintao/Downloads/snp_dominant.txt", sep="\t", index=False)

splice = df[(df['dbscSNV_ADA_SCORE'] > 0.5) & (df['dbscSNV_RF_SCORE'] > 0.5)]
splice.to_csv("/Users/chengjintao/Downloads/novel/splice.txt", sep="\t", index=False)


df = pd.read_csv('/Users/chengjintao/Downloads/novel/indel_0810.txt', delimiter = "\t")
recessive = df[(df['Daughter'].str.startswith('1/1') | df['Daughter'].str.startswith('1|1')) & (df['Dad'].str.startswith('1/1') | df['Dad'].str.startswith('1|1'))]
recessive1 = recessive[(~recessive['Mom'].str.startswith('1/1')) & (~recessive['Mom'].str.startswith('1|1'))]
recessive2 = recessive1[(~recessive1['Grandma'].str.startswith('1/1')) & (~recessive1['Grandma'].str.startswith('1|1'))]
recessive3 = recessive2[(~recessive1['Grandpa'].str.startswith('1/1')) & (~recessive2['Grandpa'].str.startswith('1|1'))]

het = df[(df['Daughter'].str.startswith('1/2') | df['Daughter'].str.startswith('1|2'))]
de_novo = df[(df['Daughter'].str.startswith('0/1') | df['Daughter'].str.startswith('0|1')) & (df['Dad'].str.startswith('0/1') | df['Dad'].str.startswith('0|1'))]
de_novo1 = de_novo[(de_novo['Mom'].str.startswith('0/0') | de_novo['Mom'].str.startswith('0|0'))]
de_novo2 = de_novo1[(~de_novo1['Grandma'].str.startswith('1/1')) & (~de_novo1['Grandma'].str.startswith('1|1'))]
de_novo3 = de_novo2[(~de_novo2['Grandpa'].str.startswith('1/1')) & (~de_novo2['Grandpa'].str.startswith('1|1'))]
de_novo4 = de_novo3[(de_novo3['Grandma'].str.startswith('0/0') | de_novo3['Grandma'].str.startswith('0|0'))]
de_novo5 = de_novo4[(de_novo4['Grandpa'].str.startswith('0/0') | de_novo4['Grandpa'].str.startswith('0|0'))]

de_novo3.to_csv("/Users/chengjintao/Downloads/dominant.txt", sep="\t", index=False)

