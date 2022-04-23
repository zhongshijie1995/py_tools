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


def paths_compare(paths_num: int = 2):
    paths = []
    dirs_dict = dict({})
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
        print('第%d组目录比第%d组目录多的文件：' % (i, j))
        result = {x: x not in dirs_dict[paths[j]] for x in dirs_dict[paths[i]]}
        for k, v in result.items():
            if v:
                print(k)
        print('--------------')
    for (i, j) in list(itertools.combinations(range(paths_num), 2)):
        print('第%d组目录与第%d组目录中内容不同的文件：' % (i, j))
        result = {x: dirs_dict[paths[i]] != dirs_dict[paths[j]] for x in dirs_dict[paths[i]] if x in dirs_dict[paths[j]]}
        for k, v in result.items():
            if v:
                print(k)
        print('--------------')


def main():
    paths_compare()


if __name__ == '__main__':
    main()
