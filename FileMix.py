import os

# 存储路径(即文件存储在哪个目录)
path=""
# 公共文件名，序号前边部分(如果文件名为file*.ts只需要输入file)
name=""
# 文件序号的最大值
index_max=0

# 检查文件是否完整
def CheckFile(index_max,name,path):
    num=[]
    for files in os.walk(path):
        files=files[2]
        for i in range(index_max+1):
            if name+str(i)+".ts" not in files:
                num.append(i)
    return num

# 合并ts文件
def mix(index_max,name,path):
    with open(path+"/"+name+".mp4","wb") as f:
        for i in range(index_max+1):
            file=open(path+"/"+name+str(i)+".ts","rb").read()
            f.write(file)
            print("[√] 已添加文件{0}{1}.ts".format(name,i))
    print("[√] 完成")

if __name__ == "__main__":
    path=input("请输入文件路径：")
    name=input("请输入公共文件名(序号前边部分):")
    index_max=int(input("请输入文件序号的最大值:"))
    print("[  ] 正在检查文件是否完整")
    num=CheckFile(index_max,name,path)
    if len(num)==0:
        print("[√] 检查完成，文件完整")
        print("[  ] 开始合并文件")
        mix(index_max,name,path)
    else:
        print("[×] 发现有缺失文件，序号为：{0}".format(num))
