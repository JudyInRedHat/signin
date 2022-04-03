# 导入库
import datetime
import os
import fileio
import random
# 首先得到现在的时间
now = datetime.datetime.now()
# 获取今天的日期
today = now.strftime("%d")
# 检查数据文件是否存在
if os.path.isfile("data.txt"):
    # 读取文件
    data_ = fileio.readAnDict("data.txt")
    if data_["date"] == today:
        print("你今天已经签到过啦~  你的人品：",data_["lucky"])
    else:
        lucky = random.randint(0,100)
        print("签到成功！你今天的人品是：",lucky)
        fileio.writeData(today,lucky)
else:
    lucky = random.randint(0,100)
    print("签到成功！你今天的人品是：",lucky)
    fileio.writeData(today,lucky)
