# coding=gbk

from decimal import *

from PycharmProjects.zzbcheck import loadFileConfig

# zhangwei 20180608

print "check zzb��"+loadFileConfig.fileDate+"�� putout file begin..."

# ֱ�Ӷ�ȡpaydetail�ļ���У��ſ���ϸ�ļ��ͷſ��ƻ��ļ�
payDetailFo = open(loadFileConfig.filepath + loadFileConfig.payDetailFilename, "r")

paydetailCount = 0

payplanCount = 0

for payDetailLine in payDetailFo.readlines():

    payDetailLine = payDetailLine .strip()

    if payDetailLine == "":

        break

    paydetailCount = paydetailCount + 1

    # print str(paydetailCount) + "��ݴ�����:" + payDetailLine

    if paydetailCount % 100 == 0:

        print str(paydetailCount) + "��ݴ�����......"

    # �ֽ�ÿһ�еķſ���ϸ����
    paydetailList = payDetailLine .split("|@#|")

    payplanCount = 0

    payplanCapitalAmount = 0

    payPlanlFo = open(loadFileConfig.filepath + loadFileConfig.payPlanlFilename, "r")

    for payplanLine in payPlanlFo .readlines():

        payplanLine = payplanLine .strip()

        if payplanLine == "":

            break

        # У�������ͱ���
        payplanList = payplanLine .split("|@#|")

        if paydetailList[1] == payplanList[1]:

            payplanCount = payplanCount + 1

            payplanCapitalAmount = payplanCapitalAmount + Decimal(str(payplanList[4]))

    payPlanlFo.close()

    if payplanCount != int(paydetailList[8]) and int(paydetailList[8]) != 0:

        print "��ݺ�:" + paydetailList[1] + ":����:" + str(paydetailList[8]) + ":����ƻ�����:" + str(payplanCount) + "��һ��"

        # break

    if Decimal(payplanCapitalAmount) != Decimal(str(paydetailList[7])):

        print "��ݺ�:" + paydetailList[1] + ":�ſ���:" + str(paydetailList[7]) + ":����ƻ�Ӧ�������ܶ�:" + str(payplanCapitalAmount) + "��һ��"

        # break

payDetailFo.close()

print "check zzb��"+loadFileConfig.fileDate+"�� putout file end..."
