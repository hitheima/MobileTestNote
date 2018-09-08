## 32.Yaml数据存储文件

```
	YAML 是一种所有编程语言可用的友好的数据序列化标准,语法和其他高阶语言类似，并且可以简单表达清单、散列表，标量等资料形态.

```

- 语法规则

```
	1.大小写敏感
	2.使用缩进表示层级关系
	3.缩进时不允许使用Tab键，只允许使用空格。
	4.缩进的空格数目不重要，只要相同层级的元素左侧对齐即可
```

- 支持的数据结构

```
	1.对象：键值对的集合，又称为映射（mapping）/ 哈希（hashes） / 字典（dictionary）
	2.数组：一组按次序排列的值，又称为序列（sequence） / 列表（list）
	3.纯量（scalars）：单个的、不可再分的值

```

- 1.对象

  - 值为字符

  ```
  	data.yaml
  	 animal: pets
  
  	转换为python代码
  	 {'animal': 'pets'}
  
  ```

  - 值为字典

  ```
  	data.yaml
  	 animal: {"ke1":"pets","key2":"app"} # python字典
  
  	转换为python代码
  	 {animal: {"ke1":"pets","key2":"app"}} # 嵌套字典结构
  
  ```

- 2.数组

  - 方式一

  ```
  	data.yaml
  	 animal: 
  	   - data1
  	   - data2
  	转换为python代码
  	 {'animal': ['data1', 'data2']}
  
  
  ```

  - 方式二

  ```
  	data.yaml
  	 animal: ['data1', 'data2'] # python列表
  
  	转换为python代码
  	 {'animal': ['data1', 'data2']} # 字典嵌套列表
  
  ```

- 纯量

```
	包含：字符串，布尔值，整数，浮点数，Null，日期

```

```
	字符串
	data.yaml
	 value: "hello"
	
	转换为python代码
	 {"value":"hello"}

```

```
	布尔值
	data.yaml
	 value1: true
	 value2: false
	
	转换为python代码
	 {'value1': True, 'value2': False}

```

```
	整数，浮点数
	data.yaml
	 value1: 12
	 value2: 12.102
	
	转换为python代码
	 {'value1': 12, 'value2': 12.102}

```

```
	空(Null)
	data.yaml
	 value1: ~ # ~ 表示为空
	转换为python代码
	 {'value1': None}

```

```
	日期
	data.yaml
	 value1: 2017-10-11 15:12:12
	转换为python代码
	 {'languages': {'value1': datetime.datetime(2017, 10, 11, 15, 12, 12)}}


```

- 锚点&和引用*

```
	锚点：标注一个内容，锚点名称自定义
	引用：使用被标注的内容<<: *锚点名

```

```
	data.yaml
	 data: &imp
  	  value: 456
     name:
      value1: 123
      <<: *imp # "<<:" 合并到当前位置，"*imp" 引用锚点imp
    转换为python代码
     {'data': {'value': 456}, 'name': {'value': 456, 'value1': 123}}

```

## 33.Python解析yaml文件

- PyYAML库安装

```
	PyYAML为python解析yaml的库
	安装：pip3 install -U PyYAML

```

- yaml文件内容

```
	Search_Data:
	  search_test_001:
	    value: 456
	    expect: [4,5,6]
	  search_test_002:
	    value: "你好"
	    expect: {"value":"你好"}

```

- 读取yaml文件

  - 方法

  ```
  	yaml.load(stream, Loader=Loader)
  	参数：
  		stream：待读取文件对象
  
  ```

  ```
  	示例：
  		import yaml
  		with open("../Data/search_page.yaml",'r') as f:
  		    data = yaml.load(f)
  		    print(type(data)) # 打印data类型
  		    print(data) # 打印data返回值
  
  	执行结果：
  		<class 'dict'>
  		{'Search_Data': {
  			'search_test_002': {'expect': {'value': '你好'}, 'value': '你好'}, 
  			'search_test_001': {'expect': [4, 5, 6], 'value': 456}}}
  
  
  ```

- 写入yaml文件内容

```
	{'Search_Data': {
				'search_test_002': {'expect': {'value': '你好'}, 'value': '你好'}, 
				'search_test_001': {'expect': [4, 5, 6], 'value': 456}}}

```

- 写yaml文件

  - 方法

  ```
  	yaml.dump(data,stream,**kwds)
  	常用参数：
  		data：写入数据类型为字典
  		stream：打开文件对象
  		encoding='utf-8' # 设置写入编码格式
  		allow_unicode=True # 是否允许unicode编码
  
  ```

  ```
  	示例：不设置编码格式
  		import yaml
  		data = {'Search_Data': {
  						'search_test_002': {'expect': {'value': '你好'}, 'value': '你好'},
  						'search_test_001': {'expect': [4, 5, 6], 'value': 456}}
  		with open("./text.yaml","w") as f: # 在当前目录下生成text.yaml文件，若文件存在直接更新内容
  		    yaml.dump(data,f)
  	执行结果：
  		1.当前目录生成text.yaml文件
  		2.文件内容：
  			Search_Data:
  			  search_test_001:
  			    expect: [4, 5, 6]
  			    value: 456
  			  search_test_002:
  			    expect: {value: "\u4F60\u597D"} # 中文出现乱码
  			    value: "\u4F60\u597D" # 中文出现乱码
  
  
  ```

  ```
  	示例：设置编码格式
  		import yaml
  		data = {'Search_Data': {
  						'search_test_002': {'expect': {'value': '你好'}, 'value': '你好'},
  						'search_test_001': {'expect': [4, 5, 6], 'value': 456}}
  		with open("./text.yaml","w") as f: # 在当前目录下生成text.yaml文件，若文件存在直接更新内容
  		    yaml.dump(data,f)
  	执行结果：
  		1.当前目录生成text.yaml文件
  		2.文件内容：
  			Search_Data:
  			  search_test_001:
  			    expect: [4, 5, 6]
  			    value: 456
  			  search_test_002:
  			    expect: {value: 你好} # 中文未出现乱码
  			    value: 你好 # 中文未出现乱码
  
  ```

