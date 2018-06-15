# coding=gbk
from PycharmProjects.zzbcheck import loadFileConfig
# zhangwei 20180608

print "check zzb【"+loadFileConfig.fileDate+"】 customer file begin..."

# 校验放款客户号
payDetailFo = open(loadFileConfig.filepath + loadFileConfig.payDetailFilename, "r")

payDetailCount = 0

for payDetailLine in payDetailFo.readlines():

    payDetailLine = payDetailLine .strip()

    if payDetailLine == "":

        break

    payDetailCount = payDetailCount + 1

    print "正在处理:" + str(payDetailCount) + ":" + payDetailLine

    paydetailList = payDetailLine .split("|@#|")

    customerCount = 0

    customerFo = open(loadFileConfig.filepath + loadFileConfig.customerFilename, "r")

    for customerLine in customerFo .readlines():

        customerLine = customerLine.strip()

        if customerLine == "":

            break

        customerList = customerLine.split("|@#|")

        if customerList[1] == paydetailList[3]:

            customerCount = customerCount + 1

            break

    customerFo.close()

    if customerCount == 0:

        print "找不到指定的客户号，借据" + payDetailLine + ":"

        break

payDetailFo.close()

print "check zzb【"+loadFileConfig.fileDate+"】 customer file end..."
