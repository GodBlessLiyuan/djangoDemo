# -*- coding: utf-8 -*-
import cv2
from numpy import *
from sklearn.decomposition import PCA
import traceback
import datetime
from sklearn import svm
import os
'''读取拍摄的图片'''
def readImg(imagePath):
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    w, h = gray.shape[0:2]
    smallImg = cv2.resize(gray, (int(h / 3), int(w / 3)))
    cascPath = "D:\\ProMe\\ImageWeb\\PythonPro\\FaceRegLM\\cvTest\\haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascPath)
    faces = faceCascade.detectMultiScale(  # 在灰度图之中找到脸
        smallImg, 1.3, 3
    )
    '''这次是小的 w=89 w=110'''
    for face in faces:
        x, y, w, h = face
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        f = cv2.resize(smallImg[y:y + h, x:x + w], (100, 100))
    cv2.normalize(f, f, 0, 255, cv2.NORM_MINMAX)
    test_face = mat(f).flatten()
    test_face = float32(test_face)
    resImgName = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    cv2.imwrite("D:\\ProMe\\ImageWeb\\PythonPro\\FaceRegLM\\Face\\test3\\" + resImgName + ".jpg", f)
    # cv2.waitKey(10)
    return test_face


'''加载全部图片，参数2是变化的'''
def loadSet(banji_Path,number):
    train_face = zeros((number, 100 * 100))  # 200*
    train_face_number = []
    pathFile = "D:\\ProMe\\ImageWeb\\PythonPro\\FaceRegLM\\Face\\" + banji_Path + "/"
    i = 0
    for files in os.listdir(pathFile):
        try:
            str_number = files.split("_")[0]  # 这是编号
            ImgFile = pathFile + files
            train_face_number.append(str_number)
            image = cv2.imread(ImgFile, 0)
            train_face[i, :] = mat(image).flatten()
            i += 1
        except Exception:
            traceback.print_exc()
    return train_face, train_face_number


'''这程序不是最终的，可能服务器的脚本找不到，先全部写在一个文件中
传入0.85,返回一个纬度值'''
def pca_reswei(data, Threshold):  # 200*11316 30维度
    data = float32(mat(data))  # mat转为矩阵
    rows, cols = data.shape  # 取大小
    '''平均脸'''
    data_mean = mean(data, 0)  # 对列求均值
    data_mean_all = tile(data_mean, (rows, 1))  # 矩阵在行列方向上拉伸
    Z = data - data_mean_all
    T1 = Z * Z.T  # 使用矩阵计算，所以前面mat
    D, V = linalg.eig(T1)  # 特征值与特征向量 #200*200的
    DIndex = argsort(-D)  # 从大到小排序
    '''
    按照道理取出阈值占比0.9；下面是单位化，总之为了计算的数据很小吧
    D是一维的长度
    DIndex[:i]也就是截取前面的长度
    '''
    lenD = len(DIndex)
    DInd_I = 0
    for j in range(lenD):
        temp_DInd_I = DIndex[:j]
        if (D[temp_DInd_I] / D.sum()).sum() >= Threshold:
            DInd_I = len(temp_DInd_I)
            break
    return DInd_I


'''主要使用svm+pca自带的方法，保存pca参数？，目录是项目工程的根目录
'''
def reg_res(testImgPath):
    banji_Path = "test2"
    '''加载图片时间done time=0.010ms  直接读取文本时间：done time=0.001ms'''
    train_face, train_face_number = loadSet(banji_Path,2)#人数是2
    # DInd_I = pca_reswei(train_face, 0.9)
    # print(DInd_I)
    DInd_I=1
    testImg = readImg(testImgPath)
    pca = PCA(n_components=DInd_I, svd_solver='randomized',  # 选择一种svd方式
              whiten=True).fit(train_face)
    '''2365.748 ms  0.004 ms'''

    savePath = "D:\\ProMe\\ImageWeb\\PythonPro\\FaceRegLM\\Face\\data\\" + banji_Path
    if not os.path.exists(savePath):
        X_train_pca = pca.transform(train_face)
        os.makedirs(savePath)
        savez(savePath + "\\" + banji_Path + ".npz", X_train_pca)

    X_pca = load(savePath + "\\" + banji_Path + ".npz")
    X_train_pca = X_pca["arr_0"]

    X_test_pca = pca.transform(testImg)
    clf = svm.SVC()
    clf.fit(X_train_pca, train_face_number)
    X_testNumber = clf.predict(X_test_pca)
    return X_testNumber[0]
    # param_grid = {'C': [1, 5, 10, 20, 30, 40],
    #               'gamma': [0.0001, 0.0005, 0.001, 0.005, 0.01, 0.1, 0.5], }
    # # param_grid = {'C': [1], 'gamma': [0.01], }
    # clf = GridSearchCV(SVC(kernel='rbf', class_weight='balanced'),
    #                    param_grid, cv=2)
    # clf = clf.fit(X_train_pca, train_face_number)
    # print(clf.best_params_)
    # y_pre=clf.predict(X_test_pca)
    # '''长度是len 范围是rannge'''
    # y_pre=y_pre[0]
    # print(y_pre)
