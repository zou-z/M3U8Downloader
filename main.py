import requests
import threading
import re
import os

# 线程数
thread_num=10
# 存储的路径
path=""
# 文件名
file_name=""
# 请求头
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}
# 文件列表
files=[]
# 已完成数量
finished_num=0
# 读写标志(避免重复下载一个文件,此变量值固定不得修改)
canRead=True
# m3u8链接
url=""
# 下载位置索引
index=0
# 未成功下载的文件
error_files=[]

# 多线程下载
def start(thread_name):
    global url
    global canRead
    global error_files
    global files
    global thread_num
    global finished_num
    global file_name
    global index
    if index==len(files):
        thread_num-=1
        if thread_num==0:
            if len(error_files)==0:
                print("[√] 已完成所有文件下载，正在合并文件...")
                with open(path+'/'+file_name,'wb') as f:
                    for i in range(len(files)):
                        f.write(files[i])
                print("[√] 完成，文件位置: {0}".format(path+'/'+file_name))
            else:
                print("[×] 还有{0}个文件未下载：{1}".format(len(error_files),error_files))
        else:
            print("[{0}] 已退出，剩余线程数{1}".format(thread_name,thread_num))
        return
    session=requests.session()
    while not canRead:
        pass
    canRead=False
    ts_name=files[index]
    ts_url=url+ts_name
    ts_index=index
    index+=1
    canRead=True
    print('[{0}] 正在下载{1}'.format(thread_name,ts_name))
    try:
        res=session.get(ts_url,headers=headers)
        while len(res.content) <1024:
            res=session.get(ts_url,headers=headers)
        files[ts_index]=res.content
        finished_num+=1
        print('[{0}] 下载完成{1} ({2}/{3})'.format(thread_name,ts_name,finished_num,len(files)))
    except:
        error_files.append(ts_name)
    t=threading.Thread(target=start,args=(thread_name,))
    t.start()

#解析m3u8信息
def parse_m3u8():
    global url
    global files
    print("[  ] 正在解析m3u8链接...")
    session=requests.session()
    res=session.get(url,headers=headers).content.decode("utf8")
    url=url[0:url.rfind("/")+1]
    files=re.findall("#EXTINF:.*?,\n(.*?)\n",res)
    print("[√] 解析完成,共{0}个文件需要下载".format(len(files)))
    if len(files)==0:
        return False
    else:
        return True

if __name__=='__main__':
    url=input("请输入m3u8链接: ")
    path=input("请输入存储位置：")
    if not os.path.exists(path):
        try:
            os.mkdir(path)
        except:
            print("创建目录失败: {0}".format(path))
            exit(0)
    file_name=input("请输入文件名：")
    while os.path.exists(path+'/'+file_name):
        file_name=input("文件名已存在，请重新输入文件名: ")
    if parse_m3u8():
        for i in range(1,thread_num+1):
            t=threading.Thread(target=start,args=("线程"+str(i),))
            t.start()
    
