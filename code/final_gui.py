
class RadiobuttonGroup():
    def __init__(self, frame, label_text, color, optionlist):
        self.frame = frame

        # 問題
        label2 = Label(self.frame, text=label_text, fg='#2F5597')
        label2.grid(row=1, column=0)
        # (Radiobutton)
        self.choice = StringVar(None, "F")
        self.buttonlist = []
        pos = 0
        for i in range(len(optionlist)):
            self.buttonlist.append(Radiobutton(self.frame, text=optionlist[i], fg=color, variable=self.choice,
                                               value=optionlist[i]))  # , command=self.getchoice))
            pos += 2
            self.buttonlist[i].grid(row=1, column=pos)

    def getchoice(self):
        choice = self.choice.get()
        return choice


class CheckbuttonGroup():
    def __init__(self, frame, label_text, color, optionlist):
        self.frame = frame

        # 問題
        label2 = Label(self.frame, text=label_text, fg='#2F5597')
        label2.grid(row=1, column=0)
        # (Checkbutton)

        self.StringVarlist = []
        self.buttonlist = []
        pos = 0
        pos_raw = 1
        for i in range(len(optionlist)):
            var = StringVar(None, "F")

            button = Checkbutton(self.frame, text=optionlist[i], fg=color, variable=var, onvalue=optionlist[i],
                                 offvalue="F", command=self.check_special_option)
            self.StringVarlist.append(var)

            self.buttonlist.append(button)
            if pos != 6:  # 選項的排序條整
                pos += 2
            else:
                pos = 2
                pos_raw += 1

            self.buttonlist[i].grid(row=pos_raw, column=pos, sticky=tk.W)  # +tk.S+tk.W+tk.E)

    def getchoice(self):
        output = []
        for i in range(len(self.StringVarlist)):
            if self.StringVarlist[i].get() == "F":
                output.append(0)
            else:
                output.append(1)
        return output

    def cancel_all_option(self):
        for i in range(len(self.StringVarlist)):
            self.StringVarlist[i].set("F")

    def check_special_option(self):
        for i in range(len(self.StringVarlist)):
            if self.StringVarlist[i].get() == "都不符合":
                self.cancel_all_option()
                self.StringVarlist[i].set("都不符合")
            elif self.StringVarlist[i].get() == "都不曾使用過":
                self.cancel_all_option()
                self.StringVarlist[i].set("都不曾使用過")


