# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 22:54:50 2016

@author: cwal3
"""

import pandas as pd
#import ploty
import pdb


df = pd.read_csv('epa_data\\dfiles.csv', index_col=False)
print df.columns
#pdb.set_trace()