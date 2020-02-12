import requests
import threading

# 最后一个文件序号(包含index_max)
index_max=96
# 最开始的文件序号(包含index_min)
index_min=60
# 存储的路径
path=""
# 线程数
thread_num=10
# 读写标志(避免重复下载一个文件,此变量值固定不得修改)
canRead=True
# 链接(如果m3u8链接为http://xxx.u3m8则只需要http://xxx即.u3m8之前那部分)
url=""
# 存储的文件名(将自动添加序号)
name=""
# 请求头
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}
# 未下载文件的序号
error_index=[]

# 多线程下载
def start(thread_name):
    global index_min
    global thread_num
    global canRead
    global error_index
    if index_min>index_max:
        thread_num-=1            
        if thread_num==0:
            print("[√] 任务完成")
            if len(error_index)>0:
                print("未完成文件序号：{0}".format(error_index))
        else:
            print("[{0}] 已退出，剩余线程数{1}".format(thread_name,thread_num))
        return
    session=requests.session()
    while not canRead:
        pass
    canRead=False
    _url=url+str(index_min)+".ts"
    _name=name+str(index_min)+".ts"
    index_min+=1
    canRead=True
    print('[{0}] 正在下载{1}'.format(thread_name,_name))
    try:
        res=session.get(_url,headers=headers)
        if int(res.headers["Content-Length"]) <1000:
            print("[{0}] 正在重新连接{1}".format(thread_name,_name))
            res=session.get(_url,headers=headers)
        while int(res.headers["Content-Length"]) <1000:
            res=session.get(_url,headers=headers)
        with open(path+'/'+_name,'wb') as f:
            f.write(res.content)
        print('[{0}] 完成{1}'.format(thread_name,_name))
    except:
        error_index.append(index_min-1)
    t=threading.Thread(target=start,args=(thread_name,))
    t.start()

# 单个下载
def start_s(index):
    session=requests.session()
    _url=url+str(index)+".ts"
    _name=name+str(index)+".ts"
    print("[  ] 正在下载{0}".format(_name))
    res=session.get(_url,headers=headers)
    if int(res.headers["Content-Length"]) <1000:
        print("[  ] 正在重新连接{0}".format(_name))
        res=session.get(_url,headers=headers)
    while int(res.headers["Content-Length"]) <1000:
        res=session.get(_url,headers=headers)
    with open(path+'/'+_name,'wb') as f:
        f.write(res.content)
    print("[√] 完成{0}".format(_name))

if __name__=='__main__':
    # 多线程下载序号连续的文件(修改代码后可下载不连续的)
    url=input("请输入链接(.u3m8之前那部分):")
    name=input("请输入文件名:")
    path=input("请输入存储位置(存储的文件夹)：")
    for i in range(1,thread_num+1):
        t=threading.Thread(target=start,args=("线程"+str(i),))
        t.start()
    '''
    # 单进程下载缺失文件
    for i in error_index:
        start_s(i)
    '''
    