import shutil
import re
import math
import os


def riyu():
    path_file = '/Users/wangdaodao/日语学习'

    os.chdir(path_file)

    print(os.getcwd())
    for a, b, c in os.walk(os.getcwd()):
        for aa in c:
            if '.' not in aa:
                old_name = '{}/{}'.format(path_file, aa)
                new_name = '{}/{}.mp4'.format(path_file, aa)
                print(old_name, new_name)
                os.rename(old_name, new_name)
            elif '2023' in aa:
                # print(os.path.join(path_file,))
                old_name = '{}/{}'.format(path_file, aa)
                bb = aa.split(' ')[-1]
                print(bb)
                new_name = '{}/{}'.format(path_file, bb)
                print(old_name, new_name)


def rename_and_move_files(src_folder, dest_folder):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)  # 如果目标文件夹不存在，创建它
    for file_name in os.listdir(src_folder):
        if file_name.endswith('.mp3'):
            print(file_name)
            base_name, ext = os.path.splitext(file_name)  # 分离文件名和扩展名
            new_base_name = re.sub(r'[^\w\s]+', '', base_name)  # 只去掉文件名中的特殊符号
            new_file_name = new_base_name + ext  # 重新组合文件名和扩展名
            src_file_path = os.path.join(src_folder, file_name)
            dest_file_path = os.path.join(dest_folder, new_file_name)
            print(dest_file_path)
            if os.path.exists(dest_file_path):
                print('存在了')
            else:
                shutil.move(src_file_path, dest_file_path)  # 移动文件



f_path = '/Users/wangdaodao/日语学习/语法'
for a, b, c in os.walk(f_path):
        for aa in c:
            if '.' not in aa:
                old_name = '{}/{}'.format(f_path, aa)
                new_name = '{}/{}.mp4'.format(f_path, aa)
                print(old_name, new_name)
                os.rename(old_name, new_name)
            elif '①' not in aa:
                old_name = '{}/{}'.format(f_path, aa)               
                new_name = '{}/①{}'.format(f_path, aa)
                os.rename(old_name, new_name)
                print(old_name, new_name)
            
