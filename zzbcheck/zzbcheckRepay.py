# coding=gbk

from decimal import *

from PycharmProjects.zzbcheck import loadFileConfig

# zhangwei 20180608

print "check zzb��"+loadFileConfig.fileDate+"�� repay file begin..."

# У�黹�����ݣ���ҪУ�黹����еĴ����ܶӦ������ʵ������Ӧ��configFile��Ϣ��ʵ����Ϣ
repayfilelFo = open(loadFileConfig.filepath + loadFileConfig.repayFilename, "r")

repayCount = 0

for repayLine in repayfilelFo .readlines():

    repayLine = repayLine .strip()

    if repayLine == "":

        break

    repayCount = repayCount + 1

    print str(repayCount) + "����״�����:" + repayLine

    # �ֽ�ÿһ�еķſ���ϸ����
    repayList = repayLine .split("|@#|")

    # У������ܶ�����Լ���Ϣ
    loanAmount = repayList[5]

    requestCapital = repayList[6]

    requestInte = repayList[7]

    actualCapital = repayList[8]

    actualInte = repayList[9]

    if Decimal(loanAmount) < Decimal(requestCapital):

        print "�����:" + repayLine + ":�����ܶ�:" + loanAmount + ":<:" + "Ӧ������:" + requestCapital

        break

    if Decimal(actualCapital) > Decimal(requestCapital):

        print "�����:" + repayLine + ":ʵ�ʻ����:" + actualCapital + ":>:" + "Ӧ������:" + requestCapital

        break

    if Decimal(actualInte) > Decimal(requestInte):

        print "�����:" + repayLine + ":ʵ�ʻ�����Ϣ:" + actualInte + ":>:" + "Ӧ����Ϣ:" + requestInte

        break

repayfilelFo.close()

print "check zzb��"+loadFileConfig.fileDate+"�� repay file end..."
