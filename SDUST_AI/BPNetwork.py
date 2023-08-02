import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier


def norm(x):
    x = x.T
    new_list = []
    for i in range(x.shape[0]):
        arr = x[i]
        Min = np.min(arr)
        Max = np.max(arr)
        new_list.append((arr - Min) / (Max - Min))
    new_list = np.asarray(new_list).T
    return new_list


def show_test_details(data, target, string):
    fig = plt.figure()
    ax = Axes3D(fig, rect=(0, 0, 1, 1), elev=20, azim=20, auto_add_to_figure=False)
    ax.scatter(data[:, 0], data[:, 1], data[:, 2], marker='o',
               c=target)
    plt.title(string)
    fig.add_axes(ax)
    plt.show()


def get_model():
    model = MLPClassifier(  # 使用MLPClassifier定义BP神经网络结构
        solver='adam',  # 使用Adam算法实现梯度下降
        activation='relu',  # 网络内部使用relu激活函数
        max_iter=1000,  # 最大迭代次数，控制模型的迭代速度
        alpha=1e-3,  # 正则化项参数
        hidden_layer_sizes=(64, 32, 32),  # 隐藏层神经元个数
    )
    return model


def get_my_data():
    my_cancer = pd.read_csv("./wdbc.data")  # 使用pandas从文件加载WDBC数据
    my_cancer = my_cancer.to_numpy()  # 转化为numpy数据矩阵
    cancer_data = my_cancer[:, 2::]  # 除去无关的身份证ID数据内容
    ori_cancer_target = my_cancer[:, 1]  # 提取数据中的诊断结果，作为target
    cancer_target = []  # 设定诊断结果的01矩阵
    for i in range(ori_cancer_target.__len__()):  # M,B英文字符转化为0，1
        if ori_cancer_target[i] == 'M':
            cancer_target.append(0)
        else:
            cancer_target.append(1)
    cancer_target = np.asarray(cancer_target)  # 将数组数据转化为numpy矩阵
    cancer_data = norm(cancer_data)
    return cancer_data, cancer_target


def main():
    bp_network = get_model()
    cancer_data, cancer_target = get_my_data()
    train_data, test_data = \
        train_test_split(cancer_data, test_size=0.2, random_state=42)  # 分割 输入data为训练0.8，预测0.2比例
    train_goal, test_goal = \
        train_test_split(cancer_target, test_size=0.2, random_state=42)  # 分割 正确结果target为训练0.8，预测0.2比例
    bp_network.fit(train_data, train_goal)  # 使用含target的训练数据，对网络进行拟合
    predict_test_labels = bp_network.predict(test_data)  # 使用测试数据进行预测
    score = bp_network.score(test_data, test_goal)  # 使用含target的测试数据，计算网络评分
    show_test_details(test_data, test_goal, 'REAL DATA')
    show_test_details(test_data, predict_test_labels, 'BP NETWORK PREDICT')
    print(f"预测准确率: {score}")


main()
