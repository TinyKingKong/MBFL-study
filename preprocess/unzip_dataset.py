# 乱
import os
import tarfile
import gzip
from pathlib import Path


def search_files(dir_path):
    result = []
    file_list = os.listdir(dir_path)  # 获取当前文件夹下的所有文件
    for file_name in file_list:
        complete_file_name = os.path.join(dir_path, file_name)  # 获取包含路径的文件名
        if os.path.isdir(complete_file_name):  # 如果是文件夹
            result.extend(search_files(complete_file_name))  # 文件夹递归
        if os.path.isfile(complete_file_name):  # 文件名判断是否为文件
            result.append(complete_file_name)  # 添加文件路径到结果列表里
    return result


def unzip_gz_file(gz_path):  # 传入路径
    try:
        for f in os.listdir(gz_path):
            if ".csv.gz" in f:
                g = gzip.GzipFile(mode="rb", fileobj=open(gz_path + "\\" + f, 'rb'))
                open(gz_path + "\\" + f.replace(".gz", ""), "wb").write(g.read())
    except Exception as e:
        print(e)


def unzip_tar_gz_files(project_id):
    # 第一步：当只有32h/168h-killmap.tar.gz或者32h-unoptimized-killmap.tar.gz时，扫描project文件夹(Chart,Time,...)，发现有.tar.gz结尾的，就解压到当前文件夹
    # project_dir = os.path.join(os.path.abspath('../..'), 'fault-localization-data',
    #                            'fault-localization.cs.washington.edu',
    #                            'data', project_id)
    # 另外5个用这个project_dir
    project_dir = os.path.join('G:\\', project_id) # Closure用这个project_dir
    print(project_dir)
    tar_gz_files_list = search_files(project_dir)
    for tar_gz_file in tar_gz_files_list:
        if not str(tar_gz_file).endswith('.tar.gz'):
            tar_gz_files_list.remove(tar_gz_file)
    print(tar_gz_files_list)

    for tar_gz_file in tar_gz_files_list:
        tar_gz_path = Path(tar_gz_file)
        f = tarfile.open(str(tar_gz_file))
        print(tar_gz_path.parent)
        f.extractall(tar_gz_path.parent)
        f.close()

def unzip_csv_gz_files(project_id):
    #第二步，只解压那些.csv.gz的文件，同样解压到当前文件夹


    # project_dir = os.path.join(os.path.abspath('../..'), 'fault-localization-data',
    #                            'fault-localization.cs.washington.edu',
    #                            'data', project_id)
    # 另外5个用这个project_dir

    project_dir = os.path.join('G:\\', str(project_id))# Closure用这个project_dir
    print(project_dir)
    file_list = search_files(project_dir)
    csv_gz_file_list = []
    for file in file_list:
        if str(file).endswith('csv.gz'):
            csv_gz_file_list.append(file)
    for csv_gz_file in csv_gz_file_list:
        csv_gz_path = Path(csv_gz_file).parent
        print(csv_gz_path)
        unzip_gz_file(str(csv_gz_path))



if __name__ == '__main__':

    # chart time Lang Math Mockito
    # unzip_tar_gz_files('Closure')
    # unzip_csv_gz_files('Closure')
    pass


