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

#### Monkey日志分析

```
--pct-touch <percent>
调整触摸事件的百分比(触摸事件是一个down-up事件，它发生在屏幕上的某单一 位置)。

--pct-motion <percent>
调整动作事件的百分比(动作事件由屏幕上某处的一个down事件、一系列的伪随机事 件和一个up事件组成)。

--pct-trackball <percent>
调整轨迹事件的百分比(轨迹事件由一个或几个随机的移动组成，有时还伴随有点击)。

--pct-pinchzoom <percent>
缩放事件百分比

--pct-nav <percent>
调整“基本”导航事件的百分比(导航事件由来自方向输入 设备的up/down/left/right组成)。

--pct-majornav <percent>
调整“主要”导航事件的百分比(这些导航事件通常引发图 形界面中的动作，如：回退按键、菜单按键)

--pct-syskeys <percent>
调整“系统”按键事件的百分比(这些按键通常被保留，由 系统使用，如Home、Back、Start Call、End Call及音量控制键)。

--pct-appswitch <percent>
调整启动Activity的百分比。在随机间隔里，Monkey将执行一个startActivity()调 用，作为最大程度覆盖包中全部Activity的一种方法。

--pct-flip <percent>
键盘翻转事件百分比

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



