## 37.Jenkins安装

```
	Jenkins是一个开源软件项目，是基于Java开发的一种持续集成工具，用于监控持续重复的工作，
	旨在提供一个开放易用的软件平台，使软件的持续集成变成可能。

	一般情况下，公司内部Jenkins安装在服务端，不需要本地安装，都已配置完成，可直接操作使用.

```

- 依赖java环境

```
	jdk1.5以上

```

### 安装jenkins

```
	1.下载jenkins.war
	2.进入jenkins.war所在目录，执行：java -jar jenkins.war
	3.浏览器进入：localhost:8080

```

### 安装所需插件

```
	1.官网下载jenkins安装包

```

```
	2.安装完成后，会自动打开页面(若没有可以手动打开浏览器输入：localhost:8080)

```

```
	3.进入默认密码提示文件，输入系统默认密码

```

![jenkins安装启动页](/Users/Yoson/Desktop/MobileTestNote/笔记/移动端测试_image/jenkins%E5%AE%89%E8%A3%85%E5%90%AF%E5%8A%A8%E9%A1%B5.png)
![jenkins初始密码](/Users/Yoson/Desktop/MobileTestNote/笔记/移动端测试_image/jenkins%E5%88%9D%E5%A7%8B%E5%AF%86%E7%A0%81.png)

```
	4.安装建议插件

```

![jenkins建议安装插件](/Users/Yoson/Desktop/MobileTestNote/笔记/移动端测试_image/jenkins%E5%BB%BA%E8%AE%AE%E5%AE%89%E8%A3%85%E6%8F%92%E4%BB%B6.png)
![jenkins插件安装中](/Users/Yoson/Desktop/MobileTestNote/笔记/移动端测试_image/jenkins%E6%8F%92%E4%BB%B6%E5%AE%89%E8%A3%85%E4%B8%AD.png)

```
	5.设置用户初始化信息

```

![jenkins设置用户信息](/Users/Yoson/Desktop/MobileTestNote/笔记/移动端测试_image/jenkins%E8%AE%BE%E7%BD%AE%E7%94%A8%E6%88%B7%E4%BF%A1%E6%81%AF.png)

```
	6.jenkins启动

```

![jenkins启动](/Users/Yoson/Desktop/MobileTestNote/笔记/移动端测试_image/jenkins%E5%90%AF%E5%8A%A8.png)

```
	7.jenkins首页

```

![jenkins首页](/Users/Yoson/Desktop/MobileTestNote/笔记/移动端测试_image/jenkins%E9%A6%96%E9%A1%B5.png)

## 38.Jenkins持续集成配置

### Jenkins安装Allure插件

```
	1.进入jenkins系统管理 -> 管理插件
	2.点击可选插件
	3.搜索框输入Allure
	4.选中安装
```

### Jenkins安装Allure Commandline工具

```
	1.进入jenkins系统管理 -> 全局工具配置
	2.找到Allure Commandline，点击Allure Commandline安装
	3.输入一个别名
	4.点击新增安装-选择解压*.ip/*.tar.gz
	5.解压目录选择已下载好的allure2.5.0.zip包所在目录(⚠️ 版本要一致)
	6.点击保存

```

![allure_commind](./%E7%A7%BB%E5%8A%A8%E7%AB%AF%E6%B5%8B%E8%AF%95_image/allure_commind.png)

### Jenkins新建一个项目

```
	1.选择新建一个自由风格的软件项目 -> 点击确定
	2.输入一些项目描述

```

```
	3.选择GitHub project 
	4.输入Project url # 因我们只是举例，所以使用自己的一个github测试脚本
	

```

![J_General](./%E7%A7%BB%E5%8A%A8%E7%AB%AF%E6%B5%8B%E8%AF%95_image/J_General.png)

### 源码管理配置

```
	5.勾选Git
	6.Repository URL输入地址同第四步
	7.点击Add添加github的用户名和密码

```

![J_源码](/Users/Yoson/Desktop/MobileTestNote/笔记/移动端测试_image/J_%E6%BA%90%E7%A0%81.png)
![github用户名密码](/Users/Yoson/Desktop/MobileTestNote/笔记/移动端测试_image/github%E7%94%A8%E6%88%B7%E5%90%8D%E5%AF%86%E7%A0%81.png)

