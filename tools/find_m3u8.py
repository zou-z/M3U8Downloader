import requests
import re

# # 获取真实的m3u8链接地址
# def get_real_m3u8_url(url):
#     real_url=""
#     session=requests.session()
#     headers={
#         "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
#     }
#     res=session.get(url=url,headers=headers).text
#     if res.find("EXT-X-STREAM-INF")==-1:
#         real_url=url
#     else:
#         url1=url[:url.rfind("/")+1]
#         url2=re.search("\n(.*?m3u8)",res).group(1)
#         real_url=url1+url2
#     return real_url

# 获取页面的m3u8链接
def get(url):
    session=requests.session()
    headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
    }
    response=session.get(url=url,headers=headers).text
    result=re.findall("\"(http.*?)\"",response,re.S)
    result+=re.findall("\"(/.*?)\"",response,re.S)
    urls=[]
    for i in result:
        if ".m3u8" in i:
            try:
                temp=re.findall("(http.*?\.m3u8)",i,re.S)[0]
                urls.append(temp.replace("\n",""))
            except:
                continue
    return urls

if __name__ == "__main__":
    res=get(input("请输入链接："))
    if len(res)==0:
        print("未发现m3u8链接！")
    else:
        for i in res:
            print(i)
