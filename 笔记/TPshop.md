## TPshop

1. 手点，基本的流程。大体的操作这个要测试的功能
2. 写测试用例。（尽可能考虑各种可能性）
3. 对着测试用例，进行功能测试。
4. 考虑自动化。

### 项目准备

准备之前用到的base和配置文件等

### 进入登录界面

1. 创建两个文件在对应的文件夹下，login_page、test_login
2. 在test_login下，setup中，连接手机（导入模块，使用init_driver函数）
3. 在login_page下，写类，继承BaseAction
4. 在test_login下，创建page对象
5. 分析步骤，发现部分步骤是必须要有的。考虑写在page的init中
6. 因为在login中，发现一定是有需要前置的步骤，在page的类里，重写init的函数，并且在调用父类init之后，执行“必要的步骤”com.tpshop.malls:id/tab_txtv

### 登录测试脚本

1. 输入手机号，输入密码，点击登录。在page中实现，并且在test调用
2. 在page中写is_login的函数。找手机号，如果找到，返回true如果没找到，会报错，在except中返回false
3. 在test中断言 is_login 的结果

### 获取toast

下载 appium-uiautomator2-driver

```
 cnpm install appium-uiautomator2-driver
```

前置代码添加

```
desired_caps['automationName'] = 'Uiautomator2'
```

使用driverWait的方式寻找

```
def find_toast(driver, message, timeout=3):
    """
    # message: 预期要获取的toast的部分消息
    """
    message = "//*[contains(@text,'" + message + "')]" # 使用包含的方式定位

    element = WebDriverWait(driver, timeout, 0.1).until(lambda x: x.find_element(By.XPATH, message))
    return element.text
```

### 将登录成功失败改为toast

1. 在base中，写了一个find_toast的函数，返回，根据部分内容，找到的全部内容。
2. 在base中，写了一个is_toast_exist的函数，如果找到，则返回true，如果找不到，则报错并且返回false
3. desired_caps['automationName'] = 'Uiautomator2'！！！！！！！
4. 切记！
5. 切记！
6. 切记！

以后，如果需要获取toast的全部内容，使用find_toast。

如果需要获取toast的部分内容是否存在，使用is_toast_exist。



### bug

关于xpath的and问题。

字符串多个条件用and连接，如果and后面直接是@那么可以不要空格。如果是其他的字符，需要加空格