class TkDemo():
    global final, select, ans ,master,ta

    def __init__(self,select,ans):
        master = Tk()
        self.master = master
        master.title('推薦系統')

        # 文字 (Label)

        title = Label(master, text='謝謝您使用本推薦軟體！\n以下請您輸入一些相關資訊，我們將藉由您所輸入的資訊推薦適合您的平台！', font='15', fg='#2F5597')
        title.pack()

        self.listbox_array = []
        self.radiogroup_list = []
        self.checkgroup_list = []

        global multichoice
        multichoice = []

        for i in range(len(select)):
            # print("i=",i)
            frame = Frame(master)
            frame.pack(fill=X)

            # 選項
            if '收入' in ans[i][0]:
                # 問題
                label = Label(frame, text=ans[i][0], fg='#2F5597')
                label.grid(row=1, column=0)

                self.salary_selected = StringVar()

                # Dictionary with options
                salary_choices = ['---請選擇---',
                                  '$5,000以下',
                                  '$5,001 ~ $10,000',
                                  '$10,001 ~ $20,000',
                                  '$20,001 ~ $30,000',
                                  '$30,001 ~ $40,000',
                                  '$40,001 ~ $50,000',
                                  '$50,001 ~ $60,000',
                                  '$60,001 ~ $70,000',
                                  '$70,001 ~ $80,000',
                                  '$80,001 ~ $90,000',
                                  '$90,001 ~ $100,000',
                                  '$100,001 ~ $110,000',
                                  '$110,001 ~ $120,000',
                                  '$120,001 ~ $130,000',
                                  '$130,001 ~ $140,000',
                                  '$140,001 ~ $150,000',
                                  '$150,001以上']

                self.salary_selected.set(salary_choices[0])  # set the default option

                popupMenu_salary = OptionMenu(frame, self.salary_selected, *salary_choices)
                # Label(mainframe, text="Choose a dish").grid(row = 1, column = 1)
                popupMenu_salary.grid(row=1, column=2)


            elif '工作狀況' in ans[i][0]:  # 單選
                # 問題
                label = Label(frame, text=ans[i][0], fg='#2F5597')
                label.grid(row=1, column=0)

                self.work_selected = StringVar()

                # Dictionary with options
                work_choices = ['---請選擇---',
                                '學生 - 未兼職',
                                '學生 - 兼職打工/實習',
                                '兼職員工（每週工作時數小於30小時）',
                                '全職員工（每週工作時數30小時以上）',
                                '待業中',
                                '退休']
                self.work_selected.set(work_choices[0])  # set the default option

                popupMenu_work = OptionMenu(frame, self.work_selected, *work_choices)
                # Label(mainframe, text="Choose a dish").grid(row = 1, column = 1)
                popupMenu_work.grid(row=1, column=2)

            # 塔位客製化
            elif ta == True and '性別' not in ans[i][0]:  # 單選
                choice = 1
                place = 2
                self.listbox_array.append(NONE)
                ta_choices = ['非常同意', '同意', '普通', '不同意', '非常不同意']
                optionlist = []
                for k in ta_choices:
                    optionlist.append(k)
                rad = RadiobuttonGroup(frame, ans[i][0], '#2F5597', optionlist)
                self.radiogroup_list.append(rad)

            elif ' - ' in ans[i][0]:  # 多選

                # 問題
                buttontext = ans[i][0][:ans[i][0].index('-')]


                # 將選項從題目分割出
                ans[i][0] = ans[i][0].split(" - ")
                ans[i][0].remove(ans[i][0][0])
                rollques = []
                rollques.append(ans[i][0][0].split(", "))
                for j in range(len(rollques)):
                    multichoice.append(len(rollques[j]) * [0])


                optionlist = []
                for j in range(len(rollques)):
                    for num in rollques[j]:
                        # self.listbox_array[i].insert(END, num)
                        optionlist.append(num)


                check = CheckbuttonGroup(frame, buttontext, '#2F5597', optionlist)
                self.checkgroup_list.append(check)

            else:  # 最上面那兩題


                choice = 1
                place = 2
                self.listbox_array.append(NONE)
                optionlist = []
                while True:
                    optionlist.append(ans[i][choice])

                    choice += 1
                    place += 2

                    if choice == (len(ans[i])):
                        break
                rad = RadiobuttonGroup(frame, ans[i][0], '#2F5597', optionlist)
                self.radiogroup_list.append(rad)

        # print(multichoice)

        frame9 = Frame(master)
        frame9.pack()
        submit = Button(frame9, text='提交', command=self.allsubmit)
        # 關視窗
        submit.grid()

        master.mainloop()

    def clicksalary(self):
        salary = self.listbox_salary.get(ACTIVE)
        print(salary)



    def clickwork(self):
        choice = self.listbox_work.get(ACTIVE)
        print(choice)

    def allsubmit(self):
        global final,a,master
        final = []

        self.outputdata = []
        for i in range(len(self.radiogroup_list)):
            final.append(self.radiogroup_list[i].getchoice())
            # print(self.radiogroup_list[i].getchoice())
            self.outputdata.append(self.radiogroup_list[i].getchoice())

        for i in range(len(self.checkgroup_list)):
            if self.checkgroup_list[i].getchoice() == multichoice[i]:
                final.append('F')
                # print('F')
            else:
                # 把list中的答案串在一起
                a = [str(x) for x in self.checkgroup_list[i].getchoice()]
                a = ''.join(a)
                a = int(a)
                # print(a)
                final.append(a)

            self.outputdata.append(self.checkgroup_list[i].getchoice())






        try:
            final.append(self.work_selected.get())
            # print("work_selected--", self.work_selected.get())
        except:
            pass

        try:
            final.append(self.salary_selected.get())
            # print(self.salary_selected.get())
        except:
            pass

        if "F" in final or "---請選擇---" in final:
            messagebox.showinfo('Oops!', '您尚有問題未填寫！')
        else:


            print("final =" ,final)  # 給群中心跑的list
            # 關視窗
            self.master.destroy()


    def getdata(self):
        return self.outputdata




import csv
from tkinter import *
import tkinter.messagebox as messagebox
import tkinter as tk



