# MovieRecommendation 

基于Python3，实现电影推荐系统，数据集是MovieLens官方数据集【见data.txt】   
   
基于用户的协同过滤算法UserCF，UserCF的思想见博客：http://blog.csdn.net/u012050154/article/details/52268057    
基于项目的协同过滤算法ItemCF  

关于推荐系统的介绍见博客：http://blog.csdn.net/u012050154/article/details/52267712
# 协同过滤

## 一、算法的基本原理

协同过滤算法，就是一种完全依赖用户和物品之间行为关系的推荐算法。

先从一个栗子入手：假设电商平台中有4个商品（游戏机、小说、杂志和电视机）。
任务：一用户X访问该网站，推荐系统要决定是否将电视机推荐给X用户。

（1）将下图的有向图转成【共现矩阵】，其中点赞可以设置为数字1，踩可以设置为-1，没有用户行为就设置为0。如果有具体的评分，也可以取具体的评分（没有用户行为也可以设置为评分的均值）。

![协同过滤](https://user-images.githubusercontent.com/46898984/155595706-4d92205e-1658-481b-8597-f069dfad685e.png)

（2）现在问题变成预测矩阵中的“问号”。在“协同”过滤算法中，推荐的原理是让用户考虑与自己兴趣相似用户的意见。所以预测的第一步就是找到与用户 X 兴趣最相似的 n（Top n 用户，这里的 n 是一个超参数）个用户，然后综合相似用户对“电视机”的评价，得出用户X 对“电视机”评价的预测。

（3）从共现矩阵中我们可以知道，用户 B 和用户 C 由于跟用户 X 的行向量近似，被选为 Top n（这里假设 n 取 2）相似用户，用户 B 和用户 C 对“电视机”的评价均是负面的。因为相似用户对“电视机”的评价是负面的，所以预测出用户 X 对“电视机”的评价也是负面的。

## 二、计算用户相似度

在共现矩阵中，每个用户对应的行向量其实就可以当作一个用户的 Embedding 向量。
利用余弦相似度了，它衡量了用户向量 i 和用户向量 j 之间的向量夹角大小。夹角越小，余弦相似度越大，两个用户越相似，定义：
$$
sim(i,j)=cos(i,j)= \frac{i⋅j}{∥i∥×∥j∥}
$$
改进：现在大佬们又使用如Word2vec，Item2vec等Embedding类的算法，将物品嵌入固定的向量空间中，再使用LSH算法(局部敏感哈希算法)取最近邻物品，即根据相似度排序取最近邻的物品。

## 三、用户评分的预测

在获得 Top n 个相似用户之后，利用 Top n 用户生成最终的用户 u 对物品 p 的评分的过程，可以基于假设：目标用户和top n用户喜好相似。最直接计算是利用用户相似度，和相似用户评价的加权平均值：
$$
\mathrm{R}_{\mathrm{u}, \mathrm{p}}=\frac{\sum_{\mathrm{s} \in \mathrm{S}}\left(\mathrm{w}_{\mathrm{u}, \mathrm{s}} \cdot \mathrm{R}_{\mathrm{s}, \mathrm{p}}\right)}{\sum_{\mathrm{s} \in \mathrm{S}} \mathrm{w}_{\mathrm{u}, \mathrm{s}}}
$$
其中Wu,s是用户u和用户s之间的相似度，而Rs,p是用户s对商品p的评分。就这样得到Ru,p即目标用户u对物品p的预测评分（其他商品也是一样道理），根据这个分数对商品排序，从而得到推荐列表。

上面的方法是用户(user)之间的相似度计算，当然也可以利用商品(item)之间的相似度计算，如下栗子：
如下图，通过用户B对图书1的评分 × 未知图书与图书1的相似度来预测用户B对剩下图书的评分。如图书2的预测评分 = 图书1的评分5分 × 图书1和图书2的相似度0.27 ，从而用户B对图书2的评分是：5*0.27=1.35。同样方式计算出其他图书的评分预测。
![商品](https://user-images.githubusercontent.com/46898984/155595774-99feff6d-76c4-44d5-a93d-af9fe5664466.png)
