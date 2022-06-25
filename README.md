# erlich-sample-ID-files

Here we provide scripts to prepare the input files needed by the [TeamErlich/personal-identification-pipeline](https://github.com/TeamErlich/personal-identification-pipeline)

TeamErlich published a software pipeline to quickly (re-)identify samples from Oxford Nanopore data given a sample database: https://github.com/TeamErlich/personal-identification-pipeline

>Sophie Zaaijer, Assaf Gordon, Daniel Speyer, Robert Piccone, Simon Cornelis Groen, Yaniv Erlich (2017)
>Rapid re-identification of human samples using portable DNA sequencing
>eLife 6:e27798, https://doi.org/10.7554/eLife.27798


# Input files for Arabidopsis

Our use case is *Arabidopsis thaliana* and we prepare the necessary input files from the variants identified in the 1001genomes project. 

>1001 Genomes Consortium
>1,135 Genomes Reveal the Global Pattern of Polymorphism in *Arabidopsis thaliana*
>Cell (2016), 166(2) 481-91. https://doi.org/10.1016/j.cell.2016.05.063


**TAIR10 genome directory at TAIR**

https://www.arabidopsis.org/download/index-auto.jsp?dir=%2Fdownload_files%2FGenes%2FTAIR10_genome_release%2FTAIR10_chromosome_files

file: *TAIR10_chr_all.fas.gz*


**VCF from 1001 genomes project**

https://1001genomes.org/data/GMI-MPI/releases/v3.1/

file: *1001genomes_snp-short-indel_only_ACGTN.vcf.gz*

We preprocess the VCF file to split multiallelic variants into multiple lines with 
```

bcftools norm -m - <vcf file>
```
