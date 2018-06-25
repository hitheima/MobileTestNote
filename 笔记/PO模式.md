## PO模式

### Page Object Model

```
	测试页面和测试脚本分离，即页面封装成类，供测试脚本进行调用。

```

### 优缺点

- 优点

```
	1.提高测试用例的可读性;
	2.减少了代码的重复;
	3.提高测试用例的可维护性，特别是针对UI频繁变动的项目;

```

- 缺点

```
	结构复杂: 基于流程做了模块化的拆分。

```

![po模式](./移动端测试_image/po&%E9%9D%9E.png)



## 项目准备

### 需求

- 更多-移动网络-首选网络类型-点击2G
- 更多-移动网络-首选网络类型-点击3G
- 显示-搜索按钮-输入hello-点击返回

### 文件目录

```
PO模式
- scripts
- - __init__.py
- - test_settting.py
- pytest.ini
```

### 代码

test_setting.py

```
from appium import webdriver


class TestSetting:

    def setup(self):
        # server 启动参数
        desired_caps = dict()
        # 设备信息
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1'
        desired_caps['deviceName'] = '192.168.56.101:5555'
        # app的信息
        desired_caps['appPackage'] = 'com.android.settings'
        desired_caps['appActivity'] = '.Settings'
        # 解决输入中文
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True

        # 声明我们的driver对象
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def test_mobile_network_2g(self):
        self.driver.find_element_by_xpath("//*[contains(@text,'更多')]").click()
        self.driver.find_element_by_xpath("//*[contains(@text,'移动网络')]").click()
        self.driver.find_element_by_xpath("//*[contains(@text,'首选网络类型')]").click()
        self.driver.find_element_by_xpath("//*[contains(@text,'2G')]").click()

    def test_mobile_network_3g(self):
        self.driver.find_element_by_xpath("//*[contains(@text,'更多')]").click()
        self.driver.find_element_by_xpath("//*[contains(@text,'移动网络')]").click()
        self.driver.find_element_by_xpath("//*[contains(@text,'首选网络类型')]").click()
        self.driver.find_element_by_xpath("//*[contains(@text,'3G')]").click()

    def test_mobile_display_input(self):
        self.driver.find_element_by_xpath("//*[contains(@text,'显示')]").click()
        self.driver.find_element_by_id("com.android.settings:id/search").click()
        self.driver.find_element_by_id("android:id/search_src_text").send_keys("hello")
        self.driver.find_element_by_class_name("android.widget.ImageButton").click()

```

pytest.ini

```
[pytest]
# 添加行参数
addopts = -s --html=./report/report.html
# 文件搜索路径
testpaths = ./scripts
# 文件名称
python_files = test_*.py
# 类名称
python_classes = Test*
# 方法名称
python_functions = test_*
```

## 多文件区分测试用例

### 需求

- 使用多个文件来区分不同的测试页面

### 好处

- 修改不同的功能找对应的文件即可

### 步骤

1. 在scripts下新建test_network.py文件
2. 在scripts下新建test_dispaly.py文件
3. 移动不同的功能代码到对应的文件
4. 移除原有的test_setting.py文件

### 文件目录

```
PO模式
- scripts
- - __init__.py
- - test_network.py
- - test_dispaly.py
- pytest.ini

```

### 代码

test_network.py

```
from appium import webdriver


class TestNetwork:

    def setup(self):
        # server 启动参数
        desired_caps = dict()
        # 设备信息
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1'
        desired_caps['deviceName'] = '192.168.56.101:5555'
        # app的信息
        desired_caps['appPackage'] = 'com.android.settings'
        desired_caps['appActivity'] = '.Settings'
        # 解决输入中文
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True

        # 声明我们的driver对象
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def test_mobile_network_2g(self):
        self.driver.find_element_by_xpath("//*[contains(@text,'更多')]").click()
        self.driver.find_element_by_xpath("//*[contains(@text,'移动网络')]").click()
        self.driver.find_element_by_xpath("//*[contains(@text,'首选网络类型')]").click()
        self.driver.find_element_by_xpath("//*[contains(@text,'2G')]").click()

    def test_mobile_network_3g(self):
        self.driver.find_element_by_xpath("//*[contains(@text,'更多')]").click()
        self.driver.find_element_by_xpath("//*[contains(@text,'移动网络')]").click()
        self.driver.find_element_by_xpath("//*[contains(@text,'首选网络类型')]").click()
        self.driver.find_element_by_xpath("//*[contains(@text,'3G')]").click()
```

