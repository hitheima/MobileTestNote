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



### 截图

应该在重要的时候，进行截图，并且上传到报告中。（比如，在测试搜索功能。那么搜索的结果，就算是重点）

截图使用，screenshot_as_file("路径")，需要在项目中，专门建立一个文件夹。名字叫做screen。来保存截图

### 上传截图到allure

```
allure.attach('描述', open('xx.png', 'rb').read(), allure.attach_type.PNG)
```

类似于allure的文字描述。第一个参数是描述，第二个参数是描述的内容，第三个参数是类型。

### 关于git的忽略文件

在上传git项目的时候，有些不需要上传的文件，比如，python的缓存以及编译文件。包括report的报告。还有pycharm的.idea等。如果不想上传，需要做一个忽略文件的操作。

忽略文件的名字，叫做.gitignore。具体规则，可以百度。一般把，github自带的python的忽略文件，再加上report和.idea就可以了。

剩下的操作都一样，这个忽略文件要放在项目目录下。（和.git同目录）

### 配置jenkins

1. 运行服务
2. 项目，git的地址，账号密码，时间触发器，pytest的环境，allure报告的文件夹名称（xml的所在的文件夹名字）。这样可以生成报告，会自动检测git代码的更变。
3. 发件人和收件人。
4. 发件人需要先测试，搜索location 配置管理员邮箱，搜索“邮件通知”配置smtp以及用户名和密码。点击测试发信。
5. 发件人正经的配置，搜索，content，需要配置选择html的模板，以及模板的内容，在上面一点，有一个英文的 email notifacation。配置smtp以及用户名和密码。

### app开发一些常识

关于toast。toast是只在android中有。不是所有的两分钟消失的那个视图都叫做toast。

android：

​	按钮：Button

​	文本框，显示文字：TextView

​	输入框，用来输入：EditText

ios：

​	按钮：UIButton

​	文本框，显示文字：UILabel

​	输入框，用来输入：UITextFiled

在iOS中也有一个叫做UITextView的东西，是用来输入大段文本的

在iOS类名中有前缀，涉及到视图都是UI开头。

### bug

关于xpath的and问题。

字符串多个条件用and连接，如果and后面直接是@那么可以不要空格。如果是其他的字符，需要加空格



