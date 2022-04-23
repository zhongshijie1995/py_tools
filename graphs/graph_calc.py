import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
import numpy as np


def get_dg():
    # 获取文件信息
    df_csv_file_path = input('请输入图信息路径：')
    # 读取给定csv的图信息
    df_dg = pd.read_csv(df_csv_file_path, dtype={'pre': str, 'node': str, 'cost': float})
    df_dg = df_dg.fillna('调度起点')
    # 回执有向权重图
    dg = nx.DiGraph()
    dg.add_weighted_edges_from(np.array(df_dg))
    return dg


def get_longest_path_length():
    print('关键路径长度：', nx.dag_longest_path_length(get_dg()))


def get_jpg():
    dg = get_dg()
    print(nx.topological_sort(dg))
    nx.draw(dg, with_labels=True)
    plt.show()


def make_dg_csv():
    mix_file_path = input('请输入多对一图信息路径：')
    dg_jpg_file_path = input('请输入图信息路径：')
    df = pd.DataFrame({'pre': [], 'node': [], 'cost': []})
    with open(mix_file_path) as f:
        lines = f.readlines()
        for line in lines:
            if ',' in line:
                v_list = line.split('&&&')
                for i in v_list[0].split(','):
                    df.loc[len(df.index)] = [i, v_list[1], v_list[2].strip()]
            else:
                v_list = line.split('&&&')
                df.loc[len(df.index)] = [v_list[0], v_list[1], v_list[2].strip()]
    df.to_csv(dg_jpg_file_path, index=False)


def menu_choose(_menu_list: list):
    while True:
        print('******************************************************')
        print('------------------------------')
        for menu in _menu_list:
            print(menu[0], menu[1])
        print('------------------------------')
        choose = int(input('请选择功能：'))
        _menu_list[choose][2]()
        print('******************************************************')


def main():
    menu_list = [
        [0, '获取有向权重图的关键路径长度', get_longest_path_length],
        [1, '将混合多前序的图转化为节点图信息', make_dg_csv],
        [2, '绘制图', get_jpg]
    ]
    menu_choose(menu_list)


if __name__ == '__main__':
    main()