test_dispaly.py

```
from appium import webdriver


class TestDisplay:

    def setup(self):
        # server 启动参数
        desired_caps = dict()
        # 设备信息
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1'
        desired_caps['deviceName'] = '192.168.56.101:5555'
        # app的信息
        desired_caps['appPackage'] = 'com.android.settings'
        desired_caps['appActivity'] = '.Settings'
        # 解决输入中文
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True

        # 声明我们的driver对象
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def test_mobile_display_input(self):
        self.driver.find_element_by_xpath("//*[contains(@text,'显示')]").click()
        self.driver.find_element_by_id("com.android.settings:id/search").click()
        self.driver.find_element_by_id("android:id/search_src_text").send_keys("hello")
        self.driver.find_element_by_class_name("android.widget.ImageButton").click()
```

## 封装前置代码

### 需求

- 将前置代码进行封装

### 好处

- 前置代码只需要写一份

### 步骤

1. 新建base文件夹
2. 新建base_driver.py文件
3. 新建函数init_driver
4. 写入前置代码并返回
5. 修改测试文件中的代码

### 文件目录

```
PO模式
- base
- - __init__.py
- - base_driver.py
- scripts
- - __init__.py
- - test_network.py
- - test_dispaly.py
- pytest.ini

```

### 代码

base_driver.py

```
from appium import webdriver


def init_driver():
    # server 启动参数
    desired_caps = dict()
    # 设备信息
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1'
    desired_caps['deviceName'] = '192.168.56.101:5555'
    # app的信息
    desired_caps['appPackage'] = 'com.android.settings'
    desired_caps['appActivity'] = '.Settings'
    # 解决输入中文
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True

    # 声明我们的driver对象
    return webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

```

test_network.py

```
from base.base_driver import init_driver


class TestNetwork:

    def setup(self):
        self.driver = init_driver()

    def test_mobile_network_2g(self):
        self.driver.find_element_by_xpath("//*[contains(@text,'更多')]").click()
        self.driver.find_element_by_xpath("//*[contains(@text,'移动网络')]").click()
        self.driver.find_element_by_xpath("//*[contains(@text,'首选网络类型')]").click()
        self.driver.find_element_by_xpath("//*[contains(@text,'2G')]").click()

    def test_mobile_network_3g(self):
        self.driver.find_element_by_xpath("//*[contains(@text,'更多')]").click()
        self.driver.find_element_by_xpath("//*[contains(@text,'移动网络')]").click()
        self.driver.find_element_by_xpath("//*[contains(@text,'首选网络类型')]").click()
        self.driver.find_element_by_xpath("//*[contains(@text,'3G')]").click()
```

test_dispaly.py

```
from base.base_driver import init_driver


class TestDisplay:

    def setup(self):
        self.driver = init_driver()

    def test_mobile_display_input(self):
        self.driver.find_element_by_xpath("//*[contains(@text,'显示')]").click()
        self.driver.find_element_by_id("com.android.settings:id/search").click()
        self.driver.find_element_by_id("android:id/search_src_text").send_keys("hello")
        self.driver.find_element_by_class_name("android.widget.ImageButton").click()
```

## 前置代码导入模块问题

### 步骤

在base的 \__init__.py 中写入

```
from base.base_driver import init_driver
```

可将test脚本中的（test_network&test_display）

```
from base.base_driver import init_driver
```

修改为（test_network&test_display）

```
from base import init_driver
```

另外，在base的 \__init__.py 因为是导入自己的模块下的某个文件，可将前面的模块名省略

```
from .base_driver import init_driver
```

