# coding = utf-8

# 基于项目的协同过滤推荐算法实现

class ItemBasedCF():
    # 初始化参数
    def __init__(self):
        # 找到相似的20部电影，为目标用户推荐10部电影
        self.n_sim_movie = 20
        self.n_rec_movie = 10

        # 将数据集划分为训练集和测试集
        self.trainSet = {}
        self.testSet = {}

        # 用户相似度矩阵
        self.movie_sim_matrix = {}
        self.movie_count = 0

        print('Similar user number = %d' % self.n_sim_movie)
        print('Recommneded movie number = %d' % self.n_rec_movie)




if __name__ == '__main__':
    rating_file = 'D:\\学习资料\\推荐系统\\ml-latest-small\\ratings.csv'
    itemCF = ItemBasedCF()
    # itemCF.get_dataset(rating_file)
    # itemCF.calc_movie_sim()
    # itemCF.evaluate()