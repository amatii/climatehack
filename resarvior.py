import json
import numpy as np
import pandas as pd
from operator import itemgetter
import matplotlib.pyplot as plt


df = pd.read_csv('reservoir.csv',sep=',')

print(df[df['id']=='ANT'])

def generate_fig(df,id_list,f,N):
	plt.figure()
	fig, ax = plt.subplots(figsize=(8,6))
	data = df[df['id'].isin(id_list[0:N])]
	
	for label, temp in data.groupby('id'):
		temp.plot(x='date',y=f,ax=ax)

	plt.legend(loc='best')
	plt.savefig('./figures/'+f+'.pdf', format='pdf')
	plt.close() 

def filter_data(df,N):
	id_list = list(set(df['id']));
	temp=[]
	temp1=[]
	filtered_df=df
	for Rid in id_list:
		if df[df['id']==Rid].shape[0]<N:
			print(df[df['id']==Rid].shape[0])
			temp.append(df[df['id']==Rid].shape[0])
			temp1.append(Rid)
	
	filtered_df= df[df['id'].isin(temp1)]
	print(len(temp))
	return (filtered_df)
N=10
tre=690
fdf=filter_data(df,tre)
id_list = list(set(fdf['id']));
generate_fig(fdf,id_list,'capacity',N)
generate_fig(fdf,id_list,'storage',N)

exit()

