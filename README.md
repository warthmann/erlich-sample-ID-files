# erlich-sample-ID-files

Here we provide scripts to prepare the input files needed by the [TeamErlich/personal-identification-pipeline](https://github.com/TeamErlich/personal-identification-pipeline) from a multi-sample VCF file.

TeamErlich published a software pipeline to quickly (re-)identify samples from Oxford Nanopore data given a sample database: https://github.com/TeamErlich/personal-identification-pipeline

>Sophie Zaaijer, Assaf Gordon, Daniel Speyer, Robert Piccone, Simon Cornelis Groen, Yaniv Erlich (2017)
>Rapid re-identification of human samples using portable DNA sequencing
>eLife 6:e27798, https://doi.org/10.7554/eLife.27798


# Input files for Arabidopsis

Our use case is *Arabidopsis thaliana* and 1,135 sequenced accessions from the [1001genomes project](https://1001genomes.org/). 

>1001 Genomes Consortium
>1,135 Genomes Reveal the Global Pattern of Polymorphism in *Arabidopsis thaliana*
>Cell (2016), 166(2) 481-91. https://doi.org/10.1016/j.cell.2016.05.063


 The 1001genomes project provides a multi-sample VCF file that contains variants for 1,135 Arabidospis accessions called against the TAIR10 genome.

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

Parse the resulting file for the genoypes and split into individual .txt files in *23andme* format, one for each sample. The tasks is parallelised with gnu parallel. Adjust the number of threads in the script!
```

bash produce23andmefile.parallel.sh <file with list of sample names> <output directory> <input vcf/bcf file>
```

Build a list of all variants, assign unique IDs, and augment the 23andme files by adding the ID to each variant. Adjust paths and filenames in the script!
```

python3 generate-dict-and-SNP-IDs.py 
```

# Fast5 files for testing

Sequencing data from a whole genome ONT (rapid) library of *Arabidopsis thaliana* on a Flongle
```

wget https://bss1innov1nafa1poc1.blob.core.windows.net/sample-container/Data-for-github/At-WGS.tar.xz
```


