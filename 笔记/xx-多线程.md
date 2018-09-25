### 线程

#### 多任务的简单介绍

- 有很多事情在现实生活的场景中是同时进行的，比如开车的时候 手和脚共同来驾驶汽车，再比如唱歌跳舞也是同时进行的。
- 多任务，就是能够在同一时间同时进行多个任务。
    
    
```
import time
import threading

def sing():
    for i in range(5):
        print("唱歌")
        time.sleep(1)

def dance():
    for i in range(5):
        print("跳舞")
        time.sleep(1)

t1 = threading.Thread(target=sing)
t2 = threading.Thread(target=dance)

t1.start()
t2.start()
```
#### 多任务的原理

- 什么叫“多任务”呢？简单地说，就是操作系统可以同时运行多个任务。打个比方，你一边在用浏览器上网，一边在听MP3，一边在用Word赶作业，这就是多任务，至少同时有3个任务正在运行。还有很多任务悄悄地在后台同时运行着，只是桌面上没有显示而已。
- 单核cpu工作原理
    - 现在，多核CPU已经非常普及了，但是，即使过去的单核CPU，也可以执行多任务。由于CPU执行代码都是顺序执行的，那么，单核CPU是怎么执行多任务的呢？
    - 答案就是操作系统轮流让各个任务交替执行，任务1执行0.01秒，切换到任务2，任务2执行0.01秒，再切换到任务3，执行0.01秒……这样反复执行下去。表面上看，每个任务都是交替执行的，但是，由于CPU的执行速度实在是太快了，我们感觉就像所有任务都在同时执行一样。
    - 真正的并行执行多任务只能在多核CPU上实现，但是，由于任务数量远远多于CPU的核心数量，所以，操作系统也会自动把很多任务轮流调度到每个核心上执行。
- 多核cpu工作原理
    - 和单核类似，相当于多了一个干活的人。

- 并发：指的是任务数多余cpu核数，通过操作系统的各种任务调度算法，实现用多个任务“一起”执行（实际上总有一些任务不在执行，因为切换任务的速度相当快，看上去一起执行而已）
#### - 并行：指的是任务数小于等于cpu核数，即任务真的是一起执行的

- 并行和并发都算是多任务，但并行实际上才是真正的多任务，并发是假的。

#### 线程的工作原理
- 以唱歌跳舞的案例说明
- 主线程
    - 我们常说的一个程序代码会从上往上执行，默认就是主线程来执行的。
- 子线程
    - 人工开启的线程。主线程会等待子线程结束后再结束。

- 线程和线程之间会进行资源的抢夺

#### 线程的两种创建方式
- 直接使用threading模块的Thread类，指定要执行的方法，再调用start
- 使用继承的方式，继承Thread类，重新run方法，创建这个对象后，再调用start

#### 查看当前程序线程数量
- threading.enumerate()
    - 获取所有线程，返回的是一个列表。
    - 如果需要个数，使用len(threading.enumerate())

#### 为子线程传递参数

- target方式

```
import time
import threading 

def sing(nums):
    for i in range(nums):
        print("唱歌")
        time.sleep(1)

def dance():
    for i in range(5):
        print("跳舞")
        time.sleep(1)

t1 = threading.Thread(target=sing, args=(3,))
t2 = threading.Thread(target=dance)

t1.start()
t2.start()
```

- 类继承方式

```
import threading

class Work1(threading.Thread):

    def __init__(self, nums):
        super().__init__()
        self.nums = nums

    def run(self):
        for i in range(self.nums):
            print("haha")


def main():
    w = Work1(2)
    w.start()

if __name__ == "__main__":
    main()
```


