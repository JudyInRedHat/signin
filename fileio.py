# 读取文件，返回一个字典
def readAnDict(file):
    data = {
        "date":'',
        "lucky":0
    }
    file_ = open(file,mode='r')
    filelist = file_.readlines()
    data["date"] = filelist[0].replace('\n','')
    data["lucky"] = int(filelist[1])
    file_.close()
    return data

# 写入文件
def writeData(date,point):
    file_ = open("data.txt",mode='w')
    file_.write(date+'\n'+str(point))
    file_.close()

#print(readAnDict("test.txt"))