def dogui(filename,select):
    global final,ans,ta
    # print(filename,select)
    if '塔位' in filename :
        ta = True
    else: ta = FALSE
    fh1 = open(filename, 'r', newline='', encoding='utf-8')
    csv1 = csv.reader(fh1)

    line = []
    for row in csv1:
        line.append(row)

    # 把被select的特徵答案輸出
    n = 0
    ans = []
    while True:
        ans.append([])
        for row in line:
            if row[select[n]] not in ans[n]:
                ans[n].append(row[select[n]])
        n = n + 1

        if n == len(select):
            break

    window = TkDemo(select,ans)

    return final






def show(recommend_brand):
    if recommend_brand == "Spotify":
        # a = "/Users/andreshih/Desktop/Github/PBC-final_project/圖片/spotify.gif"
        a = "/Users/andreshih/Desktop/Github/PBC-final_project/圖片/spotify.gif"
    elif recommend_brand == "KKBOX":
        a ='/Users/andreshih/Desktop/Github/PBC-final_project/圖片/kkbox.gif'
    elif recommend_brand == "Apple Music":
        a = '/Users/andreshih/Desktop/Github/PBC-final_project/圖片/apple.gif'

    elif recommend_brand == 'Mixer Box':
        a = '/Users/andreshih/Desktop/Github/PBC-final_project/圖片/mixer_box.gif'
    elif recommend_brand == 'My Music':
        a = '/Users/andreshih/Desktop/Github/PBC-final_project/圖片/my_music.gif'
    elif recommend_brand == 'Street Voice 街聲':
        a = '/Users/andreshih/Desktop/Github/PBC-final_project/圖片/street_voice.gif'
    elif recommend_brand == '香港和合石靈骨塔 (HK)':
        a = '/Users/andreshih/Desktop/Github/PBC-final_project/圖片/1.gif'

    elif recommend_brand == '龍巖櫻花陵園 (LungYen)':
        a = '/Users/andreshih/Desktop/Github/PBC-final_project/圖片/2.gif'

    elif recommend_brand == '美國Lakewood陵園 (Lakewood)':
        a = '/Users/andreshih/Desktop/Github/PBC-final_project/圖片/3.gif'

    elif recommend_brand == "巴黎拉雪茲神父墓園 (Paris) ":
        a = '/Users/andreshih/Desktop/Github/PBC-final_project/圖片/4.gif'

    elif recommend_brand == '美國舊金山靈骨塔 (SF)':
        a = '/Users/andreshih/Desktop/Github/PBC-final_project/圖片/5.gif'

    else:
        a = '/Users/andreshih/Desktop/Github/PBC-final_project/圖片/tenor.gif'

    r1 = tk.Tk()
    r1.title('謝謝您的填答！')
    r1.geometry('400x400')

    tk.Label(r1, text="在與資料庫交叉比對之後，\n我們推薦您的品牌為" + str(recommend_brand)+" !").place(x=100, y=90)
    img = tk.PhotoImage(file = a)
    l1 = tk.Label(r1, image = img)
    l1.place(x=120, y=150)
    r1.mainloop()


import tkinter.messagebox as messagebox
class choice():
    global choice
    def __init__(self):
        master = Tk()
        self.master = master
        master.title('推薦系統')

        # 文字 (Label)

        title = Label(master, text='謝謝您使用本推薦軟體,\n以下請您選擇感興趣的商品！', font='15', fg='#2F5597')
        title.pack()

        self.radiogroup_list = []
        self.checkgroup_list = []

        frame = Frame(master)
        frame.pack(fill=X)
        choice = 1
        place = 2
        # optionlist = ["音樂串流軟體","保養品","塔位"]
        optionlist = ["音樂串流軟體","塔位"]

        rad = RadiobuttonGroup(frame, "請您選擇感興趣的商品", '#2F5597', optionlist)
        self.radiogroup_list.append(rad)


        frame9 = Frame(master)
        frame9.pack()
        submit = Button(frame9, text='提交', command=self.allsubmit)
        # 關視窗
        submit.grid()
        master.mainloop()


    def allsubmit(self):
        global final, a, master,choice,ch
        final = []

        self.outputdata = []
        for i in range(len(self.radiogroup_list)):
            final.append(self.radiogroup_list[i].getchoice())
            # print(self.radiogroup_list[i].getchoice())

        choice = str(self.radiogroup_list[i].getchoice())

        # print("choice =", choice)  # 給群中心跑的list

        self.master.destroy()



def cho():
    global  choice
    monitor =  choice()
    return choice