import os


def test_os():
    print(os.listdir("D:/test"))        # 返回指定目录下的所有文件名
#     print(os.path.isdir("D:/test"))   # 判断指定路径是否为目录
#     print(os.path.exists("D:/test"))  # 判断指定路径是否存在


def get_files_recursion_from_dir(path):
    """
    从指定的文件夹中使用递归的方式，读取全部的文件列表
    :param path: 被判断的文件夹
    :return: list，包含全部的文件，如果目录不存在或者无文件就返回一个空list
    """
    print(f"当前判断的文件夹是，{path}")
    file_list = []
    if os.path.exists(path):
        for f in os.listdir(path):
            new_path = path + "/" + f
            if os.path.isdir(new_path):
                file_list += get_files_recursion_from_dir(new_path)
            else:
                file_list.append(new_path)
    else:
        print("目录不存在")
        return []
    return file_list


if __name__ == '__main__':
    print(get_files_recursion_from_dir("D:/test"))
