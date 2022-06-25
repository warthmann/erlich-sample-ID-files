##The erlich pipeline will only accept biallelic SNPs. 
##A biallelic vcf file should be produced upstream with 'bcftools norm -m -', indels are purged in the script below.
##you will need to provide a txt file ('listofsamplenamesfile') listing sample names to extract into 23 and me format from your VCF file.
## such file can be produced with 'bcftools query -l'
## the erlich pipline wants the suffix .txt, the outputdirectory must exist!
## usage: produce23andmefile.parallel.sh listofsamplenamesfile outputdirectory vcffile
## e.g. bash bash/produce23andmefile.parallel.sh bash/losamplenames.txt 23andmefiles/ vcf/1001genomes_snp-short-indel_only_ACGTN.multiallelic-split.vcf.gz

los=$1
outdir=$2
vcf=$3

cat $los \
| parallel --jobs 30 \
" \
bcftools query \
-s {} \
-f '%ID\t%CHROM\t%POS\t[%TGT]\n' \
-i 'GT=\"alt\" && TYPE=\"SNP\" ' \
$vcf \
|  sed 's+|++g;s+/++g' \
> $outdir/{}.23.txt \
"

