import pandas as pd 
import numpy as np 

dates = pd.date_range('20190921111630',periods=5)
pd = pd.DataFrame(np.arange(25).reshape((5,5)),index=dates,columns=['A','B','C','D','F'])


pd.to_excel('C:/Users/M/Desktop/输出excel/output.xlsx')

print (pd)