### 代码

base/\__init__.py

```
from .base_driver import init_driver
```

### 好处

系统内部都是这么写的，也更省事儿。

## 分离测试脚本和页面

### 需求

- 测试脚本只剩流程
- 其他的步骤放倒page中

### 好处

- 测试脚本只专注过程
- 过程改变只需要修改脚本

### 步骤

1. 新建page文件夹
2. 新建network_page.py文件
3. 新建display_page.py文件
4. init函数传入driver
5. init进入需要测试的页面
6. page中新建“小动作”函数
7. 移动代码
8. 修改测试文件中的代码

### 文件目录

```
PO模式
- base
- - __init__.py
- - base_driver.py
- page
- - __init__.py
- - network_page.py
- - display_page.py
- scripts
- - __init__.py
- - test_network.py
- - test_dispaly.py
- pytest.ini
```

### 代码

display_page.py

```
class DisplayPage:

    def __init__(self, driver):
        self.driver = driver

    def click_display(self):
        self.driver.find_element_by_xpath("//*[contains(@text,'显示')]").click()

    def click_search(self):
        self.driver.find_element_by_id("com.android.settings:id/search").click()

    def input_search_keyword(self, text):
        self.driver.find_element_by_id("android:id/search_src_text").send_keys(text)

    def click_back(self):
        self.driver.find_element_by_class_name("android.widget.ImageButton").click()
```



network_page.py

```
class NetworkPage:

    def __init__(self, driver):
        self.driver = driver

    def click_more(self):
        self.driver.find_element_by_xpath("//*[contains(@text,'更多')]").click()

    def click_mobile_network(self):
        self.driver.find_element_by_xpath("//*[contains(@text,'移动网络')]").click()

    def click_first_network(self, text):
        self.driver.find_element_by_xpath("//*[contains(@text,'首选网络类型')]").click()

    def click_2g_network(self):
        self.driver.find_element_by_xpath("//*[contains(@text,'2G')]").click()

    def click_3g_network(self):
        self.driver.find_element_by_xpath("//*[contains(@text,'3G')]").click()
```



test_display.py

```
from base import init_driver
from page.display_page import DisplayPage


class TestDisplay:

    def setup(self):
        self.driver = init_driver()
        self.display_page = DisplayPage(self.driver)

    def test_mobile_display_input(self):
        self.display_page.click_display()
        self.display_page.click_search()
        self.display_page.input_search_keyword("hello")
        self.display_page.click_back()
```



test_network.py

```
from base import init_driver
from page.network_page import NetworkPage


class TestNetwork:

    def setup(self):
        self.driver = init_driver()
        self.network_page = NetworkPage(self.driver)

    def test_mobile_network_2g(self):
        self.network_page.click_more()
        self.network_page.click_mobile_network()
        self.network_page.click_first_network()
        self.network_page.click_2g_network()

    def test_mobile_network_3g(self):
        self.network_page.click_more()
        self.network_page.click_mobile_network()
        self.network_page.click_first_network()
        self.network_page.click_3g_network()
```

## 输入文字由脚本传入

### 需求

将display配置中的hello移动到test脚本中。

input方法，需要传一个要输入文字的参数，并在方法中使用。

### 好处

- 方便脚本做参数化

### 步骤

### 文件目录

### 代码

## 实验 - find_element_by_xxx和find_element

```
self.driver.find_element_by_xpath("//*[contains(@text,'移动网络')]")
<==>
self.driver.find_element(By.XPATH, "//*[contains(@text,'移动网络')]")
```

class_name 和 id 一样。

可以将字符串部分，写在最上面。

当获取方式不变，获取的字符串的部分发生改变的时候，可以快速的修改。

此时会发现，如果有一个元素的获取方式发生变换后，需要上下改两个地方。先保留疑问。

## 实验 - 元组的写法

```
a = 1, 2
```

a 本质上是一个元组

## 实验 - 二次封装find_element

自己写一个find_element方法。

