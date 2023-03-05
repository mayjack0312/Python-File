'''
1.1首先需要一个班级的成员名单，包括学号和姓名。通过遍历进行统计提交情况（我现在没有名单，使用字典的方式进行后续比较）
1.2编写遍历文件夹下文件的方法，并且拿到文件的名称，提取姓名和学号（供后边统计使用）。
1.3实现已经提交人员名单.
初始化一个提交人员的list，通过上边遍历的文件学号（即文件夹下存在的都是已经提交的），添加到这个list中。
1.4实现未提交作业的人员名单.
通过遍历原始字典下，进行提交名单的list嵌套。使用if进行判断，如果字典中存在提交名单的内容，把它剔除掉。最后把字典转成list输出。
1.5实现生成未提交人员的excel文件（固定代码，按照模板使用即可）
'''

'''
如果（if） 就（冒号） ，否则的话（不管冒号，直接跳过）
'''

'''
缩进就是每一行前面加空格或者Tab。Python约定一个文件里，要么都用空格来缩进，要么都用Tab来锁进，不能有的行用空格 有的行用Tab。
Python还约定，类似于：if a==b: #没有缩进  print "line1"  #缩进两个空格  print "line2"  #缩进两个空格print "line3"  #没有缩进如果a和b相等，就会打出line1 line2 line3。
如果a和b不等，就会打出lin3。因为line1和line2的缩进相同，它们被认为都是if判断需要执行的语句。
line3缩进跟line1 line2不一样，所以不属于if内部的语句，所以不管ab的值如何，都会被打印。对于循环也是如此。

例如一个for循环下有缩进就代表语句是for循环的一部分，没有缩进就代表语句在for循环之外。
for、while循环以及if…else语句、try…except语句都是需要缩进的。

代码世界里也有阶级关系
一个年级中会有很多个班级存在，大家都是同一级别的
各个班又会有属于自己的同学存在，每个班对应的同学就会包裹(缩进)在这个班里

北信
    数字商务
        3+2
            1班
            2班
        3+3
            3班
            4班
    人工智能
        3+2
            1班
            2班
        3+3
            3班
            4班
    电子信息
        3+2
            1班
            2班
        3+3
            3班
            4班
    产业互联网
        3+2
            1班
            2班
        3+3
            3班
            4班
    食品健康
        3+2
            1班
            2班
        3+3
            3班
            4班
'''

# 导入os库
import os
# 导入xlwt库
import xlwt
# 导入time库
import time

# 定义一个函数，参数为基础目录base。
def findAllFile(base):
    # os.walk() 方法可以遍历一个目录下的所有子目录和文件，并返回文件路径。
    # 它返回一个三元组 (dirpath, dirnames, filenames)，分别表示当前遍历到的目录、当前目录下子目录名列表、当前目录下文件名列表。
    for root, ds, fs in os.walk(base):
        # 遍历当前目录下的文件列表，每个文件名作为一个生成器的一个项被一次迭代返回。
        for f in fs:
            # 将文件名f返回给生成器的调用者。
            yield f
'''
这个函数在被调用时返回一个生成器（generator），可以用于按需逐个获取文件名，避免一次性获取所有文件名导致内存溢出。比如可以这样使用：
for filename in findAllFile('/path/to/directory'):
    print(filename)
'''
# 定义函数main。
def main():
    # 获取当前工作目录的路径，并将其转换为字符串形式，去除双引号和单引号。
    base = repr((os.getcwd())).strip('"\'')
    # 设定一个变量count并将其赋值为0。
    count=0
    # 定义一个字典，它包含3个键值对，每个键都是一个字符串，它们是'01'，'02'和'03'，每个键都对应一个空字符串。
    num_name={
    '01': '',
    '02': '',
    '03': ''
    }
    # 创建空列表submit_list。
    submit_list=[]
    # 创建空列表submit_list2
    submit_list2=[]

    '''
    for i in findAllFile(base):
        for a in num_name:
            if i.split("2234011")[1][0:2]==a:
                submit_list.append(a+''+num_name[a])
                submit_list2.append(a)
                count += 1
    '''

    # 在base目录中查找所有的文件并对每个文件进行操作，将返回值赋给变量i。
    for i in findAllFile(base):
        # 如果i的前两个字符等于num_name字典中a这个key对应的value，执行以下操作。
        for a in num_name:
            if i[0:2]==a:
                # 在submit_list列表的末尾添加字符串，其内容为a和num_name[a]的组合。
                submit_list.append(a+''+num_name[a])
                # 在submit_list2列表的末尾添加a。
                submit_list2.append(a)
                # count加1。
                count += 1
    # 添加一个for循环，遍历num_name字典的键，将所有等于submit_list2中的元素的键删除。
    for key in list(num_name.keys()):
        for i in submit_list2:
            if key==i:
                # 如果num_name字典中的某个键等于submit_list2中的某个元素，则删除该键对应的键值对，并继续循环。
                del num_name[key]
                continue
    print('共提交',count,'份作业')
    print('提交名单',submit_list)
    print('未交', len(num_name),'人，名单',list(num_name.values()))
    print('是否生成excel文件？1是2否')
    # 这行代码将用户从命令行中输入的值赋给了变量flag。该程序现在等待用户输入，等用户输入完毕后才会继续执行。
    flag = input()
    # 这是一条条件语句：如果flag的值等于字符串'1'，将进行以下操作。
    if flag=='1':
        #这行代码通过输出语句向命令行中输出一段字符串，对用户进行提示并告知程序已经执行完毕。
        print('生成完毕，请在本程序同级目录查看')
        # 利用xlwt库创建一个新的Excel工作簿，将其赋给变量f。
        f = xlwt.Workbook()
        # 在工作簿中创建一个名为未交作业名单的新工作表，将其赋给变量sheet1。cell_overwrite_ok=True是一个可选参数，表示在向工作簿中添加单元格时可以覆盖现有单元格。
        sheet1 = f.add_sheet('未交作业名单', cell_overwrite_ok=True)
        # 设置工作表中第一列的宽度为256 * 38，其中256表示每个单元格默认的宽度单位，而38则是自定义的列宽。
        col1 = sheet1.col(0)
        col1.width = 256 * 38
        # 第一个是行，第二格式列 都是从0开始，这个循环通过索引，向每一行的第一列（索引号为0）中写入值，通过列表num_name中的键值对，其中键表示行号，值表示该行中的文本。
        for i in range(0, len(list(num_name.keys()))):
            sheet1.write(i, 0, list(num_name.values())[i])
        # 保存文件,将Excel工作簿保存在同级目录下一个名为未交作业名单.xls的文件中。
        f.save('未交作业名单.xls')
    # 如果flag的值不是'1'，则这个程序会在命令行输出一条字符串，告知用户程序已经取消生成，此时程序会等待2秒钟后退出。这需要使用time库中的sleep()函数来实现。
    else:
        print('取消生成')
        time.sleep(2)

# 这段代码是一个条件语句，它检查变量name的值是否等于字符串'main'。如果是，则调用一个名为main()的函数。
# 这通常用于执行脚本文件时，因为Python的解释器将脚本文件的名称作为模块名存储在__name__变量中。
# 如果脚本文件的名称为'main.py'，则当您运行脚本文件时，__name__变量的值将自动设置为'main'，因此该文件中的所有代码都可以包含在这个if语句下面，并且只有当脚本文件作为主程序运行时，才会执行main()函数。
# 这样可以避免将模块引入其他模块时自动执行一些代码，从而使脚本更灵活。
if __name__ == '__main__':
    main()
