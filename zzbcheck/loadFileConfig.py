# coding=gbk

import ConfigParser

# �����ļ����� zhangwei 20180608
# ��Ϊ�ļ����õ�gbk���ַ�������Ϊ������ʾ�ļ��е����ģ�����Ҳ����gbk�ı���

configFile = "/Users/xinxinuser/Library/Preferences/PyCharm2018.1/scratches/scratch.ini"

print "load file��" + configFile + "�� begin..."

config = ConfigParser.ConfigParser()

# config.add_section("zzbfile")

config.readfp(open(configFile, "rb"))

# ͨ���
sign = config.get("zzbfile", "sign")

print 'sign:    ' + sign

# �ļ�����
fileDate = config.get("zzbfile", "fileDate")

print 'fileDate:    ' + fileDate

# �ļ�����·��
filepath = config.get("zzbfile", "filepath").replace(sign, fileDate)

print 'filepath:    ' + filepath

# �ſ���ϸ�ļ�
payDetailFilename = config.get("zzbfile", "payDetailFilename").replace(sign, fileDate)

print 'payDetailFilename:    ' + payDetailFilename

# ����ƻ��ļ�
payPlanlFilename = config.get("zzbfile", "payPlanlFilename").replace(sign, fileDate)

print 'payPlanlFilename:    ' + payPlanlFilename

# �ͻ���Ϣ�ļ�
customerFilename = config.get("zzbfile", "customerFilename").replace(sign, fileDate)

print 'customerFilename:    ' + customerFilename

# ������ϸ�ļ�
repayFilename = config.get("zzbfile", "repayFilename").replace(sign, fileDate)

print 'repayFilename:    ' + repayFilename

# ��Ŀ����ļ�
kmyeFilename = config.get("zzbfile", "kmyeFilename").replace(sign, fileDate)

print 'kmyeFilename:    ' + kmyeFilename

print "load file��" + configFile + "�� end..."
