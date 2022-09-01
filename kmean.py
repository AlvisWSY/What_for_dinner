import numpy as np  
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
 
def kmeans_building(x1,x2,types_num,types,colors,shapes):
    X = np.array(list(zip(x1, x2))).reshape(len(x1), 2)  
    kmeans_model = KMeans(n_clusters=types_num).fit(X) # 设置聚类数n_clusters的值为types_num
    # 整理分类好的原始数据, 并画出聚类图
    x1_result=[]; x2_result=[]
    for i in range(types_num):
        temp=[]; temp1=[]
        x1_result.append(temp)
        x2_result.append(temp1)
    for i, l in enumerate(kmeans_model.labels_):  # 画聚类点
        x1_result[l].append(x1[i])
        x2_result[l].append(x2[i])
        plt.scatter(x1[i], x2[i], c=colors[l],marker=shapes[l])
    for i in range(len(list(kmeans_model.cluster_centers_))): # 画聚类中心点
        plt.scatter(list(list(kmeans_model.cluster_centers_)[i])[0],list(list(kmeans_model.cluster_centers_)[i])[1],c=colors[i],marker=shapes[i],label=types[i])
    plt.legend()
    return kmeans_model,x1_result,x2_result
