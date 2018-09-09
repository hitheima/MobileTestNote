## 35.Allure报告

### Allure介绍

```
	Allure是一个独立的报告插件，生成美观易读的报告，目前支持语言：Java, PHP, Ruby, Python, Scala, C#。
```

### Allure安装

```
	1.安装pytest的插件包pytest-allure-adaptor: pip3 install pytest-allure-adaptor
```

### Allure帮助文档

```
	https://docs.qameta.io/allure/#_about
```

### 生成Allure报告

```
	命令行参数：pytest --alluredir report  # 在执行命令目录生成report文件夹，文件夹下包含xml文件
```

- 示例

```
	pytest.ini

	[pytest]
	;--html=./report.html
	;删除原生html，增加Allure
	addopts = -s --alluredir report
	# 测试路径
	testpaths = ./Test
	# 测试文件名
	python_files = test_*.py
	# 测试类名
	python_classes = Test_*
	# 测试的方法名
	python_functions = test_*

```

```
	test_all.py

	class Test_allure:
	    def setup(self):
	        pass
	    def teardown(self):
	        pass
	    def test_al(self):
	        assert 0
```

```
	操作步骤：
		1.命令行进入pytest.ini所在目录
		2.输入命令：pytest
	执行结果：
		1.pytest.ini所在目录生成report文件夹，文件夹下生成一个xml文件

```

![allure_xml](./%E7%A7%BB%E5%8A%A8%E7%AB%AF%E6%B5%8B%E8%AF%95_image/allure_xml.png)

### xml转html工具安装

#### mac版本

```
	1.：brew install allure
	2.进入report上级目录执行命令：allure generate report/ -o report/html --clean
	3.report目录下会生成index.html文件，即为可视化报告

```

#### windows版本

```
	1.下载压缩包allure-2.6.0.zip
		地址：https://bintray.com/qameta/generic/allure2
	2.解压
	3.将压缩包内的bin目录配置到path系统环境变量
	4.进入report上级目录执行命令：allure generate report/ -o report/html --clean
	5.report目录下会生成index.html文件，即为可视化报告

```

![allure_html](./%E7%A7%BB%E5%8A%A8%E7%AB%AF%E6%B5%8B%E8%AF%95_image/allure_html.png)

## 36.Allure之Pytest

### 添加测试步骤

```
	方法：@allure.step(title="测试步骤001")

```

```
	示例：
		test_all.py
		import allure, pytest
		class Test_allure:
		    def setup(self):
		        pass
		    def teardown(self):
		        pass
		    @allure.step('我是测试步骤001')
		    def test_al(self, a):
		        assert a != 2

```

![allure步骤](/Users/Yoson/Desktop/MobileTestNote/笔记/移动端测试_image/allure%E6%AD%A5%E9%AA%A4.png)

### 添加测试描述

#### 文字描述

```
	方法：allure.attach('描述', '我是测试步骤001的描述～～～')

```

```
示例：
		test_all.py
		import allure, pytest
		class Test_allure:
		    def setup(self):
		        pass
		    def teardown(self):
		        pass
		    @allure.step('我是测试步骤001')
		    def test_al(self, a):
		    	allure.attach('描述', '我是测试步骤001的描述～～～', allure.attach_type.TEXT)
		        assert a != 2

```

![allure步骤描述](/Users/Yoson/Desktop/MobileTestNote/笔记/移动端测试_image/allure%E6%AD%A5%E9%AA%A4%E6%8F%8F%E8%BF%B0.png)

```
allure.attach('描述', '我是测试步骤001的描述～～～', allure.attach_type.TEXT)
# 若类型是文字，最后一个参数可以省略。
allure.attach('描述', '我是测试步骤001的描述～～～')
```

#### 图片描述

截图并上传

```
self.driver.get_screenshot_as_file("./xxx.png")

with open("./xxx.png", 'rb') as f:
    allure.attach('描述', f.read(), allure.attach_type.PNG)
    
或者：

allure.attach("截图：", self.driver.get_screenshot_as_png(), allure.attach_type.PNG)

第一种是截图保存到本地，并上传本地图片。
第二种是直接截图上传。
```

### 添加严重级别

```
	测试用例设置不同的严重级别，可以帮助测试和开发人员更直观的关注重要Case.
```

```
	方法：@pytest.allure.severity(Severity)
	参数：
		Severity：严重级别(BLOCKER,CRITICAL,NORMAL,MINOR,TRIVIAL)
	使用方式：
		@pytest.allure.severity(pytest.allure.severity_level.CRITICAL）
```

```
	示例：
		test_all.py
		import allure, pytest
		class Test_allure:
		    def setup(self):
		        pass
		    def teardown(self):
		        pass
		    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL）
		    @allure.step('我是测试步骤001')
		    def test_al(self, a):
		    	allure.attach('描述', '我是测试步骤001的描述～～～')
		        assert a != 2

```

![allure严重级别](/Users/Yoson/Desktop/MobileTestNote/笔记/移动端测试_image/allure%E4%B8%A5%E9%87%8D%E7%BA%A7%E5%88%AB.png)

