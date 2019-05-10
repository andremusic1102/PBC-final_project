#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2019/1/9 05:11
# @Author  : Andre Shih
# @File    : __init__.py
# @Function: -----------



# 選資料庫
import final_gui as gui
step0 = gui.cho()
# print(step0)

if "音樂串流軟體" == step0:
    # filename = "/Users/andreshih/Desktop/Final_Project/data/music_final_data.csv"
    filename = "/Users/andreshih/Desktop/Github/PBC-final_project/data/music_final_data.csv"
    num = 2

# elif "保養品" == step0:
#     filename = "/Users/andreshih/Desktop/Final_Project/data/final_data new.csv"
#     num = 28

else:
    filename = "/Users/andreshih/Desktop/Github/PBC-final_project/data/塔位_final_data.csv"
    num = 5


# 特徵選擇
import features_selection as fs
step1 = fs.run(filename,num)

select_index  = step1[0]
select_list = step1[1]
data_frame = step1[2]


# GUI 填問卷
import final_gui as gui
step2 = gui.dogui(filename,select_list)


# 群中心推薦
import recomend as re
step3 = re.dore(filename,select_index,step2,data_frame)
recommend_brand = step3


# GUI 推薦圖r
step4 = gui.show(recommend_brand)






