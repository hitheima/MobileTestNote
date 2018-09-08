## 14.Pytest安装和介绍

- 介绍

```
	pytest是python的一种单元测试框架，同自带的Unittest测试框架类似，相比于Unittest框架使用起来更简洁，效率更高。
```

- 特点:

```
	1.非常容易上手，入门简单，文档丰富，文档中有很多实例可以参考
	2.支持简单的单元测试和复杂的功能测试
	3.支持参数化
	4.执行测试过程中可以将某些测试跳过，或者对某些预期失败的Case标记成失败
	5.支持重复执行失败的Case
	6.支持运行由Nose , Unittest编写的测试Case
	7.具有很多第三方插件，并且可以自定义扩展
	8.方便的和持续集成工具集成
```

### Pytest安装

```
	1.mac／linux：sudo pip3 install -U pytest # -U:可以理解为--upgrade，表示已安装就升级为最新版本
	2.管理员方式运行cmd：pip3 install -U pytest
```

### Pytest安装成功校验

```
	1.进入命令行
	2.运行：pytest --version # 会展示当前已安装版本
```

## 15.Pytest运行方式

### Hello Pytest

```
	# file_name: test_abc.py
	import pytest # 引入pytest包
	def test_a(): # test开头的测试函数
	    print("------->test_a")
	    assert 1 # 断言成功
	def test_b():
	    print("------->test_b")
	    assert 0 # 断言失败
	if __name__ == '__main__':
	    # pytest.main("-s  test_abc.py") # 调用pytest的main函数执行测试
		pytest.main(["-s", "login.py"])
```

```
	执行结果：
		test_abc.py 
		------->test_a
		. # .(代表成功)
		------->test_b
		F # F(代表失败)
```

### Pytest运行方式

- 1.测试类主函数模式

```
	pytest.main(["-s", "test_abc.py"])
```

- 2.命令行模式

```
	pytest 文件路径／测试文件名
	例如：
		pytest -s test_abc.py
```

## 16.setup和teardown函数

- 概述

```
	1.setup和teardown主要分为：函数级、类级、模块级、功能级。
	2.存在于测试类内部
```

### 函数级别

```
	运行于测试方法的始末，即:运行一次测试函数会运行一次setup和teardown
```

```
	代码示例：
		import pytest
		class TestABC:
			# 函数级开始
		    def setup(self):
		        print("------->setup_method")
		    # 函数级结束
		    def teardown(self):
		        print("------->teardown_method")
		    def test_a(self):
		        print("------->test_a")
		        assert 1
		    def test_b(self):
		        print("------->test_b")
		if __name__ == '__main__':
		    pytest.main("-s  test_abc.py")
```

```
	执行结果：
		test_abc.py 
		------->setup_method # 第一次 setup()
		------->test_a
		.
		------->teardown_method # 第一次 teardown()
		------->setup_method # 第二次 setup()
		------->test_b
		.
		------->teardown_method # 第二次 teardown()
```

### 类级别

```
	运行于测试类的始末，即:在一个测试内只运行一次setup_class和teardown_class，不关心测试类内有多少个测试函数。
```

```
	代码示例：
		import pytest
		class TestABC:
			# 测试类级开始
		    def setup_class(self):
		        print("------->setup_class")
		    # 测试类级结束
		    def teardown_class(self):
		        print("------->teardown_class")
		    def test_a(self):
		        print("------->test_a")
		        assert 1
		    def test_b(self):
		        print("------->test_b")
		if __name__ == '__main__':
		    pytest.main("-s  test_abc.py")
```

```
	执行结果：
		test_abc.py 
		------->setup_class # 第一次 setup_class()
		------->test_a
		.
		------->test_b
		F 
		------->teardown_class # 第一次 teardown_class()
```

## 17.Pytest配置文件

```
	pytest的配置文件通常放在测试目录下，名称为pytest.ini，命令行运行时会使用该配置文件中的配置.
```

### 配置pytest命令行运行参数

```
	[pytest]
	addopts = -s ... # 空格分隔，可添加多个命令行参数 -所有参数均为插件包的参数
```

### 配置测试搜索的路径

```
	[pytest]
	testpaths = ./scripts  # 当前目录下的scripts文件夹 -可自定义
```

### 配置测试搜索的文件名

```
	[pytest]
	python_files = test_*.py  
	# 当前目录下的scripts文件夹下，以test_开头，以.py结尾的所有文件 -可自定义
```

### 配置测试搜索的测试类名

```
	[pytest]
	python_classes = Test*  
	# 当前目录下的scripts文件夹下，以test_开头，以.py结尾的所有文件中，以Test_开头的类 -可自定义
```

### 配置测试搜索的测试函数名

```
	[pytest]
	python_functions = test_*       
	# 当前目录下的scripts文件夹下，以test_开头，以.py结尾的所有文件中，以Test_开头的类内，以test_开头的方法 -可自定义

```

