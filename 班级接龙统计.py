# -*- coding:utf-8 -*-
from wxpy import *

bot = Bot(cache_path=True)
group_name ='编程练习测试' #群名称
my_group = bot.groups(update=True).search(group_name)[0]
key_word = "在岗情况和疫情报告" #接龙关键词，群消息必须含连续的这些关键词
all_people =["张三","李四","王五","陈六","赵七","小懒人","师弟"]
@bot.register(my_group, msg_types=TEXT)
def group(msg):
    # print(msg.text) #输出群消息
    if key_word in msg.text : #判断消息是否接龙，即表头是否含关键词
        print('开始进入接龙')
        content = msg.text
        done_count = 0 #初始接龙人数为0
        not_yet = "" #还没接龙的人员，初始为空
        for people in all_people: #从所有人员列表中逐一取出
            if people in content: #如果这个名字在这条消息里，则下一步
                done_count +=1 #接龙人数+1
            else:
                at_them = "@" +people +"，"  #把这个没接龙的人前面加个@
                not_yet += at_them  #如果不在群消息里面，则放入未接龙成员合集
        print("已登记人数：%s人" % done_count)  # 直接控制台打印登记人数
        if done_count == len(all_people) :  #全部人数
            msg.sender.send("今日接龙已全员完成，共%s人"%done_count) #往群里面发送已完成信息
        elif 3 < done_count < len(all_people): # 大于3个人之后开始反馈，可以自己设定，没必要每收到一条信息就反馈一次
            msg.sender.send("已接龙人数：%s人。未上报群成员为：%s请及时接龙并到到体验群领资源"%(done_count,not_yet))
            # 往群里发送为完成的人员名单
bot.join() #程序开始
msg.sender.send("今日接龙已全员完成，共%s人"%done_count)
