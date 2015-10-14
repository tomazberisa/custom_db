#!/usr/bin/env python3

import commanderline.commander_line as cl
import pandas as pd
import gzip

def custom_db(db_gz, gt_23andMe_gz, n_snps=100000, out_file_gz='out_custom_db.txt.gz'):
    '''
+-----------+
| custom_db |
+-----------+

Script used to pull out SNPs present in database and 23andMe file, sort by F_ST, and write top n_snps to gzipped out_file

Package dependencies:
pandas
commanderline
'''
    print('Reading database...')
    db=pd.read_csv(db_gz, compression='gzip', sep=' ')
    print('Reading 23andMe file...')
    gt=pd.read_csv(gt_23andMe_gz, compression='gzip', usecols=[1,2], sep='\t', comment='#', header=None)
    gt.columns=['chr','pos']
    print('Merging...')
    m=pd.merge(db, gt, on=['chr','pos'])
    print('Sorting by F_ST...')
    m=m.sort_values(by='fst', ascending=False)
    print('Filtering...')
    m_out=m.iloc[:n_snps, :(len(m.columns)-1)]
    print('Sorting by chr & pos, and writing to file...')
    with gzip.open(out_file_gz, 'wt') as f_out:
        m_out.sort_values(by=['chr','pos']).to_csv(f_out, sep=' ', index=False)

cl.commander_line(custom_db) if __name__ == '__main__' else None
