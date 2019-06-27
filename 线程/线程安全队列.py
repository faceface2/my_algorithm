import queue
import threading
import time


## 封装的安全队列类（十分通用）
class SafeQueue(threading.Thread):
    # 退出队列的信号
    SIG_QUIT = 'sig_quit'

    def __init__(self, recv_calback):
        threading.Thread.__init__(self)
        ## 构造线程安全队列
        self.Q = queue.Queue()
        self.recv_calback = recv_calback
        self.start()

    # 放入队列
    def put(self, datas):
        threadName = threading.currentThread().name
        self.Q.put(datas)

    # 关闭队列
    def close(self):
        self.put(SafeQueue.SIG_QUIT)

    ##主循环,处理队列接收
    def run(self):
        while True:
            try:
                datas = self.Q.get()
                if datas == SafeQueue.SIG_QUIT:  # 收到退出队列信号
                    break
                # 回调客户端
                self.recv_calback(datas)
            except:  # 抛出打断异常
                break


##队列回调函数
def queue_callback(datas):
    print("接收到数据:", datas)
    ## 将子任务结果加入 全局集合
    try:
        array_mutex.acquire()  # 锁定
        datas_array.append(datas)
        if len(datas_array) == 4:
            safeQueue.close()
            print("=======大任务计算结束===========  result:", datas_array)
    finally:
        array_mutex.release()  # 释放


## 子任务计算函数
def calclulate():
    threadName = threading.currentThread().name
    print(threadName, ' 正在计算')
    time.sleep(2)
    print(threadName, ' 计算完成,加入队列')
    # 将结果放入队列
    safeQueue.put(threadName + "' result")


####  ----------  main start   ----------

# 创建锁
array_mutex = threading.Lock()
## 存储 子任务计算结果的 集合
datas_array = []

##构造安全队列
safeQueue = SafeQueue(queue_callback)

##开启4 个子任务,开始计算
for i in range(1, 5):
    threading.Thread(target=calclulate).start()
