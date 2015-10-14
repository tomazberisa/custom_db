#!/usr/bin/env python3

import commanderline.commander_line as cl
import pandas as pd
import gzip

def fst(row):
    a1=row.apply(lambda el: int(el.split(',')[0]))
    a2=row.apply(lambda el: int(el.split(',')[1]))
    p=a1/(a1+a2)
    p_mean=sum(a1)/(sum(a1)+sum(a2))
    c=(a1+a2)/(sum(a1)+sum(a2))

    pq2=(2*p_mean*(1-p_mean))
    
    fst_val=(pq2-sum(c*2*p*(1-p)))/pq2

    return fst_val

def calc_fst(ref_gz, out_gz='out_db_fst.txt.gz'):
    '''
+----------+
| calc_fst |
+----------+

Helper script to calculate F_ST for Ancestry-format reference files. Output is the input file with an additional column named 'fst'

Details about Ancestry:
https://bitbucket.org/joepickrell/ancestry

Package dependencies:
pandas
commanderline
'''
    print('Reading Ancestry-format reference file...')
    d=pd.read_csv(ref_gz, sep=' ')
    # Drop null columns, e.g., last column followed by a column delimiter will result in a null column
    d=d.dropna(axis=1,how='all')
    print('Calculatng F_ST...')
    d['fst']=d.iloc[:,6:].apply(fst, axis=1) 
    # Drop SNPs without F_ST
    d=d.dropna(subset=['fst'])
    print('Writing output file...')
    with gzip.open(out_gz, 'wt') as f_out:
        d.to_csv(f_out, sep=' ', index=False)

cl.commander_line(calc_fst) if __name__ == '__main__' else None

