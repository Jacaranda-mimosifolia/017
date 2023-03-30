a1 = """\
----欢迎使用联系人功能菜单----
1.查询全部联系人
2.搜索联系人
3.新建联系人
4.删除联系人
5.退出功能菜单
----------中国电信---------"""
list = {"光头强":17707604771,"李老板":13823926843,"熊大":13423960887,"吉吉":13608413827}
print(a1)
while True:
    A = input("请输入操作指令：")
    if A == "1":
        print("全部联系人:",str(list).replace("{", "").replace("}", ""))
    elif A == "2":
        a2 = input("请输入查找联系人姓名：")
        if list.get(a2) == None:
            print("该联系人不存在")
        else:
            print(a2, ":", list.get(a2))
    elif A == "3":
        n = input("请输入新建联系人姓名：")
        m = int(input("请输入新建联系人电话号码："))
        if n in list.keys() and m not in list.values():
            while True:
                a3 = input("该联系人已存在，是否修改联系人信息：")
                if a3 == "是":
                    list[n]=m
                    print("已成功修改联系人信息")
                    break
                elif a3 == "否":
                    print("已取消当前操作")
                    break
                else:
                    print("无法识别")
        elif m in list.values():
            print("当前号码已存在")
        else:
            list[n]=m
            print("新建成功")
    elif A == "4":
        a4 = input("请输入删除联系人姓名：")
        if a4 in list.keys():
            del list[a4]
            print("已删除该联系人")
        elif a4 not in list.keys():
            print("该联系人不存在")
    elif A == "5":
        print("Goodbye!")
        break
    else:
        print("暂无该功能")