### 构建触发器

```
	8.勾选Poll SCM # 根据定时任务，查看github版本是否更新，如果更新会自动构建项目
	9.输入crontab命令
		举例：
			*/1 * * * * # 每一分钟检查一次
	10.点击增加构建步骤，选择Execute shell，win选择 execute windows shell
	11.Command输入
		mac：
		export PATH=$PATH:"pytest可执行文件的目录"
		pytest
		
		windows：
		PATH=$PATH;      #(到scripts)
		pytest

```

![J_构建](/Users/Yoson/Desktop/MobileTestNote/笔记/移动端测试_image/J_%E6%9E%84%E5%BB%BA.png)

```
时程表的格式如下:
f1 f2 f3 f4 f5 program
其中 f1 是表示分钟，f2 表示小时，f3 表示一个月份中的第几日，f4 表示月份，f5 表示一个星期中的第几天。program 表示要执行的程式。

```

### 构建后操作

```
	12.点击增加构建后操作步骤，选择Allure Report
	13.Path路径输入：生成的报告文件夹名称
	⚠️ 文件夹名称与pytest生成的报告文件夹名称一致

```

![J_构建后](/Users/Yoson/Desktop/MobileTestNote/笔记/移动端测试_image/J_%E6%9E%84%E5%BB%BA%E5%90%8E.png)

## 39.jenkins触发项目构建方式

### 手动触发构建

- 点击立即构建

### 更新github代码

- 触发器在定时任务到达时，会出发项目构建

![手动构建](/Users/Yoson/Desktop/MobileTestNote/笔记/移动端测试_image/%E6%89%8B%E5%8A%A8%E6%9E%84%E5%BB%BA.png)

## 40.Jenkins邮件配置

### 发件人配置

```
	配置邮件系统用户：
		系统管理-系统设置-Jenkins Location
		系统管理员邮件地址：用户名@163.com(发送邮件用户)
	配置系统邮件：
		系统管理-系统设置-邮件通知
		SMTP服务器：例 smtp.163.com
		用户默认邮件后缀：例如 @163.com
		高级-使用SMTP认证
		输入发送邮箱和密码 -可以使用测试邮件验证
```

```
配置(发送附件)邮件：
	系统管理-系统设置-Extended E-mail Notification
	SMTP server：例 smtp.163.com
	Default user E-mail suffix：例如 @163.com
	高级-Use SMTP Authentication - 输入发送邮件的邮箱和密码
	Default Content Type: HTML(text/html)
	Default Content(报告模版,使用以下html代码即可):
	       <hr/>(本邮件是程序自动下发的，请勿回复！)<hr/>
			项目名称：$PROJECT_NAME<br/><hr/>
			构建编号：$BUILD_NUMBER<br/><hr/>
			git版本号：${GIT_REVISION}<br/><hr/>
			构建状态：$BUILD_STATUS<br/><hr/>
			触发原因：${CAUSE}<br/><hr/>
			目录：${ITEM_ROOTDIR}<br/><hr/>
			构建日志地址：<a href=" ">${BUILD_URL}console</a ><br/><hr/>
			构建地址：<a href="$BUILD_URL">$BUILD_URL</a ><br/><hr/>
			报告地址：<a href="${BUILD_URL}allure">${BUILD_URL}allure</a ><br/><hr/>
			失败数：${FAILED_TESTS}<br/><hr/>
			成功数：${FAILED_TESTS}<br/><hr/>
			变更集：${JELLY_SCRIPT,template="html"}<br/><hr/>
```

### 收件人配置

```
	# 添加测试报告接收邮件列表

	14.点击增加构建后操作步骤，选择Editable Email Notification 
	15.点击Advanced Setting…
	16.点击Triggers中的高级按钮
	17.Recipient List输入邮件接收列表，多个邮件逗号分隔


```

![邮件列表](/Users/Yoson/Desktop/MobileTestNote/笔记/移动端测试_image/%E9%82%AE%E4%BB%B6%E5%88%97%E8%A1%A8.png)



## 