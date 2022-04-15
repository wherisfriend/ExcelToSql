#  ===========================主文件==============================
# 将Excel表的表名与数据库的table名对应
import xlrd
import pandas as pd
from pandas import DataFrame
from xlrd import sheet
import wtxt617 as xls
import operate_mysql as to_mysql

Rfile = '中创熔铸小数据库901.xls'
wb = xlrd.open_workbook(Rfile)
sheets = wb.sheet_names()
sheet_nums = len(sheets)

#   ==========================安装excel表的sheet顺序给设备命名=================================
tables=['ronglian1_table', 'ronglian2_table','baowen_table', 'diancijiaoban1_table', 'diancijiaoban2_table', 'guolv_table', 'chuqi_table', 'chuchen_table', 'zhuzao_table', 'gaosudaiju_table', 
        'junre1_table', 'junre2_table', 'junre3_table', 'junre4_table', 'junre5_table', 'lengque_table', 'zhuoshui_table', 'jingshui_table', 'kongya_table']
print("该xls文件中含有{}, 共{}sheet表".format(sheets, sheet_nums))

for m in range(sheet_nums):
    print("{}***执行{}表的数据处理".format(m, sheets[m]))  
    xls.data_deal(sheets[m], tables[m])


print("\n****所有设备建表完毕*****")
print("\n****开始写入数据库*****\n")


# 写入到mysql数据来
to_mysql.write_to_mysql('设备表908含01.sql', 'mini_zc_rongzhu')
