# coding=gbk

from decimal import *

from PycharmProjects.zzbcheck import loadFileConfig

# zhangwei 20180608

print "check zzb【"+loadFileConfig.fileDate+"】 repay file begin..."

# 校验还款数据，主要校验还款交易中的贷款总额，应还本金，实还本金，应还configFile利息，实还利息
repayfilelFo = open(loadFileConfig.filepath + loadFileConfig.repayFilename, "r")

repayCount = 0

for repayLine in repayfilelFo .readlines():

    repayLine = repayLine .strip()

    if repayLine == "":

        break

    repayCount = repayCount + 1

    print str(repayCount) + "还款交易处理中:" + repayLine

    # 分解每一行的放款明细数据
    repayList = repayLine .split("|@#|")

    # 校验贷款总额，本金以及利息
    loanAmount = repayList[5]

    requestCapital = repayList[6]

    requestInte = repayList[7]

    actualCapital = repayList[8]

    actualInte = repayList[9]

    if Decimal(loanAmount) < Decimal(requestCapital):

        print "还款交易:" + repayLine + ":贷款总额:" + loanAmount + ":<:" + "应还本金:" + requestCapital

        break

    if Decimal(actualCapital) > Decimal(requestCapital):

        print "还款交易:" + repayLine + ":实际还款本金:" + actualCapital + ":>:" + "应还本金:" + requestCapital

        break

    if Decimal(actualInte) > Decimal(requestInte):

        print "还款交易:" + repayLine + ":实际还款利息:" + actualInte + ":>:" + "应还利息:" + requestInte

        break

repayfilelFo.close()

print "check zzb【"+loadFileConfig.fileDate+"】 repay file end..."