调用系统的find_element方法，并接受系统的返回值，系统需要传两个参数，我们的方法传一个参数，但是是一个元组，里面有两个元素。第一个元素表示系统方法的第一个参数，第二个元素表示系统方法的第二个参数。

```
# 元素的特征(元组)
mobile_network_button = By.XPATH, "//*[contains(@text,'移动网络')]"

#调用
find_element(self.mobile_network_button)

# 封装后的函数
def find_element(feature):
	# 调用系统的方法
	return self.driver.find_element(feature[0], feature[1])
```

## 抽取find_element和元素的特征到page

### 需求

- 将find_element_by_xxx改为driver中的find_element方法

### 好处

- 提高复用性

### 步骤

1. 观察find_element方法，需要两个参数，一个是找的方式（by），一个是找什么（字符串）。
2. 自己在page中单独写一个find_element方法，调用系统并使用元组的形式进行传参

### 文件目录

```
PO模式
- base
- - __init__.py
- - base_driver.py
- page
- - __init__.py
- - network_page.py
- - display_page.py
- scripts
- - __init__.py
- - test_network.py
- - test_dispaly.py
- pytest.ini
```

### 代码

display_page.py

```
from selenium.webdriver.common.by import By


class DisplayPage:

    display_button = By.XPATH, "//*[contains(@text,'显示')]"
    search_button = By.ID, "com.android.settings:id/search"
    search_edit_text = By.ID, "android:id/search_src_text"
    back_button = By.CLASS_NAME, "android.widget.ImageButton"

    def __init__(self, driver):
        self.driver = driver

    def click_display(self):
        self.find_element(self.display_button).click()

    def click_search(self):
        self.find_element(self.search_button).click()

    def input_keyword(self, content):
        self.find_element(self.search_edit_text).send_keys(content)

    def click_back(self):
        self.find_element(self.back_button).click()

    def find_element(self, feature):
        return self.driver.find_element(feature[0], feature[1])

```



network_page.py

```
from selenium.webdriver.common.by import By


class NetwrokPage:

    more_button = By.XPATH, "//*[contains(@text,'更多')]"
    mobile_network_button = By.XPATH, "//*[contains(@text,'移动网络')]"
    first_network_button = By.XPATH, "//*[contains(@text,'首选网络类型')]"
    network_2g_button = By.XPATH, "//*[contains(@text,'2G')]"
    network_3g_button = By.XPATH, "//*[contains(@text,'3G')]"

    def __init__(self, driver):
        self.driver = driver

    def click_more(self):
        self.find_element(self.more_button).click()

    def click_mobile_network(self):
        self.find_element(self.mobile_network_button).click()

    def click_first_network(self):
        self.find_element(self.first_network_button).click()

    def click_2g_network(self):
        self.find_element(self.network_2g_button).click()

    def click_3g_network(self):
        self.find_element(self.network_3g_button).click()

    def find_element(self, feature):
        return self.driver.find_element(feature[0], feature[1])

```



## 抽取点击和输入到page

### 需求

将click和send_keys像find_element一样进行封装。

封装好后的使用方式为

```
self.click(self.network_button)
```

### 好处

写法更简单，并为后期抽取到base做准备。

### 步骤

1. 在page中写一个click方法。
2. 参数为“特征”。
3. 在自己的click函数中查找并点击。
4. send_keys同理。

### 文件目录

```
PO模式
- base
- - __init__.py
- - base_driver.py
- page
- - __init__.py
- - network_page.py
- - display_page.py
- scripts
- - __init__.py
- - test_network.py
- - test_dispaly.py
- pytest.ini
```



### 代码

display_page.py

```
from selenium.webdriver.common.by import By


class DisplayPage:

    display_button = By.XPATH, "//*[contains(@text,'显示')]"
    search_button = By.ID, "com.android.settings:id/search"
    search_edit_text = By.ID, "android:id/search_src_text"
    back_button = By.CLASS_NAME, "android.widget.ImageButton"

    def __init__(self, driver):
        self.driver = driver

    def click_display(self):
        self.click(self.display_button)

    def click_search(self):
        self.click(self.search_button)

    def input_keyword(self, content):
        self.input(self.search_edit_text, content)

    def click_back(self):
        self.click(self.back_button)

    def find_element(self, feature):
        return self.driver.find_element(feature[0], feature[1])

    def click(self, feature):
        self.find_element(feature).click()

    def input(self, feature, text):
        self.find_element(feature).send_keys(text)

```



