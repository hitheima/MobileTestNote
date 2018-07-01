### 获取toast

安装node.js （使用 npm 或 node 验证）

```
node-v8.11.3-x64.msi进行安装
```

安装cnpm （使用cnpm验证）

```
npm install -g cnpm --registry=https://registry.npm.taobao.org
```

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

### 