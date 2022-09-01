{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": ,
   "id": "0b4444bb",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np  \n",
    "from sklearn.cluster import KMeans\n",
    "import matplotlib.pyplot as plt\n",
    " \n",
    "def kmeans_building(x1,x2,types_num,types,colors,shapes):\n",
    "    X = np.array(list(zip(x1, x2))).reshape(len(x1), 2)  \n",
    "    kmeans_model = KMeans(n_clusters=types_num).fit(X) \n",
    "    x1_result=[]; x2_result=[]\n",
    "    for i in range(types_num):\n",
    "        temp=[]; temp1=[]\n",
    "        x1_result.append(temp)\n",
    "        x2_result.append(temp1)\n",
    "    for i, l in enumerate(kmeans_model.labels_): \n",
    "        x1_result[l].append(x1[i])\n",
    "        x2_result[l].append(x2[i])\n",
    "        plt.scatter(x1[i], x2[i], c=colors[l],marker=shapes[l])\n",
    "    for i in range(len(list(kmeans_model.cluster_centers_))):\n",
    "        plt.scatter(list(list(kmeans_model.cluster_centers_)[i])[0],list(list(kmeans_model.cluster_centers_)[i])[1],c=colors[i],marker=shapes[i],label=types[i])\n",
    "    plt.legend()\n",
    "    return kmeans_model,x1_result,x2_result"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3.8.8 64-bit ('base': conda)",
   "language": "python",
   "name": "python388jvsc74a57bd0b4dd568c1cd3f39d93132ac3881c8c227ac882cbf5cf32a9a74e936c7fb23d10"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
