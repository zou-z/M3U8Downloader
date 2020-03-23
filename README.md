# M3U8Downloader
m3u8视频多线程下载器（自动合成ts文件）
## 调用的库
requests  
threading  
re  
os 
## 使用方法  
运行main.py后按提示输入m3u8链接即可下载m3u8视频  
## 可配置的参数
(1) thread_num: 多线程数量
## 提示  
如果需要下载一些第一次下载失败的ts文件，可以将这些ts文件名填入files变量，并注释parse_m3u8函数中files的赋值  

