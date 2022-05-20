import os
import xlwt
def findAllFile(base):
    for root, ds, fs in os.walk(base):
        for f in fs:
            yield f

def main():
    base = r'C:/Users/13552/Desktop/3月2号'
    count=0
    num_name={
    '1': '李蕊',
    '2': '崇家畅',
    '3': '张佳琪',
    '4': '姜明伟',
    '5': '李浩宇',
    '6': '邵雨生',
    '7': '安皓',
    '8': '安硕',
    '9': '蔡宇杰',
    '10': '孙铱洋',
    '11': '王一帆',
    '12': '韩奉孝',
    '13': '李宏扬',
    '14': '杨佳一',
    '15': '赵衍儒',
    '16': '李铭杨',
    '17': '李奕菲',
    '18': '刘博文',
    '19': '高非凡',
    '20': '李冬',
    '21': '任轩祺',
    '22': '赵宏博',
    '23': '谭博文',
    '24': '王麒淞'
    }
    submit_list=[]
    submit_list2=[]
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
        print('生成完毕，请在桌面查看')
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
        f.save(r"C:\Users\13552\Desktop\3月2号\名单.xls")
    else:
        print('取消生成')
if __name__ == '__main__':
    main()