## 34.Yaml数据驱动应用

```
	目标集成Pytest完成测试任务

```

- 测试项目

```
	业务：
		1.进入设置点击搜索按钮
		2.输入搜索内容
		3.点击返回

```

- 目录结构

```
		App_Project # 项目名称
		  - Basic # 存储基础设施类
		  	- __init__.py # 空文件
		  	- Init_Driver.py # 手机驱动对象初始化
		  	- Base.py # 方法的二次封装
		  	- read_data.py #数据解析读取方法
		  - Page # 存储封装页面文件
		  	- __init__.py # 存储页面元素
		  	- search_page.py # 封装页面元素的操作方法
		  - Data # 存储数据文件
		  	- search_data.yaml(也可以是其他文件比如txt，excel，json，数据库等)
		  - Test # 存储测试脚本目录
		  	- test_search.py # 测试搜索文件
		  - pytest.ini # pytest运行配置文件

```

- 前置条件

```
	1.手机驱动对象独立 # 见PO章节代码
	2.方法的二次封装 # 见PO章节代码
	3.完成页面的封装 # 见PO章节代码

```

- 待完成任务

```
	1.编写数据驱动文件search_data.yaml
	2.编写解析yaml文件类/方法
	3.编写测试脚本

```

- 编写search_data.yaml

```
	search_test_001: # 用例编号
	  input_text: "你好" # 测试输入数据
	search_test_002:
	  input_text: "1234"
	search_test_003:
	  input_text: "*&^%"

```

- 编写解析yaml方法

```
	read_data.py

	import yaml,os
	class Read_Data:
	    def __init__(self,file_name):
	        '''
	        	使用pytest运行在项目的根目录下运行，即App_Project目录
	        	期望路径为：项目所在目录/App_Project/Data/file_name
	        '''
	        self.file_path = os.getcwd() + os.sep + "Data" + os.sep + file_name 
	    def return_data(self):
	        with open(self.file_path,'r') as f:
	            data = yaml.load(f) # 读取文件内容
	            return data

	    # data:{"search_test_001":{"input_text": "你好"},"search_test_002":{"input_text": "1234"},"search_test_003":{"input_text": "*&^%"}}


```

- 测试脚本编写

```
	test_search.py

	import sys,os
	# 因为需要在项目的根目录下运行，所以需要添加python包搜索路径
	# pytest命令运行路径：App_Project目录下
	# os.getcwd(): App_Project所在目录/App_Project
	sys.path.append(os.getcwd())

	# 导入封装好的页面类
	from Page.search_page import Search_Page
	# 导入独立的手机驱动对象
	from Basic.Init_Driver import init_driver
	from Basic.read_data import Read_Data
	import pytest
	def package_param_data():
	    list_data = [] # 存储参数值列表，格式[(用例编号1,输入内容2),(用例编号1,输入内容2)...]
	    yaml_data = Read_Data("search_data.yaml").return_data() # 返回yaml文件读取数据
	    for i in yaml_data.keys():
	        list_data.append((i,yaml_data.get(i).get('input_text'))) # list_data中添加参数值
	    return list_data

	class Test_Search:
		'''
			我们希望测试函数运行多次，不希望每运行一次做一次初始化和退出，
			所以使用setup_class，teardown_class，
			测试类内只运行一次初始化和结束动作.
		'''
	    def setup_class(self):
	        self.driver = init_driver()

	    @pytest.mark.parametrize('test_id,input_text',package_param_data()) # 参数传递三组参数，会运行三次
	    def test_search(self,test_id,input_text):
	        # 示例化页面封装类
	        sp = Search_Page(self.driver)
	        # 调用操作类
	        print("test_id:",test_id)
	        sp.input_search_text(input_text)
	        # 退出driver对象

	    def teardown_class(self):
	        self.driver.quit()



```

- pytest的配置文件

```
	pytest.ini

	[pytest]
	addopts = -s  --html=./report.html
	# 测试路径
	testpaths = ./Test
	# 测试文件名
	python_files = test_*.py
	# 测试类名
	python_classes = Test_*
	# 测试的方法名
	python_functions = test_*


```

- 项目运行

```
	1.启动appium 服务：地址 127.0.0.1 端口 4723
	2.启动模拟器
	3.进入项目根目录:App_Project
	4.命令行输入pytest运行测试

```

- 测试报告
  ![search报告](/Users/Yoson/Desktop/MobileTestNote/笔记/移动端测试_image/search%E6%8A%A5%E5%91%8A.png)

## 