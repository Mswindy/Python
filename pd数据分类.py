from pandas import Series,DataFrame
import pandas as pd
import numpy as np
from numpy import nan as NA 
#from matplotlib import pyplot as plt
ages = [20,22,25,27,21,23,37,31,61,45,41,32]
#将所有的ages进行分组
bins = [18,25,35,60,100]
#使用pandas中的cut对年龄数据进行分组
cats = pd.cut(ages,bins)

print(cats)
