# U3M8_Download
u3m8视频多线程下载以及合成工具
## 调用的库
requests  
threading  
os
## 文件结构  
Download.py #(下载模块)多线程、单线程下载  
FileMix.py #(合成模块)检查文件完整性、视频合成  
## 使用方法
(1)先运行Download.py文件下载每一段视频  
(2)再运行FileMix.py文件合成下载好的视频
## 下载模块中的参数
需要输入的参数：  
(1)链接(url):原链接中.u3m8之前那部分  
(2)文件名(name):每一小段视频的文件名(自动添加序号)，可随意输入  
(3)存储位置(path):存储每一段视频的文件夹的路径  
可调节参数：  
(1)开始的序号：index_min(包含index_min)  
(2)结束的序号：index_max(包含index_max)  
(3)线程数：thread_num  
(4)请求头：headers(如果服务器屏蔽可尝试在此变量中添加其他参数)  
## 合成模块中的参数
需要输入的参数：  
(1)文件路径(path)：视频存储的路径(运行Download.py时输入的存储位置(path))  
(2)文件名(name)：每一段视频的公共文件名(运行Download.py时输入的文件名(name))  
(3)文件序号的最大值(index_max)：也就是Download.py中index_max参数的值  
## 提示  
(1)如果有因为一些因素而没有下载的文件序号将存储在变量error_index中，程序执行完将输出这些序号，然后只运行注释那部分下载缺失的文件  
(2)如果中途退出程序，可运行FileMix.py获取缺失文件的序号，再用Download.py中单线程或多线程下载缺失的文件，最后再次运行FileMix.py合成下载的视频文件

