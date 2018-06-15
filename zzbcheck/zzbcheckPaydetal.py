# coding=gbk

from decimal import *

from PycharmProjects.zzbcheck import loadFileConfig

# zhangwei 20180608

print "check zzb【"+loadFileConfig.fileDate+"】 putout file begin..."

# 直接读取paydetail文件，校验放款明细文件和放款还款计划文件
payDetailFo = open(loadFileConfig.filepath + loadFileConfig.payDetailFilename, "r")

paydetailCount = 0

payplanCount = 0

for payDetailLine in payDetailFo.readlines():

    payDetailLine = payDetailLine .strip()

    if payDetailLine == "":

        break

    paydetailCount = paydetailCount + 1

    # print str(paydetailCount) + "借据处理中:" + payDetailLine

    if paydetailCount % 100 == 0:

        print str(paydetailCount) + "借据处理中......"

    # 分解每一行的放款明细数据
    paydetailList = payDetailLine .split("|@#|")

    payplanCount = 0

    payplanCapitalAmount = 0

    payPlanlFo = open(loadFileConfig.filepath + loadFileConfig.payPlanlFilename, "r")

    for payplanLine in payPlanlFo .readlines():

        payplanLine = payplanLine .strip()

        if payplanLine == "":

            break

        # 校验期数和本金
        payplanList = payplanLine .split("|@#|")

        if paydetailList[1] == payplanList[1]:

            payplanCount = payplanCount + 1

            payplanCapitalAmount = payplanCapitalAmount + Decimal(str(payplanList[4]))

    payPlanlFo.close()

    if payplanCount != int(paydetailList[8]) and int(paydetailList[8]) != 0:

        print "借据号:" + paydetailList[1] + ":期数:" + str(paydetailList[8]) + ":还款计划期数:" + str(payplanCount) + "不一致"

        # break

    if Decimal(payplanCapitalAmount) != Decimal(str(paydetailList[7])):

        print "借据号:" + paydetailList[1] + ":放款金额:" + str(paydetailList[7]) + ":还款计划应还本金总额:" + str(payplanCapitalAmount) + "不一致"

        # break

payDetailFo.close()

print "check zzb【"+loadFileConfig.fileDate+"】 putout file end..."
