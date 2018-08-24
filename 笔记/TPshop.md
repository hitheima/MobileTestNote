

## TPShop

### 跑脚本

在1.0的时候，写的自动化脚本。在下一个版本的时候先跑一边。看报告

1. 如果通过 - 基本上这些功能都没有问题。

2. 如果没有通过 - 进行功能测试 - 找原因 
   1. 如果是脚本设计的问题，不忙的时候修改脚本
   2. 如国是软件的问题，写报告，让开发改！！！

### 下载&安装

http://sj.qq.com/myapp/detail.htm?apkName=com.tpshop.malls&apkCode=2

com.tpshop.malls_2.1.0_2.apk

### 测试用例

| 测试用例编号   | 测试用例标题 | 预置条件 | 测试步骤 | 预期结果 | 实际结果 |
| -------------- | ------------ | -------- | -------- | -------- | -------- |
|  |    |  |          |          |          |

- test_login_001
  - 正确手机号
  - 正确密码
- test_login_002
  - 正确手机号
  - 错误密码
- test_login_003
  - 正确手机号+空格
  - 正确密码
- test_login_004
  - 空格+正确手机号
  - 正确密码
- test_login_005
  - 多一位手机号
  - 正确密码
- test_login_006
  - 少一位手机号
  - 正确密码
- test_login_007
  - 空手机号
  - 正确密码
- test_login_008
  - 正确手机号
  - 空密码
- test_login_009
  - 不符合规则的手机号码
  - 正确的密码

### 分析哪些可以用参数化

也就是哪些脚本的流程是相同的。

### 初始化项目

新建项目

将之前的项目中的base和pytest.ini直接复制到新的项目中。

参考：https://github.com/hitheima/TPShop_BJ4.git（以后简称之前的项目）

### 上传到github

- 网站

1. git创建新项目
2. 准备获取远程地址
3. 不要勾选readme等三个文件

- pycharm

1. 进入到项目目录
2. git init
3. 复制之前的项目的忽略文件，并拷贝到项目下
4. git 提交
5. git 添加远程地址
6. git push

### 跳转到登录界面

1. 创建scripts和page模块。
2. 创建test_login文件。
3. 编写setup代码
4. 连接手机，需要用到init_driver（导模块）
   1. 检查跳转到的程序是否正确
5. 创建page入口，需要用到Page（导模块）
   1. 创建page文件，并写类。
   2. 需要创建LoginPage对象
      1. 创建login_page文件，并写类。
   3. 创建LoginPage需要driver
      1. 在page中，写构造方法（init），并且传入driver
   4. 增加属性装饰器，让方法变成属性。@property
6. 编写test_login脚本的注释
   1. 首页 - 我的
   2. 我的 - 登录/注册
   3. 登录 - 输入用户名
   4. 登录 - 输入密码
   5. 登录 - xxx
7. 注意：元素在哪个页面就是哪个页面。
8. 创建home_page和mine_page。
9. 在这两个文件中，写对应的类，元素，动作
10. 在test_login进行调用

### 登录基本功能

1. 编写test_login脚本的注释

   1. 在跳转到登录界面后
   2. 登录 - 输入用户名
   3. 登录 - 输入密码
   4. 登录 - 点击登录
   5. 使用断言+条件的形式，判断是否登录成功
      1. 判断的条件，根据测试用例中的预期来写（toast=对应的提示）
      2. 在base中写一个is_toast_exist的方法专门用来判断toast是否存在
         1. 通过try的形式，如果find_toast不报错，返回True，反之亦然


### 修改find_element的默认时间

1. 因为toast的时间很短，如果使用我们之前写的find_element方法，那么频率为1秒一次。
2. 此时toast很可能已经消失，所以想让这个时间尽量小。
3. 我们需要在find_element增加默认参数，timeout，poll，如果有其他需要，则传入指定参数即可。
4. 注意：int可以自动转float，float不可以自动转int

### 登录的数据参数化

1. 新建data文件夹，创建login_data的文件。
2. 使用之前的形式来写数据。
3. 主要是三个内容。
4. 用户名，密码，期望结果。
5. 修改对应的test_login脚本即可。

### 登录功能增加报告描述

1. 在page的动作中，增加step步骤。
2. 在里面的涉及输入的部分，增加所输入的用户名和密码，使用attach方法。

### 只输入用户名或密码的脚本

1. 先写数据。
2. 一个只有用户名，密码为空字符串
3. 一个只有密码，用户名为空字符串
4. 编写一个test_login_miss_part函数
   1. 判断，
   2. 如果有用户名，只输入用户名
   3. 如果有密码，只输入密码
   4. 断言 判断登录按钮是否为不可用状态
      1. 在base中，写一个is_feature_enabled的方法
      2. 这个函数，根据feature，再通过find_element找到元素
      3. 再通过get_attribute("enabled")获取状态。
      4. 注意，获取到的是一个 “true” 或者 ”false“ 的字符串 
      5. 判断字符串后，返回对应的布尔值

