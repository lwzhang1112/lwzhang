# coding=gbk
from PycharmProjects.zzbcheck import loadFileConfig
# zhangwei 20180608

print "check zzb��"+loadFileConfig.fileDate+"�� customer file begin..."

# У��ſ�ͻ���
payDetailFo = open(loadFileConfig.filepath + loadFileConfig.payDetailFilename, "r")

payDetailCount = 0

for payDetailLine in payDetailFo.readlines():

    payDetailLine = payDetailLine .strip()

    if payDetailLine == "":

        break

    payDetailCount = payDetailCount + 1

    print "���ڴ���:" + str(payDetailCount) + ":" + payDetailLine

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

        print "�Ҳ���ָ���Ŀͻ��ţ����" + payDetailLine + ":"

        break

payDetailFo.close()

print "check zzb��"+loadFileConfig.fileDate+"�� customer file end..."
