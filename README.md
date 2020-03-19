# U3M8_Download
u3m8视频多线程下载以及合成工具
## 调用的库
requests  
threading  
re  
os 
## 使用方法  
运行main.py后按提示输入即可下载u3m8视频  
## 可配置的参数
(1) thread_num: 多线程数量
## 提示  
如果需要下载一些第一次下载失败的ts文件，可以将这些ts文件名填入files变量，并注释parse_u3m8函数中files的赋值  

