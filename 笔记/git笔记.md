### 下载

https://gitforwindows.org/

### 配置

```
$ git config --global user.name "John Doe"
$ git config --global user.email johndoe@example.com
```

```
git config --list   # 查看配置信息
```

### 常用命令

初始化一个git项目（告诉git这个项目让它管理）

```
git init
```

查看当前的文件的git的状态

如果提示 “Not a git repository ” 意味着，不是一个git项目，需要使用git init进行初始化

如果提示 “Untracked files ” 意味着，文件没有被追踪

```
git status
```

告诉git，管理某个文件（追踪某个文件）

```
git add <文件名> # 添加一个文件进行追踪
git add . # 添加所有的文件
```

提交版本

```
git commit -m "注释"
```

### sourcetree 账户问题

https://blog.csdn.net/jiangyu1013/article/details/78850735

进入这个文件夹：C:\Users\你的电脑名字\AppData\Local\Atlassian\SourceTree  ， 在此找到或者新建一个 json 类型的文件，取名为：accounts.json。

​    即：在这个目录下新建一个全名为 `accounts.json` 的文件。

注意： `Windows` 系统文件后缀是默认隐藏的，需要先显示文件的后缀名，然后随便新建一个 `文本文档` ，将文件全名改为 `accounts.json` 即可。

```
[
  {
    "$id": "1",
    "$type": "SourceTree.Api.Host.Identity.Model.IdentityAccount, SourceTree.Api.Host.Identity",
    "Authenticate": true,
    "HostInstance": {
      "$id": "2",
      "$type": "SourceTree.Host.Atlassianaccount.AtlassianAccountInstance, SourceTree.Host.AtlassianAccount",
      "Host": {
        "$id": "3",
        "$type": "SourceTree.Host.Atlassianaccount.AtlassianAccountHost, SourceTree.Host.AtlassianAccount",
        "Id": "atlassian account"
      },
      "BaseUrl": "https://id.atlassian.com/"
    },
    "Credentials": {
      "$id": "4",
      "$type": "SourceTree.Model.BasicAuthCredentials, SourceTree.Api.Account",
      "Username": "",
      "Email": null
    },
    "IsDefault": false
  }
]
```

重新打开sourcetree

检测到没有Mxxxxxxx。接下来，会通过以下三种方式进行解决。

选最后一个，“我不使用”



### 注册github账号

https://guides.github.com/activities/hello-world/

打开  github.com

点击 sign up



### 把代码如何放在github上

点击“新建仓库”

输入“仓库名称”

有个 desc 的描述，可选

后面三个，“readme” “忽略文件” “许可证”， 都不选择。

此处，下一步，会有提示。

使用cmd进入到 需要的提交的项目的目录下。

使用，提示的命令。（第一次，中途会提示输入github用户名和密码）

```
git init # 初始化项目

git add . # 把当前目录下的所有文件，交给git管理

git commit -m "first commit" # 提交

git remote add origin https://github.com/hitheima/popopo.git # 建立远端连接

git push -u origin master # 推送到远端
```

### 如何下载github的项目

- download zip 下载
  - 进入项目主页，右侧有一个绿色的按钮，点击后，选择download zip即可
- clone 克隆
  - 从远端第一次放到本地的过程叫做克隆（cheakout）
  - 在github主页上，项目会有一个地址，通过sourceTree进行克隆
  - sourceTree点击新仓库，从url克隆。
  - 将“xxxx.git”的地址，赋值到soureceTree中的url中。
  - 选择，存放路径即可。

### PULL

作用，已经本地和远端建立连接的情况下（已经clone过了），将远端的代码，同步到本地。（让本地保持和远端一样）。这个过程叫做pull

在sourceTree中，使用拉去，点击确定。

### 切换版本

切换版本，就是可以快速的预览，之前的文件的情况。

在sourceTree中，直接双击。

### 多次commit后再push

如果本地项目进行修改之后，sourceTree会提示，修改文件的个数。

如果想使用sourceTree进行提交，需要先勾选“暂存的文件”（需要提交什么，就勾选什么。允许部分提交）

提交之后，此时远端并不会发生变化。需要进行一次push（推送），让远端同步本地的代码。让远端和本地保持一致。

### 关于提交时间

提交的时间，以每次commit为准。与push无关。

### 提交的时候同时推送

在提交写注释的时候，最下方有一个，“立即推送并更变 orgin/master”。

这个选项，表示。提交并且推送到远端

### 小总结

commit 

push

pull

clone

add

init

### 冲突

冲突发生的情况，在多个人开发中，出现了，同一个文件同一行代码的修改。会产生这个问题。

在pull的时候，会发生。（当远端的某一个文件的某一行。和本地不同， 并且不是之前的版本）

解决的问题的方法，需要自己权衡。保留或者删除。删除多余的<<<< ===== >>>> 相关信息、

```
<<<<<< HEAD
print(1)
======
print(2)
>>>>>> 8ux8vus8fsd8fus8dufs

HEAD部分是自己的代码
远端版本号的代码是远端的代码
```

重新提交，并推送。





