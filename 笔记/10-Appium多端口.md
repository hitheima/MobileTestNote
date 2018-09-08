### appium多端口

目标，让一个脚本去跑到多台手机。

注意点： appium sever端口要不同，开启多个。bootstrap端口要不同，开启多个。udid需要指定，udid表示设备的唯一表示符号，通过 adb devices 查看。 前半部分都是，比如模拟器的（192.168.57.101:5555）。

appium server  和  bootstrap 和 udid 应该是成对出现的。

命令：

```
appium -p 4723 -bp 4724 -U 192.168.57.101:5555
```

-p 表示 appium的端口

-bp 表示 bootstrap的端口

-U 表示设备的标识符

修改init_driver让，init_driver接受port的参数。并且进行对应的连接。

记得，创建的是不同的driver对象。

因为如果使用threading.Thread的这种形式，需要指定执行的函数，所以，把需要执行的代码，封装成一个函数。然后使用

```
    ports = ["4723", "4725"]

    for i in ports:
        threading.Thread(target=do, args=(i,)).start()
```

来去执行创建多个driver并且进行脚本的操作。

