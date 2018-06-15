### webview

#### 查看webview元素的方式

在浏览器中 输入 chrome://inspect 地址

可以看到对用的手机设备，已经已经有的webview

- 方式1
  - 点击inspect查看元素信息。


- 方式2

  - 通过自己电脑上的浏览器chrom打开对应的手机的webview的页面（m.baidu.com）

  - 在页面点击右键，选择检查。（不是查看源代码）

  - 点击红色的按钮，进入查看元素的模式

    ​

  - ![Snip20180410_57](./Snip20180410_57.png)

  ​

  - 选中需要查看的控件，右侧源码即可跳转。

#### 实现webview自动化

- 前置代码，和之前相同（打开的包名和启动名是浏览器软件）

- 获取，driver的所有的上下文。

  - 得到，一个原生的app的字符串，还有其他各种webview的字符串。

    ```
    contexts = driver.contexts
    for i in contexts:
        print(i)
    ```

  - 如：

  - NATIVE_APP
    WEBVIEW_cn.goapk.market
    WEBVIEW_com.android.browser

- 通过，driver的switchto来切换上下文

  ```
  # 告诉appium需要查找的是 com.android.browser程序的webview的内容
  driver.switch_to.context("WEBVIEW_com.android.browser")
  ```

- 根据之前找到的html中的id来进行查找，函数同样适用find_element_by_xxxxx

- 包括，点击已经输入文字等api都是相同的。



#### 关于空白

```
使用chrome浏览器，输入chrome://inspect可以调试android app里面的网页，如果inspect的时候，是空白，

那就在C:\Windows\System32\drivers\etc\hosts文件加入

61.91.161.217 chrome-devtools-frontend.appspot.com
61.91.161.217 chrometophone.appspot.com
```

```
但是，chrome://inspect/#devices出现空白页的情况不止上面的原因

可以试一下chrome://appcache-internals/#清除一下这里的缓存，基本解决
```

### iOS

#### 运行iOS项目

快捷键 command + r

或者

点击左上角“播放”按钮

编译的快捷键 command + b

![Snip20180409_45](/Users/Yoson/Desktop/%E7%A7%BB%E5%8A%A8%E7%AB%AF%E6%B5%8B%E8%AF%95/%E7%A7%BB%E5%8A%A8%E7%AB%AF%E6%B5%8B%E8%AF%95-%E7%AC%AC11%E5%A4%A9/%E7%AC%94%E8%AE%B0/Snip20180409_45.png)



#### iOS前置代码

```
# server 启动参数
desired_caps = {}
# 设备信息
desired_caps['platformName'] = 'iOS'
desired_caps['platformVersion'] = '11.3'
desired_caps['deviceName'] = 'iPhone 8 Plus'
# app的信息
desired_caps['app'] = "com.itheima.HMWaiMai1"
# 解决输入中文
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True

# 不要重置应用
desired_caps['noReset'] = True

# 声明我们的driver对象
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
```

##### 已经安装

```
desired_caps['app'] = "com.itheima.HMWaiMai1"
```

要一份源码，打开Xcode，选择对应模拟器，“command+r”运行

![Snip20180409_23](/Users/Yoson/Desktop/%E7%A7%BB%E5%8A%A8%E7%AB%AF%E6%B5%8B%E8%AF%95/%E7%A7%BB%E5%8A%A8%E7%AB%AF%E6%B5%8B%E8%AF%95-%E7%AC%AC11%E5%A4%A9/%E7%AC%94%E8%AE%B0/Snip20180409_23.png)

```
desired_caps['deviceName'] = 'iPhone 8'
# 这个key “deviceName” 在iOS中是有用的。在android中可以随便写，只要不是不传或空字符串都可以。但是，在iOS中，应该写对应的设备名字，如果名字是正确的(iPhone 6s)，会重新打开，如果没有对应的设备名字，会报错。
```

##### 没有安装

```
desired_caps['app'] = os.path.abspath("./HMWaiMai.app")  # 建议！！！
```

