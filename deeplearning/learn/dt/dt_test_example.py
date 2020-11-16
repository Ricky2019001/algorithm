import math
import operator
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import pickle


def createDataSet():
    '''
    自定义数据set
    :return: dataSet, labels
    '''
    dataSet = [[0, 0, 0, 0, 'no'],
               [0, 0, 0, 1, 'no'],
               [0, 1, 0, 1, 'yes'],
               [0, 1, 1, 0, 'yes'],
               [0, 0, 0, 0, 'no'],
               [1, 0, 0, 0, 'no'],
               [1, 0, 0, 1, 'no'],
               [1, 1, 1, 1, 'yes'],
               [1, 0, 1, 2, 'yes'],
               [1, 0, 1, 2, 'yes'],
               [2, 0, 1, 2, 'yes'],
               [2, 0, 1, 1, 'yes'],
               [2, 1, 0, 1, 'yes'],
               [2, 1, 0, 2, 'yes'],
               [2, 0, 0, 0, 'no']]
    labels = ['年龄', '有工作', '有自己的房子', '信贷情况']
    return dataSet, labels

def calShanEnt(dataSet):
    """

    :param dataSet:
    :return:
    """
    rowLen = len(dataSet)
    lableCnt = {}
    for feaVec in dataSet:
        lable = feaVec[-1]
        if lable not in lableCnt.keys():
            lableCnt[lable] = 0
        lableCnt[lable] += 1
    # cal pro
    calShanPro = 0.0
    for key in lableCnt.keys():
        pro = float(lableCnt[key]) / rowLen
        calShanPro -= pro * math.log(pro, 2)
    return calShanPro


def splitDataSet(dataSet, featureIndex, feature):
    """

    :param dataSet:
    :param featureIndex:
    :param feature:
    :return:
    """
    subDataSet = []
    for elem in dataSet:
        if elem[featureIndex] == feature:
            featureComp = elem[:featureIndex]
            featureComp.extend(elem[featureIndex+1:])
            subDataSet.append(featureComp)
    return subDataSet


def chooseBestFeatFromData(dataSet):
    """

    :param dataSet:
    :return:
    """
    numFeat = len(dataSet[0]) - 1
    baseEnt = calShanEnt(dataSet)
    bestInfoGain = 0.0
    bestFeature = -1
    # all feature
    for i in range(numFeat):
        featElems = [elem[i] for elem in dataSet]
        uniqueVals = set(featElems)
        featEnt = 0.0
        for j in uniqueVals:
            # split dataSet
            subDataSet = splitDataSet(dataSet, i, j)
            pro = float(len(subDataSet))/len(dataSet)
            featEnt += pro * calShanEnt(subDataSet)
        infoGain = baseEnt - featEnt
        print("第%d个特征的增益为%.3f" % (i, infoGain))

        #judge and choose best feature
        if bestInfoGain < infoGain:
            bestInfoGain = infoGain
            bestFeature = i
    print("最优索引 %d" % bestFeature)
    return bestFeature

# 出现最多的实例
def majorityCnt(labels):
    classList = {}
    for elem in labels:
        if elemKey not in elem.keys():
            classList[elemKey] = 0
        classList[elemKey] += 1
    labelSort = sorted(classList.items(), key=lambda x, y: cmp(x[1], y[1]), reverse=True)
    return labelSort[0]



# ID3 algorithm
def createID3Tree(dataSet, labels, featLabels):
    """
    function description
    :param dataSet: data set
    :param labels: class lable
    :param featLabels: best feature
    :return:
    """
    # 取分类标签
    classLabel = [elem[-1] for elem in dataSet]
    # 如果类别相同，结束
    if classLabel.count(classLabel[0]) == len(classLabel):
        return classLabel[0]

    # 遍历后，取出现次数最多的类标签
    if len(dataSet[0]) == 1:
        return majorityCnt[classLabel]
    # 选择最优特征
    bestFeature = chooseBestFeatFromData(dataSet)
    bestFeatureLabel = labels[bestFeature]
    featLabels.append(bestFeatureLabel)

    # 根据最有特征生tree
    myTree = {bestFeatureLabel: {}}

    # del 使用过的lable
    del(labels[bestFeature])
    # 找到到训练集中所有到最优特征的属性值
    featValues = [elem[bestFeature] for elem in dataSet]
    # 去掉重复的属性值
    uniqueVals = set(featValues)

    # 遍历特征，创建决策树
    for value in uniqueVals:
        myTree[bestFeatureLabel][value]=createID3Tree(splitDataSet(dataSet, bestFeature, value),
                                                      labels,featLabels)
    return myTree

# count leaf number
def cntLeafNum(myTree):
    """
    count leaf number
    :param myTree:
    :return:
    """
    cnt = 0
    elemKey = next(iter(myTree))
    elemVal = myTree[elemKey]
    for key in elemVal.keys():
        if type(elemVal[key]).__name__ == 'dict':
            cnt += cntLeafNum(elemVal[key])
        cnt += 1
    return cnt

def deepTree(myTree):
    """
    get depth of tree
    :param myTree:
    :return:
    """
    maxDepth = 0
    elemKey = next(iter(myTree))
    elemVal = myTree[elemKey]
    for key in elemKey.keys():
        if type(elemVal[key]).__name__=='dict':
            depth = 1 + deepTree(elemVal[key])
        else:
            depth = 1
        if depth > maxDepth:
            maxDepth = depth
    return maxDepth

def classify(myTree, featLables, testSet):
    """
    使用决策树进行分类
    :param myTree: 已经生成的决策树
    :param featLables: 存储选择的最优特征
    :param testSet: 测试数据列表，顺序对应最优特征标签
    :return:
    """
    firstStr = next(iter(myTree))
    secondDict = myTree[firstStr]
    featIndex = featLables.index(firstStr)

    for key in secondDict.keys():
        if testSet[featIndex] == key:
            if type(secondDict[key]).__name__=='dict':
                classLabels = classify(secondDict[key], featLables, testSet)
            else:
                classLabels = secondDict[key]
    return classLabels

def storeTree(myTree, filename):
    """
    存储决策树
    :param myTree:
    :param filename: 决策树存储的name
    :return:
    """
    with open(filename, 'wb') as fw:
        pickle.dump(myTree, fw)

def grabTree(filename):
    with open(filename, 'rb') as fd:
        return pickle.load(fd)

if __name__ == '__main__':
    dataSet, labels = createDataSet()
    shanEnt = calShanEnt(dataSet)
    bestFeature = chooseBestFeatFromData(dataSet)
    print("特征：%s" % labels[bestFeature])
    featLabels = []
    myTree = createID3Tree(dataSet, labels, featLabels)
    print(myTree)
    testSet = [0, 1]
    rest = classify(myTree, featLabels, testSet)
    if rest=='yes':
        print('放贷')
    storeTree(myTree, 'classifierStorage.txt')
    myTree = grabTree('classifierStorage.txt')
    print(myTree)
