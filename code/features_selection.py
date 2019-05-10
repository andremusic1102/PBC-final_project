




def run(filename,num):

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
        # print(data[i])
        dic = {label:idx for idx,label in enumerate(np.unique(data[i]))}
        # print(dic)
        data[i] = data[i].map(dic)
        # print(data[i])

    # 找出品牌結果在哪一欄
    column_num = len(data.columns)
    brand_col_num = column_num - 1

    print(column_num)
    print(brand_col_num)


    X, y = data[data.columns[1:brand_col_num]] , data[data.columns[brand_col_num]]

    # print(X)
    # print()
    # print()
    # print()
    # print()
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
    from sklearn.svm import SVC
    from sklearn.model_selection import StratifiedKFold
    from sklearn.feature_selection import RFECV

    # Create the RFE object and compute a cross-validated score.
    svc = SVC(kernel="linear")
    # 以疊代排序特徵影響力，並以交叉驗證來選出具有實際影響力的特徵
    # 在使用RFECV指令前，需要建立支持向量機物件，以及交叉驗證的形式。本範例仍使用SVC以及線性核函數來作為主要的分類機。


    print("開始執行：以疊代排序特徵影響力，並以交叉驗證來選出具有實際影響力的特徵....")
    # classifications
    rfecv = RFECV(estimator=svc, step=1, cv=StratifiedKFold(num) ,scoring='accuracy')
    # 音樂 4 : 50秒 預測率 =  0.707
    # 健身房 28
    # 塔位 5


    # 在交叉驗證的部分，我們使用StratifiedKFold指令來做K 堆疊(Fold)的交叉驗證。也就是將資料分為K堆，
    # 一堆作為預測用，剩下的(K-1)堆則用來訓練，經過計算後，再以另外一堆作為預測，重複K次。
    # 而scoring參數則是依照分類資料的形式，輸入對應的評分方式。
    # 以本例子為超過兩類型的分類，因此使用'accuracy'來對多重分類的評分方式。

    rfecv.fit(X, y)
    print()
    print("Optimal number of features : %d" % rfecv.n_features_)
    print("預測率 =",max(rfecv.grid_scores_))
    print("Ranking of features : %s" % rfecv.ranking_)


    # 找出要的特徵
    index = 0
    select_index = {}
    select_column = []
    weight_sum = 0

    for i in rfecv.ranking_:
        if i == 1:
            # 權重
            weight = model.feature_importances_[index]
            weight_sum += weight
            select_index[index] = weight
            # 特徵
            a = data.columns[index]
            select_column.append(a)
        index += 1

    # 把所選的特徵的權重，做成比例
    for i in select_index.keys():
        select_index[i] = select_index[i] / weight_sum





    # print('first_check = ',data.columns[0])
    # print()
    # print('select_index : weight =',select_index)
    # print()
    # print('select_list=',select_index.keys())
    print()
    select_list = [i for i in select_index.keys()]
    print('select_list =',select_list)
    print()
    print('select_column =',select_column)




    # # 如果想看特定的欄位
    # # print(data[data.columns[20]])
    
    import matplotlib.pyplot as plt
    # 畫圖
    # Plot number of features VS. cross-validation scores
    plt.figure()
    plt.xlabel("Number of features selected")
    plt.ylabel("Cross validation score (nb of correct classifications)")
    plt.plot(range(1, len(rfecv.grid_scores_) + 1), rfecv.grid_scores_)
    plt.show()

    return select_index , select_list,data_frame