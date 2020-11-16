import pandas as pd
from sklearn.preprocessing import LabelEncoder

if __name__ == '__main__':

    with open('lenses.txt', 'r') as fd:
        lense = [inst.strip().split('\t') for inst in fd.readlines()]
    lense_target = []
    for each in lense:
        lense_target.append(each[-1])
    lenses_labels = ['age', 'prescript', 'astigmatic', 'tearRate']
    leanse_dict = {}
    lense_list = []
    for each_label in lenses_labels:
        for each in lense:
            lense_list.append(each[lenses_labels.index(each_label)])
        leanse_dict[each_label]=lense_list
        lense_list = []
    print(leanse_dict)
    lense_pd = pd.DataFrame(leanse_dict)
    print(lense_pd)

    # 创建LabelEncoder()对象，用于序列化
    label_encoder = LabelEncoder()
    for col in lense_pd.columns:
        lense_pd[col] = label_encoder.fit_transform(lense_pd[col])
    print(lense_pd)