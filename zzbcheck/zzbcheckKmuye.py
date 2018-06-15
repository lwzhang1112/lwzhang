# coding=gbk

from decimal import *

from PycharmProjects.zzbcheck import loadFileConfig

import time

# zhangwei 20180608

print "check zzb ��"+loadFileConfig.fileDate+"�� kmye file begin..."

# У���Ŀ����
kmyefilelFo = open(loadFileConfig.filepath + loadFileConfig.kmyeFilename, "r")

kmyeCount = 0

# �ſ���Ŀ���
# ��������
payDebitAcount = Decimal(0.00)

# Ӧ�ձ������
payCreditAcount = Decimal(0.00)

# Ӧ�մ�����Ϣ
payDebitInte = Decimal(0.00)

# ������Ϣ����
payCreditInte = Decimal(0.00)

for kmyeLine in kmyefilelFo  .readlines():

    kmyeLine = kmyeLine .strip()

    if kmyeLine == "":

        break

    kmyeCount = kmyeCount + 1

    # print str(kmyeCount) + "��Ŀ�ļ�������:" + kmyeLine

    # �ֽ�ÿһ�еķſ���ϸ����
    kmyeList = kmyeLine.split("|@#|")

    # У��������Ŀ��������
    kmacount = kmyeList[8]

    #��Ŀ��
    kmcode = kmyeList[6]

    #���׺�
    transcode = kmyeList[3]

    kmflag = kmyeList[5]

    if transcode == "10100101":

        if kmcode == "1121100202" and kmflag == "��":

            payDebitAcount = payDebitAcount + Decimal(kmacount)

            print str(kmyeCount) + "��Ŀ�ļ�������------��:" + kmyeLine + "payDebitAcount:" + str(payDebitAcount)

            print str(kmyeCount) + "��Ŀ�ļ�������------��:payDebitAcount:" + str(payDebitAcount)

            time.sleep(1)

        if kmcode == "12213099" and kmflag == "��":

            payCreditAcount = payCreditAcount + Decimal(kmacount)

            print str(kmyeCount) + "��Ŀ�ļ�������------��:" + kmyeLine + "payCreditAcount:" + str(payCreditAcount)

            print str(kmyeCount) + "��Ŀ�ļ�������------��:payCreditAcount:" + str(payCreditAcount)

            time.sleep(1)

if payDebitAcount != payCreditAcount:

    print "�ſ���Ŀ-��������:" + str(payDebitAcount) + ":Ӧ�ձ������:" + str(payCreditAcount) + "�ſ���Ŀ-����������Ӧ�ձ�������Ӧ����..."

    raise RuntimeError("�ſ���Ŀ-��������:" + str(payDebitAcount) + ":Ӧ�ձ������:" + str(payCreditAcount) + "�ſ���Ŀ-����������Ӧ�ձ�������Ӧ����...")

# У��ſ�ı���
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

    print "ʵ�ʷſ��:" + str(actualPayAmount) + ":��Ŀ�����:" + str(payDebitAcount) + "�ſ��Ŀ�����ʵ�ʷſ����Ӧ����..."

    raise RuntimeError("ʵ�ʷſ��:" + str(actualPayAmount) + ":��Ŀ�����:" + str(payDebitAcount) + "�ſ��Ŀ�����ʵ�ʷſ����Ӧ����...")

kmyefilelFo.close()


# У�黹����صĿ�Ŀ���
kmyefilelFo = open(loadFileConfig.filepath + loadFileConfig.kmyeFilename, "r")

kmyeCount = 0

# �����ܽ��
kmpayDebitAcount = Decimal(0.00)
# Ӧ������
kmpayRequestCapital = Decimal(0.00)
# Ӧ����Ϣ
kmpayRequestInte = Decimal(0.00)
# ʵ������
kmpayActualCapital = Decimal(0.00)
# ʵ����Ϣ
kmpayActualInte = Decimal(0.00)

for kmyeLine in kmyefilelFo  .readlines():

    kmyeLine = kmyeLine .strip()

    if kmyeLine == "":

        break

    kmyeCount += 1

    # print str(kmyeCount) + "������ؿ�Ŀ�ļ�������:" + kmyeLine

    # �ֽ�ÿһ�еķſ���ϸ����
    kmyeList = kmyeLine.split("|@#|")

    # У��������Ŀ��������
    transcode = kmyeList[3]

    kmcode = kmyeList[6]

    flag = str(kmyeList[5])

    kmacount = kmyeList[8]

    if transcode == "10200301" or transcode == "700101" or transcode == "10200201":
        # �����У��
        if kmcode == "1121100202" and flag == "��":

            kmpayActualCapital = kmpayActualCapital + Decimal(kmacount)

            print str(kmyeCount) + "������ؿ�Ŀ�ļ�������---����--��:" + kmyeLine

            print str(kmyeCount) + "������ؿ�Ŀ�ļ�������---����--��:kmpayActualCapital:" + str(kmpayActualCapital)

            time.sleep(1)

        # ������ϢУ��
        if kmcode == "51011011" and flag == "��":

            kmpayActualInte = kmpayActualInte + Decimal(kmacount)

            print str(kmyeCount) + "������ؿ�Ŀ�ļ�������---��Ϣ--��:" + kmyeLine

            print str(kmyeCount) + "������ؿ�Ŀ�ļ�������---��Ϣ--��:kmpayActualInte:" + str(kmpayActualInte)

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

    # ��ȡ����Ӧ������Ӧ����Ϣ��ʵ������ʵ����Ϣ
    requestRepayCapital = requestRepayCapital + requestCapital

    requestRepayInte = requestRepayInte + requestInte

    actualRepayCapital = actualRepayCapital + actualCapital

    actualRepayInte = actualRepayInte + actualInte

repayFo.close()

if actualRepayCapital != kmpayActualCapital:

    print "��Ŀʵ�ʱ���" + str(kmpayActualCapital) + ":������ˮʵ�ձ���:" + str(actualRepayCapital) + "�Բ���"

    raise RuntimeError("��Ŀʵ�ʱ���" + str(kmpayActualCapital) + ":������ˮʵ�ձ���:" + str(actualRepayCapital) + "�Բ���")

if actualRepayInte != kmpayActualInte:

    print "��Ŀʵ����Ϣ��" + str(kmpayActualInte) + ":������ˮʵ����Ϣ:" + str(actualRepayInte) + "�Բ���"

    raise RuntimeError("��Ŀʵ�ʱ���" + str(kmpayActualCapital) + ":������ˮʵ�ձ���:" + str(actualRepayCapital) + "�Բ���")

print "check zzb��"+loadFileConfig.fileDate+"�� kmye file end..."
