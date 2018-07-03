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

    

  - ![Snip20180410_57](移动端测试_image/Snip20180410_57.png)

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

### 