network_page.py

```
from selenium.webdriver.common.by import By


class NetwrokPage:

    more_button = By.XPATH, "//*[contains(@text,'更多')]"
    mobile_network_button = By.XPATH, "//*[contains(@text,'移动网络')]"
    first_network_button = By.XPATH, "//*[contains(@text,'首选网络类型')]"
    network_2g_button = By.XPATH, "//*[contains(@text,'2G')]"
    network_3g_button = By.XPATH, "//*[contains(@text,'3G')]"

    def __init__(self, driver):
        self.driver = driver

    def click_more(self):
        self.click(self.more_button)

    def click_mobile_network(self):
        self.click(self.mobile_network_button)

    def click_first_network(self):
        self.click(self.first_network_button)

    def click_2g_network(self):
        self.click(self.network_2g_button)

    def click_3g_network(self):
        self.click(self.network_3g_button)

    def find_element(self, feature):
        return self.driver.find_element(feature[0], feature[1])

    def click(self, feature):
        self.find_element(feature).click()

    def input(self, feature, text):
        self.find_element(feature).send_keys(text)

```



## 抽取find&input&click到base_action

### 需求

将find&input&click等基本动作放倒base_action中

### 好处

增加复用性，以后基本不需要调用find_element方法

### 步骤

1. 在base中新建一个base_action.py
2. 将三个方法都移动到对应的BaseAction下
3. 使Page继承BaseAction，从而可以直接使用self.click等方法
4. 在base的init方法中，传入driver解决使用driver的问题
5. 移除page中的init（创建page对象的时候，如果没有init会调用父类的init）

### 文件目录

```
PO模式
- base
- - __init__.py
- - base_action.py
- - base_driver.py
- page
- - __init__.py
- - network_page.py
- - display_page.py
- scripts
- - __init__.py
- - test_network.py
- - test_dispaly.py
- pytest.ini
```

### 代码

display_page.py

```
from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class DisplayPage(BaseAction):

    display_button = By.XPATH, "//*[contains(@text,'显示')]"
    search_button = By.ID, "com.android.settings:id/search"
    search_edit_text = By.ID, "android:id/search_src_text"
    back_button = By.CLASS_NAME, "android.widget.ImageButton"

    def click_display(self):
        self.click(self.display_button)

    def click_search(self):
        self.click(self.search_button)

    def input_keyword(self, content):
        self.input(self.search_edit_text, content)

    def click_back(self):
        self.click(self.back_button)

```



network_page.py

```
from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class NetwrokPage(BaseAction):

    more_button = By.XPATH, "//*[contains(@text,'更多')]"
    mobile_network_button = By.XPATH, "//*[contains(@text,'移动网络')]"
    first_network_button = By.XPATH, "//*[contains(@text,'首选网络类型')]"
    network_2g_button = By.XPATH, "//*[contains(@text,'2G')]"
    network_3g_button = By.XPATH, "//*[contains(@text,'3G')]"

    def click_more(self):
        self.click(self.more_button)

    def click_mobile_network(self):
        self.click(self.mobile_network_button)

    def click_first_network(self):
        self.click(self.first_network_button)

    def click_2g_network(self):
        self.click(self.network_2g_button)

    def click_3g_network(self):
        self.click(self.network_3g_button)


```



base_action.py

```
class BaseAction:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, feature):
        return self.driver.find_element(feature[0], feature[1])

    def click(self, feature):
        self.find_element(feature).click()

    def input(self, feature, text):
        self.find_element(feature).send_keys(text)
```



## 增加WebDriverWait

### 需求

在找元素的时候都增加WebDriverWait

### 好处

防止手机卡顿的时候突然找不到元素

### 步骤

