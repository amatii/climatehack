import json
import numpy as np
import pandas as pd
from operator import itemgetter
import matplotlib.pyplot as plt


df = pd.read_csv('reservoir.csv',sep=',')



print(df[df['id']=='ANT'])

#exit()
plt.figure()
fig, ax = plt.subplots(figsize=(8,6))

for Rid in ['ANT','ALM']:
	temp = df[df['id']==Rid]
	temp.plot(x='date',y='storage',ax=ax)

plt.legend(loc='best')
plt.savefig('./figures/'+'1.pdf', format='pdf')
plt.close() 
exit()

