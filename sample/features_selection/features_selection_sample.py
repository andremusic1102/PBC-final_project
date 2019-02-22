#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2019/1/3 13:53
# @Author  : Andre Shih
# @File    : features_selection_sample.py
# @Function: -----------




import csv
import pandas as pd
import numpy as np


# # 22個特徵 選9
# # 讀資料欄位
# filename = "/Users/andreshih/Desktop/features_selection/data1.csv"
# # 沒有欄位，純資料
# filename2 = "/Users/andreshih/Desktop/features_selection/data1_2.csv"


# # 254個特徵 選43
# # 讀資料欄位
# filename = "/Users/andreshih/Desktop/features_selection/python_cleaned_data.csv"
# # 沒有欄位，純資料
# filename2 = "/Users/andreshih/Desktop/features_selection/python_cleaned_data_2.csv"


#
# # 問題答案範例0110001
# # 讀資料欄位
filename = "/Users/andreshih/Desktop/features_selection/cleaned_data.csv"
# # 沒有欄位，純資料
# filename2 = "/Users/andreshih/Desktop/features_selection/cleared_data_2.csv"
filename2 = "/Users/andreshih/Desktop/final_data.csv"

# filename = "/Users/andreshih/Desktop/test_data.csv"
# filename2 = "/Users/andreshih/Desktop/test_data_2.csv"





# 讀欄位
fh1 = open(filename, 'r', newline='', encoding='utf-8')
csv1 = csv.DictReader(fh1)
cname1 = csv1.fieldnames
# print(cname1)
fh1.closed

# 找出品牌結果
num = 0
for i in cname1:
    num += 1
    # if i  == '哪一個音樂串流App是您最常使用的？ (請勾選題目中有顯示的品牌。如果您最近一年只使用一個品牌，請勾選該品牌)':
    if i  == '請問哪一個音樂串流App是您最常使用的？ (請勾選題目中有顯示的品牌。如果您最近一年只使用一個品牌，請勾選該品牌)':
        # print(num)
        ans_num = num - 1


print(num)
print(ans_num)




# 创建特征列表
# 使用pandas.read_csv函数  读取指定数据。
data = pd.read_csv(filename2,names = cname1)

# 将''替换为标准缺失值表示。
data = data.replace(to_replace = '', value = np.nan)
# 丢弃带有缺失值的数据（只要有一个维度有缺失）。
data = data.dropna(how = 'any')

# 输出data的数据量和维度。
data.shape

# print(data.shape)
# print("-------")


# 把特徵轉成數值
for i in cname1:
    dic = {label:idx for idx,label in enumerate(np.unique(data[i]))}
    # print(dic)
    data[i] = data[i].map(dic)
    # print(data[i])


# print(data[cname1[1:ans_num]])
# print()
# print("===========================")
# print()
# print(data[cname1[ans_num]])
X, y = data[cname1[1:ans_num]] , data[cname1[ans_num]]






# # 法一
# # RFE  要事先知道要選幾個特徵
# # 設迴圈跑出來 最好的結果是
# # 0.717948717948718   選11個
#
#
# from sklearn.feature_selection import RFE
# from sklearn.svm import LinearSVC
# from  sklearn import model_selection
#
# # best = 0
# # for i in range(1,22):
#
# ## 特征提取
# estimator = LinearSVC()
# selector = RFE(estimator=estimator, n_features_to_select = 8)
# # 要選3個特徵
# X_t = selector.fit_transform(X, y)
# ### 切分测试集与验证集
# X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y,
#                                                                     test_size=0.25, random_state=0, stratify=y)
# X_train_t, X_test_t, y_train_t, y_test_t = model_selection.train_test_split(X_t, y,
#                                                                             test_size=0.25, random_state=0,
#                                                                             stratify=y)
# ## 测试与验证
# clf = LinearSVC()
# clf_t = LinearSVC()
# clf.fit(X_train, y_train)
# clf_t.fit(X_train_t, y_train_t)
#
# print("Original DataSet: test score=%s" % (clf.score(X_test, y_test)))
# print("Selected DataSet: test score=%s" % (clf_t.score(X_test_t, y_test_t)))
#
# # # 測試最準
# # if best < clf_t.score(X_test_t, y_test_t):
# #     best = clf_t.score(X_test_t, y_test_t)
# #     choice = i
#
# print("N_features %s" % selector.n_features_) # 保留的特征数
# print("Support is %s" % selector.support_) # 是否保留
# print("Ranking %s" % selector.ranking_) # 重要程度排名
#
#
# # 找出要的特徵
# index = 0
# select = []
# for i in selector.ranking_:
#     index += 1
#     if i == 1:
#         select.append(index)
# print('select=',select)
#
#
# print()
# print()
# print()
# # print(best,choice)











