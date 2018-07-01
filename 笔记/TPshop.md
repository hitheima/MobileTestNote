

## TPShop

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

参考：https://github.com/hitheima/SZ_TPShop（以后简称之前的项目）

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

   

### 

