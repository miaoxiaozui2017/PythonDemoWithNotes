# 综述
* 使用 **图（graph）** 来表示计算任务
* 图中节点被称之为 **op** 。一个op获得0个或多个Tensor，执行计算，产生0个或多个Tensor。
* 使用 **tensor** 表示数据，每个Tensor可以看作是一个类型化的多维数组。一个 tensor 包含一个静态类型 rank, 和 一个 shape.
* 通过 **变量(Variable)** 维护状态信息。
  >Note:通常会将一个统计模型中的参数表示为一组变量. 
    ```python
    # python code
    # 下面的例子演示了如何使用变量实现一个简单的计数器

    # 创建一个变量, 初始化为标量 0.
    state = tf.Variable(0, name="counter")

    # 创建一个 op, 其作用是使 state 增加 1

    one = tf.constant(1)
    new_value = tf.add(state, one)
    update = tf.assign(state, new_value)

    # 启动图后, 变量必须先经过`初始化` (init) op 初始化,
    # 首先必须增加一个`初始化` op 到图中.
    init_op = tf.initialize_all_variables()

    # 启动图, 运行 op
    with tf.Session() as sess:
    # 运行 'init' op
    sess.run(init_op)
    # 打印 'state' 的初始值
    print sess.run(state)
    # 运行 op, 更新 'state', 并打印 'state'
    for _ in range(3):
        sess.run(update)
        print sess.run(state)

    # 输出:

    # 0
    # 1
    # 2
    # 3
    ```
* 使用 **feed** 和 **fetch** 可以为任意的操作（arbitray operation）赋值或者从其中获取数据
    * fetch: 为了取回操作的输出内容, 可以在使用 Session 对象的 run() 调用 执行图时, 传入一些 tensor, 这些 tensor 会帮助你取回结果. 需要获取的多个 tensor 值，在 op 的一次运行中一起获得（而不是逐个去获取 tensor）。
        ```python
        # fetch
        input1 = tf.constant(3.0)
        input2 = tf.constant(2.0)
        input3 = tf.constant(5.0)
        intermed = tf.add(input2, input3)
        mul = tf.mul(input1, intermed)

        with tf.Session():
        result = sess.run([mul, intermed])
        print result

        # 输出:
        # [array([ 21.], dtype=float32), array([ 7.], dtype=float32)]
        ```
    * feed:可以临时替代图中的任意操作中的 tensor 可以对图中任何操作提交补丁, 直接插入一个 tensor.可以提供 feed 数据作为 run() 调用的参数. feed 只在调用它的方法内有效, 方法结束, feed 就会消失. 
        >Note:最常见的用例是将某些特殊的操作指定为 "feed" 操作, 标记的方法是使用 tf.placeholder() 为这些操作创建占位符. 
        ```python
        # feed
        input1 = tf.placeholder(tf.types.float32)
        input2 = tf.placeholder(tf.types.float32)
        output = tf.mul(input1, input2)

        with tf.Session() as sess:
        print sess.run([output], feed_dict={input1:[7.], input2:[2.]})

        # 输出:
        # [array([ 14.], dtype=float32)]
        ```
        >Note2:如果没有正确提供 feed, placeholder() 操作将会产生错误. 
* 在被称之为会话（Session）的上下文（context）中执行图。即图必须在 **会话** 里被启动。
* **会话** 将图的 **op** 分发到诸如CPU或GPU之类的 **设备** 上，同时提供执行op的方法。执行后，将产生的tensor返回。
    >Note:在<b><i>Python</i></b>语言中, 返回的<em>tensor</em>是*numpy ndarray*对象;在*C和C++*语言中,返回的*tensor*是*tensorflow::Tensor*实例.
* TensorFlow程序：构建阶段（op的执行步骤被描述成一个图），执行阶段（使用会话执行图中的op）。
    * 构建图
        * 创建源op（source op）。不需要任何输入，例如 **常量(Constant)** 。输出被传递给其他op做运算。
            >Note:<b><i>Python</i></b>库中,op构造器的返回值代表被构造出的op的输出, 这些返回值可以传递给其它op构造器作为输入.TensorFlow Python库有一个*默认图(default graph)*,op构造器可以为其增加节点.

            ```python
            # python code-1
            import tensorflow as tf
            # 创建一个常量 op, 产生一个 1x2 矩阵. 这个 op 被作为一个节点
            # 加到默认图中.
            #
            # 构造器的返回值代表该常量 op 的返回值.
            matrix1 = tf.constant([[3., 3.]])
            # 创建另外一个常量 op, 产生一个 2x1 矩阵.
            matrix2 = tf.constant([[2.],[2.]])
            # 创建一个矩阵乘法 matmul op , 把 'matrix1' 和 'matrix2' 作为输入.
            # 返回值 'product' 代表矩阵乘法的结果.
            product = tf.matmul(matrix1, matrix2)
            ```
    * 启动图
        * 创建一个 Session 对象, 如果无任何创建参数, 会话构造器将启动默认图.
            ```python
            # python code-2
            # 启动默认图.
            sess = tf.Session()

            # 调用 sess 的 'run()' 方法来执行矩阵乘法 op, 传入 'product' 作为该方法的参数. 
            # 上面提到, 'product' 代表了矩阵乘法 op 的输出, 传入它是向方法表明, 我们希望取回
            # 矩阵乘法 op 的输出.
            #
            # 整个执行过程是自动化的, 会话负责传递 op 所需的全部输入. op 通常是并发执行的.
            # 
            # 函数调用 'run(product)' 触发了图中三个 op (两个常量 op 和一个矩阵乘法 op) 的执行.
            #
            # 返回值 'result' 是一个 numpy `ndarray` 对象.
            result = sess.run(product)
            print result
            # ==> [[ 12.]]

            # 任务完成, 关闭会话.
            sess.close()

            ## 或使用“with”代码块自动完成关闭
            #with tf.Session() as sess:
            #result = sess.run([product])
            #print result
            ```
    * 交互式使用 **(?)**
        * 为了便于使用诸如 IPython 之类的 Python 交互环境, 可以使用 InteractiveSession 代替 Session 类, 使用 Tensor.eval() 和 Operation.run() 方法代替 Session.run(). 这样可以避免使用一个变量来持有会话.
            ```python
            # python code-3
            # 进入一个交互式 TensorFlow 会话.
            import tensorflow as tf
            sess = tf.InteractiveSession()

            x = tf.Variable([1.0, 2.0])
            a = tf.constant([3.0, 3.0])

            # 使用初始化器 initializer op 的 run() 方法初始化 'x' 
            x.initializer.run()

            # 增加一个减法 sub op, 从 'x' 减去 'a'. 运行减法 op, 输出结果 
            sub = tf.sub(x, a)
            print sub.eval()
            # ==> [-2. -1.]
            ```
