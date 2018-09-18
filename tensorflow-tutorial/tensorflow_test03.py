import tensorflow as tf

# 输出两个矩阵相乘的结果
# create two matrixes
matrix1 = tf.constant([[3,3]])
matrix2 = tf.constant([[2],[2]])
product = tf.matmul(matrix1,matrix2)

# 两种形式使用会话控制Session
# method 1
sess = tf.Session()
result = sess.run(product)
print(result)
sess.close()
#[[12]]

# method 2
with tf.Session() as sess:
    result2 = sess.run(product)
    print(result2)
#[[12]]
