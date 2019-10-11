import pandas as pd 

people = pd.read_excel('C:\\Users\\M\\Desktop\\python\\计算机学院研究生.xlsx')

x = people.loc[:,['姓名','政治面貌']]

a = x.sort_values(by='政治面貌')
print(a)