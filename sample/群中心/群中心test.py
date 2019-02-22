
# 這個是要根據features selection承接下來的
# filename = "/Users/andreshih/Desktop/final_data.csv"
# select_index = {0: 0.037830303132297294, 1: 0.23818554400813743, 22: 0.07609427008528967, 27: 0.20168879632506012, 31: 0.03584622691887085, 32: 0.06057890051647437, 33: 0.3497759590138704}
# data_frame =  (304, 36)

# filename = "/Users/andreshih/Desktop/健身生態研究.csv"

filename = "/Users/andreshih/Desktop/塔位.csv"

select_index = {1: 0.132486714071408, 7: 0.11546467620265684, 10: 0.08570238422020159, 18: 0.14975804837690293, 22: 0.10253750046675195, 23: 0.1456488300548995, 24: 0.1224804260958752, 25: 0.1459214205113039}
data_frame =  (288, 28)


import numpy as np
import csv
import pandas as pd



## 承接準備
selected_features = []
weight = []
for key,value in select_index.items():
    selected_features.append(key)
    weight.append(value)
raw_data = [data_frame[0],data_frame[1],len(selected_features), "隨便設之後會覆蓋"]
# 資料數 # 維度 # 群  # 起始點


n = raw_data[0]  # 資料數
m = raw_data[1]  # 維度
k = raw_data[2]  # 群
j = raw_data[3]  # 起始點





# 紀錄每個點的info
# 定義距離＝ 每個維度差的平方＊權重
class Point():
    def __init__(self, info):
        # 紀錄每個點的每維 => 已經轉成數字
        self.info = info[:-1]
        self.itscenter = j

        # 品牌要轉回中文 - value 轉回 key
        for i in brand_dict.keys():
            brand = brand_dict[i]
            if info[-1] == brand:
                info[-1] = i
                # print(i)
        self.brand = info[-1]

    def distance(self, origin):
        dis = 0
        # len(weight) = 被選取要比較的維度
        for i in range(len(weight)):
            # print(i)
            # 乘以權重
            dis += ((self.info[i] - origin.info[i]) ** 2 * weight[i])
        return dis








# 群中心算法
def run(start):

    global best_ratio ,best_start,best_runlist,points

    start_index = start-1
    runlist = [start_index]
    dis_to_center = [0] * n
    # print(runlist)


    # 算目前離起始點最遠的地點當下個群中心
    for i in range(n):
        dis = points[i].distance(points[start_index])
        dis_to_center[i] = dis
    # print(dis_to_center)



    # 找滿群中心的數量
    while True:
        if len(runlist) == k:
            break
        farest_dis = max(dis_to_center)
        next_center = dis_to_center.index(farest_dis)
        points[next_center].itscenter = next_center

        for i in range(n):
            dis = points[i].distance(points[next_center])
            # print(dis)
            if dis < dis_to_center[i]:
                dis_to_center[i] = dis
                points[i].itscenter = next_center+1
        runlist.append(next_center)

    # index 轉成runlist要加一
    # 要print list 中的東西轉成字串再join
    runlist = [str(x + 1) for x in runlist]
    # print(runlist)
    # print(",".join(runlist))


    # 開始計算正確率
    total_ratio = 0.0
    # 已算出的群中心
    for i in runlist:
        # print("群中心＝",i)
        i = int(i)
        amount = 0  # 該center有多少點
        correct = 0

        # 跑各個點看是否跟自己的群中心品牌一致
        for j in range(0, n):
            # print(j)
            # 該點是這個群中心
            if points[j].itscenter == i:
                amount += 1
                # 品牌一致  index 所以要減一
                if points[j].brand == points[i-1].brand:
                    correct += 1

        # 看正確率如何定義
        # 算出正確的比例
        try:
            ratio = correct / amount
        except:
            ratio = 0
        total_ratio += ratio

        # 挑出最好
        if best_ratio < total_ratio:
            best_ratio = total_ratio
            best_start = start
            best_runlist = runlist

    return best_start, best_ratio, best_runlist









######### 主要code開始  ##############


# 讀資料
data = pd.read_csv(filename)
column_name = data.columns

# 把特徵轉成數值 - 等等各維度比較dis可以取用
for i in data.columns:
    dic = {label:idx for idx,label in enumerate(np.unique(data[i]))}
    # print(dic)
    data[i] = data[i].map(dic)
    # print(data[i])

    # 記錄品牌的dic
    if i == data.columns[-1]:
        brand_dict = dic

# selected_features最後加上品牌的那欄
selected_features.append(len(column_name) - 1)
print()
print("被選擇出的特徵,品牌的index依序為= ",selected_features)



# 列出全部資料所選的特徵 ＝ 等等跑群中心
selected_data_features = []
brand_list = []
for j in range(n):
    get = []
    for i in selected_features:
        a = data[data.columns[i]][j]
        # 如果是最後一個為品牌
        if selected_features[-1] == i:
            if a not in brand_list:
                brand_list.append(a)

        a = int(a)
        get.append(a)
    selected_data_features.append(get)


print()
print("品牌總共有以下 =",str(len(brand_list))+"種")
print(" ,".join(brand_dict.keys()))
# print("每筆資料中，被選出的特徵 ＝",selected_data_features)








# 把所有資料所選特徵.品牌 用class Points 記錄下來
points = []
index  =  0
for i in selected_data_features:
    # print(i)
    each_point = Point(i)
    points.append(each_point)
    index += 1






# 先跑全部的點 找出最佳起始點
best_ratio = 0
best_start = "nope"
best_runlist = "nope"
print()
print("開始找最佳群中心起始點...")
for start in range(1,n+1):
    run(start)

# print("best_ratio =",best_ratio)
print()
print("最佳群中心起始點 =",best_start)




# 再用最佳起始點去跑
run(best_start)
print()
print("群中心依序 =",best_runlist)





# 群中心各自的品牌
# runlist 轉 index 所以要減一
print()
print("群中心品牌依序 ＝",[points[int(i)-1].brand for i in best_runlist])




