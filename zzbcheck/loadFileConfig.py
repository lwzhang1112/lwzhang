# coding=gbk

import ConfigParser

# 加载文件配置 zhangwei 20180608
# 因为文件是用的gbk的字符，所以为了能显示文件中的中文，这里也采用gbk的编码

configFile = "/Users/xinxinuser/Library/Preferences/PyCharm2018.1/scratches/scratch.ini"

print "load file【" + configFile + "】 begin..."

config = ConfigParser.ConfigParser()

# config.add_section("zzbfile")

config.readfp(open(configFile, "rb"))

# 通配符
sign = config.get("zzbfile", "sign")

print 'sign:    ' + sign

# 文件日期
fileDate = config.get("zzbfile", "fileDate")

print 'fileDate:    ' + fileDate

# 文件所在路径
filepath = config.get("zzbfile", "filepath").replace(sign, fileDate)

print 'filepath:    ' + filepath

# 放款明细文件
payDetailFilename = config.get("zzbfile", "payDetailFilename").replace(sign, fileDate)

print 'payDetailFilename:    ' + payDetailFilename

# 还款计划文件
payPlanlFilename = config.get("zzbfile", "payPlanlFilename").replace(sign, fileDate)

print 'payPlanlFilename:    ' + payPlanlFilename

# 客户信息文件
customerFilename = config.get("zzbfile", "customerFilename").replace(sign, fileDate)

print 'customerFilename:    ' + customerFilename

# 还款明细文件
repayFilename = config.get("zzbfile", "repayFilename").replace(sign, fileDate)

print 'repayFilename:    ' + repayFilename

# 科目余额文件
kmyeFilename = config.get("zzbfile", "kmyeFilename").replace(sign, fileDate)

print 'kmyeFilename:    ' + kmyeFilename

print "load file【" + configFile + "】 end..."