## 18.Pytest常用插件

```
	插件列表网址：https://plugincompat.herokuapp.com
	包含很多插件包，大家可依据工作的需求选择使用。

```

```
	前置条件：
		1.文件路径：
			- Test_App
			- - test_abc.py
			- - pytest.ini
		2.pyetst.ini配置文件内容：
			[pytest]
			# 命令行参数
			addopts = -s
			# 搜索文件名
			python_files = test_*.py
			# 搜索的类名
			python_classes = Test*
			# 搜索的函数名
			python_functions = test_*

```

### Pytest测试报告

```
	通过命令行方式，生成xml/html格式的测试报告，存储于用户指定路径。

```

```
	插件名称：pytest-html
	安装方式：
		1.安装包方式 python setup.py install 
		2.命令行 pip3 install pytest-html
	使用方法：
		命令行格式：pytest --html=用户路径/report.html

```

```
	示例：
		import pytest
		class TestABC:
			def setup_class(self):
				print("------->setup_class")
			def teardown_class(self):
				print("------->teardown_class")
			def test_a(self):
				print("------->test_a")
				assert 1
			def test_b(self):
				print("------->test_b")
				assert 0 # 断言失败
	运行方式：
		1.修改Test_App/pytest.ini文件，添加报告参数，即：addopts = -s --html=./report.html 
			# -s:输出程序运行信息
			# --html=./report.html 在当前目录下生成report.html文件
			⚠️ 若要生成xml文件，可将--html=./report.html 改成 --html=./report.xml
		2.命令行进入Test_App目录
		3.执行命令： pytest
	执行结果：
		1.在当前目录会生成assets文件夹和report.html文件

```

![报告截图](/Users/Yoson/Desktop/MobileTestNote/%E7%AC%94%E8%AE%B0/%E7%A7%BB%E5%8A%A8%E7%AB%AF%E6%B5%8B%E8%AF%95_image/report.png)

### Pytest控制函数执行顺序

```
	函数修饰符的方式标记被测试函数执行的顺序.

```

```
	插件名称：pytest-ordering
	安装方式：
		1.安装包方式 python setup.py install 
		2.命令行 pip3 install pytest-ordering
	使用方法：
		1.标记于被测试函数，@pytest.mark.run(order=x)
		2.根据order传入的参数来解决运行顺序
		3.order值全为正数或全为负数时，运行顺序：值越小，优先级越高
		4.正数和负数同时存在：正数优先级高

```

```
	默认情况下，pytest是根据测试方法名由小到大执行的,可以通过第三方插件包改变其运行顺序。

```

```
	默认执行方式
	示例：
		import pytest
		class TestABC:
		    def setup_class(self):
		        print("------->setup_class")
		    def teardown_class(self):
		        print("------->teardown_class")
		    def test_a(self):
		        print("------->test_a")
		        assert 1
		    def test_b(self):
		        print("------->test_b")
		        assert 0
		if __name__ == '__main__':
		    pytest.main("-s  test_abc.py")
	执行结果：
		test_abc.py 
		------->setup_class
		------->test_a # 默认第一个运行
		.
		------->test_b # 默认第二个运行
		F
		------->teardown_class

```

```
	示例：
		import pytest
		class TestABC:
			def setup_class(self):
				print("------->setup_class")

			def teardown_class(self):
				print("------->teardown_class")
			@pytest.mark.run(order=2)
			def test_a(self):
				print("------->test_a")
				assert 1

			@pytest.mark.run(order=1)
			def test_b(self):
				print("------->test_b")
				assert 0
		if __name__ == '__main__':
				pytest.main("-s  test_abc.py")
	执行结果：
		test_abc.py
		------->setup_class
		------->test_b # order=1 优先运行
		F
		------->test_a # order=2 晚于 order=1 运行
		.
		------->teardown_class


```

### Pytest失败重试

```
	通过命令行方式，控制失败函数的重试次数。

```

```
	插件名称：pytest-rerunfailures
	安装方式：
		1.安装包方式 python setup.py install 
		2.命令行 pip3 install pytest-rerunfailures
	使用方法：
		命令行格式：pytest --reruns n # n：为重试的次数

```

```
	示例：
	import pytest
	class Test_ABC:
		def setup_class(self):
			print("------->setup_class")
		def teardown_class(self):
			print("------->teardown_class")
		def test_a(self):
			print("------->test_a")
			assert 1
		def test_b(self):
			print("------->test_b")
			assert 0 # 断言失败
	运行方式：
		1.修改Test_App/pytest.ini文件，添加失败重试参数，即：addopts = -s  --reruns 2 --html=./report.html 
			# -s:输出程序运行信息
			# --reruns 2 ：失败测试函数重试两次
			# --html=./report.html 在当前目录下生成report.html文件
		2.命令行进入Test_App目录
		3.执行命令： pytest
	执行结果：
		1.在测试报告中可以看到两次重试记录

```

