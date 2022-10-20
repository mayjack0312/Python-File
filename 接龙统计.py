在这里插入代码片#名单的绝对路径，其中'\\'可以用'/'代替
infile='D:\\大三上\\name.txt'

f=open(infile,'r', encoding="utf-8")
sourceInLine=f.readlines()
dataset=[]
for line in sourceInLine:
    temp=line.strip('\n')
    dataset.append(temp)
    
# 接龙信息，粘贴在三重引号'''   '''之间
msg = '''#接龙
11.4 中午打卡

1. 郑小杰 体温36.6 健康
2. 雷小 体温36.6 健康
3. 吴小新  体温36.5  健康
4. 田小 体温36.5 健康
5. 洪小临 体温36.5 健康
6. 程小初 体温36.5 健康
7. 喻小姣 体温36.5 健康
8. 李小成 体温36.4 健康
9. 王小 体温36.3 健康
10. 姜小泽 体温36.5℃ 健康
11. 言小梅 体温36.5 健康
12. 黄小轩 体温36.2 健康
13. 罗小睿 体温36.5 健康
14. 王小羽 体温36.5 健康
15. 王小怡 体温36.5 健康
16. 罗小菲 体温36.5℃ 健康
17. 齐小成 体温36.5 健康
18. 杨小 体温36.5 健康
19. 曹小源 体温36.5 健康
20. 金小麟 体温36.5 健康'''

# 查找、打印没接龙的人
for name in dataset:
    name = ''.join(name)
    where = msg.find(name) 
    if where == -1:
        print(name)
