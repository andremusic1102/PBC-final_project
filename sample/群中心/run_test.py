

#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2019/1/5 15:17
# @Author  : Andre Shih
# @File    : test.py
# @Function: -----------


#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2019/1/3 13:53
# @Author  : Andre Shih
# @File    : features_selection.py
# @Function: -----------


# filename = "/Users/andreshih/Desktop/final_data.csv"
# filename = "/Users/andreshih/Desktop/健身生態研究.csv"
filename = "/Users/andreshih/Desktop/塔位.csv"
import csv
import pandas as pd
import numpy as np



# 建特徵列表
# 使用pandas.read_csv函数  讀取指定数据。
data = pd.read_csv(filename)

# 輸出data的数據量和维度。
data_frame = data.shape
print("data_frame = ",data_frame)

# 把特徵轉成數值
for i in data.columns:
    # print(i)
    dic = {label:idx for idx,label in enumerate(np.unique(data[i]))}
    # print(dic)
    data[i] = data[i].map(dic)
    # print(data[i])

# 找出品牌結果在哪一欄
column_num = len(data.columns)
brand_col_num = column_num - 1

# print(column_num)
# print(brand_col_num)


X, y = data[data.columns[1:brand_col_num]] , data[data.columns[brand_col_num]]
# print(X)
# print(y)




# 特徵重要性分析 ExtraTreesClassifier
from sklearn.ensemble import ExtraTreesClassifier
# feature extraction
model = ExtraTreesClassifier()
model.fit(X, y)
# print(model.feature_importances_)
# 總合會是1
# print(sum(model.feature_importances_))




# RFECV  可以算出幾個特徵去預測最準
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.model_selection import StratifiedKFold
from sklearn.feature_selection import RFECV

# Create the RFE object and compute a cross-validated score.
# svc = SVC(kernel="linear")
# 以疊代排序特徵影響力，並以交叉驗證來選出具有實際影響力的特徵
# 在使用RFECV指令前，需要建立支持向量機物件，以及交叉驗證的形式。本範例仍使用SVC以及線性核函數來作為主要的分類機。

# choicelist = [2, 0.6198779424585876, 3, 0.5256410256410257, 4, 0.5333333333333333, 5, 0.585406162464986, 6, 0.6039529914529914, 7, 0.5994897959183673, 8, 0.579861111111111, 9, 0.5685626102292768, 10, 0.6022835497835498, 11, 0.6062967335694608, 12, 0.6269029581529582, 13, 0.6275641025641026, 14, 0.622562358276644, 15, 0.6255026455026456, 16, 0.6384920634920634, 17, 0.649953314659197, 18, 0.6879188712522046, 19, 0.6780284043441939, 20, 0.6991269841269842, 21, 0.708692365835223, 22, 0.7173881673881674, 23, 0.7035886818495515, 24, 0.7048280423280424, 25, 0.7046349206349205, 26, 0.7294566544566544, 27, 0.7109053497942386, 28, 0.7491071428571429]






choicelist = [0,0]
features_selection_num_list = [0,0]
for i in range(2,12):
    print(i)

    svc = SVC(kernel="linear")
    # classifications
    rfecv = RFECV(estimator=svc, step=1, cv=StratifiedKFold(i) ,scoring='accuracy')
    # 50秒 預測率 =  0.707

    # 在交叉驗證的部分，我們使用StratifiedKFold指令來做K 堆疊(Fold)的交叉驗證。也就是將資料分為K堆，
    # 一堆作為預測用，剩下的(K-1)堆則用來訓練，經過計算後，再以另外一堆作為預測，重複K次。
    # 而scoring參數則是依照分類資料的形式，輸入對應的評分方式。
    # 以本例子為超過兩類型的分類，因此使用'accuracy'來對多重分類的評分方式。

    rfecv.fit(X, y)
    # print("Optimal number of features : %d" % rfecv.n_features_)
    features_selection_num_list.append(rfecv.n_features_)


    # choicelist.append(i)
    choicelist.append(max(rfecv.grid_scores_))
    # print("Ranking of features : %s" % rfecv.ranking_)

print(choicelist)




a = max(choicelist)
print(a)
index = choicelist.index(a)
print(index)
print(features_selection_num_list)


# # 找出要的特徵
# index = 0
# select_index = {}
# select_column = []
# weight_sum = 0
#
# for i in rfecv.ranking_:
#     if i == 1:
#         # 權重
#         weight = model.feature_importances_[index]
#         weight_sum += weight
#         select_index[index] = weight
#         # 特徵
#         a = data.columns[index]
#         select_column.append(a)
#     index += 1
#
# # 把所選的特徵的權重，做成比例
# for i in select_index.keys():
#     select_index[i] = select_index[i] / weight_sum
#
#
#
#
#
# # print('first_check = ',data.columns[0])
# print()
# print('select_index : weight =',select_index)
# print()
# print('select_list=',select_index.keys())
# print()
# print('select_list=',[i for i in select_index.keys()])
# print()
# print('select_column=',select_column)
#



#
#
# # 如果想看特定的欄位
# # print(data[data.columns[48]])
#
#
# # 畫圖
# # Plot number of features VS. cross-validation scores
# plt.figure()
# plt.xlabel("Number of features selected")
# plt.ylabel("Cross validation score (nb of correct classifications)")
# plt.plot(range(1, len(rfecv.grid_scores_) + 1), rfecv.grid_scores_)
# plt.show()
# #
