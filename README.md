# custom_db

Script used to pull out SNPs present in database and 23andMe file, sort by F_ST, and write top n_snps to gzipped out_file

Package dependencies:
- pandas
- commanderline

custom_db arguments (and defaults if defined):
  --db_gz
  --gt_23andMe_gz
  --n_snps=100000
  --out_file_gz='out_custom_db.txt.gz'

# calc_fst

Helper script to calculate F_ST for Ancestry-format reference files. Output is the input file with an additional column named 'fst' (SNPs with NaN for F_ST are removed)

Details about Ancestry:
https://bitbucket.org/joepickrell/ancestry

Package dependencies:
- pandas
- commanderline

calc_fst arguments (and defaults if defined):
  --ref_gz
  --out_gz='out_db_fst.txt.gz'

# validate_bootstrap

Script that takes into account bootstrap replicates and outputs estimated "super-ancestries". Main input is a text file, where the first line is the .Q output filename of a regular Ancestry run and remaining lines are the .Q files of bootstrap replicates.

Details about Ancestry:
https://bitbucket.org/joepickrell/ancestry

Package dependencies:
- pandas
- commanderline

validate_bootstrap arguments (and defaults if defined):

  --file_list
  
  --negligible_threshold=0.01
  
  --bootstrap_confidence=0.8
  
