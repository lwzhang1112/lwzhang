# coding=gbk

from decimal import *

from PycharmProjects.zzbcheck import loadFileConfig

import time

# zhangwei 20180608

print "check zzb 【"+loadFileConfig.fileDate+"】 kmye file begin..."

# 校验科目数据
kmyefilelFo = open(loadFileConfig.filepath + loadFileConfig.kmyeFilename, "r")

kmyeCount = 0

# 放款本金科目余额
# 贷款本金余额
payDebitAcount = Decimal(0.00)

# 应收本金余额
payCreditAcount = Decimal(0.00)

# 应收贷款利息
payDebitInte = Decimal(0.00)

# 贷款利息收入
payCreditInte = Decimal(0.00)

for kmyeLine in kmyefilelFo  .readlines():

    kmyeLine = kmyeLine .strip()

    if kmyeLine == "":

        break

    kmyeCount = kmyeCount + 1

    # print str(kmyeCount) + "科目文件处理中:" + kmyeLine

    # 分解每一行的放款明细数据
    kmyeList = kmyeLine.split("|@#|")

    # 校验整个科目余额的数据
    kmacount = kmyeList[8]

    #科目号
    kmcode = kmyeList[6]

    #交易号
    transcode = kmyeList[3]

    kmflag = kmyeList[5]

    if transcode == "10100101":

        if kmcode == "1121100202" and kmflag == "借":

            payDebitAcount = payDebitAcount + Decimal(kmacount)

            print str(kmyeCount) + "科目文件处理中------借:" + kmyeLine + "payDebitAcount:" + str(payDebitAcount)

            print str(kmyeCount) + "科目文件处理中------借:payDebitAcount:" + str(payDebitAcount)

            time.sleep(1)

        if kmcode == "12213099" and kmflag == "贷":

            payCreditAcount = payCreditAcount + Decimal(kmacount)

            print str(kmyeCount) + "科目文件处理中------贷:" + kmyeLine + "payCreditAcount:" + str(payCreditAcount)

            print str(kmyeCount) + "科目文件处理中------贷:payCreditAcount:" + str(payCreditAcount)

            time.sleep(1)

if payDebitAcount != payCreditAcount:

    print "放款本金科目-贷款本金余额:" + str(payDebitAcount) + ":应收本金余额:" + str(payCreditAcount) + "放款本金科目-贷款本金余额与应收本金余额对应不上..."

    raise RuntimeError("放款本金科目-贷款本金余额:" + str(payDebitAcount) + ":应收本金余额:" + str(payCreditAcount) + "放款本金科目-贷款本金余额与应收本金余额对应不上...")

# 校验放款的本金
actualPayAmount = Decimal(0.00)

payDetailFo = open(loadFileConfig.filepath + loadFileConfig.payDetailFilename, "r")

for payDetailLine in payDetailFo.readlines():

    payDetailLine = payDetailLine.strip()

    if payDetailLine == "":

        break

    paydetailList = payDetailLine.split("|@#|")

    actualPayAmount = actualPayAmount + Decimal(paydetailList[7])

payDetailFo.close()

kmyefilelFo.close()

if actualPayAmount != payDebitAcount:

    print "实际放款本金:" + str(actualPayAmount) + ":科目总余额:" + str(payDebitAcount) + "放款科目余额与实际放款金额对应不上..."

    raise RuntimeError("实际放款本金:" + str(actualPayAmount) + ":科目总余额:" + str(payDebitAcount) + "放款科目余额与实际放款金额对应不上...")

kmyefilelFo.close()


# 校验还款相关的科目金额
kmyefilelFo = open(loadFileConfig.filepath + loadFileConfig.kmyeFilename, "r")

kmyeCount = 0

# 还款总金额
kmpayDebitAcount = Decimal(0.00)
# 应还本金
kmpayRequestCapital = Decimal(0.00)
# 应还利息
kmpayRequestInte = Decimal(0.00)
# 实还本金
kmpayActualCapital = Decimal(0.00)
# 实还利息
kmpayActualInte = Decimal(0.00)

for kmyeLine in kmyefilelFo  .readlines():

    kmyeLine = kmyeLine .strip()

    if kmyeLine == "":

        break

    kmyeCount += 1

    # print str(kmyeCount) + "还款相关科目文件处理中:" + kmyeLine

    # 分解每一行的放款明细数据
    kmyeList = kmyeLine.split("|@#|")

    # 校验整个科目余额的数据
    transcode = kmyeList[3]

    kmcode = kmyeList[6]

    flag = str(kmyeList[5])

    kmacount = kmyeList[8]

    if transcode == "10200301" or transcode == "700101" or transcode == "10200201":
        # 还款本金校验
        if kmcode == "1121100202" and flag == "贷":

            kmpayActualCapital = kmpayActualCapital + Decimal(kmacount)

            print str(kmyeCount) + "还款相关科目文件处理中---本金--贷:" + kmyeLine

            print str(kmyeCount) + "还款相关科目文件处理中---本金--贷:kmpayActualCapital:" + str(kmpayActualCapital)

            time.sleep(1)

        # 还款利息校验
        if kmcode == "51011011" and flag == "贷":

            kmpayActualInte = kmpayActualInte + Decimal(kmacount)

            print str(kmyeCount) + "还款相关科目文件处理中---利息--贷:" + kmyeLine

            print str(kmyeCount) + "还款相关科目文件处理中---利息--贷:kmpayActualInte:" + str(kmpayActualInte)

            time.sleep(1)

kmyefilelFo.close()

actualRepayAmount = Decimal(0.00)

requestRepayCapital = Decimal(0.00)

requestRepayInte = Decimal(0.00)

actualRepayCapital = Decimal(0.00)

actualRepayInte = Decimal(0.00)

repayFo = open(loadFileConfig.filepath + loadFileConfig.repayFilename, "r")

for repayLine in repayFo .readlines():

    repayLine = repayLine .strip()

    if repayLine == "":

        break

    repaydetailList = repayLine. split("|@#|")

    loanAmount = Decimal(repaydetailList[5])

    requestCapital = Decimal(repaydetailList[6])

    requestInte = Decimal(repaydetailList[7])

    actualCapital = Decimal(repaydetailList[8])

    actualInte = Decimal(repaydetailList[9])

    # 获取本期应还本金、应还利息、实还本金、实还利息
    requestRepayCapital = requestRepayCapital + requestCapital

    requestRepayInte = requestRepayInte + requestInte

    actualRepayCapital = actualRepayCapital + actualCapital

    actualRepayInte = actualRepayInte + actualInte

repayFo.close()

if actualRepayCapital != kmpayActualCapital:

    print "科目实际本金：" + str(kmpayActualCapital) + ":交易流水实收本金:" + str(actualRepayCapital) + "对不上"

    raise RuntimeError("科目实际本金：" + str(kmpayActualCapital) + ":交易流水实收本金:" + str(actualRepayCapital) + "对不上")

if actualRepayInte != kmpayActualInte:

    print "科目实际利息：" + str(kmpayActualInte) + ":交易流水实收利息:" + str(actualRepayInte) + "对不上"

    raise RuntimeError("科目实际本金：" + str(kmpayActualCapital) + ":交易流水实收本金:" + str(actualRepayCapital) + "对不上")

print "check zzb【"+loadFileConfig.fileDate+"】 kmye file end..."
