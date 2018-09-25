### git 三种形式

- 三种形式
  - 命令行
  - GUI - sourcetree
  - pycharm 

### 安装git

双击 “Git-2.17.1.2-64-bit.exe” 一路next

验证：

在命令行中输入 git 只要不是提示“内部外部命令” 即为成功

### 安装 source tree

双击 ”SourceTreeSetup-2.5.5.exe“ 会直接打开 提示登录用户的一个界面

直接关闭。

进入 ”C:\Users\你的电脑名字\AppData\Local\Atlassian\SourceTree“ 将 account.json 发到这个目录中

在次从桌面进入sourcetree

如果没有， ”C:\Users\你的电脑名字\AppData\Local\SourceTree\app-2.1\sourcetree.exe“ 将这个文件 右键-发送到桌面快捷方式

### 安装source tree可能出现的问题

- 缺少 .net freamwork 4.7.1
  - 安装 ”NDP472-KB4054530-x86-x64-AllOS-ENU.exe“

### 注册github账号

地址: github.com

选择 sign up

输入 用户名 邮箱 密码

选择 免费计划

点击 start a new project，会跳转到 让我们确认 邮箱的页面

查看自己的邮箱，在邮箱中点击相应得了链接

### 配置git信息

```
$ git config --global user.name "John Doe"
$ git config --global user.email johndoe@example.com
```

```
git config --list   # 查看配置信息
```

### 将文件上传到github（命令行）

1. 在github新建项目

   1. 点击新建仓库（不要中文）
   2. 输入项目名称
   3. 点击确定

2. 在自己电脑上新建一个文件夹，里面放上文件

   1. 新建了一个和项目名称一样的文件夹
   2. 在里面放了一个  newfile.txt
   3. 在txt中输入了一些文字

3. 打开命令行，进入到电脑之前新建的文件夹下

4. 输入命令

   ```
   git init
   git add newfile.txt(自己的文件)
   git commit -m "first commit"
   git remote add origin https://github.com/hitheima/xxxxxxxxxxxx.git(自己的项目地址)
   git push -u origin master
   ```

5. 中间会弹出一个github的登录页面，输入自己的用户名和密码

6. 刷新网页，此时会看到文件夹中的文件，即可

### 在原有基础上增加新的&修改文件（命令行）

```
git add newfile.txt(自己的文件)
git commit -m "first commit"
git push -u origin master
```

### 忽略文件

在项目中新建一个 “.gitignore” 的文件

在里面填写忽略的规则

```
.idea
.pytest_cache
report
__pycache__
```

### sourcetree 使用

git init

上面五个按钮的最后，有一个create，选择对应的项目即可。

git add

进入项目 点击暂存

git commit

点击左上角 提交，输入 注释信息，点击提交

git remote

点击 仓库，点击添加远端仓库

![image-20180821095839001](/var/folders/jv/bhg2sgp12c198mtscdjxpmrw0000gn/T/abnerworks.Typora/image-20180821095839001.png)

git push

左上角 点击 推送



### jenkins 快速安装

win：

```
c:/users/小明/.jenkins/
```

mac：

```
/users/小明/.jenkins
```

mkdir创建文件夹.jenkins

### 启动jenkins

```
1.进入jenkins.war所在目录，执行：java -jar jenkins.war
2.浏览器进入：localhost:8080
```

### clone

git clone 地址

概念：第一次从远端下载到本地叫做 克隆

远端已经添加，自己不需要再去操作

### pull

对应着push，pull表示，从远端更新到本地

### commit之前一定先pull

应该：pull-提交-push

如果运气不好，可能会发生下面的情况。

没有错：提交-pull-push

sourcetree的“线”，不是一条

### 图的点表示commit

可以通过commit的时间，来看出是基于哪一个版本修改的。

### 冲突

修改了同一个文件的同一行。

发生冲突时正常的，应该尽量去规避（比如：忽略文件，多沟通），但是不能保证完全的规避。

解决冲突：手动删除，根据需求考虑保留哪些代码

```
>>>>>>> HEAD
assert 0
=======
assert 2
<<<<<<< 2df72bca6332
```

head 到 = 表示自己的版本

= 到 版本号 表示服务器的版本

### GitHub - 添加成员

进入项目 - setting - Collaborators - 输入对方用户名， 对方在邮件中点击连接即可。

### GitHub - 修改他人的开源项目

需要作者审核

fork原作者的项目 - 修改自己fork的项目，commit，push - new pull request - 等待作者审核

### 创建github项目是的三个文件

readme - 项目介绍

ignore - 忽略文件

licenes - 许可证



