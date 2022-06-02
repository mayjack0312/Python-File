import os
import xlwt
import time

def findAllFile(base):
    for root, ds, fs in os.walk(base):
        for f in fs:
            yield f

def main():
    base = repr((os.getcwd())).strip('"\'')
    count=0
    num_name={
    '01': '',
    '02': '',
    '03': '',
    '04': '',
    '05': '',
    '06': '',
    '07': '',
    '08': '',
    '09': '',
    '10': '',
    '11': '',
    '12': '',
    '13': '',
    '14': '',
    '15': '',
    '16': '',
    '17': '',
    '18': '',
    '19': '',
    '20': '',
    '21': '',
    '22': '',
    '23': '',
    '24': ''
    }
    submit_list=[]
    submit_list2=[]
    for i in findAllFile(base):
        for a in num_name:
            if i[0:2]==a:
                submit_list.append(a+''+num_name[a])
                submit_list2.append(a)
                count += 1
    for key in list(num_name.keys()):
        for i in submit_list2:
            if key==i:
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
