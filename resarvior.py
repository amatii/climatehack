import json
import numpy as np
import pandas as pd
from operator import itemgetter
import matplotlib.pyplot as plt


df = pd.read_csv('reservoir.csv',sep=',')
print(df[df['id']=='ANT'])

exit()
filename= "reservoir.json"
with open(filename, 'r') as infile: 
	data  = json.load(infile)
print(data)