# # 法三 LogisticRegression 和 SGDClassifier中的fit函数/模块用来训练模型参数
#
#
# # 使用sklearn.cross_valiation里的train_test_split模块用于分割数据。
# from sklearn.model_selection import train_test_split
#
# # 随机采样25%的数据用于测试，剩下的75%用于构建训练集合。
# X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.25,random_state=33)
# # print("data[cname1[10]]",data[cname1[10]])
#
#
# # 查验训练样本的数量和类别分布。
# y_train = pd.Series(y_train)
# y_train.value_counts()
#
# # 查验测试样本的数量和类别分布。
# y_test = pd.Series(y_test)
# y_test.value_counts()
#
#
# from sklearn.preprocessing import StandardScaler
# from sklearn.linear_model import LogisticRegression
# from sklearn.linear_model import SGDClassifier
#
# # 标准化数据，保证每个维度的特征数据方差为1，均值为0。使得预测结果不会被某些维度过大的特征值而主导。
# ss = StandardScaler()
# X_train = ss.fit_transform(X_train)
# X_test = ss.transform(X_test)
#
# # 初始化LogisticRegression与SGDClassifier。
# lr = LogisticRegression()
# sgdc = SGDClassifier()
#
# # 调用LogisticRegression中的fit函数/模块用来训练模型参数。
# lr.fit(X_train, y_train)
# # 使用训练好的模型lr对X_test进行预测，结果储存在变量lr_y_predict中。
# lr_y_predict = lr.predict(X_test)
#
#
# # 调用SGDClassifier中的fit函数/模块用来训练模型参数。
# sgdc.fit(X_train, y_train)
# # 使用训练好的模型sgdc对X_test进行预测，结果储存在变量sgdc_y_predict中。
# sgdc_y_predict = sgdc.predict(X_test)
#
# # 从sklearn.metrics里导入classification_report模块。
# from sklearn.metrics import classification_report
#
# # 使用逻辑斯蒂回归模型自带的评分函数score获得模型在测试集上的准确性结果。
# print("Accuracy of LR Classifier:", lr.score(X_test, y_test))
# # 利用classification_report模块获得LogisticRegression其他三个指标的结果。
# # print(classification_report(y_test, lr_y_predict, target_names=['Benign', 'Malignant']))
#
#
# # 使用随机梯度下降模型自带的评分函数score获得模型在测试集上的准确性结果。
# print('Accuarcy of SGD Classifier:', sgdc.score(X_test, y_test))
# # 利用classification_report模块获得SGDClassifier其他三个指标的结果。
# # print(classification_report(y_test, sgdc_y_predict, target_names=['Benign', 'Malignant']))






# 補充
# PCA 主成因分析
from sklearn.decomposition import PCA
# feature extraction
pca = PCA(n_components=3)
fit = pca.fit(X)
# summarize components
# print("Explained Variance: %s" % fit.explained_variance_ratio_)
print(fit.components_)






# 為啥會變動？
# 特征重要性分析 ExtraTreesClassifier
from sklearn.ensemble import ExtraTreesClassifier
# feature extraction
model = ExtraTreesClassifier()
model.fit(X, y)
# print(model.feature_importances_)
# 總合會是1
# print(sum(model.feature_importances_))



check = []
num = 0
for i in model.feature_importances_:
    check.append(i)
    num += 1
# print(check)
# print(num)



order = []
while True:
    if max(check) == -1:
        break
    a = max(check)
    ord = check.index(a)
    order.append(ord+1)
    check[ord] = -1
    # break

print("order=",order)
# print(check)
print(max(order))










# 法二
# RFECV  可以算出幾個特徵去預測最準

import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.model_selection import StratifiedKFold
from sklearn.feature_selection import RFECV

# 以疊代排序特徵影響力，並以交叉驗證來選出具有實際影響力的特徵
#
# 在使用RFECV指令前，需要建立支持向量機物件，以及交叉驗證的形式。本範例仍使用SVC以及線性核函數來作為主要的分類機。
#
# 在交叉驗證的部分，我們使用StratifiedKFold指令來做K 堆疊(Fold)的交叉驗證。也就是將資料分為K堆，
# 一堆作為預測用，剩下的(K-1)堆則用來訓練，經過計算後，再以另外一堆作為預測，重複K次。

#
# 而scoring參數則是依照分類資料的形式，輸入對應的評分方式。
# 以本例子為超過兩類型的分類，因此使用'accuracy'來對多重分類的評分方式。


# Create the RFE object and compute a cross-validated score.
svc = SVC(kernel="linear")

# The "accuracy" scoring is proportional to the number of correct
# classifications
rfecv = RFECV(estimator=svc, step=1, cv=StratifiedKFold(2),
              scoring='accuracy')

rfecv.fit(X, y)

print("Optimal number of features : %d" % rfecv.n_features_)
print("Ranking of features : %s" % rfecv.ranking_)

# 找出要的特徵
index = 0
select = []
select_column = []
for i in rfecv.ranking_:
    if i == 1:
        select.append(index)

        a = cname1[index]
        select_column.append(a)

    index += 1

print('select=',select)
print('first_check = ',cname1[0])
print('select_column=',select_column)










# Plot number of features VS. cross-validation scores
plt.figure()
plt.xlabel("Number of features selected")
plt.ylabel("Cross validation score (nb of correct classifications)")
plt.plot(range(1, len(rfecv.grid_scores_) + 1), rfecv.grid_scores_)
plt.show()

