#!/usr/bin/env python3

import commanderline.commander_line as cl
import pandas as pd
import gzip

ancestry_translation = { "ARABIAN" : "NEAREAST",
                         "ASHKENAZI" : "ASHKENAZI-EMED",
                         "BALOCHI-MAKRANI-BRAHUI" : "CASIA",
                         "BANTUKENYA" : "EAFRICA",
                         "BANTUNIGERIA" : "WAFRICA",
                         "BIAKA" : "CAFRICA",
                         "CAFRICA" : "CAFRICA",
                         "CAMBODIA-THAI" : "SEASIA",
                         "CSAMERICA" : "AMERICAS",
                         "CYPRUS-MALTA-SICILY" : "ASHKENAZI-EMED",
                         "EAFRICA" : "EAFRICA",
                         "EASIA" : "EASIA",
                         "EASTSIBERIA" : "NEASIA",
                         "FINNISH" : "NEEUROPE",
                         "GAMBIA" : "WAFRICA",
                         "GUJARAT" : "SASIA",
                         "HADZA" : "EAFRICA",
                         "HAZARA-UYGUR-UZBEK" : "CASIA",
                         "ITALY-BALKANS" : "ITALY-BALKANS",
                         "JAPAN-KOREA" : "EASIA",
                         "KALASH" : "CASIA",
                         "MENDE" : "WAFRICA",
                         "NAFRICA" : "NAFRICA",
                         "NCASIA" : "NCASIA",
                         "NEAREAST" : "NEAREAST",
                         "NEASIA" : "NEASIA",
                         "NEEUROPE" : "NEEUROPE",
                         "NEUROPE" : "NEUROPE",
                         "NGANASAN" : "NEASIA",
                         "OCEANIA" : "OCEANIA",
                         "PATHAN-SINDHI-BURUSHO" : "CASIA",
                         "SAFRICA" : "SAFRICA",
                         "SAMERICA" : "AMERICAS",
                         "SARDINIA" : "SWEUROPE",
                         "SEASIA" : "SEASIA",
                         "SSASIA" : "SASIA",
                         "SWEUROPE" : "SWEUROPE",
                         "TAIWAN" : "SEASIA",
                         "TUBALAR" : "NEASIA",
                         "TURK-IRAN-CAUCASUS" : "TURK-IRAN-CAUCASUS"
}

def validate_bootstrap(file_list, negligible_threshold=0.01, bootstrap_confidence=0.8):
     # first file in file_list is file containing results without bootstrap, remaining files are bootstrap results
     
     results=pd.DataFrame()

     with open(file_list, 'rt') as f_in:
          for i,f in enumerate(f_in):
               f=f.strip()
               d1=pd.read_csv(f, header=None, sep=' ')
               d1['super']=d1[0].apply(lambda el: ancestry_translation[el])
               d2=d1.groupby('super').sum()
               d2.columns=[i]

               results=pd.concat([results, d2], axis=1)

     results=results.dropna(subset=[0])

     bootstrap_replicate_count=results.iloc[:,1:].apply(lambda el: el>=negligible_threshold).T.sum()/(len(results.columns)-1)

     filt=bootstrap_replicate_count.apply(lambda el: el>=bootstrap_confidence)

     interm_results=results[filt][0]

     ambig=1-interm_results.sum()

     final_results=pd.concat([interm_results, pd.Series({'AMBIGUOUS':ambig})])

     print(final_results)

cl.commander_line(validate_bootstrap) if __name__ == '__main__' else None