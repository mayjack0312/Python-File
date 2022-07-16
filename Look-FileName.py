# coding=utf-8

import os

path = repr((os.getcwd())).strip('"\'')

def print_files(path):
    lsdir = os.listdir(path)
    dirs = [i for i in lsdir if os.path.isdir(os.path.join(path, i))]
    files = [i for i in lsdir if os.path.isfile(os.path.join(path, i))]
    if files:
        for f in files:
            print(os.path.join(path, f))
    if dirs:
        for d in dirs:
            print_files(os.path.join(path, d))

fileList = os.listdir(path)
def show_file_tree(path):
    file_list=os.listdir(path)
    global file_count, folder_count
    for i in file_list:
        path_now = path + "\\" + i
        if os.path.isdir(path_now)==True:
            folder_count=folder_count+1
            show_file_tree(path_now)
        else:
            file_count = file_count + 1

if __name__ == '__main__':
    file_count = 0
    folder_count = 0
    dict_count=show_file_tree(path)

    print("当前目录路径：",path)
    print("总文件个数(计算后）:",file_count)
    print("总文件夹个数(计算后）:",folder_count)
    print("当前目录下所有文件：")
    print(str(fileList))
    print("目录下所有文件路径：")
    print_files(path)
