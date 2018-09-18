# tensor:零阶张量->数值，一阶张量->向量，二阶张量->矩阵，。。。
# flow：算法设计图，设计好了放入数据即可执行
# tensorflow如何搭建模型

# 1.创建数据
import tensorflow as tf
import numpy as np

# create data
x_data = np.random.rand(100).astype(np.float32)
y_data = x_data*0.1 + 0.3

# 2.搭建模型
# 用tf.Variable来创建描述y的参数，把y_data = x_data*0.1+0.3想象成y=Weights*x + biases
Weights = tf.Variable(tf.random_uniform([1],-1.0,1.0))
biases = tf.Variable(tf.zeros([1]))

y = Weights*x_data + biases
# 3.计算误差
# 计算y和y_data的误差
loss = tf.reduce_mean(tf.square(y-y_data))
# 4.传播误差
# 使用梯度下降法Gradient Descent作为误差传递方法，使用optimizer进行参数的更新
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)

# 5.训练
# 在使用神经网络结构之前，必须初始化所有Variable
# init = tf.initialize_all_variables()  # tf马上就要废弃这种写法？
init = tf.global_variables_initializer()    # 替换成这样就好
# 创建会话Session用来执行init初始化步骤，用Session来ru每一次的training的数据，逐步提升神经网络的预测准确性
sess = tf.Session()
sess.run(init)  # Very important

for step in range(201):
    sess.run(train)
    if step % 20 == 0:
        print(step,sess.run(Weights),sess.run(biases))

