# -*- coding: utf-8 -*-
# @Author : ZhaoKe
# @Time : 2021-04-01 15:12
import numpy as np
import matplotlib.pyplot as plt

from utils.Entities import VM, Cloudlet


def get_sample_data():
    data = []
    with open('cloudlets20r2data.txt', 'r') as f:
        for i in range(20):
            str = f.readline()
            nums = str[10:-5].split(', ')
            # print(nums)
            nums = list(map(float, nums))
            # print(nums)
            data.append(nums)
        f.close()
    # data = np.array(data, )
    # print(data)
    temp = np.sum(data, axis=0)
    NUM_MAX1 = temp[0]
    NUM_MAX2 = temp[1]
    num = 20
    # CPU
    data_mean1 = NUM_MAX1 / num
    print(data_mean1)
    new_data1 = np.random.normal(loc=data_mean1 - 0.0596, scale=0.06, size=num)
    # 内存
    data_mean2 = NUM_MAX2 / num
    print(data_mean2)
    new_data2 = np.random.normal(loc=data_mean2 - 37, scale=47, size=num)
    # # IO
    # data_mean3 = NUM_MAX3 / num
    # print(data_mean3)
    # new_data3 = np.random.normal(loc=data_mean3 - 0.708, scale=0.308, size=num)

    data = np.array([new_data1, new_data2])

    data = data.transpose()
    # print(data)
    for i in data:
        print('Cloudlet(', i[0], ',', i[1], '),')


def generateDataFromSrcData():
    data = []
    with open('cloudlets20r2data.txt', 'r') as f:
        for i in range(20):
            str = f.readline()
            nums = str[10:-5].split(', ')
            # print(nums)
            nums = list(map(float, nums))
            # print(nums)
            data.append(nums)
        f.close()
    data = np.array(data)
    print(data)
    # means = np.mean(data, axis=0)
    # stds = np.std(data, axis=0)
    # new_data = []
    # for i in range(2):
    #     new_data.append(np.random.normal(loc=means[i], scale=stds[i], size=12))
    # new_data = np.array(new_data).transpose()
    #
    for it in data:
        print("Cloudlet(", it[0], ',', it[1], "),")
    # # pass


def print_as_csv():
    nodes = [
        VM(0, 0.762, 2, 920, 2223, 400, 2000),
        VM(1, 0.762, 2, 1200, 2223, 1000, 2000),
        VM(2, 0.762, 2, 850, 2223, 800, 2000),
        VM(3, 0.762, 2, 1200, 2223, 900, 2000),  # 4
    ]
    lets = [
        Cloudlet(0.078400, 60.689797, 228.9767518),
        Cloudlet(0.065683, 185.848012, 187.979460),
        Cloudlet(0.050440, 96.030497, 206.7731532),
        Cloudlet(0.104019, 131.428883, 218.7860084),  # 4
        Cloudlet(0.022355, 192.582491, 231.97106946),
        Cloudlet(0.232862, 226.085299, 233.033903),
        Cloudlet(0.194654, 77.503350, 190.41556474),
        Cloudlet(0.148194, 241.349622, 264.54314854),  # 8
        Cloudlet(0.146926, 199.978750, 248.28244),
        Cloudlet(0.081256, 149.824589, 243.1697241),
        Cloudlet(0.237547, 141.050771, 277.01199505),
        Cloudlet(0.138457, 139.508608, 271.253561477),
        Cloudlet(0.088451, 133.618232, 245.98393322),
        Cloudlet(0.266167, 156.087665, 214.0397748),
        Cloudlet(0.130581, 158.033508, 251.243065088),
        Cloudlet(0.099247, 211.409329, 197.81288978),  # 16
        Cloudlet(0.124647, 259.696868, 245.596727694),
        Cloudlet(0.076976, 186.666789, 277.310805967),  # 18
    ]
    for node in nodes:
        print(node.str_as_row())
    print("--------")
    for let in lets:
        print(let.str_as_row())


if __name__ == '__main__':
    # get_sample_data()
    # generateDataFromSrcData()
    print_as_csv()