1. 将BaseAction中的find_element方法中，嵌套一个WebDriverWait

### 文件目录

```
PO模式
- base
- - __init__.py
- - base_action.py
- - base_driver.py
- page
- - __init__.py
- - network_page.py
- - display_page.py
- scripts
- - __init__.py
- - test_network.py
- - test_dispaly.py
- pytest.ini
```



### 代码

base_action.py

```
from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, feature):
        wait = WebDriverWait(self.driver, 5, 1)
        return wait.until(lambda x: x.find_element(feature[0], feature[1]))

    def click(self, feature):
        self.find_element(feature).click()

    def input(self, feature, text):
        self.find_element(feature).send_keys(text)
```



## 增加find_elements

### 需求

在Base_action中写一个find_elements方法

### 好处

find_element和find_elements都可能会用到，方便以后调用

### 步骤

1. 复制一份find_element
2. 直接在副本的element后面加s即可

### 文件目录

```
PO模式
- base
- - __init__.py
- - base_action.py
- - base_driver.py
- page
- - __init__.py
- - network_page.py
- - display_page.py
- scripts
- - __init__.py
- - test_network.py
- - test_dispaly.py
- pytest.ini
```



### 代码

```
from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, feature):
        wait = WebDriverWait(self.driver, 5, 1)
        return wait.until(lambda x: x.find_element(feature[0], feature[1]))

    def find_elements(self, feature):
        wait = WebDriverWait(self.driver, 5, 1)
        return wait.until(lambda x: x.find_elements(feature[0], feature[1]))
    
    def click(self, feature):
        self.find_element(feature).click()

    def input(self, feature, text):
        self.find_element(feature).send_keys(text)
```



## action导入模块的问题

### 需求

让base_action像base_driver一样在\__init__中导入

### 好处

其他地方是有base_action不在需要写base.base_action

### 代码

base/\__init__.py

```
from .base_driver import init_driver
from .base_action import BaseAction
```

将page中的

```
from base.base_action import BaseAction
```

改为

```
from base import BaseAction
```

## 代码page的统一入口

### 需求

会有一些需求是在页面中调用其他页面的“动作”，比如某些登录。

### 好处

方便调用其他页面的动作

### 步骤

1. 新建一个page.py文件。
2. 写对应个数的函数并用属性装饰器装饰
3. 直接返回对应的page对象
4. 增加 \__init__ 函数传入driver

### 文件目录

```
PO模式
- base
- - __init__.py
- - base_action.py
- - base_driver.py
- page
- - __init__.py
- - page.py
- - network_page.py
- - display_page.py
- scripts
- - __init__.py
- - test_network.py
- - test_dispaly.py
- pytest.ini
```



### 代码

page.py

```
from .network_page import NetwrokPage
from .display_page import DisplayPage


class Page:

    def __init__(self, driver):
        self.driver = driver

    @property
    def display(self):
        return DisplayPage(self.driver)

    @property
    def network(self):
        return NetwrokPage(self.driver)
```



test_display.py

```
from base import init_driver
from page.page import Page


class TestDisplay:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def test_display_search(self):
        self.page.display.click_display()
        self.page.display.click_search()
        self.page.display.input_keyword("hello")
        self.page.display.click_back()

```



test_network.py

```
from base import init_driver
from page.page import Page


class TestNetwrok:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def test_network_2g(self):
        self.page.network.click_more()
        self.page.network.click_mobile_network()
        self.page.network.click_first_network()
        self.page.network.click_2g_network()

    def test_network_3g(self):
        self.page.network.click_more()
        self.page.network.click_mobile_network()
        self.page.network.click_first_network()
        self.page.network.click_3g_network()
```

## page导入模块的问题

### 需求

让page像base_driver一样在\__init__中导入

### 好处

其他地方是有page不在需要写page.page

### 代码

page/\__init__.py

```
from .page import Page
```

将scripts中的

```
from page.page import Page
```

改为

```
from page import Page
```

## XPath特殊处理

### 需求

### 好处

### 步骤

### 文件目录

### 代码