![失败重试](/Users/Yoson/Desktop/MobileTestNote/笔记/移动端测试_image/%E9%87%8D%E8%AF%95.png)

## 19.Pytest高阶用法

### 跳过测试函数

```
	根据特定的条件，不执行标识的测试函数.

```

```
	方法：
		skipif(condition, reason=None)
	参数：
		condition：跳过的条件，必传参数
		reason：标注原因，必传参数
	使用方法：
		@pytest.mark.skipif(condition, reason="xxx")

```

```
	示例：
		import pytest
		class TestABC:
			def setup_class(self):
				print("------->setup_class")
			def teardown_class(self):
				print("------->teardown_class")
			def test_a(self):
				print("------->test_a")
				assert 1
			@pytest.mark.skipif(condition=2>1,reason = "跳过该函数") # 跳过测试函数test_b
			def test_b(self):
				print("------->test_b")
				assert 0
	执行结果：
		test_abc.py 
		------->setup_class
		------->test_a #只执行了函数test_a
		.
		------->teardown_class
		s # 跳过函数


```

### 标记为预期失败函数

```
	标记测试函数为失败函数


```

```
	方法：
		xfail(condition=None, reason=None, raises=None, run=True, strict=False)
	常用参数：
		condition：预期失败的条件，必传参数
		reason：失败的原因，必传参数
	使用方法：
		@pytest.mark.xfail(condition, reason="xx")

```

```
	示例：
		import pytest
		class TestABC:
			def setup_class(self):
				print("------->setup_class")
			def teardown_class(self):
				print("------->teardown_class")
			def test_a(self):
				print("------->test_a")
				assert 1
			@pytest.mark.xfail(2 > 1, reason="标注为预期失败") # 标记为预期失败函数test_b
			def test_b(self):
				print("------->test_b")
				assert 0
	执行结果：
		test_abc.py 
		------->setup_class
		------->test_a
		.
		------->test_b
		------->teardown_class
		x  # 失败标记


```

### 函数数据参数化

```
	方便测试函数对测试数据的获取。
```

```
	方法：
		parametrize(argnames, argvalues, indirect=False, ids=None, scope=None)
	常用参数：
		argnames：参数名
		argvalues：参数对应值，类型必须为list
					当参数为一个时格式：[value]
					当参数个数大于一个时，格式为:[(param_value1,param_value2.....),(param_value1,param_value2.....)]
	使用方法:
		@pytest.mark.parametrize(argnames,argvalues)
		⚠️ 参数值为N个，测试方法就会运行N次
```

```
	单个参数示例：
		import pytest
		class TestABC:
			def setup_class(self):
				print("------->setup_class")
			def teardown_class(self):
				print("------->teardown_class")

			@pytest.mark.parametrize("a",[3,6]) # a参数被赋予两个值，函数会运行两遍
			def test_a(self,a): # 参数必须和parametrize里面的参数一致
				print("test data:a=%d"%a)
				assert a%3 == 0
	执行结果:
		test_abc.py 
		------->setup_class
		test data:a=3 # 运行第一次取值a=3
		.
		test data:a=6 # 运行第二次取值a=6
		. 
		------->teardown_class
```

```
	多个参数示例：
		import pytest
		class TestABC:
			def setup_class(self):
				print("------->setup_class")
			def teardown_class(self):
				print("------->teardown_class")

			@pytest.mark.parametrize("a,b",[(1,2),(0,3)]) # 参数a,b均被赋予两个值，函数会运行两遍
			def test_a(self,a,b): # 参数必须和parametrize里面的参数一致
				print("test data:a=%d,b=%d"%(a,b))
				assert a+b == 3
	执行结果：
		test_abc.py 
		------->setup_class
		test data:a=1,b=2 # 运行第一次取值 a=1,b=2
		.
		test data:a=0,b=3 # 运行第二次取值 a=0,b=3
		.
		------->teardown_class


```

```
	函数返回值类型示例：
		import pytest
		def return_test_data():
			return [(1,2),(0,3)]
		class TestABC:
			def setup_class(self):
				print("------->setup_class")
			def teardown_class(self):
				print("------->teardown_class")

			@pytest.mark.parametrize("a,b",return_test_data()) # 使用函数返回值的形式传入参数值
			def test_a(self,a,b):
				print("test data:a=%d,b=%d"%(a,b))
				assert a+b == 3
	执行结果：
		test_abc.py 
		------->setup_class
		test data:a=1,b=2 # 运行第一次取值 a=1,b=2
		.
		test data:a=0,b=3 # 运行第二次取值 a=0,b=3
		.
		------->teardown_class


```