```
desired_caps['app'] = "./test_ios/HMWaiMai.app"
```

找到项目下的Products文件夹，里面有项目名.app，如果为红色，按下“command+b”进行编译，自动生成。

![Snip20180409_25](/Users/Yoson/Desktop/%E7%A7%BB%E5%8A%A8%E7%AB%AF%E6%B5%8B%E8%AF%95/%E7%A7%BB%E5%8A%A8%E7%AB%AF%E6%B5%8B%E8%AF%95-%E7%AC%AC11%E5%A4%A9/%E7%AC%94%E8%AE%B0/Snip20180409_25.png)

对着 项目.app 右键 - 选择 show in finder（在资源管理器中打开）- 直接把这个app拖到终端中，即可查看路径。

#### appium查看元素-android

```
mac: appium - new session window 

windows: file - new session window 
```

desired capabilities 中填写对应前置代码的key-value

![Snip20180409_41](/Users/Yoson/Desktop/%E7%A7%BB%E5%8A%A8%E7%AB%AF%E6%B5%8B%E8%AF%95/%E7%A7%BB%E5%8A%A8%E7%AB%AF%E6%B5%8B%E8%AF%95-%E7%AC%AC11%E5%A4%A9/%E7%AC%94%E8%AE%B0/Snip20180409_41.png)

点击start session即可![Snip20180409_42](/Users/Yoson/Desktop/%E7%A7%BB%E5%8A%A8%E7%AB%AF%E6%B5%8B%E8%AF%95/%E7%A7%BB%E5%8A%A8%E7%AB%AF%E6%B5%8B%E8%AF%95-%E7%AC%AC11%E5%A4%A9/%E7%AC%94%E8%AE%B0/Snip20180409_42.png)

#### appium左侧三个功能

- 选择元素
- 模拟滑动
- 点击

#### appium右侧五个功能

- 返回
- 刷新
- 录制脚本（代码）
- 搜索
- 退出

#### appium查看元素-iOS

原理和 android 相同

写入对应的前置代码参数即可

![Snip20180409_43](/Users/Yoson/Desktop/%E7%A7%BB%E5%8A%A8%E7%AB%AF%E6%B5%8B%E8%AF%95/%E7%A7%BB%E5%8A%A8%E7%AB%AF%E6%B5%8B%E8%AF%95-%E7%AC%AC11%E5%A4%A9/%E7%AC%94%E8%AE%B0/Snip20180409_43.png)

#### 点击事件

test_ios.py

```
import os, sys

sys.path.append(os.getcwd())

from base.base_driver import init_iOS_driver
from page.login_page import LoginPage


class Test_ios:

    def setup(self):
        self.driver = init_iOS_driver()
        self.login_page = LoginPage(self.driver)

    def test_login(self):
        self.login_page.click_rice()

```

login_page.py

```
from selenium.webdriver.common.by import By

from base.base_action import BaseAction

class LoginPage(BaseAction):

    rice = By.XPATH, "name,地狱饭"

    def click_rice(self):
        self.find_element(self.rice).click()
```

#### 滑动

只用之前的base进行验证

```
self.login_page.scroll_page_one_time()
```

### Monkey

#### 环境

同Android环境

#### 什么是Monkey

顾名思义，Monkey就是猴子，  Monkey测试，就像一只猴子， 在电脑面前，乱敲键盘在测试。  猴子什么都不懂， 只知道乱敲

通过Monkey程序模拟用户触摸屏幕、滑动Trackball、 按键等操作来对设备上的程序进行压力测试，检测程序多久的时间会发生异常

#### Monkey用来做什么

Monkey 主要用于Android 的压力测试  自动的一个压力测试小工具， 主要目的就是为了测试app 是否会Crash.

#### Monkey程序介绍

