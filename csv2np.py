import pandas as pd
import numpy as np
import ast

def csv2np_fun(filename):
    data = pd.read_csv(filename,delimiter='\t',header=None)
    data = data[0].str.split(',"', expand=True)

    i,j,m,n=0,0,0,0
    m=data.shape[0]
    n=data.shape[1]

    for i in range(m):
        for j in range(n):
            c=data.iloc[i,j]
            # if not None
            if c:
                d=c.replace('"','')
                # str 2 list
                d=ast.literal_eval(d)
                data.loc[i,j]=d
            else:
                continue


    data_np=np.array(data)
    return data_np