## 20.Pytest-fixture

```
	fixture修饰器来标记固定的工厂函数,在其他函数，模块，类或整个工程调用它时会被激活并优先执行,
		通常会被用于完成预置处理和重复操作。

```

```
	方法：fixture(scope="function", params=None, autouse=False, ids=None, name=None)
	常用参数:
		scope：被标记方法的作用域
			function" (default)：作用于每个测试方法，每个test都运行一次
			"class"：作用于整个类，每个class的所有test只运行一次
			"module"：作用于整个模块，每个module的所有test只运行一次
			"session：作用于整个session(慎用)，每个session只运行一次
		params：(list类型)提供参数数据，供调用标记方法的函数使用
		autouse：是否自动运行,默认为False不运行，设置为True自动运行

```

### fixture(通过参数引用)

```
	示例：
		import pytest
		class TestABC:
		    @pytest.fixture()
		    def before(self):
		        print("------->before")
		    def test_a(self,before): # ⚠️ test_a方法传入了被fixture标识的函数，已变量的形式
		        print("------->test_a")
		        assert 1
		if __name__ == '__main__':
		    pytest.main("-s  test_abc.py")

```

```
	执行结果：
		test_abc.py 
		------->before # 发现before会优先于测试函数运行
		------->test_a
		.  

```

### fixture(通过函数引用)

```
	示例：
		import pytest
		@pytest.fixture() # fixture标记的函数可以应用于测试类外部
		def before():
		    print("------->before")
		@pytest.mark.usefixtures("before")
		class TestABC:
		    def setup(self):
		        print("------->setup")
		    def test_a(self):
		        print("------->test_a")
		        assert 1
		if __name__ == '__main__':
		    pytest.main("-s  test_abc.py")

```

```
	执行结果：
		test_abc.py 
		------->before # 发现before会优先于测试类运行
		------->setup
		------->test_a
		.

```

### fixture(默认设置为运行)

```
	示例：
		import pytest
		@pytest.fixture(autouse=True) # 设置为默认运行
		def before():
		    print("------->before")
		class TestABC:
		    def setup(self):
		        print("------->setup")
		    def test_a(self):
		        print("------->test_a")
		        assert 1
		if __name__ == '__main__':
		    pytest.main("-s  test_abc.py")

```

```
	执行结果：
		test_abc.py 
		------->before # 发现before自动优先于测试类运行
		------->setup
		------->test_a
		.

```

### fixture(作用域为function)

```
	示例：
		import pytest
		@pytest.fixture(scope='function',autouse=True) # 作用域设置为function，自动运行
		def before():
		    print("------->before")
		class TestABC:
		    def setup(self):
		        print("------->setup")
		    def test_a(self):
		        print("------->test_a")
		        assert 1
		    def test_b(self):
		        print("------->test_b")
		        assert 1
		if __name__ == '__main__':
		    pytest.main("-s  test_abc.py")

```

```
	执行结果：
		test_abc.py
		------->before # 运行第一次
		------->setup
		------->test_a
		.------->before # 运行第二次
		------->setup
		------->test_b
		.

```

### fixture(作用域为class)

```
	示例：
		import pytest
		@pytest.fixture(scope='class',autouse=True) # 作用域设置为class，自动运行
		def before():
		    print("------->before")
		class TestABC:
		    def setup(self):
		        print("------->setup")
		    def test_a(self):
		        print("------->test_a")
		        assert 1
		    def test_b(self):
		        print("------->test_b")
		        assert 1
		if __name__ == '__main__':
		    pytest.main("-s  test_abc.py")

```

```
	执行结果：
		test_abc.py
		------->before # 发现只运行一次
		------->setup
		------->test_a
		.
		------->setup
		------->test_b
		.

```

### fixture(返回值)

```
	示例一:
		import pytest
		@pytest.fixture()
		def need_data():
		    return 2 # 返回数字2

		class TestABC:
		    def test_a(self,need_data):
		        print("------->test_a")
		        assert need_data != 3 # 拿到返回值做一次断言

		if __name__ == '__main__':
		    pytest.main("-s  test_abc.py")
	执行结果：
		test_abc.py 
		------->test_a
		.  

```

```
	示例二:
		import pytest
		@pytest.fixture(params=[1, 2, 3])
		def need_data(request): # 传入参数request 系统封装参数
		    return request.param # 取列表中单个值，默认的取值方式

		class TestABC:

		    def test_a(self,need_data):
		        print("------->test_a")
		        assert need_data != 3 # 断言need_data不等于3

		if __name__ == '__main__':
		    pytest.main("-s  test_abc.py")
	执行结果：
		# 可以发现结果运行了三次
		test_abc.py 
		1
		------->test_a
		.
		2
		------->test_a
		.
		3
		------->test_a
		F 

```

## 