- Monkey程序由Android系统自带，使用Java语言写成，在Android文件系统中的存放路径是： /system/framework/monkey.jar；   
- Monkey.jar程序是由一个名为“monkey”的Shell脚本来启动执行，shell脚本在Android文件系统中 的存放路径是：/system/bin/monkey；  
- Monkey 命令启动方式：    
  - 可以通过PC机CMD窗口中执行: adb shell monkey ｛+命令参数｝来进行Monkey测试          
  - 在PC上adb shell 进入Android系统，通过执行 monkey {+命令参数} 来进行Monkey 测试          
  - 在Android机或者模拟器上直接执行monkey 命令，可以在Android机上安装Android终端模拟器  （Terminal Emulator for Android）

#### Monkey输出日志

```
adb shell monkey -p cn.goapk.market 100 > 路径/log.txt
```

#### Monkey基本参数介绍

- -p <允许的包名列表>         

用此参数指定一个或多个包。指定包之后，monkey将只允许系统启动指定的app。如果指定包， monkey将允许系统启动设备中的所有app。  

指定一个包：adb shell monkey -p cn.goapk.market 100   

指定多个包：adb shell monkey -p fishjoy.control.menu  –p cn.goapk.market 100  

- -v        

用亍指定反馈信息级别（信息级别就是日志的详细程度），总共分3个级别，分别对应的参数如下 表所示： 

Level 0  :  adb shell monkey -p cn.goapk.market -v 100               // 缺省值，仅提供启动提示、测试完成和最终结果等少量信息   

Level 1  :  adb shell monkey -p cn.goapk.market -v  -v 100          // 提供较为详细的日志，包括每个发送到Activity的事件信息

Level 2  :  adb shell monkey -p cn.goapk.market -v  -v  -v 100     // 最详细的日志，包括了测试中选中/未选中的Activity信息

- -s（随机数种子）            

用亍指定伪随机数生成器的seed值，如果seed相同，则两次Monkey测试所产生的事件序列也相同的。  示例：

monkey测试1：adb shell monkey -p cn.goapk.market –s 10 100                

monkey测试2：adb shell monkey -p cn.goapk.market –s 10 100  

- --throttle <毫秒>            

用亍指定用户操作（即事件）间的时延，单位是毫秒；如果指定这个参数，monkey会尽可能快的 生成和发送消息。 示例：adb shell monkey -p cn.goapk.market --throttle 3000 100   

#### Monkey  日志分析

```
--pct-touch <percent>
调整触摸事件的百分比(触摸事件是一个down-up事件，它发生在屏幕上的某单一 位置)。

--pct-motion <percent>
调整动作事件的百分比(动作事件由屏幕上某处的一个down事件、一系列的伪随机事 件和一个up事件组成)。

--pct-trackball <percent>
调整轨迹事件的百分比(轨迹事件由一个或几个随机的移动组成，有时还伴随有点击)。

--pct-nav <percent>
调整“基本”导航事件的百分比(导航事件由来自方向输入 设备的up/down/left/right组成)。

--pct-majornav <percent>
调整“主要”导航事件的百分比(这些导航事件通常引发图 形界面中的动作，如：回退按键、菜单按键)

--pct-syskeys <percent>
调整“系统”按键事件的百分比(这些按键通常被保留，由 系统使用，如Home、Back、Start Call、End Call及音量控制键)。

--pct-appswitch <percent>
调整启动Activity的百分比。在随机间隔里，Monkey将执行一个startActivity()调 用，作为最大程度覆盖包中全部Activity的一种方法。

--pct-anyevent <percent>
调整其它类型事件的百分比。它包罗了所有其它类型的事件，如：按键、其它不常用的设备按钮、等等。
```

- 正常情况

如果Monkey测试顺利执行完成， 在log的最后， 会打印出当前执行事件的次数和所花费的时间； // Monkey finished 代表执行完成

- 异常情况

Monkey 测试出现错误后，一般的分析步骤
看Monkey的日志 (注意第一个swith以及异常信息等)
\1. 程序无响应的问题: 在日志中搜索 “ANR”
\2. 崩溃问题：在日志中搜索 “Exception”   (如果出现空指针， NullPointerException)  肯定是有bug
Monkey 执行中断， 在log最后也能看到当前执行次数

### MonkeyRunner

#### 

