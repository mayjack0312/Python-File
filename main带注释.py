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
    flag = input()
    if flag=='1':
        print('生成完毕，请在本程序同级目录查看')
        # 创建工作簿
        f = xlwt.Workbook()
        # 创建一个sheet
        sheet1 = f.add_sheet('未交作业名单', cell_overwrite_ok=True)
        col1 = sheet1.col(0)
        col1.width = 256 * 38
        # 第一个是行，第二格式列 都是从0开始
        for i in range(0, len(list(num_name.keys()))):
            sheet1.write(i, 0, list(num_name.values())[i])
        # 保存文件
        f.save('未交作业名单.xls')
    else:
        print('取消生成')
        time.sleep(2)

if __name__ == '__main__':
    main()