### 显示密码的脚本的基本功能

1. 首页 - 我的
2. 我的 - 登录/注册
3. 输入密码
4. 点击显示密码按钮
5. 判断刚刚输入的密码是否存在
   1. 在base中，增加一个is_feature_exist的方法
   2. 根据feature通过find_element方法进行查找。
   3. 如果找到，则返回true
   4. 如果没找到会报错，在except中返回false即可

### 关于显示点击显示密码的补充

1. 在点击显示密码之前，应该先判断，输入密码后，是找不到的。（密码默认是隐藏的状态）
2. 当一开始找不到的时候再去点击显示密码，并判断第二是是否可以找到。
3. 根据第二次的结果，进行断言，第二次能找到，则断言成功，第二次没有找打，则断言失败

### 显示密码的参数化

- 普通的参数化
  - 数据不需要通过yml加载，自己写函数。因为随机的数字是yml没法生成的。
- fixture
  - 数据不需要通过yml加载，自己写函数。因为随机的数字是yml没法生成的。

1. 都是在类中，写函数。
2. 写一个专门生成多位数字的随机数的字符串
3. 在列表中，调用多次这个函数，或者自己另开一个方法，来拼一个list
4. 关于fixture
   1. 需要在函数的fixture标记中，写一个params的参数，并且传入一个列表。
   2. 这个列表的元素个数，决定着这个test脚本运行的次数。
   3. 如果想获取这个列表中的元素，需要在fixture所标记的函数中，写一个request参数
   4. request中的param就是 params列表中的每个值。
   5. 将param进行返回，可以知己在使用fixture的函数中，进行使用。

### 判断登录状态

- 思路：
  - 进入到我的页面
  - 点击设置
  - 如果设置上方的标题是
    - 设置
      - 已经登录
    - 登录
      - 没有登录
- 步骤：
  - is_login是在我的界面进行判断，所以函数应该写在mine_page中
  - 点击设置
  - 找到标题的id进行判断，text是否等于设置
    - 如果是，已经登录
    - 如果不是，没有登录
  - 在真正的return之前，应该先将界面返回到“我的”的位置。
  - 在之前，添加一个返回操作
    - 因为在appium1.7中，
    - 如果使用了Uiautomator2，那么，使用press_keycode执行案件操作
    - 如果没有使用Uiautomator2，那么，使用key_event执行案件操作
    - 自己在base中写一个函数，通过driver的capabilities是否有“automationName”的key判断
    - 执行对应的代码

### 收货地址之前登录

- 先写test_address的脚本，在这个页面中，点击我的
- 判断登录状态，如果没有登录，则登录
  - 在登录的页面中（login_page）单独写一个函数，
  - 这个函数可以输入正确的用户名和密码，并且点击登录。
- 点击收货地址，在if外编写

### *在base中编写根据方向参数滑动一屏的方法

```
    def scroll_page_one_time(self, direction="up"):
        """
        调用一次滑动一屏
        :param direction: 方向 默认为从下往上
            "up":从下往上 "down":从上往下 "left":从右往左 "right":从左往右
        :return:
        """
        # 滑动
        screen_width = self.driver.get_window_size()["width"]
        screen_height = self.driver.get_window_size()["height"]

        center_x = screen_width * 0.5
        center_y = screen_height * 0.5

        start_x, start_y, end_x, end_y = 0, 0, 0, 0

        if direction in ["up", "down"]:
            start_x = center_x
            start_y = screen_height * 0.75
            end_x = center_x
            end_y = screen_height * 0.25
        elif direction in ["left", "right"]:
            start_x = screen_width * 0.75
            start_y = center_y
            end_x = screen_width * 0.25
            end_y = center_y

        if direction in ["up", "left"]:
            self.driver.swipe(start_x, start_y, end_x, end_y, 3000)
        elif direction in ["down", "right"]:
            self.driver.swipe(end_x, end_y, start_x, start_y, 3000)
        else:
            raise Exception("direction参数只能使用 up/down/left/right")

        time.sleep(1)
```

### *在base中编写滑动查找特征的方法

```
def is_feature_exist_scroll_page(self, feature, direction="up"):
    """
    滑动查找某个特征是否存在，并返回
    :param feature: 特征
    :param direction: 方向 默认为从下往上
        "up":从下往上 "down":从上往下 "left":从右往左 "right":从左往右
    :return:
    """
    record = ""
    while True:
        if record == self.driver.page_source:
            return False
        record = self.driver.page_source
        try:
            self.find_element(feature)
            return True
        except TimeoutException:
            self.scroll_page_one_time(direction)
```

### 查找收货地址的元素并点击

```
if self.page.mine.is_feature_exist_scroll_page(self.page.mine.address_feature):  # 如果找到则返回true
    # 点击进入收货地址
    self.page.mine.click_address()
else:
    assert False
```





### 

