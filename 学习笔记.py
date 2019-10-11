import pandas as pd                 #处理数据的
import numpy as np                  #处理数据的
import matplotlib.pyplot as plt     #画图表的，而且特别好看

#pandas 已经使用的命令
data = pd.read_excel('C:\\Users\\M\\Desktop\\python\\计算机学院研究生.xlsx')      #读取原始数据
data = pd.to_excel('C:\\Users\\M\\Desktop\\output.xlsx')       #输出数据到excel
data = pd.DataFram(colums=list('ABCD'),index=list('1234') )    #生成一个DataFrame，行是ABCD，列是1234

a = data.at['3行','2列']      #访问data中某一位置数据
a = data.loc['3行','2列']     #效果同上
a = data.loc['缪奇峰']        #访问缪奇峰(行)的所有数据
a = data.iloc[1,2]            #访问1行2列的数据

a = data.sort_values(by='出生日期')             #按照‘出生日期’的值进行排序
a = data[data.出生日期 > 19950101]              #访问出生日期大于19950101的人
data[data.出生日期 > 19950101] ='都是我小弟'     #出生日期大于19950101，值改成‘都是我小弟’

a = data.学号       #访问某一列的数据，数据类型为数组
a = data[10:45]     #data的10~45行的数据
a = data.生日.max() #生日这一列的最大值，最小为min()
a = data.学号.mean()#求学号这一列的平均值
a = data.shape      #表格的形状，行列数
a = data.shape[0]   #表格的行数，[1]为列

#numpy 已经使用的命令
a = np.arange(33)  #生成0~33的一个数组
a = np.nan          #a的值为空 NaN

#matplotlib 已经使用的命令
data = pd.read_excel('C:\\Users\\M\\Desktop\\数学建模\\运动学片段\\3低速\\final.xlsx')
plt.plot(data.speed, linewidth=2)  # 这里只指定了一个列表，那么就当作是输出参数，输入参数从0开始，就会发现没有正确绘制数据
plt.title("Driving Cycle vehicle_3", fontsize=24)  # 指定标题，并设置标题字体大小
plt.xlabel("Time(s)", fontsize=14)  # 指定X坐标轴的标签，并设置标签字体大小
plt.ylabel("Speed(km/h)", fontsize=14)  # 指定Y坐标轴的标签，并设置标签字体大小
plt.tick_params(axis='both', labelsize=14)  # 参数axis值为both，代表要设置横纵的刻度标记，标记大小为14
plt.show()  # 打开matplotlib查看器，并显示绘制的图形
plt.savefig('C:\\Users\\M\\Desktop\\数学建模\\运动学片段\\document1片段\\图表\\data.png')