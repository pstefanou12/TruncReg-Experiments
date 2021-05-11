import subprocess
import torch as ch
import pandas as pd 
import numpy as np
import csv
import json

# commands and arguemnts
command = 'Rscript'
path2script = '/Users/patroklos/TruncReg-Experiments/TruncReg Script.R'

# variable number of args in list 
args = ['-10', 'left']

X = ch.randn(2, 2) 
y = ch.randn(2, 1)

# save data to csv
concat = ch.cat([X, y], dim=1)
concat_np = concat.numpy() 

"""
DATA FORMAT: 
    -First n-1 columns are independent variables 
    -nth column is dependent variable
"""
concat_df = pd.DataFrame(concat_np)
concat_df.to_csv('data.csv')

# build subprocess 
"""
Arguments 
- c - truncation point (float) 
- dir - left or right -> type of truncation (str) 
"""
cmd = [command, path2script] + args 

# check_output will run the command and store the result
result = subprocess.check_output(cmd, universal_newlines=True)

print("result:\n ", result)
