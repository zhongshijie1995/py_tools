import itertools
import os
import hashlib


def get_file_md5(file_path: str) -> str:
    with open(file_path, 'rb') as f:
        md5_obj = hashlib.md5()
        while True:
            d = f.read(8096)
            if not d:
                break
            md5_obj.update(d)
        hash_code = md5_obj.hexdigest()
    md5 = str(hash_code).lower()
    return md5


def paths_compare(paths_num: int = 2) -> dict:
    paths = []
    dirs_dict = dict({})
    compare_dict = dict({})
    for i in range(paths_num):
        target_dir = input('请输入第%d组目录：' % i)
        paths.append(target_dir)
        dirs_dict[target_dir] = dict({})
        for root, dirs, names in os.walk(target_dir):
            for filename in names:
                file_path = os.path.join(root, filename)
                sub_file_path = '.' + file_path.strip(target_dir)
                dirs_dict[target_dir][sub_file_path] = get_file_md5(file_path)
    for (i, j) in list(itertools.permutations(range(paths_num), 2)):
        result = {x: x not in dirs_dict[paths[j]] for x in dirs_dict[paths[i]]}
        tmp = []
        for k, v in result.items():
            if v:
                tmp.append(k)
        compare_dict['第%d组目录 - 第%d组目录：' % (i, j)] = tmp
    for (i, j) in list(itertools.combinations(range(paths_num), 2)):
        result = {x: dirs_dict[paths[i]] != dirs_dict[paths[j]] for x in dirs_dict[paths[i]] if x in dirs_dict[paths[j]]}
        tmp = []
        for k, v in result.items():
            if v:
                tmp.append(k)
        compare_dict['第%d组文件 != 第%d组文件：' % (i, j)] = tmp
    return compare_dict


def main():
    for k, v in paths_compare().items():
        print(k)
        for i in v:
            print(v)
        print('-------------------------------')


if __name__ == '__main__':
    main()
